<template>
  <div class="wrapper-products">
    <div class="products">
      <div class="product" v-for="product of products" :key="product.id">
        <a href="#" @click.prevent="openProduct(product)">{{product.title}}</a>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "index",
  async asyncData({$axios}) {
    const data = await $axios.$get('https://hoodiyalko.avallon.im/app/products');
    const products = data.products;
    return {products}
  },
  data: () => ({
    products:[]
  }),
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
  height: 100%;
  width: 100%;
  background-color: yellowgreen;
}
</style>
