<script>
  import Card from "./card.svelte";
  import axios from "axios";
  import { onMount } from 'svelte';

  let activeButton = null;
  let cards = []; 
  let filteredCards = [];
  let objectTypes = []

  activeButton = 1;

  function setActive(buttonNumber) {
    if (activeButton !== buttonNumber) {
      activeButton = buttonNumber;
      filterCardsByCategory(buttonNumber);
    }
  }

  async function fetchObjects() {
    try {
      const response = await axios.get('http://localhost:8000/api/objects/');
      cards = await Promise.all(response.data.map(async (object) => {
        const cityName = await fetchCityName(object.address.city);
        return {
          city: cityName, 
          street: object.address.street, 
          house: object.address.house, 
          seaDistance: object.address.sea_distance, 
          nameObject: object.name, 
          minPrice: object.min_price, 
          type: object.type, 
          images: object.images.length > 0 ? object.images[0].media : null, 
          tags: object.tags.map(tag => tag) 
        };
      }));
      console.log(cards)
      filterCardsByCategory(activeButton);
    } catch (error) {
      console.error('Ошибка при получении данных:', error);
    }
  }

  function filterCardsByCategory(categoryId) {
    if (categoryId) filteredCards = cards.filter(card => card.type.id === categoryId);
    else filteredCards = cards;
  }

  async function fetchCityName(cityId) {
        try {
            const response = await axios.get(`http://localhost:8000/api/city/${cityId}/`);
            return response.data.name; 
        } catch (error) {
            console.error('Error fetching city name:', error);
            return null; 
        }
    }


  async function fetchObjectTypes() {
    try {
      const response = await axios.get('http://localhost:8000/api/types-of-objects/');
      objectTypes = response.data;
    } catch (error) {
      console.error("Ошибка при получении типов объектов:", error.response);
    }
  }

  onMount(()=>{
    fetchObjects();
    fetchObjectTypes()
  })
</script>

<main>
  <h1 class="animate__animated wow animate__fadeInDown">Объекты с лучшим рейтингом</h1>
  
  <section class="animate__animated wow animate__fadeInDown">
    {#each objectTypes as type}
      <button 
        class={activeButton === type.id ? 'active' : ''} 
        on:click={() => setActive(type.id)} 
        id={`b${type.id}`}>
        {type.name}
      </button>
    {/each}
  </section>
  
  <nav>
    {#each filteredCards as card}
      <Card 
        city={card.city} 
        distans={card.seaDistance}
        nameObject={card.nameObject} 
        sale={card.minPrice}
        hrefs={card.images} 
        tegs={card.tags} 
      />
    {/each}
  </nav>

  <div class="block animate__animated wow animate__fadeInUp">
    <a id="more-variants" href="">Смотреть еще {cards.length} вариантов</a>
  </div>
  <br><br>
</main>


<style>
  nav {
    margin-top: 20px;
    display: flex;
    width: clamp(320px, 100%, 1500px);
    flex-wrap: wrap;
    gap: 20px;
  }

  #more-variants {
    background-color: var(--color);
    padding: 9px 19px;
    color: white;
    text-decoration: none;
    border-radius: 10px;
    font-size: 20px;
    transition: 0.3s;
  }

  #more-variants:hover{
    background-color: var(--colorHover);
  }

  .block {
    margin-top: 50px;
    text-align: start;
    width: clamp(320px, 100%, 1300px);
  }

  .active {
    color: var(--color);
    border-bottom: 3px var(--color) solid;
  }

  #gorizontal-line {
    width: 100%;
    display: none;
    margin-top: 50px;
  }

  main {
    display: flex;
    justify-content: center;
    flex-direction: column;
    margin: 0 auto;
    width: clamp(320px, 100%, 1500px);
  }

  h1 {
    font-weight: 500;
    font-size: 32px; 
  }

  button {
    background-color: transparent;
    color: #777777;
    border: none;
    cursor: pointer;
    text-wrap: nowrap;
    transition: all 0.3s ease;
    font-size: 20px;
    font-weight: 400;
    line-height: 23.7px;
    text-align: left;
    text-underline-position: from-font;
    text-decoration-skip-ink: none;
    padding-bottom: 5px;
    margin-right: 20px;
  }

  section {
    display: flex;
    margin-top: 30px;
    gap: 20px;
    overflow-x: scroll;
    padding-bottom: 20px;
  }

  section::-webkit-scrollbar {
    height: 4px;    
  }

  section::-webkit-scrollbar-thumb {
    background-color: #77777773; 
    border-radius: 10px; 
  }
  section::-webkit-scrollbar-track {
    background: transparent;
  }

  @media(max-width:716px){
    h1{
      text-align: center;
    }
  }

  @media(max-width:1200px){
    nav{
      align-items: center;
      justify-content: center;
    }
  }
</style>