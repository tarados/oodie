<template>
  <div class="wrapper">
    <div class="row">
      <router-link :to="{name: 'Product', params: {id: product.id} }"
                   v-for="(product, index) in prodList" :key="index"
                   :class="{product: large, brand: small}"
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
import {mapGetters} from 'vuex'

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
      small: null
    }
  },
  computed: {
    ...mapGetters(["allProducts", "allCategories"]),
    prodList() {
      if (this.categoryId) {
        return this.allProducts.filter(product => product.category === this.categoryId);
      } else {
        return this.allProducts;
      }
    }
  },
  methods: {
    loadSize() {
      if (this.size === 'small') {
        this.small = true;
        this.large =false;
        } else {
        this.small = false;
        this.large = true;
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
  width: calc((100% / 12) * 6 - 20px);
  height: 100%;
  margin: 0 10px 0 10px;
  text-align: center;
  padding-bottom: 1rem;
  text-decoration: none;
  color: #3d4246;
}

.brand {
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

/*media queries*/
@media screen and (max-width: 1240px) {
  .product {
    width: calc((100% / 12) * 4 - 20px);
  }
}

@media screen and (max-width: 860px) {
}

@media screen and (max-width: 620px) {
  .product {
    width: calc((100% / 12) * 6 - 20px);
  }
}

@media screen and (max-width: 450px) {
  .product {
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
