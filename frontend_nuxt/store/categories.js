export const state = () => ({
  categories: []
})

export const mutations = {
  setProducts(state, categories) {
    state.categories = categories
  }
}

export const actions = {
  async fetch({commit}) {
    const data = await this.$axios.$get('https://hoodiyalko.avallon.im/app/products');
    const categories = data.categories;
    commit('setProducts', categories);
  }
}

export const getters = {
  categories: s => s.categories
}
