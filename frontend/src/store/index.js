import Vue from 'vue'
import Vuex from 'vuex'
import productsStore from "./module/productsStore";
import basketStore from "./module/basketStore";

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    productsStore,
    basketStore
  }
})
