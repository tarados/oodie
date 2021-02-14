<template>
  <div class="slider-wrapper">
    <div class="slider" :style="{'margin-left': '-' + 100 * currentSlideIndex + '%'}">
      <div class="slider_item"
           v-for="(slider, index) in allProducts"
           :key="index"
      >
        <img :src="slider.image" width="340px">
      </div>
    </div>
    <svg viewBox="4 0 8 16" width="12" height="16" class="eapps-instagram-feed-posts-slider-nav-icon">
      <path d="M11.7,7.3l-6-5.9c-0.4-0.4-1.1-0.4-1.5,0c-0.4,0.4-0.4,1.1,0,1.5L9.5,8l-5.2,5.2
        c-0.4,0.4-0.4,1.1,0,1.5c0.4,0.4,1.1,0.4,1.5,0l6-6C12.1,8.3,12.1,7.7,11.7,7.3z"></path>
    </svg>
    <div class="radius"></div>
    <button @click="prevSlide">Prev</button>
    <button @click="nextSlide">Next</button>
  </div>
</template>

<script>
import {mapGetters} from 'vuex'

export default {
  name: "Slider",
  data() {
    return {
      currentSlideIndex: 0,
      isOffSet: false
    }
  },
  computed: {
    ...mapGetters(["allProducts"])
  },
  methods: {
    prevSlide() {
      if (this.currentSlideIndex > 0) {
        this.currentSlideIndex--;
      }
    },
    nextSlide() {
      if (this.currentSlideIndex >= (this.allProducts.length - 1) / 5) {
        this.currentSlideIndex = 0;
      } else {
        this.currentSlideIndex++;
      }
    }
  },
  mounted() {
  }
};
</script>

<style>
.slider-wrapper {
  margin: 0 auto;
  width: 95%;
  overflow: hidden;
  position: relative;
}

.slider {
  display: flex;
  flex-wrap: nowrap;
  overflow: hidden;

}

.slider .slider_item {
  width: 340px;
  height: 340px;
}

.slider .slider_item:nth-child(odd) {
  margin: 0 9px 0;
}

.slider .slider_item img {
  display: block;
  transform: scale(1);
  height: auto;
  object-fit: cover;
}

.slider-wrapper svg {
  position: absolute;
  top: 45%;
  right: 0;
  fill: rgb(255, 255, 255)
}

.slider-wrapper .radius {
  position: absolute;
  top: 45%;
  right: 0;
  width: 5em;  /* ширина в два раза меньше высоты, иначе получится полуовал */
  height: 10em;
  border: 2px solid red;
  border-radius: 0 100% 100% 0 / 0 50% 50% 0;
  background: mistyrose;
}

</style>
