export default {
    actions: {},
    mutations: {
        addProducts(state, products) {
            state.productsList = products;
        },
        setCurrentProduct(state, product) {
            state.currentProduct = product;
        }
    },
    state: {
        productsList: [],
        currentProduct: null
    },
    getters: {
        allProducts(state) {
            return state.productsList;
        }
    }
}

