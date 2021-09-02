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
    const cities = await this.$axios.$get('https://hoodiyalko.avallon.im/app/cities');
    // const cities = data.data;
    commit('setCities', cities);
  }
}

export const getters = {
  cities: s => s.cities
}
