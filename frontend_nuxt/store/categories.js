import {get} from '~/assets/js/api'

export const state = () => ({
  categories: []
})

export const mutations = {
  setCategories(state, categories) {
    state.categories = categories
  }
}

export const actions = {
  async fetch({commit}) {
    const data = await get('products');
    const categories = data.categories;
    commit('setCategories', categories);
  }
}

export const getters = {
  categories: s => s.categories
}
