<template>
  <div class="wrapper">
    <div class="row">
      <router-link :to="{name: 'Product', params: {id: product.id} }"
                   v-for="product in prodList" :key="product.title"
                   :class="{ product: large, item_sm: small}"
      >
        <img :src="product.image">
        <h4>{{ product.title }}</h4>
        <div class="price-box">
          <span v-if="product.new_price" class="no-current">{{ product.price }} грн</span>
          <span v-else>{{ product.price }} грн</span>
          <span class="old" v-show="product.new_price">{{ product.new_price }} грн</span>
        </div>
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
            },
            category: {
                type: String
            }
        },
        data() {
            return {
                large: true,
                small: false
            }
        },
        computed: {
            ...mapGetters(["allProducts"]),
            prodList() {
                if (this.category) {
                    return this.allProducts.filter(product => product.category[0] === this.category);
                } else {
                    return this.allProducts.filter(product => product.category[0] !== 'oodie');
                }
            }
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
                this.$emit('productsList', response.products);
            }
        },
        mounted() {
            console.log(this.allProducts);
            this.loadProducts();
            this.setItem();
        }
    }
</script>

<style scoped>
  .wrapper {
    margin-top: 3rem;
  }

  h4 {
    margin-top: 1%;
    margin-bottom: 0;
  }

  .row {
    max-width: 1200px;
    margin: 0 auto;
    display: flex;
    flex-wrap: wrap;
    justify-content: flex-start;
    align-items: center;
    align-content: center;
  }

  .product {
    padding-bottom: 1rem;
    text-decoration: none;
    color: #3d4246;
    width: calc((100% / 12) * 6 - 30px);
    margin: 0 15px;
  }

  .price-box span {
    margin-top: 1%;
    margin-bottom: 1%;
  }

  .item_sm {
    padding-bottom: 1rem;
    text-decoration: none;
    color: #3d4246;
    width: calc((100% / 12) * 4 - 30px);
    margin: 0 15px;
  }

  .product img, .item_sm img {
    width: 100%;
  }

  .price-box {
    width: 100%;
    display: inline-flex;
    flex-wrap: wrap;
    justify-content: space-between;
  }

  span.old {
    color: red;
    flex-grow: 25;
  }

  .no-current {
    text-decoration: line-through;
    flex-grow: 1;
  }

  /*media queries*/
  @media screen and (max-width: 1200px) {
    .product {
      padding-left: 0;
    }

  }

  @media screen and (max-width: 960px) {
    h4,
    .price-box {
      font-size: 2.5vw;
    }

    .header h2 {
      font-size: calc(3.125vw + 10px);
    }
  }


  @media screen and (max-width: 750px) {
    .product {
      flex-basis: 600px;
    }

    .item_sm {
      width: calc((100% / 12) * 6 - 30px);
    }

  }

  @media screen and (max-width: 420px) {
    .item_sm {
      width: calc((100% / 12) * 12 - 30px);
    }
  }

  @media screen and (max-width: 375px) {

  }

  @media screen and (max-width: 360px) {

  }


</style>