<template>
  <div class="wrapper-products">
    <div class="products">
      <div class="product" v-for="product of products" :key="product.id">
        <a href="#" @click.prevent="openProduct(product)">
          <img :src="product.image">
        </a>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "index",
  async fetch({store}) {
    if (store.getters['products/products'].length === 0) {
      await store.dispatch('products/fetch')
    }
  },
  data: () => ({
    // products:[]
  }),
  computed: {
    products() {
      return this.$store.getters['products/products']
    }
  },
  methods: {
    openProduct(product) {
      this.$router.push('/products/' + product.id);
    }
  }
}
</script>

<style scoped>
.wrapper-products {
  max-width: 1240px;
  margin: 40px auto 40px;
}
.products {
  display: grid;
  grid-template-columns: repeat(2, 600px);
  grid-auto-rows: 600px;
  grid-gap: 20px;
}
.product {
  overflow: hidden;
}
.product img {
  width: 100%;
}
</style>
