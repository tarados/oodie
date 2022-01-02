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
  products: (state) => state.products,
  getQuantity: (state) => (id, size) => {
    if (!state.products.find(item => item.id === id)) {
      return null
    }
    const product = state.products.find(item => item.id === id);
    if (!product.availability.find(el => el.size === size)) {
      return null
    }
    if (!product.availability.find(el => el.size === size).quantity) {
      return null
    }
    return  product.availability.find(el => el.size === size).quantity;
  }
}
