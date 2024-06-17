/** @type {import('tailwindcss').Config} */
export default {
  plugins: [],
  theme: {
    fontFamily: {
      'sans': ['Roboto', 'sans-serif']
    },
    extend: {},
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
