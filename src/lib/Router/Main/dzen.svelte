<script>
    import dzen from '../../../assets/dzen.png'
    import qr from '../../../assets/dzenQR.png'
</script>
<a href="" class="animate__animated animate__backInRight wow">
<main>
    <img id="tg" src="{dzen}" alt="tg">
    
    <section>
        <img id="qr" src="{qr}" alt="">
        <div class="info">
            <h1>Наш Яндекс Дзен</h1>
            <p>Актуальные новости и лучшие места для проведения отпуска!</p>
            <a href="">Перейти на дзен</a>
        </div>
    </section>
</main>
</a>

<style>
    *{
        color: rgb(0, 0, 0);
    }

    main{
        width: 100%;
        max-width: 1216px;
        border-radius: 10px;
        padding: 20px;
        background: #ffffff;
        display: flex;
        justify-content: space-around;
        align-items: center;
        box-shadow: 0px 4px 4px 0px #00000040;
    }

    #tg{
        width: 211px;
        height: 62px;
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