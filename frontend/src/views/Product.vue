<template>
  <div>
    <Navbar/>
    <div class="wrapper">
      <div class="row">
        <div class="item left">
          <img :src="this.allProduct.image_list[0]" class="noZoomImg">
        </div>
        <div class="item right">
          <h1>{{this.allProduct.title}}</h1>
          <div class="price">{{this.allProduct.price}} Sale</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
    import Navbar from "../components/Navbar";
    import {get} from "../js/send";
    import {mapGetters} from 'vuex'

    export default {
        name: "Product",
        components: {
            Navbar
        },
        computed: {
            ...mapGetters(["allProduct"]),
            ...mapGetters(["allProducts"])
        },
        methods: {
            async loadProduct(id) {
                const response = await get('products/product' + '/' + id);
                this.$store.commit('addProduct', response.product);
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
    padding-left: 10px;
    color: #eb6f6e;
  }
</style>