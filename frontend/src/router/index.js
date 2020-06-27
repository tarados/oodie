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
        path: '/products/product',
        name: 'Product',
        component: () => import('../views/Product')
    }

];

const router = new VueRouter({
    mode: 'history',
    routes
});

export default router
