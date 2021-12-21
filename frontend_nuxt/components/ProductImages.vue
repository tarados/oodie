<template>
  <client-only>
    <div class="wrapper-slider">
      <vueper-slides
        class="slider1"
        ref="vueperslides1"
        @slide="$refs.vueperslides2 && $refs.vueperslides2.goToSlide($event.currentSlide.index, { emit: false })"
        :slide-ratio="841 / 561"
        :bullets="false">
        <vueper-slide
          v-for="(slide, i) in slides"
          :key="i"
          :image="slide.image"
        />
      </vueper-slides>

      <vueper-slides
        ref="vueperslides2"
        :slide-ratio="1 / 3.5"
        :gap="2"
        :dragging-distance="120"
        @slide="$refs.vueperslides1 && $refs.vueperslides1.goToSlide($event.currentSlide.index, { emit: false })"
        :visible-slides="3"
      >
        <vueper-slide
          v-for="(slide, i) in slides"
          :key="i"
          :image="slide.image"
          @click.native="$refs.vueperslides2 && $refs.vueperslides2.goToSlide(i)">
        </vueper-slide>
      </vueper-slides>
    </div>
  </client-only>

</template>

<script>
import {VueperSlides, VueperSlide} from 'vueperslides'
import "vueperslides/dist/vueperslides.css";

export default {
  name: "ProductImages",
  props: {
    slides: {
      type: Array
    }
  },
  components: {
    VueperSlides,
    VueperSlide
  }
}
</script>

<style scoped>

.slider1 {
  margin-bottom: 15px;
}

.slider2 {
  display: flex;
  flex-wrap: wrap;
  margin-top: 0.25rem;
}

.slider {
  width: 120px;
  height: 120px;
  overflow: hidden;
  margin-right: 8px;
  margin-bottom: 12px;
}
</style>
