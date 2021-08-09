<template>
  <div class="error">
    <h1>Error 404</h1>

    <nuxt-link to="/">Home</nuxt-link>
  </div>
</template>

<script>
export default {
  name: "error"
}
</script>

<style scoped>
.error {
  width: 600px;
  margin: 0 auto;
  text-align: center;
  padding-top: 4rem;
}
h1 {
  color: red;
}
</style>
