// import Vue from 'vue'

export default {
    actions: {},
    mutations: {
        addProducts(state, items) {
            const products = [];
            items.forEach(item => {
                item.image = "http://localhost:8000" + item.image;
                products.push(item);
            })
            state.productsList = products;
        },
        addProduct(state, product) {
            const equality = state.productsList.filter(item => item.id === product.id)
            let imageUrls = product.image_list.map(item => "http://localhost:8000" + item);
            product.image_list = imageUrls;
            product.title = equality[0].title;
            product.price = equality[0].price;
            state.productCase = product;
        }
    },
    state: {
        productsList: [],
        productCase: {}
    },
    getters: {
        allProducts(state) {
            return state.productsList;
        },
        allProduct(state) {
            return state.productCase;
        }
    }
}

