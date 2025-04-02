import { defineConfig } from "vite";
import tailwindcss from "@tailwindcss/vite";

export default defineConfig({
  clearScreen: false,
  server: {
    cors: {
      origin: "http://localhost:8000",
    },
  },
  plugins: [tailwindcss()],
});
