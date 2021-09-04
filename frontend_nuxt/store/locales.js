import {get} from '~/assets/js/api'

export const state = () => ({
  locales: []
})

export const mutations = {
  setLocales(state, data) {
    state.locales = data
  }
}

export const actions = {
  async fetch({commit}) {
    const data = await get('locales');
    let localesKey = Object.keys(data);
    let locales = [];
    localesKey.forEach(item => {
      locales.push(item.slice(0, 2));
    })
    commit('setLocales', locales);
  }
}

export const getters = {
  locales: s => s.locales
}
