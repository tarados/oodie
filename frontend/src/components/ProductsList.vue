<template>
  <div class="wrapper">
    <div class="row">
      <div v-for="product in prodList" :key="product.id"
           @click="toProduct(product)"
           :class="{product: large, brand: small}"
      >
        <img
            :src="product.image"
            :class="{black: productAvailability(product) <= 0}"
        >
        <div
            class="preorder-mark"
            :class="{mark_large: large, mark_small: small}"
            v-if="productPreorder(product)"
        >
          {{ 'ProductStatusPreorder' | localize }}
        </div>
        <div
            class="preorder-mark"
            :class="{mark_large: large, mark_small: small}"
            v-if="productAvailability(product) <= 0"
        >
          {{ 'AvailabilityNo' | localize }}
        </div>
        <h4>{{ product.title_translate | localize(product.title) }}</h4>
        <div class="price-box">
          <span v-if="product.new_price" class="no-current">{{ product.price }} грн</span>
          <span v-else>{{ product.price }} грн</span>
          <span class="old" v-show="product.new_price">{{ product.new_price }} грн</span>
        </div>

      </div>
    </div>
  </div>
</template>

<script>
import {mapState} from 'vuex'
// import router from "@/router";

export default {
  name: "Collections",
  props: {
    categoryId: {
      type: Number
    },
    size: String
  },
  data() {
    return {
      category: '',
      large: null,
      small: null,
      black: true
    }
  },
  computed: {
    ...mapState(["productsList"]),
    prodList() {
      if (this.categoryId) {
        return this.productsList.filter(product => product.category === this.categoryId);
      } else {
        return this.productsList;
      }
    }
  },
  methods: {
    loadSize() {
      if (this.size === 'small') {
        this.small = true;
        this.large = false;
      } else {
        this.small = false;
        this.large = true;
      }
    },
    productPreorder(product) {
      return product.availability && product.availability[0] && product.availability[0].preorder;
    },
    productAvailability(product) {
      try {
        return product.availability[0].quantity;
      } catch (TypeError) {
        return 0
      }
    },
    toProduct(product) {
      if (this.productAvailability(product) > 0) {
        this.$router.push({name: 'Product', params: {id: product.id}});
      }
    }
  },
  mounted() {
    this.loadSize();
  }
}
</script>

<style scoped>
.wrapper {
  max-width: 1240px;
  margin: 40px auto 40px;
}

h4 {
  margin: 2%;
  text-align: center;
}

.row {
  display: flex;
  flex-wrap: wrap;
}

.product {
  position: relative;
  width: calc((100% / 12) * 6 - 20px);
  height: 100%;
  margin: 0 10px 0 10px;
  text-align: center;
  padding-bottom: 1rem;
  text-decoration: none;
  color: #3d4246;
}

.brand {
  position: relative;
  width: calc((100% / 12) * 4 - 20px);
  height: 100%;
  margin: 0 10px 0 10px;
  text-align: center;
  padding-bottom: 1rem;
  text-decoration: none;
  color: #3d4246;
}

.product img,
.brand img {
  width: 100%;
  height: 100%;
}

.product img.black {
  -webkit-filter: grayscale(100%);
  -moz-filter: grayscale(100%);
  -o-filter: grayscale(100%);
  filter: grayscale(100%);
}

.price-box {
  width: 100%;
  margin-bottom: 10px;
  display: inline-flex;
  flex-wrap: wrap;
  justify-content: center;
  align-items: center;
}

.price-box span {
  margin: 1%;
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
}

.no-current {
  text-decoration: line-through;
}

.preorder-mark {
  position: absolute;
  background-color: rgba(0, 0, 0, 0.5);
  width: 60%;
  padding-top: 8px;
  padding-bottom: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  text-transform: uppercase;
  text-align: center;
  font-size: 20px;
  font-family: 'Roboto', sans-serif;
  left: 20%;
}

.mark_large {
  top: 74%;
}

.mark_small {
  top: 70%;
}

.availability {
  opacity: 0;
}


/*media queries*/
@media screen and (max-width: 1240px) {
  .product {
    /*width: calc((100% / 12) * 4 - 20px);*/
  }
}

@media screen and (max-width: 1000px) {
  .preorder-mark {
    top: 72%;
  }

  .product {
    /*width: calc((100% / 12) * 4 - 20px);*/
  }
}

@media screen and (max-width: 860px) {
  .brand {
    width: calc((100% / 12) * 6 - 20px);
  }

  .preorder-mark {
    top: 68%;
  }
}

@media screen and (max-width: 660px) {
  .preorder-mark {
    top: 64%;
    padding-top: 4px;
    padding-bottom: 4px;
    font-size: 16px;
  }
}

@media screen and (max-width: 620px) {
  .preorder-mark {
    top: 62%;
    padding-top: 4px;
    padding-bottom: 4px;
    font-size: 16px;
  }

  .product,
  .brand {
    width: calc((100% / 12) * 6 - 20px);
  }
}

@media screen and (max-width: 450px) {
  .preorder-mark {
    top: 70%;
    padding-top: 4px;
    padding-bottom: 4px;
    font-size: 16px;
  }
}

@media screen and (max-width: 450px) {
  .product,
  .brand {
    width: calc((100% / 12) * 12 - 20px);
  }
}

@media screen and (max-width: 375px) {

}

@media screen and (max-width: 360px) {

}

@media screen and (max-width: 320px) {

}

@media screen and (max-width: 280px) {

}


</style>
