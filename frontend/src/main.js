import Vue from 'vue'
import Vuelidate from "vuelidate"
import Autocomplete from '@trevoreyre/autocomplete-vue'
import App from './App.vue'
import router from './router'
import store from './store'
import './style/index.css'
import * as Sentry from "@sentry/browser";
import { Integrations } from "@sentry/tracing";

Sentry.init({
  Vue,
  dsn: "https://bdc6ae9fbb5947c3aacc15db656193d5@o498785.ingest.sentry.io/5578616",
  autoSessionTracking: true,
  integrations: [
    new Integrations.BrowserTracing(),
  ],

  // We recommend adjusting this value in production, or using tracesSampler
  // for finer control
  tracesSampleRate: 1.0,
});

Vue.config.productionTip = false;

Vue.use(Vuelidate);
Vue.use(Autocomplete);

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app');
store.dispatch('loadFromCard');
store.dispatch('loadProducts');

