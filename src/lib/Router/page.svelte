<script>
  import { onMount } from 'svelte';
  import { addToFavorites, getFavorites } from './scripts/favorites'; 
  import Cookies from 'js-cookie';
  import axios from "axios";

  export let filteredApartments; 
  let isLoggedIn = false;

  console.log(filteredApartments)

  onMount(() => {
      isLoggedIn = !!Cookies.get('token'); 
  });

  async function addToFavoritesHandler(apartment) {
    if (isLoggedIn) {
        try {
            const response = await axios.get(`/api/objects/${apartment.id}/add_to_favorites/`);
            console.log('Добавлено в избранное:', response.data);
        } catch (error) {
            console.error('Ошибка при добавлении в избранное:', error.response ? error.response.data : error.message);
        }
    } else {
        addToFavorites(apartment.id);
        console.log('Сохранено в куки:', apartment.id);
    }
}

  function next(index) {
      filteredApartments[index].currentIndex = (filteredApartments[index].currentIndex + 1) % filteredApartments[index].images.length;
  }

  function previous(index) {
      filteredApartments[index].currentIndex = (filteredApartments[index].currentIndex - 1 + filteredApartments[index].images.length) % filteredApartments[index].images.length;
  }
</script>

{#if filteredApartments.length > 0}
  {#each filteredApartments as apartment, index}
  <div class="container">
      <div class="block1">
          <div class="slider">
              {#if !apartment.currentIndex}
                {apartment.currentIndex = 0} <!-- Инициализация текущего индекса -->
              {/if}
              <div class="slides" style="transform: translateX(-{apartment.currentIndex * 100}%)">
                  {#each apartment.images as image}
                      <div class="slide">
                          <img src={image} alt={apartment.title} />
                      </div>
                  {/each}
              </div>
              {#if apartment.images.length > 1} <!-- Отображаем стрелки только если больше одного изображения -->
                  <button class="button button-left" on:click={() => previous(index)} disabled={apartment.currentIndex === 0}>◀</button>
                  <button class="button button-right" on:click={() => next(index)} disabled={apartment.currentIndex === apartment.images.length - 1}>▶</button>
              {/if}
          </div>
      </div>

      <div class="block2">
          <div class="start">
              <h1 class="title">{apartment.title}</h1>
              <p class="description">{apartment.description}</p>
              <div class="features-container">
                  <div class="features">
                    <p>{apartment.city}</p>
                    <p>Количество комнат: {apartment.features?.rooms}</p>
                    <p>Площадь: {apartment.features?.area} м²</p>
                    <p>Этаж: {apartment.features?.floor}</p>
                    <p>Максимальное количество гостей: {apartment.features?.maxGuests}</p>
                    <button on:click={() => addToFavoritesHandler(apartment)}>Добавить в избранное</button>
                  </div>
              </div>
              <div class="blockPrice">
                  <p class="price">Цена: {apartment.minPrice} руб. в сутки</p>
              </div>
          </div>
          <div class="end">
              <button class="contact-button">Связаться с хозяином</button>
          </div>
      </div>
  </div>
  {/each}
{:else}
  <p>Нет доступных квартир для вашего поиска.</p>
{/if}
<style>
  * {
    box-sizing: border-box;
  }

  .block1{
    width: 500px;
  }

  .info {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 10px;
  }

  .start {
    padding: 0 20px 0 20px;
  }

  .end {
    margin-top: 40px;
  }

  .block2 {
    display: grid;
    width: 700px;
    height: 500px;
    grid-template-rows: 1fr auto;
  }

  .container {
    max-width: 1200px;
    display: flex;
    justify-content: center;
    background: white;
    border-radius: 8px;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
  }

  .slider {
    position: relative;
    width: 100%;
    height: 100%;
    overflow: hidden;
    border-radius: 8px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  }

  .slides {
    display: flex;
    transition: transform 0.5s ease;
    width: 100%;
    height: 100%;
  }

  .slide {
    min-width: 100%;
    height: 100%;
  }

  .slide img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    border-radius: 8px;
  }

  .button {
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    background-color: rgba(255, 255, 255, 0.329);
    box-shadow: 0 0 3px rgba(0, 0, 0, 0.281);
    color: rgb(37, 37, 37);
    border: none;
    padding: 10px 15px;
    cursor: pointer;
    border-radius: 100%;
    transition: background-color 0.3s;
  }

  .button-left {
    left: 10px;
  }

  .button-right {
    right: 10px;
  }

  .button:hover {
    background-color: rgba(172, 172, 172, 0.705);
  }

  .title {
    font-size: 28px;
    margin: 20px 0;
    color: #333;
    text-align: center;
  }

  .description {
    margin: 20px 0;
    font-size: 16px;
    line-height: 1.5;
    color: #555;
  }

  .price {
    font-size: 24px;
    color: var(--color);
    margin: 10px 0;
    text-align: end;
  }

  .features-container {
    margin: 20px 0;
    text-align: center;
  }

  .features {
    margin-top: 10px;
    font-size: 16px;
    color: #555;
    text-align: left;
    padding: 10px;
    border: 1px solid #ddd;
    border-radius: 5px;
    background-color: #f9f9f9;
  }

  .contact-button {
    background-color: var(--color);
    color: white;
    padding: 12px 20px;
    border: none;
    border-bottom-right-radius: 5px;
    border-top-right-radius: 5px;
    cursor: pointer;
    width: 100%;
    transition: background-color 0.3s;
  }

  .contact-button:hover {
    background-color: #39087c;
  }

  @media (max-width: 600px) {
    .title {
      font-size: 24px;
    }

    .price {
      font-size: 20px;
    }

    .contact-button {
      padding: 10px;
    }
  }
</style>