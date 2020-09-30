import Vue from 'vue'
import Vuelidate from "vuelidate"
import Autocomplete from '@trevoreyre/autocomplete-vue'
import App from './App.vue'
import router from './router'
import store from './store'
import './style/index.css'

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

