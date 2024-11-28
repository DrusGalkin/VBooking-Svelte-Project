<script>
    import houseInForest from '../assets/popular-img/rent-a-house.png';
</script>

<main>
    <section class="animate__animated wow animate__fadeIn">
        <img src="{houseInForest}" alt="">

        <div class="block">

            <div class="block3 animate__animated wow animate__fadeInUp">
                <h1>Сдать жилье на VisualBooking</h1>
                <p>Получай доход, сдавай жилье.</p>                
            </div>

            <button class="animate__animated wow animate__fadeInDown">
                Подробнее
            </button>
        </div>
    </section>
    
</main>

<style>

    button{
        text-decoration: none;
        color: white;
        width: 270px;
        height: 49px;
        gap: 0px;
        border-radius: 20px;
        opacity: 0px;
        font-family: Rubik;
        font-size: 20px;
        font-weight: 400;
        line-height: 23.7px;
        text-underline-position: from-font;
        text-decoration-skip-ink: none;
        background-color: var(--color);
        transition: 0.3s;
        margin-top: 30px;
    }

    .block3{
        text-align: end;
    }

    .block h1{
        font-family: Rubik;
        font-size: 30px;
        font-weight: 500;
        line-height: 35.55px;
        text-underline-position: from-font;
        text-decoration-skip-ink: none;
        margin-bottom: 10px;
        text-align: center;
    }

    .block{
        margin-right: 70px;
    }

    .block p{
        font-family: Rubik;
        font-size: 20px;
        font-weight: 400;
        line-height: 23.7px;
        text-underline-position: from-font;
        text-decoration-skip-ink: none;
    }

    .block2{
        display: flex;
        justify-content: end;
        align-items: end;
        width: 100%;
        max-width: 500px;
        margin-top: 40px;
        transition: all 0.3s ease 0s;
    }

    button:hover{
        background-color: var(--colorHover);
    }

    .block{
        display: flex;
        justify-content: center;
        align-items: end;
        flex-direction: column;
        top: 40%;
        right: 0;
        position: absolute;
        color: white;
        
    }

    section{
        position: relative;
        width: 100%;
    }

    img{
        width: 100%;
        max-width: 1200px;
        height: 439px;
        object-fit: cover;
        border-radius: 10px;
    }
    
    main{       
        display: flex;
        justify-content: center;
        align-items: center;
        margin: 0 auto;
        width: 100%;
    }

    @media(max-width:876px){
        .block{
            margin-right: 0;
            width: 100%;
            align-items: center;
         }

         .block3{
            align-items: center;
            display: flex;
            flex-direction: column;
         }

        .block2{
            justify-content: center;
        }
    }
</style>