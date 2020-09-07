import Vue from 'vue'
import Vuelidate from "vuelidate"
import Autocomplete from '@trevoreyre/autocomplete-vue'
import VueBreadcrumbs from 'vue-2-breadcrumbs'
import App from './App.vue'
import router from './router'
import store from './store'
import './style/index.css'

Vue.config.productionTip = false;

Vue.use(Vuelidate);
Vue.use(Autocomplete);
Vue.use(VueBreadcrumbs);

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app');
store.dispatch('loadFromCard');
