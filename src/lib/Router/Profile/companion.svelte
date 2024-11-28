<script>
    import axios from "axios";
    import Cookies from 'js-cookie'; 

    export let userTravelers
    const [year, month, day] = userTravelers.date_of_birth.split('-');
    let isDeleted = true;

    async function deleteCompanuon(){
        try{
            await axios.delete(`http://127.0.0.1:8000/api/travelers/${userTravelers.id}/`, {
                headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${Cookies.get("token")}`,
               }
            })
            isDeleted = false;
        }catch(error){
            
        }
    }
</script>

{#if isDeleted}
    <main>
        <h1>{userTravelers.name} {userTravelers.surname}</h1>
        <p id="birthdate">Дата рождения: <br>
            {day}.{month}.{year}
        </p>
        <hr>
        <p id="edit">Редактировать</p>
        <p id="delete" on:click={deleteCompanuon} >Удалить</p>
    </main>
{/if}

<style>
    main{
        width: 261px;
        border: 0.2px solid #49494931;
        border-radius: 5px;
        padding: 10px;
    }

    #edit, #delete{
        font-size: 14px;
        font-weight: 300;
        line-height: 16.59px;
    }

    #delete{
        color: gray;
        cursor: pointer;
        transition: 0.2s;
    }

    #delete:hover{
        color: red;
    }

    #edit{
        color: var(--color);
        cursor: pointer;
        margin-bottom: 3px;
    }

    h1{
        font-size: 16px;
        font-weight: 400;
        line-height: 18.96px;
        margin-bottom: 5px;
    }

    hr{
        margin: 8px 0 8px 0;
    }

    #birthdate{

        font-size: 12px;
        font-weight: 300;
        line-height: 14.22px;
    }
</style>