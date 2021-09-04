import {get} from '~/assets/js/api'

export const state = () => ({
  warehouses: []
})

export const mutations = {
  setWarehouses(state, warehouses) {
    state.warehouses = warehouses
  }
}

export const actions = {
  async fetch({commit}, cityId) {
    const endpoint ='warehouse?city_id=' + cityId;
    const warehouses = await get(endpoint);
    // const warehouses = await this.$axios.$get('https://hoodiyalko.avallon.im/app/warehouse?city_id=' + cityId);
    commit('setWarehouses', warehouses);
  }
}

export const getters = {
  warehouses: s => s.warehouses
}
