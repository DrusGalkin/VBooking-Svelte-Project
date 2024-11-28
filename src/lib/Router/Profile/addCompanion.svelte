<script>
    import { onMount } from "svelte";
    import axios from "axios";
    import Cookies from 'js-cookie';
    import { navigate } from 'svelte-routing';

    let modalBlok = false;

    function toggleModal() {
        modalBlok = !modalBlok;
    }
    // console.log('Токен:', Cookies.get('token'));
    // Переменные для формы
    let name = '';
    let surname = '';
    let patronymic = '';
    let date_of_birth = '';
    let citizenship = [1];
    let sex = '';
    let token

    async function submitForm(event) {
    event.preventDefault(); 

    const travelerData = {
        name,
        surname,
        patronymic,
        date_of_birth,
        sex
    };

    // console.log('Отправляемые данные:', travelerData); // Отладка

    try {
        const response = await axios.post('http://127.0.0.1:8000/api/travelers/', travelerData, {
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${Cookies.get('token')}`,
            }
        });
        // console.log('Компаньон создан:', response.data);
        toggleModal();
    } catch (error) {
        if (error.response) {
            if (error.response.status === 401) {
                await refreshTokenFunc(); 
            }
        } else {
            // console.error('Ошибка:', error.message); 
        }
    }
}

async function refreshTokenFunc() {
    try {
      const response = await axios.post('http://localhost:8000/api/auth/jwt/refresh/', {
        refresh: Cookies.get("refreshToken")
      });
      token = response.data.access
      Cookies.set("tokenRes", token)
      console.log('Обновление токена:', token);
      return token
    } catch (error) {
      console.error('Ошибка обновления токена:', error.response.data);
      navigate('/');
    }
  }
</script>

<main on:click={toggleModal}>
    <svg width="33" height="33" viewBox="0 0 33 33" fill="none" xmlns="http://www.w3.org/2000/svg">
        <g clip-path="url(#clip0_9_96)">
            <path d="M16.4488 18.3163C21.0534 18.3163 24.7883 14.5814 24.7883 9.97673C24.7883 5.37208 21.0534 1.66278 16.4488 1.66278C11.8441 1.66278 8.10925 5.39766 8.10925 9.97673C8.10925 14.5558 11.8441 18.3163 16.4488 18.3163ZM16.4488 3.8372C19.8255 3.8372 22.5883 6.59999 22.5883 9.97673C22.5883 13.3535 19.8255 16.1163 16.4488 16.1163C13.072 16.1163 10.3093 13.3535 10.3093 9.97673C10.3093 6.59999 13.072 3.8372 16.4488 3.8372Z" fill="#0162CD"/>
            <path d="M2.0209 31.3372H30.979C31.593 31.3372 32.079 30.8512 32.079 30.2372C32.079 24.4814 27.3976 19.7744 21.6162 19.7744H11.3837C5.62788 19.7744 0.920898 24.4558 0.920898 30.2372C0.920898 30.8512 1.40694 31.3372 2.0209 31.3372ZM11.3837 21.9744H21.6162C25.8116 21.9744 29.2651 25.0953 29.8023 29.1372H3.19764C3.73485 25.1209 7.18834 21.9744 11.3837 21.9744Z" fill="#0162CD"/>
            <rect x="19" y="25.4977" width="3.39906" height="16" rx="1" transform="rotate(-90 19 25.4977)" fill="white"/>
            <rect x="25" y="17" width="4" height="13.5962" rx="1" fill="white"/>
            <rect x="20" y="24.6479" width="1.69953" height="14" transform="rotate(-90 20 24.6479)" fill="#0162CD"/>
            <rect x="26" y="17.8498" width="2" height="11.8967" fill="#0162CD"/>
        </g>
        <defs>
            <clipPath id="clip0_9_96">
                <rect width="33" height="33" fill="white"/>
            </clipPath>
        </defs>
    </svg>
    <p>Добавить</p>
</main>

{#if modalBlok}
<div class="modal">
    <div class="modal-content">
        <span class="close" on:click={toggleModal}>&times;</span>
        <h2>Создать компаньона</h2>
        <form on:submit={submitForm}>
            <div class="block">
                <div class="test">
                    <div class="input">
                        <input type="text" id="name" bind:value={name} required />
                        <label for="name">Имя</label>
                    </div>
        
                    <div class="input">
                        <input type="text" id="surname" bind:value={surname} required />
                        <label for="surname">Фамилия</label>
                    </div>
        
                    <div class="input">
                        <input type="text" id="patronymic" bind:value={patronymic} />
                        <label for="patronymic">Отчество</label>
                    </div>
                </div>
    
                <div class="test">
                    <div class="input">
                        <input type="date" id="birthdate" bind:value={date_of_birth} required />
                        <label for="birthdate">Дата рождения</label>
                    </div>
        
                    <div class="input b">
                        <select id="citizenship"  required>
                            <option value="" disabled selected>Выберите гражданство</option>
                            <option value="Россия">Россия</option>
                            <option value="США">США</option>
                            <option value="Канада">Канада</option>
                            <option value="Другие">Другие</option>
                        </select>
                        <label for="citizenship">Гражданство</label>
                    </div>
        
                    <div class="input b">
                        <select id="gender" bind:value={sex} required>
                            <option value="" disabled selected>Выберите пол</option>
                            <option value="Мужчина">Мужчина</option>
                            <option value="Женщина">Женщина</option>
                            <option value="Другой">Другой</option>
                        </select>
                        <label for="gender">Пол</label>
                    </div>
                </div>
            </div>
            <button type="submit">Добавить</button>
        </form>
    </div>
</div>
{/if}

<style>
    main {
        display: flex;
        align-items: center;
        cursor: pointer;
    }


    .modal {
        display: flex;
        justify-content: center;
        align-items: center;
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background-color: rgba(0, 0, 0, 0.5);
        z-index: 1000;
    }

    .modal-content {
        background-color: white;
        padding: 20px;
        border-radius: 5px;
        width: 600px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        position: relative;
    }

    .close {
        position: absolute;
        top: 10px;
        right: 15px;
        font-size: 20px;
        cursor: pointer;
    }

    h2 {
        margin-bottom: 20px;
        color: #0162CD;
    }

    .input{
        position: relative;
        margin-bottom: 15px;
    }

    .input.b label{
        background-color: #eeeeee;
        border-top-left-radius: 5px;
        border-top-right-radius: 5px;
    }

    input[type="text"],
    input[type="date"],
    select {
        width: 100%;
        padding: 10px;
        margin-bottom: 10px;
        border: 1px solid #ccc;
        border-radius: 4px;
        box-sizing: border-box;
        color: grey;
        font-size: 14px;
        transition: border-color 0.3s ease;
        outline: none;
    }

    label {
        position: absolute;
        left: 12px;
        top: 12px;
        transition: 0.2s ease all;
        color: #aaa;
        pointer-events: none;
        background: white; /* Добавлено для фона */
        padding: 0 4px; /* Добавлено для отступа */
    }

    /* Анимация при фокусе и наличии текста */
    .input input:focus + label,
    .input input:not(:placeholder-shown) + label {
        top: -10px; /* Поднимаем label */
        left: 12px; /* Сдвигаем label */
        font-size: 12px; /* Уменьшаем размер шрифта */
        color: #808080; /* Изменяем цвет текста */
    }

    .input select:focus + label,
    .input select:not([value=""]) + label {
        top: -10px; /* Поднимаем label */
        left: 12px; /* Сдвигаем label */
        font-size: 12px; /* Уменьшаем размер шрифта */
        color: #808080; /* Изменяем цвет текста */
    }
    
    button {
        background-color: #0162CD;
        color: white;
        border: none;
        padding: 10px;
        border-radius: 5px;
        cursor: pointer;
        width: 100%;
        font-size: 16px;
    }

    button:hover {
        background-color: #014f9f;
    }

    main {
        width: 261px;
        border: 0.2px solid #49494931;
        border-radius: 5px;
        padding: 10px;
        display: flex;
        flex-direction: column;
        flex-grow: 1;
        height: auto;
        justify-content: center;
        align-items: center;
    }

    p {
        font-size: 12px;
        font-weight: 300;
        line-height: 14.22px;
        color: gray;
        transition: 0.3s;
    }

    .block {
        display: flex;
        gap: 20px;
        justify-content: center;
        align-items: center;
    }

    .test {
        display: flex;
        flex-direction: column;
        flex-grow: 1;
    }

    form {
        display: flex;
        flex-direction: column;
    }

    p:hover {
        color: var(--color);
    }
</style>