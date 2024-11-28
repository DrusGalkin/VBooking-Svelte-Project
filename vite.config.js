import { defineConfig } from 'vite'
import { svelte } from '@sveltejs/vite-plugin-svelte'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [svelte()],
  server: {
        watch: {
            usePolling: true,
        },
        host: true, // needed for the DC port mapping to work
        strictPort: true,
        port: 5173,
        hmr: {
            host: 'localhost',
        },
    }
})
