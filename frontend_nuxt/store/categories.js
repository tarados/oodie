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
    const data = await this.$axios.$get('https://hoodiyalko.avallon.im/app/products');
    console.log(data.categories);
    const categories = data.categories;
    commit('setCategories', categories);
  }
}

export const getters = {
  categories: s => s.categories
}
