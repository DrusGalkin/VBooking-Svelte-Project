<script>
  import { onMount } from 'svelte';
  import axios from 'axios';
  import { Route, Router, navigate } from 'svelte-routing';
  import { addToFavorites, getFavorites, clearFavorites } from './Router/scripts/favorites.js'
  import Cookies from 'js-cookie'; 
  export let isOpenLog = false;
  let isReg = false;
  let isLog = true;
  let email = '';
  let phone = '';
  let surname = '';
  let name = '';
  let patronymic = '';
  let password = '';
  let repeatPassword = '';
  let token = null;
  let refreshToken = null;

  // Роли
  let user = "user";
  let owner = "owner";
  let choose = user; // По умолчанию выбрать пользователя

  // Логи ошибок
  let errorEmail = '';
  let errorPhone = '';
  let errorPassword = '';
  let valid, validLog = ''


  onMount(() => {
    token = Cookies.get('token');
    refreshToken = Cookies.get('refreshToken');
  });

  function close() {
    isOpenLog = false;
  }

  function openReg() {
    isLog = false;
    isReg = true;
  }

  function openLog() {
    isLog = true;
    isReg = false;
  }

  function chooseUser() {
    choose = user; 
  }

  function chooseOwner() {
    choose = owner;
  }

  // Регистрация
  async function registerUser(event) {
    event.preventDefault();
    resetErrors();

    if (password !== repeatPassword) {
        errorPassword = 'Пароли не совпадают';
        return;
    }

    try {
        const response = await axios.post('http://localhost:8000/api/users/', {
            email,
            phone,
            surname,
            name,
            patronymic,
            password,
            position: choose
        });

        console.log('Регистрация прошла успешно:', response.data);
        await addFavoritesToUser(response.data.id); // Добавьте избранные в базу данных
        openLog();
    } catch (error) {
        console.log(error);
    }
}

  function resetErrors() {
    errorEmail = '';
    errorPhone = '';
    errorPassword = '';
  }

  // Логин
  async function loginUser(event) {
    event.preventDefault();
    resetErrors();

    try {
      const response = await axios.post('http://localhost:8000/api/auth/jwt/create/', {
        email,
        password
      });

      localStorage.setItem("pass", password)
      localStorage.setItem("email", email)

      token = response.data.access;
      refreshToken = response.data.refresh;

      Cookies.set('token', token,  { expires: 7, path: '/' });
      Cookies.set('refreshToken', refreshToken,  { expires: 7, path: '/' });

      await makeRequest();
      navigate('/profile');
    } catch (error) {
      console.error('Ошибка входа:', error.response.data);
      validLog = "Не верный логин или пароль"

      Object.assign(valid.style,{
        opacity : 1,
        transition : "0.3s",
        color : "red",
      })
      setTimeout(() => {
          Object.assign(valid.style, {
          opacity : 0,
        });
      }, 3000);
    }
  }

async function addFavoritesToUser(userId) {
    const favorites = getFavorites();
    if (favorites.length > 0) {
        try {
            for (const id of favorites) {
                await axios.get(`http://localhost:8000/api/objects/${id}/add_to_favorites/?user_id=${userId}`);
            }
            clearFavorites(); 
        } catch (error) {
            console.error('Ошибка при добавлении избранных:', error);
        }
    }
}

async function makeRequest() {
    try {
      const headers = {
        Authorization: `Bearer ${Cookies.get("token")}`
      };
      const response = await axios.get('http://localhost:8000/api/users/profile/', { headers });
      Cookies.set("info", JSON.stringify(response.data), { expires: 7 });
      localStorage.setItem("info", response.data)
      return response.data.id;
    } catch (error) {
      console.error('Ошибка при выполнении запроса:', error.response.status);
      if (error.response.status === 401) {
        await refreshTokenFunc(); // Обновляем токен
        return await makeRequest(); // Повторяем запрос
      } else {
        throw error;
      }
    }
  }

  // Обновление токена
  async function refreshTokenFunc() {
    try {
      const response = await axios.post('http://localhost:8000/api/auth/jwt/refresh/', {
        refresh: Cookies.get("refreshToken")
      });

      token = response.data.access;
      Cookies.set('token', token, { expires: 7 }); // Обновляем токен в куки
    } catch (error) {
      console.error('Ошибка обновления токена:', error.response.data);
      navigate('/'); // Перенаправляем при ошибке
    }
  }

</script>

