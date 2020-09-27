<template>
  <div>
    <Breadcrumbs :current-category="this.currentCategory" :current-product="this.currentProduct.title"/>
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
          <div class="product-category">
            <span>бренд: </span>
            <div>{{ this.currentCategory }}</div>
          </div>
          <div class="product-price">
            <div class="price">
              <div class="current" v-if="this.currentProduct.new_price">
                {{ this.currentProduct.price }} грн
              </div>
              <div v-else>
                {{ this.currentProduct.price }} грн
              </div>
              <div
                  :class="{ markdown: !currentProduct.new_price}"
                  class="red"
              >
                {{ this.currentProduct.new_price }} грн
              </div>
            </div>
          </div>
          <div class="product-title">
            <div>{{ this.currentProduct.title }}</div>
          </div>
          <div class="size-block" v-show="this.currentProduct.category !== 1">
            <div
                class="square"
                v-for="(availability, index) in availabilities"
                :class="{selected: index === size}"
                :key="index"
                @click="select(index)"
            >
              {{ availability.size }}
            </div>
          </div>
          <div class="size-table" v-show="this.currentProduct.category !== 1">
            <router-link
                :to="{name: 'Table'}"
            >
              <small>Таблица размеров</small>
            </router-link>
          </div>
          <div class="btn" @click="toCard">в корзину</div>
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
import Breadcrumbs from "@/components/Breadcrumbs";
import {required} from 'vuelidate/lib/validators';

export default {
  name: "Product",
  data() {
    return {
      imageIndex: 0,
      size: 0,
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
  validations: {
    size: {required}
  },
  components: {
    VueperSlide,
    VueperSlides,
    Breadcrumbs
  },
  computed: {
    currentProduct() {
      try {
        return this.$store.state.productsStore.currentProduct
      } catch (TypeError) {
        return {}
      }

    },
    currentCategory() {
      try {
        return this.$store.getters.allCategories.find(category => category.id === this.currentProduct.category).title;
      } catch (TypeError) {
        return ''
      }

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
      const availability = this.availabilities.length > 0 ? this.availabilities[this.size] : {
        'size': '',
        'quantity': '0'
      };
      const productToCard = {
        'id': this.currentProduct.id,
        'title': this.currentProduct.title,
        'price': this.currentProduct.new_price ? this.currentProduct.new_price : this.currentProduct.price,
        'quantity': 1,
        'availability': availability.quantity,
        'size': availability.size,
        'image': this.currentProduct.image_list[this.imageIndex]
      };
      if (productToCard.size === '') {
        delete productToCard.size;
      }
      const total = parseFloat(productToCard.price).toFixed(1) * parseFloat(productToCard.quantity).toFixed(1);
      productToCard.total = total;
      this.$store.commit("addProduct", productToCard);
      this.$router.push({name: 'Card'});
    },
    select(index) {
      this.size = index;
    }
  },
  mounted() {
    this.loadProduct(this.$route.params.id);
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
  margin-top: 0.25rem;
}

.slider {
  width: calc((100% / 12) * 3 - 1rem);
  margin: 0 2% 1% 0;
}

.slider img:hover {
  border: 1px solid black;
}

.slide-image:hover {
  border: 1px solid black;
}

.price {
  margin: 15px 0;
  font-size: 1.5rem;
  text-transform: uppercase;
  letter-spacing: 0.08em;
}

.red {
  /*color: #eb6f6e;*/
}

.right {
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
}

.description {
  margin-top: 3rem;
  line-height: 1.6rem;
}

.markdown {
  display: none;
}

.item-left {

}

.btn {
  display: flex;
  justify-content: center;
  width: 30%;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  white-space: normal;
  font-size: 1rem;
  border: none;
  border-radius: 0;
  background-color: black;
  color: white;
  padding: 0.75rem 1.5rem;
  margin-top: 1rem;
  text-decoration: none;
  transition: opacity 1s ease-in;
  cursor: pointer;
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
  padding-top: 5px;
  margin: 1% 2.5% 1% 1%;
}

.size-block .square:hover {
  background-color: #7ec699;
  cursor: pointer;
}

.size-table {
  height: 3rem;
  display: flex;
  justify-content: flex-start;
  align-items: center;
  font-size: 1rem;
}

.size-table a {
  cursor: pointer;
  color: #908383;
  font-weight: 600;
  letter-spacing: 0.04em;
}

.product-category {
  display: inline-flex;
  align-items: baseline;
  justify-content: start;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.08em;

}

.product-category span {
  font-size: 1rem;
  color: #9b9b9b;
}

.product-category div {
  font-size: 1.5rem;
  margin-left: 1%;
}

.product-title {
  border-bottom: 2px solid #9a9a9a;
  padding-bottom: 1rem;
  margin-bottom: 1rem;
}

.product-title div {
  font-size: 1.5rem;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  font-weight: 600;
}

.current {
  text-decoration: line-through;
  margin-bottom: 1rem;
  color: #9b9b9b;
}

.button-block {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-around;
}

.selected {
  background-color: #c7d9d8;
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

  .btn,
  .size-block {
    width: auto;
  }

}

@media screen and (max-width: 375px) {

}

@media screen and (max-width: 360px) {

}

@media screen and (max-width: 320px) {

}

</style>