import Vue from 'vue'
import Vuelidate from "vuelidate"
import AutocompleteVue from 'autocomplete-vue'
import App from './App.vue'
import router from './router'
import store from './store'
import './style/index.css'

Vue.config.productionTip = false;
Vue.component('autocomplete-vue', AutocompleteVue);
Vue.use(Vuelidate);

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app');
store.dispatch('loadFromCard');