{#if isOpenLog}
  <div class="modal">
    <div class="modal-content">
      <div class="block">
        <span class="close" on:click={close}>&times;</span>
 
        {#if isLog}
        <div class="validLog">
          <p id="validLog" bind:this = {valid}>{validLog}</p>
          <h2>Вход</h2> 
        </div>
        {/if}
      
        {#if isReg}
          <h2>Регистрация</h2>
        {/if}
      </div>
      {#if isReg}
      <div class="chooseReg">
        <button class="role-button" on:click={chooseUser}>Пользователь</button>  
        <button class="role-button" on:click={chooseOwner}>Владелец</button>  
      </div>

        <form on:submit={registerUser}>
          <div class="test {errorEmail ? 'error' : ''}">
            <input class="test_input" id="email" type="text" bind:value={email} placeholder=" " />
            <label class="test_label" for="email">Эл. Почта</label>
            <p>{errorEmail}</p>
          </div>

          <div class="test {errorPhone ? 'error' : ''}">
            <input class="test_input" id="phone" type="text" bind:value={phone} placeholder=" " />
            <label class="test_label" for="phone">Номер телефона</label>
            <p>{errorPhone}</p>
          </div>

          <div class="test">
            <input class="test_input" id="lastName" type="text" bind:value={surname} placeholder=" " />
            <label class="test_label" for="lastName">Фамилия</label>
          </div>

          <div class="test">
            <input class="test_input" id="firstName" type="text" bind:value={name} placeholder=" " />
            <label class="test_label" for="firstName">Имя</label>
          </div>

          <div class="test">
            <input class="test_input" id="middleName" type="text" bind:value={patronymic} placeholder=" " />
            <label class="test_label" for="middleName">Отчество</label>
          </div>

          <div class="test {errorPassword ? 'error' : ''}">
            <input class="test_input" id="password" type="password" bind:value={password} placeholder=" " />
            <label class="test_label" for="password">Пароль</label>
            <p>{errorPassword}</p>
          </div>

          <div class="test">
            <input class="test_input" id="repeatPassword" type="password" bind:value={repeatPassword} placeholder=" " />
            <label class="test_label" for="repeatPassword">Повторите пароль</label>
          </div>

          <div class="button">
            <a class="switch-link" on:click={openLog}>Вход</a>
            <button class="submit-button" type="submit">Отправить</button>
          </div>
        </form>
      {/if}

      {#if isLog}
        <form id="log" on:submit={loginUser}>
          <div class="test {errorEmail ? 'error' : ''}">
            <input class="test_input" id="email" type="text" bind:value={email} placeholder=" " />
            <label class="test_label" for="email">Эл. Почта</label>
            <p>{errorEmail}</p>
          </div>

          <div class="test">
            <input class="test_input" id="password" type="password" bind:value={password} placeholder=" " />
            <label class="test_label" for="password">Пароль</label>
          </div>


          <div class="button">
            <a class="switch-link" on:click={openReg}>Регистрация</a>
            <button class="submit-button" type="submit">Отправить</button>
          </div>
        </form>
      {/if}
    </div>
  </div>
{/if}
<style>
  .validLog{
    display: flex;
    flex-direction: row-reverse;
    align-items: center;
    gap: 10px;
  }

  #validLog{
    text-align: center;
    color: red;
    font-size: 13px;
  }

  .block h2{
    font-size: 25px;
  }

  form {
    width: 100%; 
  }

  #log {
    margin-top: 20px;
  }

  .test {
    position: relative;
    margin-bottom: 1.5em;
    width: 100%; 
  }

  .test_input {
    width: 100%;
    padding: 0.8em;
    border: 1px solid #ccc;
    border-radius: 4px;
    font-size: 1em;
    outline: none;
    box-sizing: border-box;
    transition: border-color 0.3s ease;
  }

  .test_input:focus {
    border-color: #007BFF;
  }

  .test_label {
    position: absolute;
    top: 1.1em;
    left: 0.8em;
    font-size: 0.85em;
    color: darkgray;
    transition: all 0.2s ease-in-out;
    pointer-events: none;
  }

  .test_input:focus + .test_label,
  .test_input:not(:placeholder-shown) + .test_label {
    top: -0.75em;
    left: 0.8em;
    font-size: 0.75em;
    color: #007BFF;
    background-color: white;
    padding: 0 0.2em;
  }

  .test p {
    font-size: 10px;
    color: red;
    margin-top: 0.25em;
  }

  .button {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  .switch-link {
    color: #007BFF;
    text-decoration: none;
    cursor: pointer;
    transition: color 0.3s ease;
  }

  .switch-link:hover {
    color: #0056b3;
  }

  .submit-button {
    background-color: #007BFF;
    color: white;
    padding: 0.7em 1.5em;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    transition: background-color 0.3s ease;
  }

  .submit-button:hover {
    background-color: #0056b3;
  }

  .modal {
    display: block;
    position: fixed;
    z-index: 1;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    overflow: auto;
    background-color: rgba(0, 0, 0, 0.4);
    padding-top: 60px;
    animation: fadeIn 0.6s;
  }

  @keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
  }

  .modal-content {
    background-color: #fefefe;
    margin: 5% auto;
    padding: 20px;
    border: 1px solid #888;
    width: 90%;
    max-width: 500px;
    border-radius: 10px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  .block {
    display: flex;
    justify-content: space-between;
    align-items: center;
    width: 100%;
    flex-direction: row-reverse;
  }

  .close {
    color: #aaa;
    font-size: 28px;
    font-weight: bold;
    cursor: pointer;
    transition: color 0.3s ease;
  }

  .close:hover {
    color: black;
  }

  .chooseReg {
    display: flex;
    justify-content: center;
    gap: 10px;
    margin-bottom: 20px;
  }

  .role-button {
    background-color: #f0f0f0;
    border: 1px solid #ccc;
    border-radius: 4px;
    padding: 0.5em 1em;
    cursor: pointer;
    transition: background-color 0.3s ease, border-color 0.3s ease;
  }

  .role-button:hover {
    background-color: #e0e0e0;
    border-color: #bbb;
  }
</style>