<template>
  <div>
    <div class="wrapper-product">
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
          <div
              class="product-category"
          >
            бренд: {{category}}
          </div>
          <div class="product-title">
            <h1>{{ this.currentProduct.title }}</h1>
          </div>
          <div class="product-price">
            <div class="price">
              <div class="current" v-show="!this.currentProduct.new_price">
                ${{ this.currentProduct.price }}
              </div>
              <div :class="{ markdown: !currentProduct.new_price}" class="red">
                {{ this.currentProduct.new_price }} грн Sale
              </div>
            </div>
          </div>
          <div class="size-block">
            <div
                class="square"
                v-for="(availability, index) in availabilities" :key="index"
            >
              {{ availability.size }}
            </div>
          </div>
          <div class="size-table">
            <router-link :to="{name: 'Brands'}">Таблица размеров</router-link>
          </div>
          <div class="button-block">
            <div class="btn-prd">
              <button class="btn" @click="toCard">add to card</button>
            </div>
          </div>
          <div class="product-description">
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
import {get} from "../js/send"
import {VueperSlides, VueperSlide} from 'vueperslides';
import 'vueperslides/dist/vueperslides.css';

export default {
  name: "Product",
  data() {
    return {
      imageIndex: 0,
      category: '',
      availabilities: [],
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
      });
      this.availabilities = response.product.availability;
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
      this.$store.commit("addProduct", productToCard);
      this.$router.push({name: 'Card'});
    },
    currentCategory() {
      this.category = this.$store.getters.allCategories.find(category => category.id === this.currentProduct.category).title;
    }
  },
  mounted() {
    this.loadProduct(this.$route.params.id);
    this.currentCategory();
  }
}
</script>

<style scoped>
.wrapper-product {
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
  color: rgb(61, 66, 70);
  width: calc((100% / 12) * 6 - 30px);
  margin: 0 15px;
  overflow: hidden;
}

.item img {
  width: 100%;
  max-height: 36rem;
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
}

.red {
  color: #eb6f6e;
}

.right {
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
}

.description {
  margin-top: 3rem;
}

.markdown {
  display: none;
}

.item-left {

}

.btn {
  width: 80%;
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

.size-block {
  width: 50%;
  display: flex;
  flex-wrap: wrap;
  justify-content: flex-start;
  align-items: center;
  height: 4rem;
  margin-top: 5%;
}

.size-block .square {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  align-items: center;
  font-size: 1.5rem;
  width: 3rem;
  height: 3rem;
  border: 1px solid grey;
  margin: 1% 2.5% 1% 1%;
}

.size-table {
  height: 3rem;
  display: flex;
  justify-content: flex-start;
  align-items: center;
  font-size: 1rem;
}

.size-table a {
  text-decoration: none;
  cursor: pointer;
}

.product-category {
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.08em;
}

/*.product-category span {*/
/*  font-size: 1.1rem;*/
/*}*/

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

@media screen and (max-width: 450px) {
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