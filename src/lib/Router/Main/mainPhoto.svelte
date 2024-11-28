<script>
    import mainPhoto from '../../../assets/main-photo.png';
    import mainPhotoBlur from '../../../assets/blur.png';
    import Search from './search.svelte';
    import Calendar from './Calendar.svelte';
</script>

<main>
    <div class="photo">
            <div class="blur"></div>
        <div class="block">
            <!-- <div class="bl">
                <Calendar />
            </div> -->
            <h1>Ваш идеальный отдых начинается здесь!</h1>
            <Search/>
        </div>
    </div>
</main>

<style>
    .bl{
        width: 300px;
    }

    .blur{
        position: relative;
        width: 100%;
        height: 600px;
    }

    .block{
        margin-top: 150px;
        position: absolute;
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
    }

    .photo{
        width: 100%;
        background: url("../../../assets/main-photo.png") no-repeat center;
        background-size: cover;
        display: flex;
        justify-content: center;
        align-items: center;

    }

    .photo h1{
        font-weight: 600;
        color: white;
        font-size: clamp(30px,1.9vw, 45px);
        text-align: center;
        margin-bottom: 20px;
    }

    @media(max-width:1101px){
        .blur{
            height: 750px;
        }
    }
</style>