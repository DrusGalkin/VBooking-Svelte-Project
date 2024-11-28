<script>
import logo from '../../../assets/logo.jpg'
import Cookies from 'js-cookie';
import { navigate } from 'svelte-routing';
let door

function reloade() {
    window.location.reload();
  }

function exit() {
    Cookies.remove("token");
    Cookies.remove("refreshToken");
    Cookies.remove("info");
    localStorage.removeItem("activeTab")
    navigate("/");
    reloade();
  }
</script>

<main>
    <div class="sd">
        <div class="logo">
            <img src="{logo}" alt="">
            <h1>VBooking</h1>
        </div>
    
        <a on:click={exit}
        on:mouseenter={()=> {door.style.fill = "red"}}
        on:mouseleave={()=> {door.style.fill = "black"}}
        >
            <svg width="16" height="15" viewBox="0 0 16 15" fill="none" xmlns="http://www.w3.org/2000/svg">
                <g clip-path="url(#clip0_1_53)">
                <path bind:this={door} d="M14.5665 7.18837L12.0755 4.85325C11.8919 4.68106 11.5947 4.68082 11.411 4.85187C11.2269 5.02303 11.2251 5.30228 11.4068 5.47563L13.0689 7.06055H6.37792C6.11798 7.06055 5.9071 7.25621 5.9071 7.5C5.9071 7.7438 6.118 7.93946 6.37792 7.93946H13.0969L11.4095 9.52229C11.2259 9.6946 11.2259 9.97474 11.4095 10.147C11.5015 10.2332 11.6221 10.2766 11.7425 10.2766C11.8629 10.2766 11.9836 10.2337 12.0755 10.1475L14.5664 7.81243C14.6547 7.72966 14.7043 7.6174 14.7043 7.50039C14.7043 7.38339 14.6547 7.27112 14.5665 7.18837Z" fill="black"/>
                <path bind:this={door} d="M10.9208 11.5364C10.6608 11.5364 10.452 11.734 10.452 11.9778V14.1211H2.23328V0.878906H10.452V3.02309C10.452 3.26688 10.6608 3.46447 10.9208 3.46447C11.1807 3.46447 11.3895 3.26688 11.3895 3.02309V0.438193C11.3895 0.194385 11.1756 0 10.9157 0H1.76617C1.50625 0 1.29578 0.194385 1.29578 0.438193V14.5627C1.29578 14.8065 1.50625 15 1.76618 15H10.9157C11.1757 15 11.3895 14.8065 11.3895 14.5627V11.9778C11.3895 11.734 11.1807 11.5364 10.9208 11.5364Z" fill="black"/>
                </g>
                <defs>
                <clipPath id="clip0_1_53">
                <rect width="16" height="15" fill="white"/>
                </clipPath>
                </defs>
            </svg>    
            <p>Выйти</p>
        </a>
    </div>
</main>

<style>
    img{
        width: 49px;
    }

    main{
        height: 70px;
        display: flex;
        justify-content: center;
        align-items: center;
        background: white;
    }

    .sd{
        width: 100%;
        max-width: 1200px;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

    path{
        transition: 0.3s;
    }

    h1{
        font-family: Rubik;
        font-size: 30px;
        font-weight: 500;
        text-underline-position: from-font;
        text-decoration-skip-ink: none;
        color: var(--color);
    }

    .logo{
        display: flex;
        align-items: center;
        justify-content: center;
    }

    a{
        display: flex;
        justify-content: center;
        align-items: center;
        cursor: pointer;
        transition: 0.3s;
        margin-right: 20px;
    }

    a:hover{
        -webkit-text-stroke: 0.06px black;
        color: red;
    }

</style>