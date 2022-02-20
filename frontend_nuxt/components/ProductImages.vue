<template>
  <client-only>
    <div class="wrapper-slider">
      <vueper-slides
        class="slider1"
        ref="vueperslides1"
        :slide-ratio="841 / 561"
        :bullets="false">
        <vueper-slide
          v-for="(slide, index) in slides"
          :key="index"
          :image="slide.image"
        />
      </vueper-slides>
      <div class="item-left-slider">
        <div class="slider" v-for="(image, index) in slides" :key="index">
          <img alt="" :src="image.image" @click="selectedImage(index)">
        </div>
      </div>
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
  },
  methods: {
    selectedImage(index) {
      this.$nuxt.$emit('image-index', index);
      this.$refs['vueperslides1'].goToSlide(index);

    }
  }
}
</script>

<style scoped>

.slider1 {
  margin-bottom: 15px;
}

.item-left-slider {
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

.slider img {
  width: 100%;
  overflow: hidden;
}

.slider img:hover {
  border: 1px solid black;
}

@media screen and (max-width: 960px) {
  .vueperslides--fixed-height {
    height: calc(100vh - 278px);
  }

}

@media screen and (max-width: 750px) {
  .vueperslides--fixed-height {
    height: calc(100vh - 318px);
  }
}

@media screen and (max-width: 650px) {
  .vueperslides--fixed-height {
    height: calc(100vh - 372px);
  }
}

@media screen and (max-width: 560px) {
  .vueperslides--fixed-height {
    height: calc(100vh - 424px);
  }

  .slider {
    width: 78px;
    height: 78px;
  }
}


@media screen and (max-width: 460px) {
  .vueperslides--fixed-height {
    height: calc(100vh - 250px);
  }
}

@media screen and (max-width: 375px) {
  .vueperslides--fixed-height {
    height: calc(100vh - 324px);
  }
}

@media screen and (max-width: 320px) {
  .vueperslides--fixed-height {
    height: calc(100vh - 370px);
  }
}


</style>
