<template>
  <div class="wrapper">

  </div>
</template>

<script>
export default {
  name: "About",
  methods: {
    basketVisible() {
      if (!this.$store.state.productsStore.basketVisible) {
        this.$store.dispatch('changeVisibleBasket')
      }
    }
  },
  mounted() {
    this.basketVisible();
  }
}
</script>

<style scoped>

</style>
