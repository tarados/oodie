import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter);

const routes = [
    {
        path: '/',
        name: 'Home',
        meta: {layout: 'main'},
        component: () => import('../views/Home')
    },
    {
        path: '/brands/',
        name: 'Products',
        meta: {layout: 'main'},
        component: () => import('../views/Products')
    },
    {
        path: '/brands/',
        name: 'Products',
        meta: {layout: 'main'},
        component: () => import('../views/Products')
    },
    {
        path: '/products/card',
        name: 'Card',
        meta: {layout: 'main'},
        component: () => import('../views/Card')
    },
    {
        path: '/products/checkout',
        name: 'Checkout',
        meta: {layout: 'main'},
        component: () => import('../views/Checkout')
    },
    {
        path: '/products/checkout/successful',
        name: 'Successful',
        meta: {layout: 'main'},
        component: () => import('../views/Successful')
    },
    {
        path: '/products/:id',
        name: 'Product',
        meta: {layout: 'main'},
        component: () => import('../views/Product')
    }

];

const router = new VueRouter({
    mode: 'history',
    routes
});

export default router
