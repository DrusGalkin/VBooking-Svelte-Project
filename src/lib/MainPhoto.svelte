<script>
    import mainPhoto from '../assets/main-photo.png';
    import mainPhotoBlur from '../assets/blur.png';
  
    import { navigate } from 'svelte-routing';
    import axios from 'axios';
    import { onMount } from 'svelte';
  
    async function goToAboutPage(params) {
      navigate(`/search?${params}`);
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
      
    let city = '';
    let adults = '';
    
    // Установим даты по умолчанию
    let today = new Date();
    let nextWeek = new Date();
    nextWeek.setDate(today.getDate() + 7);
  
    let first_day = today.toISOString().split('T')[0]; 
    let last_day = nextWeek.toISOString().split('T')[0];
  
    const handleSubmit = async (event) => {
      event.preventDefault();
  
      if (!city) {
        alert('Пожалуйста, выберите город.');
        return;
      }
  
      const params = new URLSearchParams({
        city,
        adults,
        first_day,
        last_day
      }).toString();
  
      try {
        const response = await axios.get(`http://localhost:8000/api/objects/?${params}`);
        await goToAboutPage(params);
      } catch (error) {
        console.error('Ошибка при отправке данных:', error);
      }
    };
  </script>
  
  <main>
    <div class="photo animate__animated animate__fadeIn wow">
      <img id="one" src="{mainPhoto}" alt="">
      <img id="two" src="{mainPhotoBlur}" alt="">
      <div class="main-text">
        <h2 id="middle">Комфортное жилье – шаг к лучшей жизни!</h2>
        <p id="noMiddle">Откройте мир вместе с нами!</p>                
      </div>
    </div>
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
  </main>

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

#noMiddle{
    background-color: white;
    padding: 5px 25px 5px 25px;
    border-bottom-left-radius: 20px;
    border-bottom-right-radius: 20px;
    box-shadow: 0 4px 2px -2px black;
    font-size: clamp(12px,1.2vw,50px);
    font-weight: 300;
    position: relative;
    top: -1px;
    text-wrap: nowrap;
}

#middle{
    width: clamp(300px,46.8750vw,1000px);
    font-size: clamp(20px,2.1vw,50px);
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
    border-radius: 50px;
    width: 100%;
    height: 600px;
    object-fit: cover;

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
    /* box-shadow: 0 0  3px red; */
    display: flex;
    justify-content: center;
    position: relative;
    top: -2.6042vw;
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
    border-radius: 15px;
    height: 80px;
    width: 120px;
    padding: 10px;
    background-color: var(--color);
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

@media(max-width:600px){
    #middle{
        width: clamp(270px,26.0417vw,600px);
        margin-bottom: 30px;
    }

    #noMiddle{
        border-bottom-left-radius: 0px;
        border-bottom-right-radius: 0px;
        border-radius: 20px;
    }

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

@media(max-width:1495px){
  #two, #one{
    border-radius: 0px;
  }
}

@media(max-width: 1040px){
    .tempLine{
        display: none;
    }

    .poisck{
        top: -200px;
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