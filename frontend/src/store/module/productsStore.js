import Vue from 'vue'
import * as card from '../../js/card'
import {get} from "@/js/send";

export default {
    actions: {
        async loadProducts(context) {
            const response = await get('products');
            context.commit('addProducts', response.products);
            context.commit('addCategories', response.categories);
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
        loadFromCard({commit}) {
            commit('addProductFromCard');
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
            card.setItems(state.cardProducts);
        },
        decrement(state, index) {
            changeQuantity(state, index, -1);
            card.setItems(state.cardProducts);

        },
        delProduct(state, index) {
            state.cardProducts.splice(index, 1);
            card.setItems(state.cardProducts);
        },
        setCurrentProduct(state, product) {
            state.currentProduct = product;
        },
        addProduct(state, product) {
            state.cardProducts.push(product);
            card.setItems(state.cardProducts);
        },
        addProductFromCard(state) {
            state.cardProducts = card.getItems();
        },
        loadCities(state, response) {
            state.citiesList = response
        },
        loadWarehouses(state, response) {
            state.warehouseList = response
        },
        isVisible(state) {
            state.basketVisible = !state.basketVisible;
        }
    },
    state: {
        productsList: [],
        categoriesList: [],
        currentProduct: null,
        cardProducts: [],
        basketVisible: true,
        citiesList: [],
        warehouseList: []
    },
    getters: {
        allProducts(state) {
            return state.productsList;
        },
        allCategories(state) {
            return state.categoriesList;
        },
        allCities(state) {
            return state.citiesList;
        },
        allWarehouses(state) {
            return state.warehouseList;
        },
        totalPrice(state) {
            let sum = 0;
            state.cardProducts.forEach(function (item) {
                sum += item.total;
            });
            return sum + ' грн';
        }
    }
}

function changeQuantity(array, index, number) {
    const item = array.cardProducts[index];
    item.quantity = item.quantity + number;
    item.total = parseFloat((item.price * item.quantity).toFixed(1));
    Vue.set(array.cardProducts, index, item);
}



