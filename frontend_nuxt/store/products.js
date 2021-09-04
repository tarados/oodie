import {get} from '~/assets/js/api'

export const state = () => ({
  products: []
})

export const mutations = {
  setProducts(state, products) {
    state.products = products
  }
}

export const actions = {
  async fetch({commit}) {
    const data = await get('products');
    const products = data.products;
    commit('setProducts', products);
  }
}

export const getters = {
  products: s => s.products
}
