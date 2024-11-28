<script>
	import mainPhoto from '../assets/main-photo.png';
    import mainPhotoBlur from '../assets/blur.png';

    import { onMount, onDestroy } from 'svelte';

let city = '';
let arrival = '';
let departure = '';
let passengers = 1;
let availableCities = ['Отель', 'Квартира', 'Коттедж']; // Заданные города
let apartments = []; // Массив квартир
let selectedCity = ''; // Выбранный город
let loading = false; // Флаг загрузки данных

// Загрузка квартир при выборе города
async function loadApartments() {
  loading = true;
  // ... (запрос на API для получения квартир по городу)
  loading = false;
}

// Обработчик выбора города
function handleCityChange(event) {
  selectedCity = event.target.value;
  loadApartments();
}

// Обработчик поиска
async function findApartments() {
  // Проверка полей
  if (!selectedCity || !arrival || !departure || !passengers) {
    alert('Пожалуйста, заполните все поля');
    return;
  }

  // Проверка занятости дней
  if (arrival >= departure) {
    alert('Дата въезда должна быть раньше даты выезда');
    return;
  }

  // ... (Проверка занятости дат для каждой квартиры)
  console.log('Поиск квартир:', selectedCity, arrival, departure, passengers);
}

// Очистка данных при размонтировании компонента
onDestroy(() => {
  availableCities = [];
  apartments = [];
});
</script>

<main>
    <div class="photo">
            <img id="one" src="{mainPhoto}" alt="">
            <img id="two" src="{mainPhotoBlur}" alt="">

            <div class="main-text">
                <h2 id="middle">Комфортное жилье – шаг к лучшей жизни!</h2>
                <p id="noMiddle">Снимайте, наслождайтесь, не беспокойтесь!</p>                
            </div>
    </div>

    <div class="poisck">
        <div class="block1">
            <form action="">
                <div class="container">
                    {#if loading}
                      <p>Загрузка Данных...</p>
                    {:else}
                    <div class="block">
                        <label for="city">Курорт или отель</label>
                        <hr id="line">
                        <select id="city" bind:value={selectedCity} on:change={handleCityChange}>
                            <option value="">Где хотите отдохнуть?</option>
                            {#each availableCities as city}
                            <option value={city}>{city}</option>
                            {/each}
                        </select>                        
                    </div>

                    <section>
                            <div class="block" id="veesd">
                                <label for="arrival">Въезд:</label>
                                <input type="date" id="arrival" bind:value={arrival} />                        
                            </div>

                            <hr id="vert-line">

                            <div class="block" id="viesde">
                                <label for="departure">Выезд:</label>
                                <input type="date" id="departure" bind:value={departure}/>                        
                            </div>

                            <hr id="vert-line">

                            <div class="block">
                                <label for="passengers">Количество человек:</label>
                                <input id="colic" type="number" min="1" value={1} />
                            </div>

                        
                        <button id="block2" type="button" on:click={findApartments}>Найти</button>                            
                    </section>


                  

                      
                    {/if}
                  
                    {#if apartments.length > 0}
                      <h2>Доступные квартиры</h2>
                      <ul>
                        {#each apartments as apartment}
                          <li>
                            <h3>{apartment.name}</h3>
                            <p>Цена: {apartment.price} руб.</p>
                            <p>Описание: {apartment.description}</p>
                            <button type="button" on:click={() => {
                              // Логика бронирования квартиры
                              console.log('Бронирование:', apartment.id); 
                            }}>Забронировать</button>
                          </li>
                        {/each}
                      </ul>
                    {/if}
                  
                  </div>
            </form>
        </div>
    </div>
</main>

<style>

#colic{
    border: none;
    margin-top: 10px;
    border-bottom: solid 1px rgba(128, 128, 128, 0.705);
}    

#vert-line{
    width: 60px;
    height: 1px;
    transform: rotate(90deg);
    background-color: rgba(128, 128, 128, 0.705);
    border: none;
}

input[type="date"]{
    border: none;
}

#veesd, #viesde{
    width: 120px;
}

section{
    display: flex;
    justify-content: center;
    align-items: center;
    flex-wrap: wrap;
    gap: 30px;
}

.container{
    display: flex;
    justify-content: space-between;
    align-items: center;
    width: 62.5vw;
    gap: 20px;
    flex-wrap: wrap;
}

.block{
    display: flex;
    flex-direction: column;
    align-items: self-start;
    justify-content: center;
    width: 200px;
    flex-wrap: wrap;
}

#noMiddle{
    background-color: white;
    padding: 5px 25px 5px 25px;
    border-bottom-left-radius: 20px;
    border-bottom-right-radius: 20px;
    box-shadow: 0 4px 5px black;
    font-size: 1.2vw;
    font-weight: 300;
}

#middle{
    font-size: 2.1vw;
    background-color: white;
    border-radius: 20px;
    padding: 5px 25px 5px 25px;
    font-weight: Medium;
    box-shadow: 0px 4px 4px black;
}

.photo{
    position: relative; 
    display: flex;
    justify-content: center;
    align-items: center;
    margin-top: 20px;  
}
 #two{
    position: absolute;
} 

select::-ms-expand {
      display: none;
    }

    select::-moz-arrow-button {
      display: none;
    }

    select:-ms-expand {
      display: none;
    }

#city{
    border: none;    
}

#two, #one{
    width: clamp(320px,75.9vw,1700px);
    height: 600px;
    object-fit: cover;
    border-radius: 50px;
}
.main-text{
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    text-align: center;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
}

.poisck{
    width: clamp(320px,70vw,1300px);
    margin: 0 auto;
    height: 80px;
    /* box-shadow: 0 0  3px red; */
    display: flex;
    justify-content: center;
    position: relative;
    top: -50px;
    flex-wrap: wrap;
}

.block1{
    background-color: var(--colorBL);
    border-radius: 15px;
    box-shadow: 0px 2px 10px black;
    padding-left: 20px;
    display: flex;
    flex-wrap: wrap;
}

.block #line{
    width: 70%;
    margin: 5px 0px 5px 0px;
    height: 1px;
    background-color: rgba(128, 128, 128, 0.212);
    border: none;
}

#block2{
    height: 80px;
    width: 120px;
    padding: 10px;
    background-color: var(--color);
    border-radius: 15px;
    color: var(--colorBL);
    font-size: 20px;
    border: none;
    cursor: pointer;
}
</style>