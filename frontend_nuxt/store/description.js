import {get} from '~/assets/js/api'

export const state = () => ({
  description: {}
})

export const mutations = {
  setDescription(state, description) {
    state.description= description
  }
}

export const actions = {
  async fetch({commit}) {
    const data = await get('description');
    const description = data.description;
    commit('setDescription', description);
  }
}

export const getters = {
  description: s => s.description
}
