<script>
  import { userStore } from '../userStore.js';
  import { onMount } from 'svelte';
  import axios from 'axios';
  import { navigate } from 'svelte-routing';
  import Cookies from 'js-cookie';
  import Page from './page.svelte';

  export let image = 'https://gb1.ru/local/templates/gb1-fishera/i/no_photo.png'; 
  const info = JSON.parse(Cookies.get('info') || '{}');
  let infoUser = true; 
  let { surname, name, patronymic, email, phone, position } = info;
  let positionUser = '';
  let showMenu = false;
  let showTooltip = false;
  let filteredApartments = []; // Для хранения загруженных объектов
  let showObjects = false; // Флаг для показа объектов
  let activeTab = ''; // Переменная для отслеживания активного таба
  let users = []; // Для хранения списка пользователей
  let showUsers = false; 
  console.log(info);

  function toggleMenu() {
    showMenu = !showMenu; 
  }

  function itsPosition() {
    if (position === "admin") positionUser = "Администратор";
    if (position === "user") positionUser = "Пользователь";
    if (position === "owner") positionUser = "Арендодатель";
    
    return positionUser;
  }

  function reloade() {
    window.location.reload();
  }

  if (!Cookies.get("token")) {
    navigate("/");
    reloade();
  }

  onMount(() => {
    const uploadButton = document.getElementById('uploadButton');

    uploadButton.addEventListener('change', async (event) => {
      const file = event.target[0]; // Получаем файл

      if (file) {
        try {
          const formData = new FormData();
          formData.append('image', file); // Добавляем файл в FormData

          const response = await fetch('URL_ДЛЯ_ЗАГРУЗКИ_ИЗОБРАЖЕНИЯ', {
            method: 'POST',
            body: formData
          });

          if (response.ok) {
            const data = await response.json();
            image = data.imageUrl; // Обновите путь к изображению
            console.log('Изображение успешно загружено:', data.imageUrl);
          } else {
            console.error('Ошибка загрузки изображения:', response.status);
          }
        } catch (error) {
          console.error('Ошибка загрузки изображения:', error);
        }
      }
    });
  });

  async function fetchUsers() {
  try {
    const token = Cookies.get("token"); // Получаем токен из cookies
    const response = await axios.get('http://localhost:8000/api/users/profile/');
    users = response.data; // Сохраняем пользователей
    console.log(users)
    showUsers = true; // Показываем пользователей
  } catch (error) {
    console.error('Ошибка при получении пользователей:', error);
    if (error.response && error.response.status === 401) {
    }
  }
}

  fetchUsers()
  async function fetchCityName(cityId) {
    try {
      const response = await axios.get(`http://localhost:8000/api/city/${cityId}/`);
      return response.data.name; 
    } catch (error) {
      console.error('Ошибка при получении названия города:', error);
      return null; 
    }
  }

  async function fetchObjects() {
    try {
      const response = await axios.get('http://localhost:8000/api/objects/');
      const fetchedApartments = await Promise.all(response.data.map(async (object) => {
        const cityName = await fetchCityName(object.address.city);
        return {
          id: object.id,
          city: cityName || object.address.city, 
          street: object.address.street, 
          house: object.address.house, 
          seaDistance: object.address.sea_distance, 
          title: object.name, 
          description: object.description || "Нет описания", 
          minPrice: object.min_price, 
          type: object.type, 
          images: object.images.length > 0 ? object.images.map(image => image.media) : [], 
          tags: object.tags.map(tag => tag.title)
        };
      }));

      filteredApartments = fetchedApartments;
      showObjects = true; 
    } catch (error) {
      console.error('Ошибка при получении данных:', error);
    }
  }

  async function deleteObject(id) {
    if (confirm('Вы уверены, что хотите удалить этот объект?')) {
      try {
        await axios.delete(`http://localhost:8000/api/objects/${id}/`);
        // Удаляем объект из списка после успешного удаления
        filteredApartments = filteredApartments.filter(object => object.id !== id);
        console.log(`Объект с id ${id} успешно удален`);
      } catch (error) {
        console.error('Ошибка при удалении объекта:', error);
      }
    }
  }


  function exit() {
    Cookies.remove("token");
    Cookies.remove("refreshToken");
    Cookies.remove("info");
    localStorage.removeItem("")
    navigate("/");
    reloade();
  }

  function handleDoorClick() {
    navigate('/');
  }

  function toggleObjects(tab) {
    if (tab === 'objects') {
      // Если текущий таб - объекты
      if (activeTab === 'objects') {
        // Если объекты уже активны, скрываем их
        showObjects = false;
        activeTab = ''; // Сбрасываем активный таб
      } else {
        // Скрываем пользователей, показываем объекты
        activeTab = 'objects';
        infoUser = false;
        fetchObjects();
      }
    } else if (tab === 'users') {

      if (activeTab === 'users') {
        // Если пользователи уже активны, скрываем их
        infoUser = true;
        showObjects = false; // Скрываем объекты
        activeTab = ''; // Сбрасываем активный таб
      } else {
        activeTab = 'users';
        infoUser = true;
        showObjects = false; 
        fetchUsers();
      }
    }
  }
