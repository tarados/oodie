<template>
  <div class="product">
    <img :src="product.image_list[0]">
    <h1>{{ product.title }} {{ $t('MenuHome') }}</h1>
    <h2>price ${{ product.price }} </h2>
    <h3>new_price ${{ product.new_price }}</h3>
  </div>
</template>

<script>
export default {
  name: "_id",
  validate({params}) {
    return /^\d+$/.test(params.id)
  },
  async asyncData({$axios, params}) {
    const data = await $axios.$get('https://hoodiyalko.avallon.im/app/products/product/' + params.id);
    const product = data.product;
    return {product}
  }
}
</script>

<style scoped>
.product {
  width: 600px;
  display: grid;
  grid-template-columns: repeat(2, 300px);
  grid-template-rows: repeat(3, auto);
  gap: 20px;
  grid-template-areas: "content header"
                       "content price"
                       "content new_price";
  margin: 1rem auto;
  padding-top: 4rem;
}

.product img {
  width: 100%;
  grid-area: content;
}

h1 {
  grid-area: header;
}

h2 {
  grid-area: price;
}

h3 {
  grid-area: new_price;
}
</style>
