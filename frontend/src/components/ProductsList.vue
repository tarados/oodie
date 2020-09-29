<template>
  <div class="wrapper">
    <div class="row" :class="size">
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
    this.$store.dispatch('loadProducts');
  }
}
</script>

<style scoped>
.wrapper {
  margin: 40px auto 60px;
}

h4 {
  margin: 2%;
  text-align: center;
}

.row {
  margin: 0 0 10% 0;
  display: grid;
  grid-template: 600px / repeat(2, 600px);
  grid-auto-rows: 600px;
  grid-row-gap: 4em;
  grid-column-gap: 1.2em;
  grid-auto-flow: row;
  justify-content: center;
}

.row.small {
  margin: 0 0 2% 0;
  display: grid;
  grid-template: 400px / repeat(3, 400px);
  grid-auto-rows: 400px;
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

  .row.small {
    grid-template: 400px / repeat(2, 400px);
  }
}

@media screen and (max-width: 860px) {
  .row.small {
    grid-template: 400px / 400px;
  }
}

@media screen and (max-width: 620px) {
  .row {
    grid-template: 450px / 450px;
    grid-auto-rows: 450px;
    margin: 0 0 15% 0;
  }
}

@media screen and (max-width: 450px) {
  .row {
    grid-template: 380px / 380px;
    grid-auto-rows: 380px;
    margin: 0 0 15% 0;
  }

  .row.small {
    grid-template: 360px / 360px;
    grid-auto-rows: 360px;
  }
}

@media screen and (max-width: 375px) {
  .row {
    grid-template: 360px / 360px;
    grid-auto-rows: 360px;
  }

  .row.small {
    grid-template: 320px / 320px;
    grid-auto-rows: 320px;
  }
}

@media screen and (max-width: 360px) {
  .row {
    grid-template: 320px / 320px;
    grid-auto-rows: 320px;
  }
}

@media screen and (max-width: 320px) {
  .row {
    grid-template: 280px / 280px;
    grid-auto-rows: 280px;
  }

  .row.small {
    grid-template: 260px / 260px;
    grid-auto-rows: 260px;
  }
}

@media screen and (max-width: 280px) {
  .row {
    grid-template: 240px / 240px;
    grid-auto-rows: 240px;
  }

  .row.small {
    grid-template: 220px / 220px;
    grid-auto-rows: 220px;
  }
}


</style>
