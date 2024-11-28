<script>
    export let hrefs = "https://avatars.mds.yandex.net/i?id=2a4caaaacef0bd85c8d7a4676f0a6ed4_l-4079525-images-thumbs&n=13";
    export let name = "Skoda рассекретила новый ультрадешевый кроссовер";
    export let info = "Skoda рассекретила новый ультрадешевый кроссовер";
</script>

<main class="animate__animated wow animate__fadeInUp">
    <img src={hrefs} alt="">

    <section>
        <h1>{name}</h1>
        <p>{info}</p>
    </section>
</main>

<style>
    main {
        border-radius: 10px;
        display: flex;
        flex-direction: column;
        gap: 10px;
        margin-bottom: 20px;
        box-shadow: 0px 4px 4px 0px #00000040;
    }

    section {
        padding: 0 10px 10px 10px;
        display: flex;
        gap: 10px;
        flex-direction: column;
    }

    p {
        font-family: Rubik;
        font-size: 14px;
        font-weight: 300;
        line-height: 16.59px;
        text-align: left;
    }

    img {
        border-radius: 10px 10px 0 0;
    }

    h1 {
        font-family: Rubik;
        font-size: 16px;
        font-weight: 400;
        line-height: 18.96px;
        text-align: left;
    }

    @media(max-width: 1200px) {
        main {
            width: 48%;
        }
    }

    @media(max-width: 500px) {
        main {
            width: 100%;
        }
    }
</style>