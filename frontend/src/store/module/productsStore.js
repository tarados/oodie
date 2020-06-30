export default {
    actions: {},
    mutations: {
        addProducts(state, products) {
            state.productsList = products;
        },
        setCurrentProduct(state, product) {
            state.currentProduct = product;
        },
        addProductFromCard(state, product) {
            state.cardProducts.push(product);
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
        }
    }
}

