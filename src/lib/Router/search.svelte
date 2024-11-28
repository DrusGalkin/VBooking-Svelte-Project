<script>
    import { onMount } from 'svelte';
    import { useLocation } from 'svelte-routing';
    import Cookies from 'js-cookie';
    import Header from '../Header.svelte';
    import { navigate } from 'svelte-routing';
    import axios from 'axios';
    import Objects from './Profile/object.svelte';
    import Search from './Main/search.svelte';
    import DoubleRangeSlider from './Main/DoubleRangeSlider.svelte';

    let city = '';
    let adults = '';
    let firstDay = '';
    let lastDay = '';
    let kids = '';
    let apartments = [];
    let filteredApartments = [];
    let toNavigate = true;
    let minPrice = 0;
    let maxPrice = 10000; 
    let selectedMinPrice = minPrice;
    let selectedMaxPrice = maxPrice;
    let selectedTags = [];
    let selectedCategories = [];

    let openFilters = true
    let filtersBlock
    let backFiltersBlock
    let tags = []

    

    function openFiltersBlock(){
        if (openFilters) {
            Object.assign(backFiltersBlock.style, {
                position: "absolute",
                display: "block",
            })

            Object.assign(filtersBlock.style, {
                display: "block",
            })
        } else{
            Object.assign(backFiltersBlock.style, {
                position: "relative",
                display: "none",
            })

            Object.assign(filtersBlock.style, {
                display: "none"
            })
        } 
        openFilters = !openFilters
    }

    async function goHome() {
        navigate(`/`);
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

    async function fetchObjects() {
        try {
            const response = await axios.get('http://localhost:8000/api/objects/');
            apartments = await Promise.all(response.data.map(async (object) => {
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
                };
            }));
            filteredApartments = apartments;
        } catch (error) {
            console.error('Error fetching objects:', error);
        }
    }

    async function getObjectForTags(){
        try{
            const response = await axios.get(`http://localhost:8000/api/tags/`)
            tags = response.data
        } catch(error){
            console.error("Ошибка при поиске объектов по тегам", error.response)
        }
    }
    getObjectForTags()
    async function fetchObjectTypeDetails(typeId) {
        try {
            const response = await axios.get(`http://localhost:8000/api/types-of-objects/${typeId}/`);
            return response.data.name;
        } catch (error) {
            console.error('Error fetching object type details:', error.response ? error.response.data : error.message);
            return 'Unknown type';
        }
    }

    function updateFilteredApartments() {
    filteredApartments = apartments.filter(apartment => {
        const matchesCity = apartment.city === city;
        const matchesMinPrice = apartment.minPrice >= +Cookies.get("min") || apartment.minPrice >= selectedMinPrice;
        const matchesMaxPrice = apartment.minPrice <= +Cookies.get("max") || apartment.minPrice <= selectedMaxPrice;

        return matchesCity && matchesMinPrice && matchesMaxPrice;
    });

    if (activeTab === "nerdeSea") {
        filteredApartments.sort((a, b) => a.seaDistance - b.seaDistance);
     }
    }


    let activeTab = "popular";
    let tabOne, tabTwo, tabThree;

    const switchTab = (tab) => {
        activeTab = tab;
        tabOne.style.textDecoration = "none";
        tabTwo.style.textDecoration = "none";
        tabThree.style.textDecoration = "none";

        if (activeTab === "popular") tabOne.style.textDecoration = "underline";
        if (activeTab === "raiting") tabTwo.style.textDecoration = "underline";
        if (activeTab === "nerdeSea") {
            tabThree.style.textDecoration = "underline";
            updateFilteredApartments();
        }
    }

    onMount(async () => {
        const params = new URLSearchParams(window.location.search);
        city = params.get('city') || '';
        adults = params.get('adults') || '';
        firstDay = params.get('first_day') || '';
        lastDay = params.get('last_day') || '';
        kids = params.get('kids') || '';

        await fetchObjects(); 
        await updateFilteredApartments(); 
    });

    $: uniqueCategories = [...new Set(apartments.map(apartment => apartment.type))];
</script>

