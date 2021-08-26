export default {
  // Global page headers: https://go.nuxtjs.dev/config-head
  head: {
    title: 'frontend_nuxt',
    htmlAttrs: {
      lang: 'en'
    },
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: '' },
      { name: 'format-detection', content: 'telephone=no' }
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }
    ]
  },

  // Global CSS: https://go.nuxtjs.dev/config-css
  css: [
    '~/assets/css/main.css'
  ],

  // Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins
  plugins: [
    '~/plugins/myplugin.js',
    '~/plugins/vueperslides.js',
    '~/plugins/vueperslide.js',
    '~/plugins/vuelidate.js'
  ],

  // Auto import components: https://go.nuxtjs.dev/config-components
  components: true,

  // Modules for dev and build (recommended): https://go.nuxtjs.dev/config-modules
  buildModules: [
  ],

  // Modules: https://go.nuxtjs.dev/config-modules
  modules: [
    // https://go.nuxtjs.dev/axios
    '@nuxtjs/axios',
    '@nuxtjs/i18n'
  ],

  // Axios module configuration: https://go.nuxtjs.dev/config-axios
  axios: {},

  i18n: {
    locales: ['ru', 'ua'],
    strategy: 'no_prefix',
    defaultLocale: 'ru',
    vueI18n: {
      fallbackLocale: 'ru',
      messages: {}
    }
  },
  // Build Configuration: https://go.nuxtjs.dev/config-build
  build: {
    transpile: [/myplugin/, /vueperslides/, /vueperslide/, /vuelidate/]
  },

  middleware: ['localization'],

  router: {
    middleware: 'localization'
  }
}

