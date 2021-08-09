<template>
  <div class="product">
    <h1>{{ product.title }}</h1>
  </div>
</template>

<script>
export default {
  name: "_id",
  data: () => ({
    product: {}
  }),
  validate({params}) {
    return /^\d+$/.test(params.id)
  },
  async asyncData({$axios, params}) {
    const data = await $axios.$get('https://hoodiyalko.avallon.im/app/products');
    let product = {}
    data.products.forEach(item => {
      if (item.id == params.id) {
        product = item;
        // return product
      }

    });
    return {product}
  },
}
</script>

<style scoped>
.product {
  width: 600px;
  margin: 0 auto;
  text-align: center;
  padding-top: 4rem;
}
</style>
