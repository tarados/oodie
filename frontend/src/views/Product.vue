<template>
  <div>
    <div class="wrapper-product" v-if="this.currentProduct">
      <div class="breadcrumbs-wrapper">
        <Breadcrumbs/>
      </div>

      <div class="row" v-if="this.currentProduct">
        <div class="item left">
          <div class="item-left">
            <vueper-slides
                :initSlide="imageIndex"
            >
              <vueper-slide v-for="(slide, i) in slides" :key="i" :image="slide.image"/>
            </vueper-slides>
          </div>

          <div class="item-left viewer">
            <vueper-slides
                class="no-shadow"
                :infinite="false"
                :visible-slides="4"
                slide-multipleq
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
          <div class="size-block" v-if="!this.hideSize">
            <div
                class="square"
                v-for="(availability, index) in availabilities"
                :class="{selected: index === size, notActive: availability.quantity <= 0}"
                :key="index"
                @click="select(index)"
            >
              {{ availability.size }}
            </div>
          </div>
          <div class="size-table" v-if="this.currentProduct.table">
            <a :href="this.currentProduct.table" target="_blank">Таблица размеров</a>
          </div>
          <div class="unavailable" v-if="isUnavailable">нет в наличии</div>
          <div class="btn" @click="toCard" v-if="!isUnavailable">в корзину</div>
          <div class="product-description">
            <div class="description">{{ this.currentProduct.description }}</div>
          </div>
        </div>
      </div>
      <div class="row" v-else>Loading...</div>
    </div>
  </div>
</template>

<script>
import {VueperSlides, VueperSlide} from "vueperslides";
import "vueperslides/dist/vueperslides.css";
import Breadcrumbs from "@/components/Breadcrumbs";
import settings from "../settings";

import {required} from "vuelidate/lib/validators";

export default {
  name: "Product",
  data() {
    return {
      imageIndex: 0,
      size: 0,
      availabilities: [],
      visibleCard: true,
      slides: [],
      hideSize: false,
      breakpoints: {
        420: {
          disable: false,
        },
      },
    };
  },
  validations: {
    size: {required},
  },
  components: {
    VueperSlide,
    VueperSlides,
    Breadcrumbs,
  },
  computed: {
    currentProduct() {
      try {
        return this.$store.state.productsStore.currentProduct;
      } catch (TypeError) {
        return {};
      }

    },
    currentCategory() {
      try {
        return this.$store.getters.allCategories.find(category => category.id === this.currentProduct.category).title;
      } catch (TypeError) {
        return "";
      }
    },
    selectedImage() {
      return this.imageIndex;
    },
    isUnavailable() {
      let num = 0;
      this.currentProduct.availability.forEach(el => num += el.quantity)
      return num <= 0;
    }
  },
  methods: {
    async loadProduct() {
      await this.$store.dispatch("loadProduct", this.$route.params.id);
      const images = this.currentProduct.image_list;
      images.forEach(image => {
        this.slides.push({
          "image": image,
        });
      });
      this.availabilities = this.currentProduct.availability;

      if (!this.availabilities.length || (this.availabilities.length === 1 && this.availabilities[0].size === settings.hideSize)) {
        this.hideSize = true;
      }

    },
    showImage(index) {
      this.imageIndex = index;
    },
    toCard() {
      const availability = this.availabilities.length > 0 ? this.availabilities[this.size] : {
        "size": "",
        "quantity": "0",
      };
      const productToCard = {
        "id": this.currentProduct.id,
        "title": this.currentProduct.title,
        "price": this.currentProduct.new_price ? this.currentProduct.new_price : this.currentProduct.price,
        "quantity": 1,
        "availability": availability.quantity,
        "size": availability.size,
        "image": this.currentProduct.image_list[this.imageIndex],
      };
      if (productToCard.size === "") {
        delete productToCard.size;
      }
      const total = parseFloat(productToCard.price).toFixed(1) * parseFloat(productToCard.quantity).toFixed(1);
      productToCard.total = total;
      this.$store.commit("addProduct", productToCard);
      this.$router.push({name: "Card"});
    },
    select(index) {
      this.size = index;
    },
    basketVisible() {
      if (!this.$store.state.productsStore.basketVisible) {
        this.$store.dispatch("changeVisibleBasket");
      }
    },
  },
  mounted() {
    this.loadProduct();
    this.basketVisible();
  },
};
</script>

