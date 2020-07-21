<template>
  <div>
    <Navbar visible-card="visible-card"/>
    <div class="wrapper">
      <div class="row" v-if="this.currentProduct">
        <div class="item left">
          <div class="item-left">
            <img :src="this.currentProduct.image_list[imageIndex]" class="zoomImg">
          </div>
          <div class="item-left viewer">
            <vueper-slides
                class="no-shadow"
                :infinite="false"
                :visible-slides="4"
                slide-multiple
                :gap="3"
                :slide-ratio="1 / 4"
                :dragging-distance="70"
                :arrows-outside="false"
            >
              <vueper-slide
                  class="slide-image"
                  v-for="(slade, i) in slides"
                  :key="i"
                  :image="slade.image"
              >
                <template v-slot:content>
                  <div class="content" @click="showImage(i)"></div>
                </template>
              </vueper-slide>
            </vueper-slides>
          </div>
          <div class="item-left-slider">
            <div class="slider" v-for="(image, index) in currentProduct.image_list" :key="image">
              <img :src="image" @click="showImage(index)">
            </div>
          </div>
        </div>
        <div class="item right">
          <div class="item-right">
            <h1>{{ this.currentProduct.title }}</h1>
          </div>
          <div class="item-right">
            <div class="price">
              <div class="current" v-show="!this.currentProduct.new_price">
                ${{ this.currentProduct.price }} Sale
              </div>
              <div :class="{ markdown: !currentProduct.new_price}">
                ${{ this.currentProduct.new_price }} Sale
              </div>
            </div>
          </div>
          <div class="item-right">
            <div class="btn-prd">
              <button class="btn" @click="toCard">add to card</button>
            </div>
          </div>
          <div class="item-right">
            <div class="description">
              {{ this.currentProduct.description }}
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
    import {get} from "../js/send"
    import {VueperSlides, VueperSlide} from 'vueperslides';
    import 'vueperslides/dist/vueperslides.css';

    export default {
        name: "Product",
        data() {
            return {
                imageIndex: 0,
                visibleCard: true,
                slides: [],
                breakpoints: {
                    420: {
                        disable: false
                    }
                }
            }
        },
        components: {
            Navbar,
            VueperSlide,
            VueperSlides
        },
        computed: {
            currentProduct() {
                return this.$store.state.productsStore.currentProduct
            }
        },
        methods: {
            async loadProduct(id) {
                const response = await get('products/product' + '/' + id);
                const images = response.product.image_list;
                images.forEach(image => {
                    this.slides.push({
                        'image': image
                    });
                })
                this.$store.commit('setCurrentProduct', response.product);
            },
            showImage(index) {
                this.imageIndex = index;
            },
            toCard() {
                const productToCard = {
                    'id': this.currentProduct.id,
                    'title': this.currentProduct.title,
                    'price': this.currentProduct.new_price ? this.currentProduct.new_price : this.currentProduct.price,
                    'quantity': 1,
                    'image': this.currentProduct.image_list[this.imageIndex]
                };
                const total = parseFloat(productToCard.price).toFixed(1) * parseFloat(productToCard.quantity).toFixed(1);
                productToCard.total = total;
                this.$store.commit("addProduct", productToCard)
                this.$router.push({name: 'Card'});
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
    /*font-family: "Roboto", "Lucida Grande", "DejaVu Sans", "Bitstream Vera Sans", Verdana, Arial, sans-serif;*/
    color: rgb(61, 66, 70);
    /*border: 1px solid black;*/
    width: calc((100% / 12) * 6 - 30px);
    margin: 0 15px;
    overflow: hidden;
  }

  .item img {
    width: 100%;
    overflow: hidden;
  }

  .item img.zoomImg:hover {
    /*max-height: 50px;*/
    /*transform: scale(1.2);*/
  }

  .content {
    width: 100%;
    height: 100%;
  }

  .item-left-slider {
    display: flex;
    flex-wrap: wrap;
    justify-content: flex-start;
    margin-top: 3rem;
  }

  .slider {
    width: calc((100% / 12) * 3 - 1rem);
    margin: 0.5rem 0.5rem;
  }

  .slider img:hover {
    border: 1px solid black;
  }

  .slide-image:hover {
    border: 1px solid black;
  }

  .price {
    margin: 10px 0;
    color: #eb6f6e;
  }

  .right {
    display: block;
  }

  .description {
    margin-top: 10rem;
  }

  .markdown {
    display: none;
  }

  .item-left {

  }

  .btn {
    width: 80%;
    /*font-family: "montreal-serialbold", sans-serif;*/
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
    margin-top: 3rem;
  }

  /*media queries**************************************************************************/
  @media screen and (max-width: 2800px) {
    .viewer {
      display: none;
    }
  }

  @media screen and (max-width: 960px) {
    h1, .current {
      font-size: calc(3.125vw + 10px);
    }
  }

  @media screen and (max-width: 420px) {
    .item {
      width: calc(100% - 30px);
    }

    .item-left-slider {
      display: none;
    }

    .viewer {
      display: contents;
    }

  }

  @media screen and (max-width: 375px) {

  }

  @media screen and (max-width: 360px) {

  }

</style>