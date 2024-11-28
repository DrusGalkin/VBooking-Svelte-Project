<script>
  import Header from './lib/Header.svelte'
  import Popular from './lib/popular.svelte'
  import SocialNetwork from './lib/social-network.svelte'
  import PopularObject from './lib/popular-object.svelte'
  import PopularArticles from './lib/popular-articles.svelte'
  import RentAHouse from './lib/rent-a-house.svelte'
  import MainPhoto from './lib/Router/Main/mainPhoto.svelte'
  import Telegram from './lib/Router/Main/telegram.svelte'
  import Dzen from './lib/Router/Main/dzen.svelte'
  import Footer from './lib/Router/Main/footer.svelte'
  import { onMount } from 'svelte';

  //Routing
  import {  Route, Router, navigate } from 'svelte-routing'
  import Search from './lib/Router/search.svelte'
  import Loader from './lib/Router/loader.svelte'
  import Profile from './lib/Router/profile.svelte'


  //test
  import Profile2 from './lib/Router/Profile/profile.svelte'

</script>

<main>
  <Router>
      <Route path="">
        <div class="mass two">
          <Header/>
        </div>
        <MainPhoto/>
        <div class="mass one">
          <Popular/>
          <PopularObject/>
          <Telegram/>
          <PopularArticles/>
          <Dzen/>
          <RentAHouse/>
        </div>
        <Footer/>
      </Route>

    <Route path='/search'>
      <div class="block">
        <Loader/>
        <Search/>
      </div>

    </Route>

    <Route path='/profile'>
      <Loader/>
      <Profile2/>
    </Route>

    <Route path='/favorites'>
      <Loader/>
    </Route>
  </Router>
</main>

<style>
  .mass.one{
    display: flex;
    flex-direction: column;
    gap: 50px;
  }

  .mass{
    width: 100%;
    max-width: 1200px;
    margin: 0 auto;
  }

  .block{
    max-width: 1200px;
    width: 100%;
    margin: 0 auto;
  }
</style>