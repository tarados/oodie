<template>
  <div class="wrapper">
    <div class="row">
      <router-link :to="{name: 'Product', params: {id: product.id} }"
                   v-for="(product, index) in prodList" :key="index"
                   class="product"
      >
        <div class="image-container"
            :style="{'background': 'url(' + product.image + ') center no-repeat', 'background-size': 'cover'}"></div>
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
    }
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
    this.$store.dispatch('loadProducts');
  }
}
</script>

<style scoped>
.wrapper {
  margin: 2% auto;
}

h4 {
  margin: 2%;
  text-align: center;
}

.row {
  margin: 0 0 5% 0;
  display: grid;
  grid-template: 600px / repeat(2, 600px);
  grid-auto-rows: 600px;
  grid-row-gap: 4em;
  grid-column-gap: 1em;
  grid-auto-flow: row;
  justify-content: center;
}

.image-container {
  width: 100%;
  height: 100%;
}

.product {
  text-align: center;
  padding-bottom: 1rem;
  text-decoration: none;
  color: #3d4246;
}

.product img, .item_sm img {
  width: 100%;
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
  .row {
    grid-template: 600px / 600px;
    grid-auto-rows: 600px;
  }
}

@media screen and (max-width: 960px) {

}

@media screen and (max-width: 750px) {

}

@media screen and (max-width: 420px) {

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