import axios from "axios";

async function messagesS() {
  const data = await axios.get('https://hoodiyalko.avallon.im/app/locales');
  const msg = data.data;
  return msg
}

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
    '~/plugins/flag.js'
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
    '@nuxtjs/i18n',
    'nuxt-client-init-module'
  ],

  // Axios module configuration: https://go.nuxtjs.dev/config-axios
  axios: {},

  i18n: {
    locales: ['ru', 'ua'],
    strategy: 'no_prefix',
    defaultLocale: 'ru',
    vueI18n: {
      fallbackLocale: 'ru',
      messages: messagesS()
    }
  },
  // Build Configuration: https://go.nuxtjs.dev/config-build
  build: {
    transpile: [/flag/]
  },

  middleware: ['localization'],

  router: {
    middleware: 'localization'
  }
}

