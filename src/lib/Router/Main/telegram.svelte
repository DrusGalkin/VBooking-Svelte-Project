<script>
    import telegram from '../../../assets/tg.png'
    import qr from '../../../assets/tgQR.png'
</script>
<a href="" class="animate__animated animate__backInLeft wow">
<main>
    <img id="tg" src="{telegram}" alt="tg">
    
    <section>
        <img id="qr" src="{qr}" alt="">
        <div class="info">
            <h1>Мы в телеграме!</h1>
            <p>Актуальные новости и лучшие места для проведения отпуска!</p>
            <a href="">Перейти в канал</a>
        </div>
    </section>
</main>
</a>

<style>
    *{
        color: white;
    }

    main{
        width: 100%;
        max-width: 1216px;
        border-radius: 10px;
        padding: 20px;
        background: #4AB6E4;
        display: flex;
        justify-content: space-around;
        align-items: center;
    }

    #tg{
        width: 126px;
        height: 123px;
        -webkit-filter: drop-shadow(5px 5px 5px #222);
        filter: drop-shadow(3px 3px 3px rgba(0, 0, 0, 0.25));
    }

    .info{
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: start;
        width: 100%;
        max-width: 510px;
        gap: 10px;
    }

    .info h1{
        font-family: Rubik;
        font-size: 30px;
        font-weight: 500;
        line-height: 35.55px;
        text-align: left;
        text-underline-position: from-font;
        text-decoration-skip-ink: none;
    }

    .info p{
        font-family: Rubik;
        font-size: 20px;
        font-weight: 400;
        line-height: 23.7px;
        text-underline-position: from-font;
        text-decoration-skip-ink: none;
    }

    .info a{
        font-family: Rubik;
        font-size: 20px;
        font-weight: 600;
        line-height: 23.7px;
        text-align: left;
        text-underline-position: from-font;
        text-decoration-skip-ink: none;
        transition: 0.5s;
    }

    .info a:hover{
        transform: scale(1.05);
    }
    
    section{
        display: flex;
        justify-content: center;
    }

    #qr{
        width: 133px;
        height: 136px;
    }

    @media(max-width:876px){
        #tg{
            display: none;
        }

        main{
            justify-content: center;
            align-items: center;
        }
    }

    @media(max-width:570px){
        section{
            flex-direction: column-reverse;
            align-items: center;
            justify-content: center;
        }

        .info{
            text-align: center;
            display: flex;
            justify-content: center;
            align-items: center;
        }

        #qr{
            margin-top: 20px;
        }
    }
</style>