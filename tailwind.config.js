/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: false,
  content: [
    "./templates/**/*.html",
    "./static/src/**/*.js",
    "node_modules/preline/dist/*.js",
  ],
  theme: {
    extend: {},
  },
  plugins: [require("preline/plugin")],
};
