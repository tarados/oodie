<template>
  <div class="wrapper">
    <img src="/images/sewer_cat.gif"/>
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
.wrapper {
  text-align: center;
  padding-bottom: 40px;
}
</style>
