<template>
  <div class="wrapper-brands">
    <BrandsList/>
  </div>
</template>

<script>

export default {
  name: "index",
  middleware: ['products']
}
</script>

<style scoped>
.wrapper-brands {
  max-width: 1380px;
  margin: 0 auto;
  padding-top: 40px;
  padding-bottom: 40px;
}

.brands-info {
  font-size: calc(1vw + 2 * (100vw / 1338));
  font-family: 'Roboto', sans-serif;
  margin: 2% 5%;
  padding: 6px;
}

@media screen and (max-width: 750px) {
  .brands-info {
    font-size: calc(1vw + 10 * (100vw / 750));
    font-family: 'Roboto', sans-serif;
  }
}
</style>
