import Vue from 'vue'
import * as card from '../../js/card'
import {get} from "@/js/send";

export default {
    actions: {
        async loadProducts(context) {
            const response = await get('products');
            context.commit('addProducts', response.products);
        },
        loadFromCard({commit}) {
            commit('addProductFromCard');
        }
    },
    mutations: {
        addProducts(state, products) {
            state.productsList = products;
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
        }
    },
    state: {
        productsList: [],
        currentProduct: null,
        cardProducts: [],
        totalPrice: 0
    },
    getters: {
        allProducts(state) {
            return state.productsList;
        },
        getTotalPrice(state) {
            let valueTotal = [];
            state.cardProducts.forEach(function (item) {
                valueTotal.push(item.total);
            });
            let totalPrice = eval(valueTotal.join('+'));
            if (totalPrice) {
                state.totalPrice = parseFloat(totalPrice).toFixed(0) + ' грн';
            } else {
                state.totalPrice = 0 + ' грн';
            }
            return state.totalPrice;
        }
    }
}

function changeQuantity(array, index, number) {
    const item = array.cardProducts[index];
    item.quantity = item.quantity + number;
    item.total = parseFloat((item.price * item.quantity).toFixed(1));
    Vue.set(array.cardProducts, index, item);
}

// function groupBy(array, key) {
//     return array.reduce((result, currentValue) => {
//         (result[currentValue[key]] = result[currentValue[key]] || []).push(
//             currentValue
//         );
//         return result;
//     }, {});
// }


