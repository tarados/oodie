<template>
  <div class="wrapper">
    <div class="row">
      <router-link :to="{name: 'Product', params: {id: product.id} }"
                   v-for="(product, index) in prodList" :key="index"
                   :class="{ product: large, item_sm: small}"
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
    thumbnail: {
      type: String
    },
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
    setItem() {
      if (this.thumbnail === 'large') {
        this.large = true;
        this.small = false;
      } else if (this.thumbnail === 'small') {
        this.large = false;
        this.small = true;
      }
    }
  },
  mounted() {
    this.$store.dispatch('loadProducts');
    this.setItem();
  }
}
</script>

<style scoped>
.wrapper {
  margin-top: 3rem;
}

h4 {
  margin: 2%;
  text-align: center;
}

.row {
  max-width: 1580px;
  margin: 0 auto;
  display: flex;
  flex-wrap: wrap;
  justify-content: flex-start;
  align-items: center;
  align-content: center;
}

.product {
  text-align: center;
  padding-bottom: 1rem;
  text-decoration: none;
  color: #3d4246;
  width: calc((100% / 12) * 6 - 30px);
  margin: 0 15px;
}

.item_sm {
  padding-bottom: 1rem;
  text-decoration: none;
  color: #3d4246;
  width: calc((100% / 12) * 4 - 30px);
  margin: 0 15px;
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
@media screen and (max-width: 1200px) {

}

@media screen and (max-width: 960px) {
  .item_sm {
    width: calc((100% / 12) * 6 - 30px);
  }
}

@media screen and (max-width: 750px) {
  .product,
  .item_sm {
    width: calc((100% / 12) * 12 - 30px);
  }
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