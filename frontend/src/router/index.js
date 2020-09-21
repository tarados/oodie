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
        path: '/about',
        name: 'About',
        meta: {layout: 'main'},
        component: () => import('../views/About')
    },
    {
        path: '/contacts',
        name: 'Contacts',
        meta: {layout: 'main'},
        component: () => import('../views/Contacts')
    },
    {
        path: '/brands/:slug',
        name: 'Brand',
        meta: {layout: 'main'},
        component: () => import('../views/Brand')
    },
    {
        path: '/brands',
        name: 'Brands',
        meta: {layout: 'main'},
        component: () => import('../views/Brands')
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
    },
    {
        path: '/products/:id/table-size',
        name: 'Table',
        meta: {layout: 'empty'},
        component: () => import('../views/Table')
    }

];

const router = new VueRouter({
    mode: 'history',
    routes
});

export default router
