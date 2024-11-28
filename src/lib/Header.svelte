<script>
  import logo from '../assets/logo.jpg';
  import { Route, Router, navigate } from 'svelte-routing';
  import ModalWin from './modalWin.svelte';
  import Cookies from 'js-cookie';

  export let toNavigate = false;
  let login = false;
  let menuOpen = false; 

  async function goTo() {
      if (toNavigate) navigate('/');
  }

  async function goToFavorites() {
      navigate('/favorites');
  }

  async function goToProfile() {
      if (Cookies.get("token") != null) navigate('/profile');
  }

  let modalIsOpen = false;

  function openModal() {
      modalIsOpen = true;
  }

  const info = JSON.parse(Cookies.get('info') || '{}');
  let { surname, name, patronymic } = info;

  if (Cookies.get("token") != null) {
      login = true;
  }
</script>

<main>
  <div on:click={goTo} class="logoTitle animate__animated animate__bounceIn wow">
      <img src={logo} alt="">
      <h2>VisualBooking</h2>
  </div>

  <div class="toolsV2">
      <a href="" on:click={goToFavorites}>Избранное</a>
      <a href="" on:click={goToFavorites}>Сдать Жилье</a>
    {#if login}
      <a id="goToProf" on:click={goToProfile}>{name}</a>
    {:else}
      <a on:click={openModal} id="login">Войти</a>
    {/if}
  </div>

  <div class="tools animate__animated animate__bounceIn wow">
      {#if menuOpen}
          <div style="font-size: 16px;" class="dropdown-menu">
              <a href="" on:click={goToFavorites}>Избранное</a>
              <a href="" on:click={goToFavorites}>Сдать Жилье</a>
              {#if login}
                  <a id="goToProf" on:click={goToProfile}>{name}</a>
              {:else}
                  <a on:click={openModal} id="login">Войти</a>
              {/if}
          </div>
      {/if}
      
      {#if !menuOpen}
          <svg on:click={() => menuOpen = !menuOpen} class="menu-icon" viewBox="0 0 24 24">
              <path d="M3 6h18M3 12h18m-7 6h7" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
          </svg>
      {:else}
          <svg on:click={() => menuOpen = !menuOpen} class="menu-icon" viewBox="0 0 24 24">
              <path d="M4 6h16M4 12h16M4 18h16" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
          </svg>
      {/if}
  </div>
</main>

<ModalWin bind:isOpenLog={modalIsOpen}/>

<style>
  #goToProf{
    color: var(--color);
  }

  *{
    margin: 0;
    padding: 0;
    font-family: 'Rubik';
  }
  
  a{
    transition: 0.3s;
  }

  a:hover{
    color: var(--color);
  }

  #goToProf{
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 10px;
    cursor: pointer;
  }

  #goToProf svg{
    width: 20px;
    height: 20px;
  }

  .logoTitle img{
    width: 60px;
    height: 60px;
  }
  .logoTitle{
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: clamp(20px,1.5vw,50px);
    cursor: pointer;
  }

  .logoTitle > h2{
    font-weight: 600;
    font-family: Rubik;
    font-size: 30px;
    font-weight: 500;
    line-height: 42.66px;
    text-align: left;
    text-underline-position: from-font;
    text-decoration-skip-ink: none;
    color: var(--color);
  }

  main{
    width: 100%;
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    padding: 10px 0;
  }

  a{
    text-decoration: none;
    font-size: 16px;
    transition: all 0.3s ease 0s;;
  }

  #login{
    background-color: var(--color);
    color: white;
    text-align: center;
    display: flex;
    justify-content: center;
    align-items: center;
    width: 74px;
    border-radius: 5px;
  }

  #login > svg{
    margin-left: 10px;
    width: 25px;
    height: 25px;
  }

  .toolsV2{
    font-size: 16px;
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 15px;
    flex-wrap: wrap;
    font-size: clamp(15px,1vw,20px);
    font-weight: 350;
  }

  .tools{
    font-size: 16px;
    display: flex;
    display: none;
    justify-content: center;
    align-items: center;
    gap: 15px;
    flex-wrap: wrap;
    font-size: clamp(15px,1vw,20px);
    font-weight: 350;
  }

  .tools>a:hover{
    transform: scale(1.1);
  }

  .dropdown-menu {
      position: absolute;
      top: 50px;
      background-color: white;
      border-radius: 5px;
      box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
      padding: 10px;
      z-index: 10;
      margin-right: 100px;
  }

  .dropdown-menu a {
      display: block;
      padding: 5px 10px;
      color: black;
      text-decoration: none;
      transition: background-color 0.3s;
  }

  .dropdown-menu a:hover {
      background-color: rgba(0, 0, 0, 0.1);
  }

  .menu-icon {
      width: 30px;
      height: 30px;
      cursor: pointer;
  }

  @media(max-width:1200px) {
    .toolsV2 {
        margin-right: 10px;
    }
  }

  @media(max-width:721px){
    .toolsV2{
      display: none;
    }

    .tools{
      display: flex;
      padding-right: 20px;
    }
  }

  @media(max-width:384px){
    .logoTitle > h2{
      font-size: 30px;
    }

    .logoTitle img{
      width: 50px;
      height: 50px;
    }
  }
</style>
