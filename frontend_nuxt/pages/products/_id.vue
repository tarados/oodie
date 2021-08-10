<template>
  <div class="product">
    <h1>{{ product.title }}</h1>
    <div class="product-content">
      <img :src="product.image_list[0]">
      <div class="product-content_price">Price {{ product.price }}</div>
      <div class="product-content_size">New price {{ product.new_price }}</div>
    </div>
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
    const data = await $axios.$get('https://hoodiyalko.avallon.im/app/products/product/' + params.id);
    const product = data.product;
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
  padding-bottom: 4rem;
}

.product-content {
  display: grid;
  grid-template-columns: 2fr 1fr;
  grid-template-rows: repeat(2, auto);
  grid-template-areas:
    "sidebar price"
    "sidebar new-price"
}

.product-content img {
  grid-area: sidebar;
  width: 100%;
}

.product-content .product-content_title {
  grid-area: header;
}

.product-content .product-content_price {
  grid-area: price;
  align-self: center;
  justify-self: center;
}

.product-content .product-content_size {
  grid-area: new-price;
  align-self: center;
  justify-self: center;
}
</style>
