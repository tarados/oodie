<template>
  <div class="slider-wrapper">
    <div
        class="slider-inner"
        ref="inner"
    >
      <div
          class="slider_item"
          ref="item"
          v-for="(slider, index) in slides" :key="index"
          :style="`background-image: url(${slider.image})`"
      >
        <div class="slider_item__background">
          <span>{{ slider.comment }}</span>
        </div>
      </div>

    </div>
    <div class="prev"
         @click="prevSlide">
      <svg viewBox="4 0 8 16" class="eapps-instagram-feed-posts-slider-nav-icon">
        <path d="M4.3,8.7l6,5.9c0.4,0.4,1.1,0.4,1.5,0c0.4-0.4,0.4-1.1,0-1.5L6.5,8l5.2-5.2c0.4-0.4,0.4-1.1,0-1.5
        c-0.4-0.4-1.1-0.4-1.5,0l-6,6C3.9,7.7,3.9,8.3,4.3,8.7z"></path>
      </svg>
      <div class="radius-prev"></div>
    </div>
    <div class="next" @click="nextSlide">
      <svg viewBox="4 0 8 16" class="eapps-instagram-feed-posts-slider-nav-icon">
        <path d="M11.7,7.3l-6-5.9c-0.4-0.4-1.1-0.4-1.5,0c-0.4,0.4-0.4,1.1,0,1.5L9.5,8l-5.2,5.2
        c-0.4,0.4-0.4,1.1,0,1.5c0.4,0.4,1.1,0.4,1.5,0l6-6C12.1,8.3,12.1,7.7,11.7,7.3z"></path>
      </svg>
      <div class="radius-next"></div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Slider",
  props: {
    slides: {
      type: Array
    }
  },
  data() {
    return {
      currentSlideIndex: 0
    }
  },
  computed: {
    bias() {
      const x = '-' + 100 * this.currentSlideIndex + '%';
      return x;
    },
    sectionCount() {
      let screenWidth = window.screen.width;
      if (screenWidth > 760) {
        return 5
      } else if (screenWidth > 450) {
        return 4
      } else {
        return 2
      }
    }
  },
  methods: {
    prevSlide() {
      for (let i = 0; i < this.sectionCount; i++) {
        let last = this.slides.pop();
        this.slides.unshift(last);
      }
    },
    nextSlide() {
      for (let i = 0; i < this.sectionCount; i++) {
        let first = this.slides.shift();
        this.slides.push(first);
      }
    }
  },
  mounted() {
    this.sectionCount;
  }
}
;
</script>

<style scoped>
.slider-wrapper {
  position: relative;
  overflow: hidden;
  height: calc(9vw + 197 * (100vw / 1838));
  margin-bottom: 1rem;
  background-color: yellow;
}

.slider-inner {

}

.slider-inner .slider_item {
  position: relative;
  width: calc(9vw + 200 * (100vw / 1838));
  height: calc(9vw + 200 * (100vw / 1838));
  display: inline-block;
  vertical-align: middle;
  border: 5px solid white;
  background-repeat: no-repeat;
  background-size: cover;
}

.slider-inner .slider_item .slider_item__background {
  display: flex;
  justify-content: center;
  align-items: center;
  opacity: 0;
  transition: all 1s ease 0s;
  width: 100%;
  height: 100%;
  color: white;
  padding: 2rem;
  background-color: black;
}

.slider-inner .slider_item .slider_item__background:hover {
  opacity: 0.8;
}

span {
  padding: 2rem;
}

.next {
  position: absolute;
  top: 40%;
  right: 0;
}

.next svg {
  position: absolute;
  width: 12px;
  height: 15px;
  top: 23px;
  left: 12px;
  fill: rgb(255, 255, 255);
}

.radius-next {
  width: 30px; /* ширина в два раза меньше высоты, иначе получится полуовал */
  height: 60px;
  border-radius: 100% 0 0 100% / 50% 0 0 50%;
  background: #000000;
  cursor: pointer;
}

.prev {
  position: absolute;
  top: 40%;
  left: 0;
}

.prev svg {
  position: absolute;
  width: 12px;
  height: 15px;
  top: 23px;
  right: 12px;
  fill: rgb(255, 255, 255);
}

.radius-prev {
  width: 30px; /* ширина в два раза меньше высоты, иначе получится полуовал */
  height: 60px;
  border-radius: 0 100% 100% 0 / 0 50% 50% 0;
  background: #000000;
  cursor: pointer;
}

@media screen and (max-width: 760px) {
  .slider-wrapper {
    height: calc(9vw + (300 + 300 * 0.7) * ((100vw - 320px) / 1838));
  }

  .slider-inner .slider_item {
    height: calc(9vw + (300 + 300 * 0.7) * ((100vw - 320px) / 1838));

  }
}

@media screen and (max-width: 450px) {
  /*.slider-inner .slider_item :nth-child(2n) {*/
  /*  border: 2px solid white;*/
  /*}*/

  .slider-inner .slider_item {
    height: 50vw;
  }
}
</style>