<main>
    <Header toNavigate={toNavigate} />
    <div class="block">
        <nav>
            <a href="" on:click={goHome} id="middle">Главная</a> <p> > </p> <p>{city}</p>
        </nav>
        <section>
            <Search
                width={90}
                type={"%"}
                city={city}
                adults={adults}
                checkInDate={firstDay}
                checkOutDate={lastDay}
                on:search={() => updateFilteredApartments()} 
            />
        </section>
    </div>

    <div class="block2">
        <div bind:this={backFiltersBlock} class="blockFilters">
            <div bind:this={filtersBlock} class="priceList">
                <div class="bablo">
                    <div class="blockProgress">
                        <div class="sliderContainer">
                            <DoubleRangeSlider 
                                min={minPrice} 
                                max={maxPrice} 
                                selectedMinPrice={selectedMinPrice} 
                                selectedMaxPrice={selectedMaxPrice} 
                                on:input={updateFilteredApartments}
                            />
                        </div>
                    </div>
                    <div class="blockChooseType">
                        <h1>Категории</h1>
                        <div class="blockYes">
                            {#each uniqueCategories as category}
                                <div class="block6">
                                    <input 
                                        type="checkbox" 
                                        value={category} 
                                        checked={selectedCategories.includes(category)} 
                                        on:change={() => {
                                            if (selectedCategories.includes(category)) selectedCategories = selectedCategories.filter(c => c !== category);
                                            else selectedCategories = [...selectedCategories, category];
                                            updateFilteredApartments();
                                        }} 
                                    />
                                    <label for="">{category.name}</label>
                                </div>
                            {/each}
                        </div>
                    </div>
                    <div class="blockChooseType">
                        <div class="blockYes">
                            {#each tags as tag}
                            <h1>{tag.type}</h1>
                            {#each tags.filter(t => t.type === tag.type) as tagTitle}
                                <div class="block6">
                                    <input type="checkbox" >
                                    <label for="">{tagTitle.title}</label>
                                </div>
                            {/each}
                        {/each}
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <div class="blockPage">
            <div class="info">
                <p>Найдено {filteredApartments.length} варианта жилья</p>
                <div class="sort">
                    <a bind:this={tabOne} on:click={() => { switchTab("popular"); updateFilteredApartments(); }}>По популярности</a>
                    <a bind:this={tabTwo} on:click={() => { switchTab("raiting"); updateFilteredApartments(); }}>По рейтингу</a>
                    <a bind:this={tabThree} on:click={() => { switchTab("nerdeSea"); updateFilteredApartments(); }}>Ближе к морю</a>

                    <svg on:click={openFiltersBlock}  class="menu-icon" viewBox="0 0 24 24">
                        <path d="M3 6h18M3 12h18m-7 6h7" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
                    </svg>

                </div>
            </div>
            <div>
                {#if filteredApartments.length > 0}
                    <div class="blockObjects">
                        {#each filteredApartments as apartment}
                            <Objects {apartment}/> 
                        {/each}
                    </div>
                {:else}
                    <div class="blockSorry">
                        <p>По вашему запросу не было найдено подходящих объектов.</p>
                    </div>
                {/if}
            </div>
        </div>
    </div>
</main>

<style>

.blockChooseType h1{
    font-size: 20px;
}

.sort svg{
    width: 40px;
    height: 40px;
    display: none;
}

.sliderContainer{
    margin-bottom: 40px;
}

main{
    margin-top: 20px;
}

.blockYes{
    display: flex;
    flex-direction: column;
}

#slidee{
    position: absolute;
    top: 13px;
}

.blockProgress {
    width: 100%; 
    margin-bottom: 20px; 
    position: relative;
}

.sliderContainer {
    position: relative;
    height: 30px; 
}

input[type='range'] {
    -webkit-appearance: none;
    position: absolute;
    width: 100%;
    height: 5px;
    background: #ddd;
    border-radius: 5px;
    pointer-events: none; 
}

input[type='range']::-webkit-slider-thumb {
    -webkit-appearance: none; 
    height: 20px; 
    width: 20px; 
    z-index: 10;
    background: #007bff; 
    border: 2px white solid;
    border-radius: 50%; 
    cursor: pointer; 
    pointer-events: auto;
    position: relative; 
    box-shadow: 0px 0px 7px rgba(0, 0, 0, 0.3); /* Тень */
}

    .blockProgress{
        display: flex;
        flex-direction: column;
    }

    .blockSorry{
        max-width: 817px;
        height: 200px;
        border: 2px #80808017 solid;
        border-radius: 15px;
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
        color: #80808090;
        text-align: center;
    }

    .blockSorry svg{
        width: 100px;
        height: 100px;
    }

    .blockProgress input{
        position: relative;
    }

    .bablo {
        display: flex;
        gap: 10px;
        flex-direction: column;
    }

    input[type="range"] {
        margin: 0 10px;
        flex: 1;
    }
    .blockObjects{
        display: flex;
        flex-direction: column;
        gap: 30px;
    }

    .blockFilters{
        width: 300px;
        background: #FFFFFF;
        padding: 25px;
        border: 2px rgba(128, 128, 128, 0.089) solid;
        border-radius: 15px;

    }

    .blockPage{
        display: flex;
        gap: 30px;
        flex-grow: 1;
        flex-direction: column;
        background: #F5F5F5;
        padding: 25px;
        border: 2px rgba(128, 128, 128, 0.089) solid;
        border-radius: 15px;
    }

    .info{
        display: flex;
        justify-content: space-between;
        color: #959595;
        font-size: 14px;
        font-weight: 300;
        line-height: 16.59px;
    }

    .sort{
        display: flex;
        justify-content: space-between;
        gap: 10px;  
    }

    .block2{
        padding-top: 20px;
        display: flex;
        justify-content: space-between;
        align-items: flex-start;
        flex-grow: 1;
        margin: 0 auto;
        width:100%;
        gap: 15px;
    }

    .block{
        margin-top: 0px;
    }
    
    nav{
        display: flex;
        gap: 10px;
        width: 90%;

        padding: 20px 0 20px 5px;
    }

    nav a{
        text-decoration: none;
        color: black;
        transition: all 0.3s ease 0s;
        cursor: cell;
    }

    nav #middle:hover{
        transform: scale(1.2);
        color: gray;
        cursor: pointer;
    }

    section h1{
        color: white;
        font-size: clamp(30px,2vw,50px);
        margin-bottom: 30px;
    }

    section{
        width: 100%;
        background: var(--color);
        padding: 20px 0px 20px 0px;
        margin: 0 auto;
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
        border-radius: 20px;
    }

    .block6 label {
        font-size: 16px;
    }

    @media(max-width:1195px){
        section{
            border-radius: 0px;
        }
    }

    @media(max-width:1042px){
        .blockFilters{
            display: none;
        }

        .priceList{
            display: none;
        }

        .block2{
            justify-content: center;
            align-items: center;
            flex-direction: column;
        }

        .info{
            align-items: center;
        }

        .sort{
            align-items: center;
        }

        .sort svg{
            display: block;
            margin-left: 10px;

        }
    }
</style>