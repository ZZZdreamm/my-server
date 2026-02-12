import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vite.dev/config/
export default defineConfig({
  base: '/',
  plugins: [
    react({
      babel: {
        plugins: [['babel-plugin-react-compiler']],
      },
    }),
  ],
  server: {
    watch: {
      usePolling: true, 
    },
    allowedHosts: [
      'frontend',   
      'localhost',  
    ],
    host: true,
    strictPort: true,
    port: 5173,
    hmr: {
      clientPort: 80,
    },
  },
})
