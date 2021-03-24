<template>
  <div class="wrapper">
    <img src="/images/sewer_cat.gif"/>
  </div>
</template>

<script>
export default {
  name: "About",
  mounted() {
    console.log(this.$router.currentRoute.name);
  }
}
</script>

<style scoped>
.wrapper {
  text-align: center;
  padding-bottom: 40px;
}

img {
  width: 100%;
  max-width: 500px;
}
</style>
