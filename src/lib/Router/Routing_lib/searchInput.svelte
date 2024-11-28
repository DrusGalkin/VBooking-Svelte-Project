<script>
  import {  Route, Router, navigate } from 'svelte-routing';
  import axios from 'axios';
  import { onMount } from 'svelte';

    async function goToAboutPage(params) {
      navigate((`/search?${params}`));
    }
    let availableCities = []; // Массив для хранения городов

    async function fetchCities() {
        try {
            const response = await axios.get('http://localhost:8000/api/city/'); 
            // console.log(response.data.map(city => city.name))
            availableCities = response.data.map(city => city.name)
        } catch (error) {
            console.error('Ошибка при получении городов:', error);
        }
    }

    onMount(() => {
        fetchCities();
    });

    export let city = '';
    export let adults = '';
    export let first_day = '';
    export let last_day = '';

    const handleSubmit = async (event) => {
    event.preventDefault();

    const params = new URLSearchParams({
        city,
        adults,
        first_day,
        last_day
    }).toString();

    try {
        await goToAboutPage(params);
        reloade()
    } catch (error) {
        console.error('Ошибка при отправке данных:', error);
    }
};

      function reloade(){
        window.location.reload();
      }
 
</script>

<div class="poisck animate__animated animate__headShake wow">
    <div class="block1">
      <form on:submit={handleSubmit}>
        <div class="container">
          <div class="block big">
            <label for="city">Курорт или отель</label>
            <nav>
              <hr id="line" class="lili">
              <select id="city" bind:value={city} required>
                <option value="">Где хотите отдохнуть?</option>
                {#each availableCities as city}
                <option value={city}>{city}</option>
                {/each}
              </select>                                
            </nav>
          </div>
          <section>
            <div class="block3">
              <div class="blockFirstLastDay">
                <div class="block" id="veesd">
                  <label for="arrival">Въезд:</label>
                  <input type="date" id="arrival" bind:value={first_day} />                        
                </div>
                <hr id="vert-line">
                <div class="block" id="viesde">
                  <label for="departure">Выезд:</label>
                  <input type="date" id="departure" bind:value={last_day}/>                        
                </div>    
                <hr id="vert-line" class="tempLine">                                                                
              </div>
              <div class="block big2">
                <hr id="line" class="lil">
                <label for="passengers">Количество человек:</label>
                <input id="colic" type="number" bind:value={adults} min="1"/>
              </div>
            </div>
            <button id="block2" type="submit">Найти</button>                            
          </section>
        </div>
      </form>
    </div>
  </div>


  <style>

    .lil{
        display: none;
    }
    
    #block2:hover{
        background-color: #39087c;
    }
    
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
        width: clamp(270px,62.5vw,1400px);
        gap: 20px;
    }
    
    .block{
        display: flex;
        flex-direction: column;
        align-items: self-start;
        justify-content: center;
        width: 200px;
        flex-wrap: wrap;
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
    
    .poisck{
        width: 100%;
        margin: 0 auto;
        /* box-shadow: 0 0  3px red; */
        display: flex;
        justify-content: center;
        position: relative;
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
    
    .block.big2 #line{
        display: none;
        width: 100%;
        margin: 5px 0px 5px 0px;
        height: 1px;
        background-color: rgba(128, 128, 128, 0.212);
        border: none;
    }
    
    .blockFirstLastDay{
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 20px;
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
        transition: 0.3s all ease 0s ;
    }
    
    .block3{
        display: flex;
        justify-content: center;
        align-items: center;
        flex-wrap: wrap;
        gap: 30px;
    }
    
    nav{
        width: 100%;
        display: flex;
        flex-direction: column;
    }
    
    @media(max-width: 410px){
        .blockFirstLastDay {
            flex-direction: column;
            align-items: center;
            gap: 20px;
        }
    
        #vert-line{
            width: 100%;
            margin: 5px 0px 5px 0px;
            height: 1px;
            background-color: rgba(128, 128, 128, 0.212);
            border: none;
            transform: none;
        }
    }
    
    @media(max-width: 1040px){
        .tempLine{
            display: none;
        }
    
        .block3{
            flex-direction: column;
        }
        .blockFirstLastDay{
            justify-content: space-around;
            width: 100%;
        }
        
        .block.big2 #line{
            display: block;
        }
    
        .block{
            width: 100%;
        }
    
        .block.big2 > label{
            margin-top: 20px;
        }
    
        #colic{
            width: 100%;
        }
    }
    
    @media(max-width: 1688px){
        .container{
            flex-direction: column;
            padding: 20px;
        }
    
        .block1{
            padding-left: 0px;
        }
    
        .block.big #line{
            width: 100%;
        }
    
        section{
            justify-content: space-between;
            width: 100%;
            flex-direction: column;
        }
    
        nav>select{
            padding: 10px 0px 0 0 ;
        }
    
        nav{
            flex-direction: column-reverse;
        }
    
        .block.big{
            width: 88%;
        }
    
        .block3{
            width: 100%;
            justify-content: space-around;
        }
    
        #block2{
            width: 100%;
        }
    }
    </style>