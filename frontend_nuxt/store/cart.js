import Vue from 'vue'
import * as cart from "~/assets/js/cart";

export const state = () => ({
  cartProducts: []
})

export const mutations = {
  setCartProducts(state, product) {
    state.cartProducts.push(product);
    cart.setItems(state.cartProducts);
  },
  delProduct(state, index) {
    state.cartProducts.splice(index, 1);
    cart.setItems(state.cartProducts);
  },
  increment(state, index) {
    changeQuantity(state, index, 1);
    cart.setItems(state.cartProducts);
  },
  decrement(state, index) {
    changeQuantity(state, index, -1);
    cart.setItems(state.cartProducts);
  },
  clearBasket(state) {
    state.cartProducts = [];
  }
}

export const getters = {
  cartProducts: s => s.cartProducts,
  totalPrice(state) {
    let sum = 0;
    state.cartProducts.forEach(function (item) {
      sum += item.total;
    });
    return sum + ' грн';
  }
}

function changeQuantity(array, index, number) {
  const item = array.cartProducts[index];
  item.quantity = item.quantity + number;
  item.total = parseFloat((item.price * item.quantity).toFixed(1));
  Vue.set(array.cartProducts, index, item);
}
