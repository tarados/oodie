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
    const data = await get('categories');
    const categories = data.categories;
    commit('setCategories', categories);
  }
}

export const getters = {
  categories: (state) => state.categories,
  getCategory: (state) => (id) => {
    if (!state.categories.find(todo => todo.id === id)) {
      return '';
    }
    return state.categories.find(todo => todo.id === id);
  }
}
