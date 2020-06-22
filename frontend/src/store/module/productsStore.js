// import Vue from 'vue'

export default {
    actions: {},
    mutations: {
        addProduct(state, items) {
            const products = [];
            items.forEach(item => {
                item.image = "http://localhost:8000" + item.image;
                products.push(item);
            })
            state.productsList = products;
        }
    },
    state: {
        productsList: []
    },
    getters: {
        allProducts(state) {
            return state.productsList;
        }
    }
}