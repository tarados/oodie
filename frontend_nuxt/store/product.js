export const state = () => ({
  product: {}
})

export const mutations = {
  setProduct(state, product) {
    state.product = product
  }
}

export const actions = {
  async fetch({commit}, id) {
    const data = await this.$axios.$get('https://hoodiyalko.avallon.im/app/products/product' + '/' + id);
    const product = data.product;
    commit('setProduct', product);
  }
}

export const getters = {
  product: s => s.product
}
