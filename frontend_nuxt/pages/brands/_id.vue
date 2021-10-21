<template>
  <div class="wrapper-brand">
    <ProductsList :ctg="ctgId" size="small"/>
  </div>
</template>

<script>

export default {
  name: "Brand",
  middleware: ['products'],
  computed: {
    ctgId() {
      return Number(this.$route.params.id);
    }
  }
}
</script>

<style scoped>
.wrapper-brand {
  display: flex;
  flex-direction: column;
  align-self: center;
}
</style>