</script>

<main>
  <nav>
    <div class="profile-title"
      on:mouseover={() => showTooltip = true}
      on:mouseout={() => showTooltip = false}
      on:click={handleDoorClick}  
    >
      <h1>Личный кабинет</h1>
      <svg version="1.1" id="Capa_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 512 512" style="enable-background:new 0 0 512 512;" xml:space="preserve"><g><g><path d="M299.29,255.5h-86.58c-85.14,0-154.42,69.27-154.42,154.42V512h395.42V409.92C453.71,324.77,384.43,255.5,299.29,255.5z M88.29,482v-72.08c0-68.61,55.82-124.42,124.42-124.42h86.58c68.6,0,124.42,55.81,124.42,124.42V482H88.29z"/></g></g><g><g><path d="M256,0c-65.84,0-119.41,53.57-119.41,119.41S190.16,238.82,256,238.82s119.41-53.57,119.41-119.41S321.84,0,256,0z M256,208.82c-49.3,0-89.41-40.11-89.41-89.41C166.59,70.11,206.7,30,256,30s89.41,40.11,89.41,89.41 C345.41,168.71,305.3,208.82,256,208.82z"/></g></g></svg>
      {#if showTooltip}
        <div class="tooltip">
          Вернуться на главную страницу
        </div>
      {/if}
    </div>

    {#if position === "admin"}
      <div class="AdminTools">
        <p on:click={() => toggleObjects('objects')} style="background: {activeTab === 'objects' ? 'white' : 'none'}; color: {activeTab === 'objects' ? 'black' : 'white'}">
          Объекты</p>

        <p id="one" on:click={() => toggleObjects('users')} style="background: {activeTab === 'users' ? 'white' : 'none'}; color: {activeTab === 'users' ? 'black' : 'white'}"
          >Пользователи</p>  
      </div>
    {/if}

    <div class="menu-container">
      <svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="currentColor" class="bi bi-list" viewBox="0 0 16 16" on:click={toggleMenu}>
        <path fill-rule="evenodd" d="M1 12h14v1H1v-1zm0-5h14v1H1V7zm0-5h14v1H1V2z"/>
      </svg>
      {#if showMenu}
        <div class="dropdown-menu">
          <p>Что-то еще будет</p>
          <hr>
          <p>Что-то еще будет</p>
          <hr>
          <p id="textExit" on:click={exit}>Выход</p>
        </div>
      {/if}
    </div>
  </nav>
  
  <div class="container">
    <section>
      {#if infoUser}
        <div class="profile-container">
          <div class="photo">
            <p>{itsPosition()}</p>
            <img src="{image}" alt="User Photo">
            <div class="upload-container">
              <input type="file" id="uploadButton" accept="image/*" hidden /> 
              <label id="textLebel" for="uploadButton">Загрузить изображение</label> 
            </div>
          </div>
          
          <div class="blockInfo">
              <div class="FIO">
                {surname} {name} {patronymic}
              </div>
              <div class="contact-info">
                <p><strong>Email:</strong> {email}</p>
                <p><strong>Телефон:</strong> {phone}</p>
              </div>
          </div>
        </div>
      {/if}
      <div class="blockss">
        {#if showObjects}
        {#each filteredApartments as apartment}
        <div class="apartaments">
          <div class="images">
     
            <img src={apartment.images.length > 0 ? apartment.images[0] : 'https://gb1.ru/local/templates/gb1-fishera/i/no_photo.png'} alt={apartment.title} />
      
          </div>

          <div class="infoObject">
            <h3>{apartment.title}</h3>
            <p>{apartment.description}</p>
            <button on:click={() => deleteObject(apartment.id)}>Удалить</button>
          </div>
        </div>
      {/each}
        {/if}
      </div>
    </section>
  </div>
</main>

<style>
  .infoObject{
    width: 300px;
    display: flex;
    justify-content: center;
    flex-direction: column;
    align-items: center;
  }

  .apartaments{
    display: flex;
  }

  .images {
    width: 300px;
    height: 300px;
  }

  .images img{
    width: 100%;
    height: 100%;
    object-fit: cover;
  }

  .AdminTools p{
    display: flex;
    justify-content: center;
    padding: 0 10px 0 10px;
    text-align: center;
    border-left: 1px rgba(255, 255, 255, 0.363) solid;
    transition: all 0.3s ease 0s;
  }

  .AdminTools{
    display: flex;
    justify-content: center;
  }

  .blockss{
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    gap: 30px;
  }

  .profile-title svg{
    width: 25px;
    height: 25px;
    fill: white;
  }

   .profile-title {
    display: flex;
    align-items: center;
    align-items: center;
    gap: 10px;
    position: relative;
  }

  .tooltip {
    position: absolute;
    top: 40px;
    left: 0;
    background-color: #ffffff;
    border: 1px solid #ccc;
    padding: 5px;
    color: black;
    border-radius: 5px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  }

  .profile-title {
    cursor: pointer;
    transition: transform 0.2s;
  }

  .profile-title:hover {
    transform: scale(1.02);
  }

  #textLebel{
    font-size: 14px;
  }

  #textExit{
    color: red;
  }

  hr{
    border: none;
    background-color: rgba(128, 128, 128, 0.116);
    height: 2px;
  }

  .dropdown-menu p {
    color: gray;
    padding: 10px 0 10px 0;
    text-wrap: nowrap;
  }

  .menu-container {
    position: relative;
  }

  nav {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background-color: #007BFF;
    color: white;
    padding: 15px 20px;
  }

  .dropdown-menu {
    position: absolute;
    right: 0;
    background-color: white;
    border-radius: 5px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
    z-index: 1000;
    margin-top: 5px;
    padding: 10px;
    min-width: 200px;
    width: 100%;
  }

  .dropdown-menu p {
    cursor: pointer;
    margin: 0;
    padding: 5px 10px;
    transition: background-color 0.3s;
  }

  .dropdown-menu p:hover {
    background-color: #f0f4f8;
  }

  .container{
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
  }

  body {
    font-family: 'Arial', sans-serif;
    background-color: #f0f4f8;
    margin: 0;
    padding: 0;
  }

  .profile-container {
    display: flex;
    padding: 30px;
    justify-content: space-between;
    background-color: #ffffff;
    border-radius: 10px;
    margin-top: 20px;
  }

  .blockInfo {
    display: flex;
    flex-direction: column;
    justify-content: start;
    align-items: center;
    padding: 20px;
    width: 60%;
  }

  .FIO {
    font-size: 26px;
    text-wrap: nowrap;
    font-weight: bold;
    margin-bottom: 10px;
    color: #333;
  }

  .contact-info {
    font-size: 16px;
    color: #555;
    text-wrap: nowrap;

  }

  .photo {
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 30%;
  }

  .photo img {
    width: 150px;
    height: 150px;
    border-radius: 50%;
    border: 5px solid #007BFF;
    margin-bottom: 10px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
  }

  .upload-container {
    text-wrap: nowrap;
    background-color: #007BFF;
    color: white;
    border-radius: 5px;
    padding: 10px;
    text-align: center;
    cursor: pointer;
    transition: background-color 0.3s ease;
  }

  .upload-container:hover {
    background-color: #0056b3;
  }

  main {
    width: 100%;
    display: flex;
    justify-content: center;
    flex-direction: column;
  }

  section {
    margin: 20px;
    width: 100%;
    min-width: 300px;
    max-width: 700px;
    border: 2px rgba(128, 128, 128, 0.192) solid;
    background-color: #ffffff;
    display: flex;
    flex-direction: column;
    border-radius: 10px;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
  }

  .photo p{
    margin: 0px 0 20px 0;
    font-size: 20px;
  }

  @media(max-width:755px){
    .profile-container{
      flex-direction: column;
      justify-content: center;
      align-items: center;
    }
  }

  @media(max-width:400px){
    .FIO{
      font-size: 21px;
    }
  }
</style>