import Vue from 'vue'
import * as card from '../../js/card'
import {get} from "@/js/api";
import defaultLocales from "@/assets/defaultLocales.json";

export default {
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
        },
        clearBasket(state) {
            state.cardProducts = [];
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
        cardProducts: [],
        basketVisible: true,
        citiesList: [],
        warehouseList: [],
        locale: 'ru',
        // locale: window.navigator.language || 'ua',
        locales: processLocalization(defaultLocales)
    },
    getters: {
        currentProduct(state) {
            return state.currentProduct;
        },
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
        },
        getLocale(state) {
            return state.locale;
        },
        getLocales(state) {
            return state.locales;
        }
    }
}

function changeQuantity(array, index, number) {
    const item = array.cardProducts[index];
    item.quantity = item.quantity + number;
    item.total = parseFloat((item.price * item.quantity).toFixed(1));
    Vue.set(array.cardProducts, index, item);
}

function processLocalization(data) {
    const result = {};

    for (let localeKey in data) {
        result[localeKey.slice(0, 2)] = data[localeKey];
    }

    return result;
}