<style scoped>
.wrapper-product {
  margin-top: 55px;
  margin-bottom: 40px;
}

.wrapper__slider {
  background-color: yellow;
  width: 100%;
  height: 570px;
}

.vueperslides--fixed-height {
  /*height: calc(100vh - 76px);*/
}

.breadcrumbs-wrapper {
  padding-left: 15px;
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
  flex-wrap: wrap;
  justify-content: flex-start;
  align-items: inherit;
  align-content: center;
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

.content {
  width: 100%;
  height: 100%;
}

.item-left {
  margin-bottom: 15px;
}

.item-left-slider {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  margin-top: 0.25rem;
}

.slider {
  width: calc((100% / 12) * 3 - 10px);
  height: calc((100% / 12) * 3 - 10px);
  /*margin: 0 2% 1% 0;*/
}


.slider img:hover {
  border: 1px solid black;
}

.slide-image:hover {
  border: 1px solid black;
}

.price {
  margin: 15px 0;
  font-size: 1.2rem;
  text-transform: uppercase;
  letter-spacing: 0.08em;
}

.red {
  /*color: #eb6f6e;*/
}

.left {

}

.right {
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
}

.description {
  margin-top: 3rem;
  line-height: 1.5rem;
  white-space: pre-wrap;
}

.markdown {
  display: none;
}

.btn {
  display: flex;
  justify-content: center;
  max-width: 200px;
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
  width: auto;
  min-width: 3rem;
  height: 3rem;
  border: 1px solid grey;
  padding: 0px 5px;
  line-height: 3rem;
  /*margin: 1% 2.5% 1% 1%;*/
}

.square + .square {
  margin-left: 8px;
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
  text-transform: uppercase;
  letter-spacing: 0.08em;

}

.product-category span {
  font-size: 1rem;
  color: #9b9b9b;
}

.product-category div {
  font-size: 1rem;
  margin-left: 1%;
}

.product-title {
  border-bottom: 2px solid #9a9a9a;
  padding-bottom: 1rem;
  margin-bottom: 1rem;
}

.product-title div {
  font-size: 1.2rem;
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

.notActive {
  background-color: #9a9a9a;
  pointer-events: none;
  cursor: default;
}

.unavailable {
  width: 200px;
  padding: 16px 8px;
  border: 2px solid #565555;
  color: #565555;
  text-align: center;
  text-transform: uppercase;
}

/*media queries**************************************************************************/
@media screen and (max-width: 2800px) {
  .viewer {
    display: none;
  }
}

@media screen and (max-width: 960px) {
  .vueperslides--fixed-height {
    height: calc(100vh - 278px);
  }

}

@media screen and (max-width: 750px) {
  .vueperslides--fixed-height {
    height: calc(100vh - 318px);
  }
}

@media screen and (max-width: 650px) {
  .vueperslides--fixed-height {
    height: calc(100vh - 372px);
  }
}

@media screen and (max-width: 560px) {
  .vueperslides--fixed-height {
    height: calc(100vh - 424px);
  }
}


@media screen and (max-width: 460px) {
  .vueperslides--fixed-height {
    height: calc(100vh - 250px);
  }

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

  .item + .item {
    margin-top: 40px;
  }

}

@media screen and (max-width: 375px) {
  .vueperslides--fixed-height {
    height: calc(100vh - 324px);
  }
}

@media screen and (max-width: 360px) {

}

@media screen and (max-width: 320px) {
  .vueperslides--fixed-height {
    height: calc(100vh - 370px);
  }
}

</style>
