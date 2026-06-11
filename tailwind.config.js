import svgToDataUri from 'mini-svg-data-uri'
import flattenColorPalette from 'tailwindcss/lib/util/flattenColorPalette'

/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  darkMode: 'class',
  theme: {
    extend: {},
  },
  plugins: [
    function ({ matchUtilities, theme }) {
      matchUtilities(
        {
          'bg-grid': (value) => ({
            backgroundImage: `url("${svgToDataUri(
              `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" width="32" height="32" fill="none" stroke="${value}"><path d="M0 .5H31.5V32"/></svg>`
            )}")`,
          }),
        },
        { values: flattenColorPalette(theme('backgroundColor')), type: 'color' }
      )
    },
  ],
}
