import Vue from "vue";
import Vuelidate from "vuelidate";
import Autocomplete from "@trevoreyre/autocomplete-vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import localizeFilter from "@/js/localize.filter";
import "./style/index.css";
import * as Sentry from "@sentry/browser";
import { Integrations } from "@sentry/tracing";
import FlagIcon from "vue-flag-icon"
import Modal from "@burhanahmeed/vue-modal-2";

Sentry.init({
  Vue,
  dsn: "https://bdc6ae9fbb5947c3aacc15db656193d5@o498785.ingest.sentry.io/5578616",
  autoSessionTracking: true,
  integrations: [
    new Integrations.BrowserTracing(),
  ],

  tracesSampleRate: 1.0,
});

Vue.use(Vuelidate);
Vue.use(FlagIcon);
Vue.use(Autocomplete);
Vue.filter("localize", localizeFilter);
Vue.use(Modal, {
  componentName: "ModalVue"
});

Vue.config.productionTip = false;

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount("#app");
store.dispatch("loadLocales");
store.dispatch("loadFromCart");
store.dispatch("loadProducts");

