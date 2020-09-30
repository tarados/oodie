<template>
  <div class="wrapper">
    <div class="row" :class="size">
      <router-link :to="{name: 'Product', params: {id: product.id} }"
                   v-for="(product, index) in prodList" :key="index"
                   class="product"
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

  },
  mounted() {
    // this.$store.dispatch('loadProducts');
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

.product img {
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

span.old {
  /*color: red;*/
}

.no-current {
  text-decoration: line-through;
}

.category-title {
  width: 80%;
  height: 3.5vmax;
  display: block;
  text-align: center;
  position: relative;
  margin-top: -15%;
  margin-left: 10%;
  background-color: #c7d9d8;
  color: white;
}

.category-title span {
  font-size: 3rem;
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
