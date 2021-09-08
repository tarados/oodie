<template>
  <div class="instagram-wrapper">
    <div class="slider-title">Мы в Instagram</div>
    <section v-if="slides">
      <Slider :slides="slides"/>
    </section>
  </div>
</template>

<script>

export default {
  name: "Instagram"
};
</script>

<style>
.instagram-wrapper .slider-title {
  font-size: 24px;
  font-weight: 600;
  text-align: center;
  line-height: 32px;
  padding: 24px 10px;
}


</style>
