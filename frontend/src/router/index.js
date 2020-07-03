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
        path: '/products/',
        name: 'Products',
        component: () => import('../views/Products')
    },
    {
        path: '/products/card',
        name: 'Card',
        component: () => import('../views/Card')
    },
    {
        path: '/products/checkout',
        name: 'Checkout',
        component: () => import('../views/Checkout')
    },

    {
        path: '/products/:id',
        name: 'Product',
        component: () => import('../views/Product')
    }

];

const router = new VueRouter({
    mode: 'history',
    routes
});

export default router
