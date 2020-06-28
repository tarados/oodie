<template>
  <div>
    <Navbar/>
    <div class="wrapper">
      <div class="row" v-if="this.currentProduct">
        <div class="item left">
          <div class="item-left">
            <img :src="this.currentProduct.image_list[0]" class="noZoomImg">
          </div>
          <div class="item-left">
          </div>
        </div>
        <div class="item right">
          <div class="item-right">
            <h1>{{this.currentProduct.title}}</h1>
          </div>
          <div class="item-right">
            <div class="price">
              <div class="current" v-show="!this.currentProduct.new_price">
                ${{this.currentProduct.price}} Sale
              </div>
              <div :class="{ markdown: !currentProduct.new_price}">
                ${{this.currentProduct.new_price}} Sale
              </div>
            </div>
          </div>
          <div class="item-right">
            <div class="btn-prd">
              <button class="btn">Купить</button>
            </div>
          </div>
        </div>
      </div>
      <div class="row" v-else>Loading...</div>
    </div>
  </div>
</template>

<script>
    import Navbar from "../components/Navbar";
    import {get} from "../js/send";

    export default {
        name: "Product",
        components: {
            Navbar
        },
        computed: {
           currentProduct() {
               return this.$store.state.productsStore.currentProduct
           }
        },
        methods: {
            async loadProduct(id) {
                const response = await get('products/product' + '/' + id);
                this.$store.commit('setCurrentProduct', response.product);
            }
        },
        mounted() {
            this.loadProduct(this.$route.params.id);
        }
    }
</script>

<style scoped>
  .wrapper {
    margin-top: 55px;
  }

  .row {
    max-width: 1200px;
    margin: 0 auto;
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    align-items: inherit;
    align-content: center;
  }

  .item {
    text-align: left;
    font-size: 1.1em;
    font-family: "Roboto", "Lucida Grande", "DejaVu Sans", "Bitstream Vera Sans", Verdana, Arial, sans-serif;
    color: rgb(61, 66, 70);
    border: 1px solid black;
    width: calc((100% / 12) * 6 - 30px);
    margin: 0 15px;
    overflow: hidden;
  }

  .item img {
    width: 100%;
  }

  .item img:hover {
    transform: scale(1.5);

  }

  .price {
    margin: 10px 0;
    color: #eb6f6e;
  }

  .right .left {
    display: block;

  }

  .markdown {
    display: none;
  }

  .item-left {

  }

  .item-right {

  }

  .btn {
    width: 80%;
    font-family: "montreal-serialbold", sans-serif;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    white-space: normal;
    font-size: 14px;
    border: none;
    border-radius: 3px;
    background-color: #ca492d;
    color: white;
    padding: 0.75rem 1.5rem;
    margin-top: 1rem;
    text-decoration: none;
    transition: opacity 1s ease-in;
  }

  .btn-prd {
    text-align: center;
  }
</style>