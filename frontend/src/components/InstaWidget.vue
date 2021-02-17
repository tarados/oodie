<template>
  <div class="slider-wrapper">
    <div class="slider" :style="{'margin-left': '-' + 1660 * currentSlideIndex + 'px'}">
      <div class="slider_item"
           v-for="(slider, index) in allProducts"
           :key="index"
      >
        <img :src="slider.image" width="332px">
      </div>
    </div>
    <div class="prev" v-if="currentSlideIndex >= 1"
         @click="prevSlide">
      <svg viewBox="4 0 8 16" width="12" height="16" class="eapps-instagram-feed-posts-slider-nav-icon">
        <path d="M4.3,8.7l6,5.9c0.4,0.4,1.1,0.4,1.5,0c0.4-0.4,0.4-1.1,0-1.5L6.5,8l5.2-5.2c0.4-0.4,0.4-1.1,0-1.5
        c-0.4-0.4-1.1-0.4-1.5,0l-6,6C3.9,7.7,3.9,8.3,4.3,8.7z"></path>
      </svg>
      <div class="radius-prev"></div>
    </div>
    <div class="next" @click="nextSlide">
      <svg viewBox="4 0 8 16" width="12" height="16" class="eapps-instagram-feed-posts-slider-nav-icon">
        <path d="M11.7,7.3l-6-5.9c-0.4-0.4-1.1-0.4-1.5,0c-0.4,0.4-0.4,1.1,0,1.5L9.5,8l-5.2,5.2
        c-0.4,0.4-0.4,1.1,0,1.5c0.4,0.4,1.1,0.4,1.5,0l6-6C12.1,8.3,12.1,7.7,11.7,7.3z"></path>
      </svg>
      <div class="radius-next"></div>
    </div>
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
      let slideCount = Math.ceil(this.allProducts.length / 5);
      if (this.currentSlideIndex >= slideCount) {
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
  overflow: hidden;
  position: relative;
}

.slider {
  display: flex;
  flex-wrap: nowrap;
  overflow: hidden;

}

.slider .slider_item {
  width: 332px;
  height: 331px;
}

.slider .slider_item img:nth-child(2n) {
  border: 15px solid white;
}

.slider .slider_item img {
  display: block;
  transform: scale(1);
  height: auto;
  object-fit: cover;
  border: 1px solid red;
}

.slider-wrapper .next svg {
  z-index: 1;
  position: absolute;
  top: 167px;
  right: 5px;
  fill: rgb(255, 255, 255);
}

.slider-wrapper .radius-next {
  position: absolute;
  top: 145px;
  right: 0;
  width: 30px;  /* ширина в два раза меньше высоты, иначе получится полуовал */
  height: 60px;
  border-radius: 100% 0 0 100% / 50% 0 0 50%;
  background: #000000;
  cursor: pointer;
}

.slider-wrapper .prev svg {
  z-index: 1;
  position: absolute;
  top: 167px;
  left: 5px;
  fill: rgb(255, 255, 255);
}

.slider-wrapper .radius-prev {
  position: absolute;
  top: 145px;
  left: 0;
  width: 30px;  /* ширина в два раза меньше высоты, иначе получится полуовал */
  height: 60px;
  border-radius: 0 100% 100% 0 / 0 50% 50% 0;
  background: #000000;
  cursor: pointer;
}

</style>
