import Vue from 'vue'
import Vuex from 'vuex'
import {get} from "@/js/api";
import * as cart from "@/js/cart";
import defaultLocales from "@/assets/defaultLocales.json";


Vue.use(Vuex)

export default new Vuex.Store({
  actions: {
    async loadProducts(context) {
      const response = await get('products');
      context.commit('addProducts', response.products);
      context.commit('addCategories', response.categories);
    },
    async loadLocales(context) {
      const response = await get('locales');

      context.commit('addLocales', processLocalization(response));
    },
    async loadProduct(context, id) {
      context.commit('setCurrentProduct', null);
      const response = await get('products/product' + '/' + id);
      context.commit('setCurrentProduct', response.product);
    },
    async loadCities(context) {
      const response = await get('cities');
      context.commit('loadCities', response);
    },
    async loadWarehouses(context, cityId) {
      const endpoint = 'warehouse' + '?city_id=' + cityId;
      const response = await get(endpoint);
      context.commit('loadWarehouses', response);
    },
    loadFromCart({commit}) {
      commit('addProductFromCart');
    },
    changeVisibleBasket({commit}) {
      commit('isVisible');
    }
  },
  mutations: {
    addProducts(state, products) {
      state.productsList = products;
    },
    addCategories(state, categories) {
      state.categoriesList = categories;
    },
    increment(state, index) {
      changeQuantity(state, index, 1);
      cart.setItems(state.cartProducts);
    },
    decrement(state, index) {
      changeQuantity(state, index, -1);
      cart.setItems(state.cartProducts);

    },
    delProduct(state, index) {
      state.cartProducts.splice(index, 1);
      cart.setItems(state.cartProducts);
    },
    setCurrentProduct(state, product) {
      state.currentProduct = product;
    },
    addProductToCart(state, product) {
      state.cartProducts.push(product);
      cart.setItems(state.cartProducts);
    },
    addProductFromCart(state) {
      state.cartProducts = cart.getItems();
    },
    loadCities(state, response) {
      state.citiesList = response
    },
    loadWarehouses(state, response) {
      state.warehouseList = response
    },
    isVisible(state) {
      state.basketVisible = !state.basketVisible;
    },
    clearBasket(state) {
      state.cartProducts = [];
    },
    setLocale(state, locale) {
      state.locale = locale;
    },
    addLocales(state, response) {
      state.locales = response;
    }
  },
  state: {
    productsList: [],
    categoriesList: [],
    currentProduct: null,
    cartProducts: [],
    basketVisible: true,
    citiesList: [],
    warehousesList: [],
    locale: getDefaultLocale(),
    locales: processLocalization(defaultLocales)
  },
  getters: {
    totalPrice(state) {
      let sum = 0;
      state.cartProducts.forEach(function (item) {
        sum += item.total;
      });
      return sum + ' грн';
    },
    breadcrumbs(state) {
      const { currentProduct, categoriesList } = state;
      const result = [];
      if (currentProduct && currentProduct.category === 1) {
        result.push({ title: "MenuHome", routeName: "Home" });
      } else {
        result.push({ title: "MenuBrandsFriends", routeName: "Brands" });

        if (currentProduct) {
          const category = categoriesList.find(category => category.id === currentProduct.category);
          if (category) {
            result.push({ title: category.title, routeName: "Brand", routeParams: { slug: category.slug } });
          }
        }
      }

      if (currentProduct) {
        result.push({ title: currentProduct.title });
      }

      return result;
    }
  }
})

function changeQuantity(array, index, number) {
  const item = array.cartProducts[index];
  item.quantity = item.quantity + number;
  item.total = parseFloat((item.price * item.quantity).toFixed(1));
  Vue.set(array.cartProducts, index, item);
}

function processLocalization(data) {
  const result = {};

  for (let localeKey in data) {
    result[localeKey.slice(0, 2)] = data[localeKey];
  }

  return result;
}

function getDefaultLocale() {
  const lang = window.navigator.language;
  if (lang) {
    return lang.slice(0, 2);
  } else {
    return 'ua'
  }
}
