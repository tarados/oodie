import {get} from "~/assets/js/api";

export const state = () => ({
  cities: []
})

export const mutations = {
  setCities(state, cities) {
    state.cities = cities
  }
}

export const actions = {
  async fetch({commit}) {
    const cities = await get('cities');
    commit('setCities', cities);
  }
}

export const getters = {
  cities: s => s.cities
}
