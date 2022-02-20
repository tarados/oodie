<template>
  <div>
    <div class="slider-title">Мы в Instagram</div>
    <Slider :slides="slides" />
  </div>
</template>

<script>
export default {
  name: "InstagramSlider",
  computed: {
    slides() {
      if (!this.$store.getters['instagram/slides'].length > 0) {
        return [];
      }
      return this.$store.getters['instagram/slides']
    }
  }
}
</script>

<style scoped>
.slider-title {
  font-size: 24px;
  font-weight: 600;
  text-align: center;
  line-height: 32px;
  padding: 24px 10px;
}
</style>
