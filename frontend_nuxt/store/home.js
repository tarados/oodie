import {get} from '~/assets/js/api'

export const state = () => ({
  home: {}
})

export const mutations = {
  setHome(state, home) {
    state.home= home
  }
}

export const actions = {
  async fetch({commit}) {
    const data = await get('home');
    const home = data.home_page;
    commit('setHome', home);
  }
}

export const getters = {
  home: s => s.home
}
