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
    const warehouses = await this.$axios.$get('https://hoodiyalko.avallon.im/app/warehouse?city_id=' + cityId);
    commit('setWarehouses', warehouses);
  }
}

export const getters = {
  warehouses: s => s.warehouses
}
