import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

Vue.use(VueRouter);

const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home
    },
    {
        path: '/collections/products/',
        name: 'Products',
        component: () => import('../views/Products')
    },
    {
        path: '/collections/products/product',
        name: 'Product',
        component: () => import('../views/Product')
    }

];

const router = new VueRouter({
    routes
});

export default router
