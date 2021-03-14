<template>
  <div class="slider-wrapper">
    <div class="slider-title">Мы в Instagram</div>
    <div class="slider" :style="{'margin-left': '-' + 100 * currentSlideIndex + '%'}">
      <a :href="`https://www.instagram.com/p/${slider.shortcode}`"
         target="_blank"
         class="slider_item"
         v-for="(slider, index) in slides"
         :key="index"
         :style="`background-image: url(${slider.image})`"
      >
        <div class="slider_item__background">
          <span>{{ slider.comment }}</span>
        </div>
      </a>
    </div>
    <div class="prev" v-if="currentSlideIndex >= 1"
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
      currentSlideIndex: 0,
    }
  },
  computed: {
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
      if (this.currentSlideIndex > 0) {
        this.currentSlideIndex--;
      }
    },
    nextSlide() {
      let slideCount = this.slides.length / this.sectionCount -1;
      if (this.currentSlideIndex >= slideCount) {
        this.currentSlideIndex = 0;
      } else {
        this.currentSlideIndex++;
      }
    }
  },
  mounted() {
    this.sectionCount;
  }
};
</script>

<style>
.slider-wrapper {
  position: relative;
  margin: 30px auto;
  overflow: hidden;

}

.slider-title {
  font-size: 24px;
  font-weight: 600;
  text-align: center;
  line-height: 32px;
  padding: 24px 10px;
}

.slider {
  width: 100%;
  height: 100%;
  display: flex;
}

.slider .slider_item {
  height: calc(9vw + 197 * (100vw / 1838));
  position: relative;
  flex: 1 0 20%;
  background-repeat: no-repeat;
  background-size: cover;
}

.slider .slider_item .slider_item__background {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  opacity: 0;
  background-color: #000000;
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
}

.slider .slider_item .slider_item__background:hover {
  opacity: 0.8;
}

.slider .slider_item:nth-child(2n) {
  border: 12px solid white;
}

.slider .slider_item:nth-child(2n):hover {
  border: 0;
}

.slider-wrapper .next {
  position: absolute;
  top: 50%;
  right: 0;
}

.slider-wrapper .next svg {
  position: absolute;
  width: 12px;
  height: 15px;
  top: 23px;
  left: 12px;
  fill: rgb(255, 255, 255);
}

.slider-wrapper .radius-next {
  width: 30px; /* ширина в два раза меньше высоты, иначе получится полуовал */
  height: 60px;
  border-radius: 100% 0 0 100% / 50% 0 0 50%;
  background: #000000;
  cursor: pointer;
}

.slider-wrapper .prev {
  position: absolute;
  top: 50%;
  left: 0;
}

.slider-wrapper .prev svg {
  position: absolute;
  width: 12px;
  height: 15px;
  top: 23px;
  right: 12px;
  fill: rgb(255, 255, 255);
}

.slider-wrapper .radius-prev {
  width: 30px; /* ширина в два раза меньше высоты, иначе получится полуовал */
  height: 60px;
  border-radius: 0 100% 100% 0 / 0 50% 50% 0;
  background: #000000;
  cursor: pointer;
}

@media screen and (max-width: 767px) {
  .slider {
    /*scroll-snap-type: x mandatory;*/
    /*overflow-x: auto;*/
  }

  .slider .slider_item {
    height: calc(9vw + (300 + 300 * 0.7) * ((100vw - 320px) / 1838));
    flex-basis: 25%;
    /*scroll-snap-align: start;*/
  }
}

@media screen and (max-width: 450px) {
  .slider .slider_item:nth-child(2n) {
    border: 2px solid white;
  }

  /*.slider .slider_item:nth-child(2n+1) {*/
  /*  border: 2px solid white;*/
  /*}*/

  .slider .slider_item {
    flex-basis: 50%;
    height: 50vw;
  }
}
</style>
