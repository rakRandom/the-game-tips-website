/** @type {import('tailwindcss').Config} */
export default {
  plugins: [],
  theme: {
    extend: {
      fontFamily: {
        'sans': ['Roboto','sans-serif'],
      },
    },
  },
  content: [
    "./index.html",
    "./src/**/*.{svelte,js,ts,jsx,tsx}",
  ],
  variants: {
    extend: {},
  },
  darkMode: "selector"
}
