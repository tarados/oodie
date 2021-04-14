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
      >
        <img :src="slider.image">
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
  text-align: center;
  margin-bottom: 1rem;
  background-color: yellow;
  height: calc(10vw + 170 * (100vw / 1838));
}

.slider-inner {
  transition: all 1s linear 0s;
}

.slider-inner .slider_item {
  /*position: relative;*/
  display: inline-block;
  vertical-align: middle;
  border: 5px solid white;
}

img {
  object-fit: cover;
  width: calc(10vw + 170 * (100vw / 1838));
  height: calc(10vw + 170 * (100vw / 1838));
}

.slider-inner .slider_item .slider_item__background {
  position: absolute;
  top: 0;
  left: 0;
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

@media screen and (max-width: 1329px) {
  .slider-wrapper {
    height: calc(10vw + 202 * ((100vw - 638px) / 1838));
  }

  img {
    width: calc(10vw + 202 * ((100vw - 638px) / 1838));
    height: calc(10vw + 202 * ((100vw - 638px) / 1838));

  }
}

@media screen and (max-width: 1200px) {
  .slider-wrapper {
    height: calc(19vw + 200 * ((100vw - 638px) / 1838));
  }

  img {
    width: calc(19vw + 200 * ((100vw - 638px) / 1838));
    height: calc(19vw + 200 * ((100vw - 638px) / 1838));

  }
}

@media screen and (max-width: 1000px) {
  .slider-wrapper {
    height: calc(21vw + 200 * (100vw / 1838));
  }

  img {
    width: calc(21vw + 200 * (100vw / 1838));
    height: calc(21vw + 200 * (100vw / 1838));

  }
}

@media screen and (max-width: 690px) {
  .slider-wrapper {
    height: calc(20vw + 215 * (100vw / 1838));
  }

  img {
    width: calc(20vw + 215 * (100vw / 1838));
    height: calc(20vw + 215 * (100vw / 1838));

  }
}

@media screen and (max-width: 610px) {
  .slider-wrapper {
    height: calc(33vw + 270 * (100vw / 1838));
  }

  img {
    width: calc(33vw + 270 * (100vw / 1838));
    height: calc(33vw + 270 * (100vw / 1838));

  }
}

@media screen and (max-width: 450px){
  .slider-wrapper {
    height: calc(32vw + 270 * (100vw / 1838));
  }

  img {
    width: calc(32vw + 270 * (100vw / 1838));
    height: calc(32vw + 270 * (100vw / 1838));
  }
}

@media screen and (max-width: 375px) {
  .slider-wrapper {
    height: calc(32vw + 244 * (100vw / 1838));
  }

  img {
    width: calc(32vw + 244 * (100vw / 1838));
    height: calc(32vw + 244 * (100vw / 1838));

  }
}

@media screen and (max-width: 320px) {
  .slider-wrapper {
    height: calc(33vw + 244 * (100vw / 1838));
  }

  img {
    width: calc(33vw + 244 * (100vw / 1838));
    height: calc(33vw + 244 * (100vw / 1838));

  }
}
</style>
