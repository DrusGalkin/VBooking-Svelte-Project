<script>
  import src1 from "../assets/popular-img/1.png";
  import src2 from "../assets/popular-img/2.png";
  import src3 from "../assets/popular-img/3.png";
  import blur from '../assets/blur-popular.png';
</script>

<main>
  <h1 class="block animate__animated wow animate__fadeInDown">Популярные курорты</h1>

  <section class="block animate__animated wow animate__fadeInUp">

    <div class="block2">
      <div class="photo">
          <img src="{src1}" alt="">
      </div>
      <h2>Геленджик</h2>
    </div>


      <div class="block2">
          <div class="photo">
            <img src="{src2}" alt="">
          </div>
        <h2>Кабардинка</h2>
      </div>



      <div class="block2">
        <div class="photo">
          <img src="{src3}" alt="">
        </div>
      <h2>Дивноморское</h2>
      </div>


  </section>
</main>

<style>
  .block2{
    display: flex;
    flex-direction: column;
    align-items: start;
  }

  main {
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: start;
    flex-direction: column;
    margin-top: 10px;
    width: 100%;
  }

  section{
      display: flex;
      justify-content: space-between;
      align-items: center;
      width: 100%;
      gap: 20px;
  }

  .photo:hover{
      transform: scale(1.01);
  }
  main h1 {
    font-weight: 500;
    font-size: 32px; 
    text-align: start;
    margin: 10px 0 10px 0;
  }

  .photo {
    position: relative;
    min-width: 300px;
    max-width: 500px;
    transition: all 0.3s ease 0s;
  }

  .photo img {
    width: 100%;
    height: 100%;
    object-fit: cover; 
  }

  #blur {
    position: absolute;
    top: 0;
    left: 0; 
  }

  h2 {
    color: rgb(0, 0, 0); 
    text-align: center;
    margin: 10px 0 10px 0; 
    font-size: 22px;
    font-weight: 400px;
  }

  @media(max-width:959px){
    section{
      flex-direction: column;
      justify-content: center;
    }

    main{
      align-items: center;
    }
  }

  @media(max-width:387px){
    main h1 {
      font-size: 30px;
    }
  }
</style>