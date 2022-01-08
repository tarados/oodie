<template>
  <div class="row">
    <div class="item left">
      <ProductImages :slides="slides"/>
    </div>
    <div class="item right">
      <div class="product-category">
        <span>{{ $t('ProductBrand') }}: </span>
        <div>{{ currentCategory }}</div>
      </div>
      <div class="product-price">
        <div class="price">
          <div class="current" v-if="product.new_price">
            {{ product.price }} грн
          </div>
          <div v-else>
            {{ product.price }} грн
          </div>
          <div
            :class="{ markdown: !product.new_price}"
            class="red"
          >
            {{ product.new_price }} грн
          </div>
        </div>
      </div>
      <div class="product-title">
        <div>{{ title }}</div>
      </div>
      <div class="size-block" v-if="!hideSizeBlock">
        <div
          class="square"
          v-for="(availability, index) in product.availability"
          :class="{selected: index === productSizeIndex, notActive: availability.quantity <= 0 && !availability.preorder}"
          :key="index"
          @click="selectSize(index)"
        >
          {{ availability.size }}
        </div>
      </div>
      <div class="size-table" v-if="product.table">
        <a :href="product.table" target="_blank">{{ $t('ProductSizeTable') }}</a>
      </div>
      <div class="btn" @click="toCart">{{ $t(`${getStatus}`) }}</div>
      <div class="preorder" v-if="preorder">{{ $t('ProductStatusPreorderDescription') }}</div>
      <div class="preorder" v-if="!preorder">{{ $t('ProductStatusBasketDescription') }}</div>
      <div class="product-description">
        <div class="description">{{ description }}</div>
      </div>
    </div>
  </div>
</template>

<script>
import {required} from "vuelidate/lib/validators";

export default {
  name: "Product",
  props: {
    product: {
      type: Object
    }
  },
  data() {
    return {
      imageIndex: 0,
      productSizeIndex: 0,
      preorder: null,
      notAvailable: null,
      slides: [],
      hideSizeBlock: false,
    };
  },
  validations: {
    size: {required},
  },
  created() {
    this.$nuxt.$on('image-index', (index) => {
      this.imageIndex = index;
    })
  },
  computed: {
    title() {
      if (this.product.title_translate) {
        return this.$t(this.product.title_translate);
      }
      return this.product.title;
    },
    description() {
      if (this.product.description_locale) {
        return this.$t(this.product.description_locale);
      }
      return this.product.description;
    },
    currentCategory() {
      const category = this.$store.getters['categories/getCategory'](this.product.category);
      if (!category) {
        return '';
      }
      if (category.title_translate) {
        return this.$t(category.title_translate);
      }
      return category.title;
    },
    getStatus() {
      if (this.preorder) {
        return 'ProductStatusPreorder';
      }
      if (this.notAvailable) {
        return 'AvailabilityNo';
      }
      return 'ProductStatusBasket';
    },
    getPreorder() {
      return this.product.availability[this.productSizeIndex].preorder;
    }
  },
  methods: {
    buttonStatus() {
      if (this.product.availability[this.productSizeIndex].quantity === 0) {
        this.notAvailable = true;
        let buttonToCart = this.$el.querySelector('.btn');
        buttonToCart.style.color = 'black';
        buttonToCart.style.backgroundColor = 'white';
        buttonToCart.style.border = '1px solid black';
      }
    },
    loadAvailability() {
      if (!this.product.availability || (this.product.availability.length === 1 &&
        this.product.availability[0].size === "ONE SIZE")) {
        this.hideSizeBlock = true;
        this.preorder = this.product.availability[0].preorder;
        this.buttonStatus();
      } else {
        this.preorder = this.getPreorder;
      }

    },
    loadImageForSliders() {
      if (this.product.image_list) {
        this.product.image_list.forEach(item => {
          this.slides.push({
            "image": item,
          });
        });
      }
    },
    toCart() {
      const availability = this.product.availability;
      const {id, title, new_price, price, image_list} = this.product;
      const productToCart = {
        id,
        'title': this.getPreorder ? title + ' (предзаказ!)' : title,
        'price': new_price ? new_price : price,
        'quantity': 1,
        'preorder': this.getPreorder,
        'size': availability[this.productSizeIndex].size,
        'image': image_list[this.imageIndex]
      };
      productToCart.total = productToCart.price;
      this.$store.commit("cart/setCartProducts", productToCart);
      if (!this.notAvailable) {
        this.$router.push("/cart");
      }
    },
    selectSize(index) {
      this.productSizeIndex = index;
    }
  },
  mounted() {
    this.loadImageForSliders();
    this.loadAvailability();
  }
}
</script>

<style scoped>
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
  color: #777676;
  font-weight: 600;
  letter-spacing: 0.04em;
}

.preorder {
  color: #9f0b05;
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
  color: #777676;
}

.product-category div {
  font-size: 1rem;
  margin-left: 1%;
}

.product-title {
  border-bottom: 2px solid #777676;
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
  color: #777676;
}

.selected {
  background-color: #c7d9d8;
}

.notActive {
  background-color: #777676;
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

@media screen and (max-width: 460px) {
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
</style>
