
   import adapter from '@sveltejs/adapter-auto';
   import preprocess from 'svelte-preprocess';
   import tailwindcss from 'tailwindcss';
   import autoprefixer from 'autoprefixer';
   import { vitePreprocess } from '@sveltejs/vite-plugin-svelte'

   /* @type {import('@sveltejs/kit').Config} */
   const config = {
     preprocess: [
       preprocess({
         postcss: {
           plugins: [tailwindcss, autoprefixer],
         },
       }),
     ],
     kit: {
       adapter: adapter(),
     },
   };

   export default config;