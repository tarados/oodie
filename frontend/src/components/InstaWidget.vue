<template>
  <div class="slider-wrapper">
    <div class="slider" :style="{'margin-left': '-' + 100.17 * currentSlideIndex + '%'}">
      <div class="slider_item"
           v-for="(slider, index) in allProducts"
           :key="index"
      >
        <img :src="slider.image" width="340px">
      </div>
    </div>
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
}

.slider {
  display: flex;
  flex-wrap: nowrap;
  justify-content: space-between;
  overflow: hidden;

}

.slider .slider_item {
  width: 340px;
  height: 340px;
  margin-right: 10px;
}

.slider .slider_item img {
  display: block;
  transform: scale(1);
  height: auto;
  object-fit: cover;
}

.offset {
  margin-left: -100%;
}

</style>
