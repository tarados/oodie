<template>
  <div class="wrapper">
    <div class="header">
      <h2>which will you choose?</h2>
    </div>
    <div class="row">
      <router-link :to="{name: 'Product', params: {id: product.id} }"
                   v-for="product in allProducts" :key="product.title"
                   :class="{ product: large, item_sm: small}"
      >
        <img :src="product.image">
        <h4>{{product.title}}</h4>
        <p>{{product.price}}</p>
        <p>{{product.id}}</p>
      </router-link>
    </div>
  </div>
</template>

<script>
    import {get} from '../js/send'
    import {mapGetters} from 'vuex'

    export default {
        name: "Collections",
        props: {
            thumbnail: {
                type: String
            }
        },
        data() {
            return {
                large: true,
                small: false,
            }
        },
        computed: {
            ...mapGetters(["allProducts"])
        },
        methods: {
            setItem() {
                if (this.thumbnail === 'large') {
                    this.large = true;
                    this.small = false;
                } else if (this.thumbnail === 'small') {
                    this.large = false;
                    this.small = true;
                }
            },
            async loadProducts() {
                const response = await get('products');
                this.$store.commit('addProducts', response.products);
            }
        },
        mounted() {
            this.loadProducts();
            this.setItem();
        }
    }
</script>

<style scoped>
  .wrapper {
    margin-top: 55px;
  }

  .header {
    margin-bottom: 55px;
  }

  .header h2 {
    text-transform: uppercase;
    text-align: center;
    letter-spacing: 0.1em;
    font-family: "montreal-serialbold", sans-serif;
    font-weight: 600;
    font-size: 1.4375em;
  }

  .row {
    max-width: 1200px;
    margin: 0 auto;
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    align-items: center;
    align-content: center;
  }

  .product {
    padding-bottom: 20px;
    width: calc((100% / 12) * 6 - 30px);
    margin: 0 15px;
  }

  .item_sm {
    padding-bottom: 20px;
    width: calc((100% / 12) * 4 - 30px);
    margin: 0 15px;
  }

  .product img, .item_sm img {
    width: 100%;
  }

  /*media queries*/
  @media screen and (max-width: 1200px) {
    .product {
      padding-left: 0;
    }
  }

  @media screen and (max-width: 750px) {
    .product {
      flex-basis: 600px;
    }
  }

  @media screen and (max-width: 420px) {

  }

  @media screen and (max-width: 375px) {

  }

  @media screen and (max-width: 360px) {

  }


</style>