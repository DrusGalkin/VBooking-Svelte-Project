<script>

</script>

<main>
    <h1 class="animate__animated wow animate__fadeInDown">Наши соц. сети</h1>

    <section>
        <a href="" class="animate__animated wow animate__fadeInLeft">
            <div class="block1">
                <svg viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <circle cx="16" cy="16" r="14" fill="url(#paint0_linear_87_7225)"></circle> <path d="M22.9866 10.2088C23.1112 9.40332 22.3454 8.76755 21.6292 9.082L7.36482 15.3448C6.85123 15.5703 6.8888 16.3483 7.42147 16.5179L10.3631 17.4547C10.9246 17.6335 11.5325 17.541 12.0228 17.2023L18.655 12.6203C18.855 12.4821 19.073 12.7665 18.9021 12.9426L14.1281 17.8646C13.665 18.3421 13.7569 19.1512 14.314 19.5005L19.659 22.8523C20.2585 23.2282 21.0297 22.8506 21.1418 22.1261L22.9866 10.2088Z" fill="white"></path> <defs> <linearGradient id="paint0_linear_87_7225" x1="16" y1="2" x2="16" y2="30" gradientUnits="userSpaceOnUse"> <stop stop-color="#37BBFE"></stop> <stop offset="1" stop-color="#007DBB"></stop> </linearGradient> </defs> </g></svg>
                    <p>t.me/visualbooking</p>
            </div>            
        </a>

        <a href="" class="animate__animated wow animate__fadeInRight">
            <div class="block2">

                <svg width="169" height="169" viewBox="0 0 169 169" fill="none"
                xmlns="http://www.w3.org/2000/svg">
                <g clip-path="url(#clip0_45_484)">
                  <path d="M84.0337 168.01H84.7036C118.068 168.01 137.434 164.651 151.152 151.333C165.139 137.206 168.369 117.709 168.369 84.4749V83.5351C168.369 50.311 165.139 30.9445 151.152 16.677C137.444 3.3594 117.938 0 84.7136 0H84.0437C50.6797 0 31.3031 3.3594 17.5856 16.677C3.59808 30.8045 0.368652 50.311 0.368652 83.5351V84.4749C0.368652 117.699 3.59808 137.066 17.5856 151.333C31.1732 164.651 50.6797 168.01 84.0337 168.01Z" fill="#202022"/>
                  <path d="M148.369 82.7304C148.369 82.0906 147.849 81.5608 147.209 81.5308C124.246 80.661 110.271 77.732 100.494 67.955C90.6967 58.1581 87.7776 44.1724 86.9079 21.1596C86.8879 20.5198 86.358 20 85.7082 20H83.0291C82.3893 20 81.8594 20.5198 81.8295 21.1596C80.9597 44.1624 78.0406 58.1581 68.2437 67.955C58.4568 77.742 44.4911 80.661 21.5283 81.5308C20.8885 81.5508 20.3687 82.0806 20.3687 82.7304V85.4096C20.3687 86.0494 20.8885 86.5792 21.5283 86.6092C44.4911 87.4789 58.4667 90.408 68.2437 100.185C78.0206 109.962 80.9397 123.908 81.8195 146.83C81.8394 147.47 82.3693 147.99 83.0191 147.99H85.7082C86.348 147.99 86.8779 147.47 86.9079 146.83C87.7876 123.908 90.7067 109.962 100.484 100.185C110.271 90.398 124.236 87.4789 147.199 86.6092C147.839 86.5892 148.359 86.0594 148.359 85.4096V82.7304H148.369Z" fill="white"/>
                </g>
                <defs>
                  <clipPath id="clip0_45_484">
                    <rect width="168.04" height="168.04" fill="white" transform="translate(0.368652)"/>
                  </clipPath>
                </defs>
              </svg>
                <p>dzen.ru/visualbooking</p>
            </div>            
        </a>


    </section>
</main>

<style>
    h1{
        font-size: clamp(40px, 2.6vw, 60px);
    }

    main{
        padding-top: 100px;
        margin: 0 auto;
        width: clamp(320px,100%,1500px);
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
    }

    a{
        color: white;
        text-decoration: none;
    }

    section{
        width: 100%;
        display: flex;
        justify-content: space-around;
        align-items: center;
        flex-wrap: wrap;
        margin-top: 30px;
        gap: 30px;
    }

    .block1{
        width: clamp(300px,36.4583vw,700px);
        border-radius: 20px;
        display: flex;
        align-items: center;
        background: rgb(0,136,204);
        background: linear-gradient(90deg, rgba(0,136,204,1) 0%, rgba(0,69,103,1) 53%, rgba(0,68,102,1) 87%);
        height: 75px;
        transition: all 0.3s ease 0s;
    }

    svg{
        width: 50px;
        height: 50px;
        margin-left: 10px;
    }
    
    .block2 > p, .block1 > p {
        margin: 0 auto;
        font-size: clamp(20px,1.5vw,40px);
    }

    .block2{
        height: 75px;
        width: clamp(300px,36.4583vw,700px);
        border-radius: 20px;
        display: flex;
        align-items: center;
        background: rgb(0,0,0);
        background: linear-gradient(90deg, rgba(0,0,0,1) 0%, rgba(102,102,102,1) 68%);
        transition: all 0.3s ease 0s;
    }

    .block2:hover, .block1:hover{
        transform: scale(1.1);
    }
</style>