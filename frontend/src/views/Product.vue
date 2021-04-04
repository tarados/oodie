<template>
  <div>
    <div class="wrapper-product" v-if="this.selectedProduct">
      <div class="breadcrumbs-wrapper">
        <Breadcrumbs/>
      </div>

      <div class="row" v-if="this.selectedProduct">
        <div class="item left">
          <div class="item-left">
            <vueper-slides
                :touchable="false"
                :bullets="false"
                :slide-ratio="841 / 561"
                :initSlide="imageIndex"
                ref="vueperslides1"
            >
              <vueper-slide v-for="(slide, i) in slides" :key="i" :image="slide.image"/>
            </vueper-slides>
          </div>

          <div class="item-left-slider">
            <div class="slider" v-for="(image, index) in selectedProduct.image_list" :key="image">
              <img :src="image" @click="$refs.vueperslides1.goToSlide(index)">
            </div>
          </div>
        </div>
        <div class="item right">
          <div class="product-category">
            <span>{{ 'ProductBrand' | localize }}: </span>
            <div>{{ this.currentCategory }}</div>
          </div>
          <div class="product-price">
            <div class="price">
              <div class="current" v-if="this.selectedProduct.new_price">
                {{ this.selectedProduct.price }} грн
              </div>
              <div v-else>
                {{ this.selectedProduct.price }} грн
              </div>
              <div
                  :class="{ markdown: !selectedProduct.new_price}"
                  class="red"
              >
                {{ this.selectedProduct.new_price }} грн
              </div>
            </div>
          </div>
          <div class="product-title">
            <div>{{ this.selectedProduct.title }}</div>
          </div>
          <div class="size-block" v-if="!this.hideSize">
            <div
                class="square"
                v-for="(availability, index) in availabilities"
                :class="{selected: index === size, notActive: availability.quantity <= 0 && !availability.preorder}"
                :key="index"
                @click="select(index)"
            >
              {{ availability.size }}
            </div>
          </div>
          <div class="size-table" v-if="this.selectedProduct.table">
            <a :href="this.selectedProduct.table" target="_blank">{{ 'ProductSizeTable' | localize }}</a>
          </div>
          <div class="btn" @click="toCart">{{ getStatus | localize }}</div>
          <div class="preorder" v-if="preorder">{{ 'ProductStatusPreorderDescription' | localize }}</div>
          <div class="preorder" v-if="!preorder">{{ 'ProductStatusBasketDescription' | localize }}</div>
          <div class="product-description">
            <div class="description">{{ this.selectedProduct.description_locale | localize(this.selectedProduct.description) }}</div>
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
import {mapState} from "vuex";
import {required} from "vuelidate/lib/validators";

export default {
  name: "Product",
  data() {
    return {
      imageIndex: 0,
      size: 0,
      availabilities: [],
      preorder: null,
      inStockNo: null,
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
    ...mapState(["currentProduct", "categoriesList"]),
    selectedProduct() {
      const product = this.currentProduct;
      if (product) {
        return product;
      } else {
        return {};
      }
    },
    currentCategory() {
      const category = this.categoriesList.find(category => category.id === this.selectedProduct.category);
      if (category && category.title) {
        return category.title;
      } else {
        return "";
      }
    },
    selectedImage() {
      return this.imageIndex;
    },
    getStatus() {
      if (this.preorder) {
        return 'ProductStatusPreorder'
      } else if (this.inStockNo) {
        return 'InStockNo'
      } else {
        return 'ProductStatusBasket'
      }
    }
  },
  methods: {
    async loadProduct() {
      await this.$store.dispatch("loadProduct", this.$route.params.id);
      const images = this.selectedProduct.image_list;
      images.forEach(image => {
        this.slides.push({
          "image": image,
        });
      });
      this.availabilities = this.selectedProduct.availability;
      if (!this.availabilities.length || (this.availabilities.length === 1 && this.availabilities[0].size === "ONE SIZE")) {
        this.hideSize = true;
        this.preorder = this.availabilities[0].preorder;
        if (this.availabilities[0].quantity === 0) {
          this.inStockNo = true;
          let buttonToCart = document.querySelector('.btn');
          buttonToCart.style.color = 'black';
          buttonToCart.style.backgroundColor = 'white';
          buttonToCart.style.border = '1px solid black';
        }
      }
    },
    showImage(index) {
      this.imageIndex = index;
    },
    toCart() {
      const availability = this.availabilities.length > 0 ? this.availabilities[this.size] : {
        "size": "",
        "quantity": "0",
        "preorder": false
      };

      const productToCart = {
        "id": this.selectedProduct.id,
        "title": this.statusProduct ? this.selectedProduct.title + ' (предзаказ!)' : this.selectedProduct.title,
        "price": this.selectedProduct.new_price ? this.selectedProduct.new_price : this.selectedProduct.price,
        "quantity": 1,
        "preorder": availability.preorder,
        "size": availability.size,
        "image": this.selectedProduct.image_list[this.imageIndex],
      };
      if (productToCart.size === "") {
        delete productToCart.size;
      }
      const total = parseFloat(productToCart.price).toFixed(1) * parseFloat(productToCart.quantity).toFixed(1);
      productToCart.total = total;
      this.$store.commit("addProductToCart", productToCart);
      this.$router.push({name: "Cart"});
    },
    select(index) {
      this.size = index;
      this.preorder = this.availabilities[index].preorder;
    },
  },
  watch: {
    size: function () {
      if (this.availabilities[this.size].preorder) {
        this.statusProduct = true
      } else {
        this.statusProduct = false
      }
    }
  },
  mounted() {
    this.loadProduct();

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

.image-container {
  width: 500px;
}

.item-left-slider {
  display: flex;
  flex-wrap: wrap;
  margin-top: 0.25rem;
}

.slider {
  width: 120px;
  height: 120px;
  overflow: hidden;
  margin-right: 8px;
  margin-bottom: 12px;
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

.right {
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
}

.description {
  line-height: 1.5rem;
  white-space: pre-wrap;
}

.markdown {
  display: none;
}

.btn {
  display: flex;
  justify-content: center;
  max-width: 240px;
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
  width: 60%;
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

.preorder {
  color: #d24e49;
  margin: 20px 0;
}

.product-category {
  display: inline-flex;
  align-items: baseline;
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

  .slider {
    width: 78px;
    height: 78px;
  }
}


@media screen and (max-width: 460px) {
  .vueperslides--fixed-height {
    height: calc(100vh - 250px);
  }

  .item {
    width: calc(100% - 30px);
  }

  .viewer {
    display: contents;
  }

  .btn,
  .size-block {
    width: auto;
  }

  .size-block .square {
    min-width: 2rem;
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

@media screen and (max-width: 320px) {
  .vueperslides--fixed-height {
    height: calc(100vh - 370px);
  }
}

</style>
