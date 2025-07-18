tailwind.config = {
  theme: {
    extend: {
      colors: {
        primary: {
          300: '#f6abb5',
          400: '#f07c8f',
          500: '#e64d69',
          600: '#ca2b50',
          700: '#b02045',
          800: '#941d40',
        },
        mirage: {
          50: '#d6d9ef',
          100: '#bdc0e4',
          700: '#49456a',
          800: '#28263a',
          950: '#0d0d11',
        },
      },
    },
  },
  daisyui: {
    themes: ['light', 'dark'],
  },
  darkMode: ['selector', '[data-theme=dark]'],
};
