<script>
    import { onMount } from 'svelte';

    let mask;

    onMount(() => {
        setTimeout(() => {
            mask.classList.add('hide');
            setTimeout(() => {
                mask.remove();
            }, 600); 
        }, 600);
    });
</script>

<div class="mask" bind:this={mask}>
    <div class="loader"></div>
</div>

<style>
    .hide {
        opacity: 0;
        transition: opacity 1s;
    }

    .mask {
        width: 100%;
        height: 100%;
        background: white;
        position: fixed;
        left: 0;
        top: 0;
        z-index: 100;
        display: flex;
        justify-content: center;
        align-items: center;
        transition: all 0.6s ease 0s;
    }

    .loader {
        width: 50px;
        height: 50px;
        border: 10px solid  #0023D7;
        border-radius: 50%;
        border-left-color: #001896 ;
        animation: loader 1.3s linear infinite;
    }

    @keyframes loader {
        100% {
            transform: rotate(360deg);
        }
    }
</style>