<script>
    import { onDestroy } from 'svelte';
    import Header from "./header.svelte";
    import Footer from "../Main/footer.svelte";
    import Cookies from 'js-cookie';
    import { onMount } from 'svelte';
    import { navigate } from 'svelte-routing';
    import axios from "axios";

    import Companion from './companion.svelte';
    import AddCompanion from './addCompanion.svelte';
    import Objects from './object.svelte';


    let userInfo;
    let showUserInfo = false;

    let sex = 'Мужчина';
    let url = 'http://127.0.0.1:8000/api/'
    let favotitsOBJ = []
    let travelers = []

    //passwords
    let old_password
    let old_password2
    let new_password
    let responseLogResPassword = ""
    let logPassword

    //images
    let responseLogimages = ''
    let logImages
    let titleImage
     let imageUrl = ''

    //settings
    let logSettingsProfile, responseLogSettingsProfile = ""

    let access, refresh

    let info = {}
    let cloneInfo = {}
    // const info = JSON.parse(Cookies.get('info') || '{}');

    let  surname,
         name, 
         email, 
         phone, 
         position, 
         id , 
         patronymic,
         image,
         date_of_birth,
         password

         

    async function makeRequest() {
    try {
      const headers = {
        Authorization: `Bearer ${access}`
      };
      const response = await axios.get('http://localhost:8000/api/users/profile/', { headers });
      info = response.data
      let  {surname,
         name, 
         email, 
         phone, 
         position, 
         id , 
         patronymic,
         image,
         date_of_birth,
         password} = info
         cloneInfo = {...info}
      return response.data.id;
    } catch (error) {
      console.error('Ошибка при выполнении запроса:', error.response.status);
      if (error.response.status === 401) {
        await refreshTokenFunc(); 
        return await makeRequest(); 
      } else {
        throw error;
      }
    }
  }

    const toggleUserInfo = () => {
        showUserInfo = !showUserInfo;
        if (userInfo) {
            userInfo.style.display = showUserInfo ? 'block' : 'none';
        }
    };

    async function editProfile() {
        const updatedData = {};

        if (phone !== cloneInfo.phone) {
            updatedData.phone = cloneInfo.phone; 
            console.log("Номер телефона был изменен");
        }

        if (email !== cloneInfo.email) {
            updatedData.email = cloneInfo.email; 
            localStorage.setItem("email", updatedData.email)
            console.log("Почта была изменена");
        }

        if (surname !== cloneInfo.surname) {
            updatedData.surname = cloneInfo.surname; 
        }

        if (name !== cloneInfo.name) {
            updatedData.name = cloneInfo.name; 
        }

        if (sex !== cloneInfo.sex) {
            updatedData.sex = cloneInfo.sex; 
        }

        if (cloneInfo.date_of_birth && date_of_birth !== cloneInfo.date_of_birth) {
            updatedData.date_of_birth = cloneInfo.date_of_birth; 
            console.log("Дата рождения была изменена");
        }

        if (patronymic !== cloneInfo.patronymic) {
            updatedData.patronymic = cloneInfo.patronymic; 
        }

        if (Object.keys(updatedData).length === 0) {
            console.log("Нет изменений для сохранения.");
            return;
        }

        try {
            const response = await axios.patch(`http://127.0.0.1:8000/api/users/${cloneInfo.id}/`, updatedData, {
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${access}`,
                },
            });
      
                if (response.status === 200) {
                    responseLogSettingsProfile = "Данные успешно изменнены!";

                    Object.assign(logSettingsProfile.style, {
                        opacity: 1,
                        color: "green"
                    });

                    setTimeout(() => {
                        Object.assign(logSettingsProfile.style, {
                            opacity: 0
                        });
                    }, 3000);
                }
            

            console.log("Профиль успешно обновлен:", response.data)
            info = response.data  
        } catch (error) {
            if (error.response && error.response.status === 401) {
                await refreshTokenFunc(); 
                await editProfile();
            }
            responseLogSettingsProfile = "Ошибка! Возможно почта или номер телефона уже зарегистрирован"
            
            Object.assign(logSettingsProfile.style, {
                        opacity: 1,
                        color: "red"
                    });

                    setTimeout(() => {
                        Object.assign(logSettingsProfile.style, {
                            opacity: 0
                        });
                    }, 3000);
            console.error("Ошибка при изменении данных пользователя", error.response);
        }
    }

    async function updateImages() {
    const file = titleImage.files[0]; // Получаем файл из элемента input
    if (file) {
        try {
            console.log("Отправляем файл:", file); // Для отладки

            const formData = new FormData();
            formData.append('image', file); // Добавляем файл к FormData

            // Отправка файла на сервер
            const response = await axios.patch(`http://127.0.0.1:8000/api/users/${cloneInfo.id}/`, formData, {
                headers: {
                    'Content-Type': 'multipart/form-data', 
                    'Authorization': `Bearer ${access}`, 
                },
            });

            console.log("Изображение успешно обновлено:", response.data);
            responseLogimages = "Изображение успешно обновлено"; // Обновление сообщения
            Object.assign(titleImage.style, {
                opacity: 1,
                color: "green"
            });

            setTimeout(() => {
                Object.assign(titleImage.style, {
                    opacity: 0
                });
            }, 3000);
            
        } catch (error) {
            if (error.response && error.response.status === 401) {
                await refreshTokenFunc();
                await updateImages(); 
            } else {
                console.error("Ошибка при изменении фото профиля", error.response);
                responseLogimages = "Ошибка при изменении фото профиля"; 
                Object.assign(titleImage.style, {
                    opacity: 1,
                    color: "red"
                });

                setTimeout(() => {
                    Object.assign(titleImage.style, {
                        opacity: 0
                    });
                }, 3000);
            }
        }
    } else {
        console.error("Файл не выбран");
        responseLogimages = "Файл не выбран"; 
    }
}
    
    async function setNewPassword() {
    try {
        const response = await axios.post(`http://127.0.0.1:8000/api/users/change_password/`, {
            old_password,
            old_password2,
            new_password,
        }, {
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${access}`,
            }
        });

        if (response.status === 200) {
            responseLogResPassword = "Пароль успешно изменен!";
            // Сброс значений
            old_password = '';
            old_password2 = '';
            new_password = '';

            Object.assign(logPassword.style, {
                opacity: 1,
                color: "green"
            });

            setTimeout(() => {
                Object.assign(logPassword.style, {
                    opacity: 0
                });
            }, 3000);
        } else {
            responseLogResPassword = "Текущий пароль неверен";
        }
    } catch (error) {
        if (error.response && error.response.status === 401) {
            console.error("Токен истек, пытаемся обновить его.");
            await refreshTokenFunc(); 
            await setNewPassword();
            
            if(error.response.status === 400) {
                responseLogResPassword = "Не удалось обновить токен, пожалуйста, войдите снова.";
                Object.assign(logPassword.style, {
                opacity: 1,
                color: "red",
            });

            setTimeout(() => {
                Object.assign(logPassword.style, {
                    opacity: 0,
                });
            }, 3000);
            }

        } else {
            responseLogResPassword = "Ошибка при смене пароля: " + (error.response?.data?.detail || "Неизвестная ошибка");
            Object.assign(logPassword.style, {
                opacity: 1,
                color: "red"
            });

            setTimeout(() => {
                Object.assign(logPassword.style, {
                    opacity: 0
                });
            }, 3000);
            console.error("Ошибка при смене пароля:", error.response);
        }
    }
}

async function refreshTokenFunc() {
    console.log('Токен обновления:', refresh); 

    if (!refresh) {
        console.warn('Токен обновления отсутствует.');
        return;
    }
    try {
        const response = await axios.post('http://127.0.0.1:8000/api/auth/jwt/refresh/', {
            refresh: refresh
        });
        console.log('Новый токен:', response.data);
        access = response.data.access
    } catch (error) {
        console.error('Ошибка обновления токена:', error.response?.data || error.message);
        if (error.response && error.response.data.code === 'token_not_valid') {
        }
    }
}

  // Логин
  async function loginUser() {
    try {
      const response = await axios.post('http://localhost:8000/api/auth/jwt/create/', {
           email: localStorage.getItem("email"),
           password: localStorage.getItem("pass")
      });

      access = response.data.access
      refresh = response.data.refresh

      await makeRequest();

    } catch (error) {
      console.error('Ошибка входа:', error.response.data);
    }
  }

    async function getFavorites() {
        try {
            const response = await axios.get(`http://localhost:8000/api/users/${id}/get_user_favorites/`);
            favotitsOBJ = await Promise.all(response.data.map(async (object) => {
                const cityName = await fetchCityName(object.address.city);
                console.log(cityName)
                return {
                    id: object.id,
                    city: cityName || object.address.city,
                    street: object.address.street,
                    house: object.address.house,
                    seaDistance: object.address.sea_distance,
                    title: object.name,
                    description: object.description || "No description",
                    minPrice: object.min_price,
                    type: object.type,
                    images: object.images.length > 0 ? object.images.map(image => image.media) : [],
                    tags: object.tags.map(tag => tag),
                    isFavorit: true,
                };
            }));
        } catch (error) {
            console.error('Error fetching objects:', error);
        }
    }

    const handleResize = () => {
        if (userInfo) { 
            userInfo.style.display = document.body.clientWidth > 769 ? 'block' : 'none'; 
        }
    };

    async function fetchCityName(cityId) {
        try {
            const response = await axios.get(`http://localhost:8000/api/city/${cityId}/`);
            return response.data.name; 
        } catch (error) {
            console.error('Error fetching city name:', error);
            return null; 
        }
    }

    window.addEventListener('resize', handleResize);
    onDestroy(() => window.removeEventListener('resize', handleResize));
    handleResize();

    async function getUserTravelers() {
        try {
            const response = await axios.get(`http://localhost:8000/api/travelers/`, {
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${access}`,
                }
            });
            travelers = response.data;
            console.log("Попутчики - ", travelers);
        } catch (error) {
            console.error('Ошибка поиска попутчиков:', error);
            if (error.response && error.response.status === 401) {
                console.error("Токен истек, пытаемся обновить его.");
                const newToken = await refreshTokenFunc();
                await getUserTravelers();
            }
        }
    }

    //Переключение страниц
    let activeTab = 'settingsProfile';

    if(localStorage.getItem("activeTab") !== null){
        activeTab = localStorage.getItem("activeTab")
        
    }
    const switchTab = (tab) => {
        activeTab = tab
        localStorage.setItem("activeTab",tab);
    };

    async function check() {
        if (!access || !refresh) {
                console.warn('Токены отсутствуют. Пользователь должен войти в систему.');
                await loginUser()
                return check()
            } else {
                console.log('Токены найдены:', { access, refresh });
                await refreshTokenFunc()
                
            }
    }

    onMount(async () =>{
        await check()
        await makeRequest()
        await getUserTravelers()
        await getFavorites()
        
    })
</script>

<main>
    <Header/>

    <div class="content">
        <div class="size">
            <h1 id="profileText">
                Личный кабинет
                <svg on:click={toggleUserInfo} class="menu-icon" viewBox="0 0 24 24">
                    <path d="M3 6h18M3 12h18m-7 6h7" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
                </svg>
            </h1>

            <div class="user">
                <div bind:this={userInfo} class="userInfo max">
                    <p id="email">{cloneInfo.email}</p>
                    <a id="profileEdite" on:click={() => switchTab('settingsProfile')}>Настроить профиль</a>
                    <hr id="line">
                    <div class="userChoose">
                        <p on:click={() => switchTab('bookings')} class:selected={activeTab === 'bookings'}>Мои бронирования</p>
                        <p on:click={() => switchTab('favorites')} class:selected={activeTab === 'favorites'}>Избранное</p>
                        <p on:click={() => switchTab('reviews')} class:selected={activeTab === 'reviews'} >Мои отзывы</p>
                        <p on:click={() => switchTab('history')} class:selected={activeTab === 'history'} >История отелей</p>
                    </div>
                </div>

                <div class="userSettings">
                    {#if activeTab === 'settingsProfile'}
                    <div class="addUserInfo" on:submit|preventDefault={editProfile}>
                            <span id="editProfff">
                                <h1>Настройка профиля</h1>
                                <p bind:this = {logSettingsProfile}>{responseLogSettingsProfile}</p> 
                            </span> 
                        <p>Введите свои данные, для автоматического заполнения при бронировании.</p>

                        <form id="settingsUser" >
                            <div class="block">
                                <div class="input">
                                    <input type="text" bind:value={cloneInfo.surname} id="surname" placeholder=" " required>
                                    <label for="surname">Фамилия</label>
                                </div>

                                <div class="input">
                                    <input type="text" bind:value={cloneInfo.name} id="name" placeholder=" " required>
                                    <label for="name">Имя</label>  
                                </div>

                                <div class="input">
                                    <input type="text" bind:value={cloneInfo.patronymic} id="surname" placeholder=" " required>
                                    <label for="surname">Отчество</label>
                                </div>

                            </div>
                        
                            <div class="block">
                                <div class="input">
                                    <input type="date" bind:value={cloneInfo.date_of_birth} id="birthdate" required>
                                    <label for="birthdate">Дата рождения</label>
                                </div>
                                <div class="input">
                                    <input type="text"  id="citizenship" placeholder=" " required>
                                    <label for="citizenship">Гражданство</label>
                                </div>
                            </div>
                        
                            <label id="gender">
                                <input type="radio" bind:group={cloneInfo.sex} value="Мужчина" checked /> Мужчина
                                <input type="radio" bind:group={cloneInfo.sex} value="Женщина" /> Женщина
                            </label>
                        
                            <div class="blockWhisPhoto">
                                <div class="block pht">
                                    <div class="input">
                                        <input type="text" bind:value={cloneInfo.phone} id="phone" placeholder=" " required>
                                        <label for="phone">Номер Телефона</label>
                                    </div>
                                    <div class="input">
                                        <input type="text" bind:value={cloneInfo.email} id="emailInput" placeholder=" " required>
                                        <label for="emailInput">Эл Почта</label>  
                                    </div>

                                    <button id="save" type="submit">Сохранить</button>
                                </div>
    
    
    
                                <div class="blockAddPhoto">
                                    <form id="formImg" on:submit|preventDefault={updateImages}>
                                        <span id="resPassMid">
                                            <h1>Фото профиля</h1>
                                            <p bind:this={titleImage}>{responseLogimages}</p>
                                        </span>
                                
                                        <img id="imgProfile" src="{cloneInfo.image}" alt="Фото профиля">
                                        <input type="file" bind:this={titleImage} accept="image/jpeg,image/png" required>
                                        <button id="updateimage">Загрузить фото</button>
                                    </form>
                                </div>
                            </div>
                        </form>
                        <hr style="margin-bottom: 20px;">
                    </div>



                    <div class="blockCompanion">
                        <hr>
                        <div class="companions">
                                {#each travelers as userTravelers}
                                    <Companion {userTravelers}/>
                                {/each}
                            <AddCompanion/>
                        </div>
                    </div>

                    <div class="blockResPassword">
                        <hr>
                        <span id="resPassMid">
                            <h1>Смена пароля</h1> <p bind:this = {logPassword}>{responseLogResPassword}</p>
                        </span>
                        <form class="formResPassword" 
                        on:submit|preventDefault={setNewPassword}
                        >
                            <div class="input">
                                <input type="password" bind:value={old_password} id="currentPassword" placeholder=" " required>
                                <label for="currentPassword">Текущий пароль</label>
                            </div>
                            <div class="input">
                                <input type="password" bind:value={old_password2} id="newPassword" placeholder=" " required>
                                <label for="newPassword">Повторите текущий пароль</label>  
                            </div>
                            <div class="input">
                                <input type="password" bind:value={new_password} id="repeatNewPassword" placeholder=" " required>
                                <label for="repeatNewPassword">Новый пароль</label>  
                            </div>
                            <button id="save">Изменить</button>
                        </form>
                    </div>

                    

                    
                    {:else if activeTab === 'bookings'}
                        <div>"Мои бронирования"</div>
                    {:else if activeTab === 'favorites'}
                        <div id="favorites">
                            "Избранное"
                            <hr id="line">

                            <div class="blockFavorites">
                                {#each favotitsOBJ as apartment}
                                    <Objects {apartment} />
                                {/each}
                            </div>
                        </div>
                    {:else if activeTab === 'reviews'}
                        <div>"Мои отзывы"</div>
                    {:else if activeTab === 'history'}
                        <div>"История отелей"</div>
                    {/if}
                </div>
            </div>
        </div>
    </div>

    <Footer/>
</main>

<style>
    #formImg{
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
    }

    #imgProfile{
        width: 150px;
        height: 150px;
        border: 2px rgba(161, 161, 161, 0.411) solid;
        border-radius: 50%;
        object-fit: cover;
    }

    input[type=file]{
        color:transparent;
    }

    .blockWhisPhoto{
        display: flex;
        justify-content: space-between;
        align-items: center;
        width: 100%;
    }

    .block.pht{
        display: flex;
        flex-direction: column;
    }

    #resPassMid p{
        color: Green;
        font-size: 13px;
        opacity: 1;
        transition: 0.3s;
    }

    #editProfff p{
        color: green;
        font-size: 13px;
        opacity: 0;
        transition: 0.3s;
    }

    #editProfff{
        display: flex;
        align-items: center;
        justify-content: start;
        gap: 10px;
        padding-bottom: 10px;
    }

    #resPassMid{
        display: flex;
        align-items: center;
        gap: 10px;
    }

    .userInfo, .userSettings {
        border-radius: 7px;
    }

    .userInfo p.selected {
        border-left: 2px var(--color) solid;
        padding-left: 13px;
        background: linear-gradient(to right, rgba(0,35,215, 0.1) 1%, transparent 100%);
    }

    .userInfo p:hover {
        color: var(--color);
    }

    #email:hover {
        color: black;
    }

    .blockAddPhoto img{
        width: 200px;
        height: 200px;
    }

    .blockAddPhoto a{
        background-color: aqua;
    }

    #updateimage{
        background-color: var(--color);
        color: white;
        width: 137px;
        height: 33px;
        border-radius: 5px;
    }

    .blockFavorites{
        display: flex;
        justify-content: center;
        flex-direction: column;
        gap: 20px;
        
    }

    .blockResPassword h1{
        font-size: 18px;
        font-weight: 400;
        line-height: 21.33px;
        margin: 20px 0 20px 0;
    }

    .formResPassword{
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
        gap: 10px;
        width: 100%;
    }

    .blockCompanion hr{
        margin: 20px 0 20px 0;
        flex-grow: 1;
    }

    .companions{
        display: flex;
        flex-wrap: wrap;
        gap: 10px;
        
    }

    .blockResPassword hr{
        margin: 20px 0 20px 0;
    }

    .formResPassword input{
        padding: 10px;
        margin-bottom: 5px;
        border: 1px solid #ccc;
        border-radius: 4px;
        box-sizing: border-box;
        width: 100%;
        max-width: 400px;
        position: relative;
        color: grey;
        font-size: 14px;
    }

    #save{
        background-color: var(--color);
        color: white;
        width: 137px;
        height: 33px;
        border-radius: 5px;
        align-self: self-start;
    }

    .user {
        display: flex;
        align-items: start;
        gap: 40px;
    }

    #gender{
        width: 100%;
        display: flex;
        gap: 10px;
        padding: 10px;
    }

    h1 > svg {
        width: 30px;
        height: 30px;
        display: none;
    }

    input[type="text"] {
        padding: 10px;
        margin-bottom: 10px;
        border: 1px solid #ccc;
        border-radius: 4px;
        box-sizing: border-box;
        width: 100%;
        max-width: 400px;
        position: relative;
        color: grey;
        font-size: 14px;
    }

    input[type="date"] {
        padding: 10px;
        margin-bottom: 10px;
        border: 1px solid #ccc;
        border-radius: 4px;
        box-sizing: border-box;
        width: 100%;
        max-width: 400px;
        position: relative;
        color: grey;
        font-size: 14px;
    }

    .block {
        width: 100%;
        display: flex;
        justify-content: space-between;
        gap: 10px;
    }

    .input {
        position: relative;
        flex-grow: 1;
        width: 100%;
    }

    .input label {
        position: absolute;
        left: 10px;
        top: 10px;
        transition: 0.2s ease all;
        color: #aaa;
        pointer-events: none;
        border-radius: 5px;
    }

    .input input:focus + label,
    .input input:not(:placeholder-shown) + label {
        top: -10px;
        left: 10px;
        font-size: 12px;
        background: white;
        color: #474747;
    }

    #settingsUser {
        display: flex;
        margin-top: 20px;
        gap: 20px;
        justify-content: center;
        flex-direction: column;
        align-items: center;
        margin-bottom: 20px;
    }

    #email {
        font-family: Rubik;
        font-size: 16px;
        font-weight: 400;
        line-height: 18.96px;
        text-align: left;
        padding-left: 15px;
    }

    .addUserInfo h1 {
        font-family: Rubik;
        font-size: 18px;
        font-weight: 400;
        line-height: 21.33px;
    }

    .addUserInfo p {
        font-family: Rubik;
        font-size: 14px;
        font-weight: 300;
        line-height: 16.59px;
    }

    .userSettings {
        width: 100%;
        max-width: 873px;
        height: auto;
        padding: 30px;
        background: white;
    }

    .userChoose {
        display: flex;
        flex-direction: column;
        gap: 5px;
        font-family: Rubik;
        font-size: 14px;
        font-weight: 400;
        line-height: 16.59px;
        text-align: left;
    }

    .userChoose p {
        cursor: pointer;
        user-select: none; 
        padding-left: 15px;
        padding-top: 12px;
        padding-bottom: 12px
    }

    #profileEdite {
        font-family: Rubik;
        font-size: 12px;
        font-weight: 400;
        line-height: 14.22px;
        text-align: left;
        color: var(--color);
        padding-left: 15px;
        cursor: pointer;
    }

    #line {
        margin: 10px 0 20px 0;
    }

    .userInfo {
        width: 270px;
        background: white;
        padding: 15px 0;
    }

    .size {
        width: 100%;
        max-width: 1200px;
    }

    #profileText {
        font-family: Rubik;
        font-size: 26px;
        font-weight: 500;
        line-height: 30.81px;
        padding: 20px 0;
        display: flex;
        justify-content: start;
        align-items: center;
        flex-direction: row;
        gap: 20px;
    }

    .content {
        display: flex;
        justify-content: center;
    }

    main {
        background: #ECEFFF;
        display: flex;
        flex-direction: column;
        min-height: 100vh; 
    }

    .content {
        flex-grow: 1;
        padding: 20px;
    }

    @media(max-width: 768px) {
        .user {
            flex-direction: column; 
            align-items: center;
        }

        .addUserInfo input[type="text"],
        .addUserInfo input[type="date"] {
            min-width: 100%;
        }

        #email {
            font-size: 14px;
            overflow: hidden;
        }

        .addUserInfo h1 {
            font-size: 16px;
        }

        .addUserInfo p {
            font-size: 12px;
        }
    }

    @media(max-width:566px) {
        .block {
            flex-direction: column;
        }
    }

    @media(max-width:769px) {
        h1 > svg {
            display: block;
        }

        .userInfo {
            display: none;
        }

        .user {
            align-items: start;
        }
    }
</style>