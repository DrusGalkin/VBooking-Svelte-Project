<script>
    import NewsBlock from "./news-block.svelte";
</script>

<main>
    <h1 class="animate__animated wow ">Полезные статьи</h1>

    <section class="horizontal-scroll">
        <NewsBlock hrefs="https://www.wikihow.com/images/thumb/a/a2/Include-CSS-Within-HTML-Web-Pages-Step-6.jpg/aid4377690-v4-728px-Include-CSS-Within-HTML-Web-Pages-Step-6.jpg.webp"/>
        <NewsBlock hrefs="https://www.wikihow.com/images/thumb/a/a2/Include-CSS-Within-HTML-Web-Pages-Step-6.jpg/aid4377690-v4-728px-Include-CSS-Within-HTML-Web-Pages-Step-6.jpg.webp"/>
        <NewsBlock hrefs="https://www.wikihow.com/images/thumb/a/a2/Include-CSS-Within-HTML-Web-Pages-Step-6.jpg/aid4377690-v4-728px-Include-CSS-Within-HTML-Web-Pages-Step-6.jpg.webp"/>
        <NewsBlock hrefs="https://www.wikihow.com/images/thumb/a/a2/Include-CSS-Within-HTML-Web-Pages-Step-6.jpg/aid4377690-v4-728px-Include-CSS-Within-HTML-Web-Pages-Step-6.jpg.webp"/>
    </section>

    <a class="animate__animated wow " href="">Читать больше</a>
</main>

<style>
    section {
        display: flex;
        padding: 10px 0;
        align-items: center;
        justify-content: space-between;
        gap: 10px;
    }

    a:hover {
        background-color: var(--colorHover);
    }

    a {
        margin-top: 30px;
        width: 235px;
        height: 41px;
        display: flex;
        justify-content: center;
        align-items: center;
        border-radius: 10px;
        background: var(--color);
        color: white;
        font-family: Rubik;
        font-size: 20px;
        font-weight: 500;
        line-height: 23.7px;
        transition: 0.3s;
    }

    h1 {
        font-family: Rubik;
        font-size: 32px;
        font-weight: 500;
        line-height: 37.92px;
        margin: 20px 0;
    }

    main {
        width: 100%;
        display: flex;
        flex-direction: column;
    }

    @media(max-width: 1200px) {
        section {
            justify-content: center;
            flex-wrap: wrap;
        }
    }
</style>