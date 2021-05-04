<template>
  <div class="slider" ref="slider">
    <div class="slider-list"
         ref="slider_list"
         v-on:mousedown="mousedown"
         v-on:mouseup="mouseup"
         v-on:scroll="mouseup"
    >
      <div class="slider-track" ref="slider_track">
        <div
            class="slider-track_section"
            ref="slider-track_section"
            v-for="(section, index) in sections" :key="index"
            :style="{opacity: index === currentSection ? 1 : 0, transform: index === prevSection ? `translateX(${direction}%)` : ''}"
        >
          <div
              class="slider-item"
              ref="slider_item"
              v-for="(slider, index) in section" :key="index"
              :style="{backgroundImage: `url(${slider.image})`}"
          >
            <!--            <a :href="`https://instagram.com/p/${slider.shortcode}`" target="_blank"></a>-->
            <div
                class="slider-item__background">
              <span>{{ slider.comment }}</span>
            </div>
          </div>
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
      counter: 0,
      currentSection: 0,
      prevSection: -1,
      direction: -1,
      animationTimer: -1,
      posInit: 0,
      posFinal: 0,
      slideIndex: 0
    }
  },
  computed: {
    sectionCount() {
      let screenWidth = window.screen.width;
      if (screenWidth > 768) {
        return 5
      } else if (screenWidth > 450) {
        return 4
      } else {
        return 3
      }
    },
    sections() {
      let chunks = [], i = 0, n = this.slides.length;
      while (i < n) {
        chunks.push(this.slides.slice(i, i += this.sectionCount))
      }
      return chunks
    }
  },
  methods: {
    mousedown(event) {
      let sliderList = this.$refs.slider_list;
      if (event) {
        this.posInit = event.screenX;
        sliderList.style.cursor = 'grabbing';
        console.log(this.posInit);
      }
    },
    mouseup(event) {
      let sliderList = this.$refs.slider_list;
      if (event) {
        if (this.animationTimer) {
          clearTimeout(this.animationTimer);
        }
        this.posFinal = event.screenX;
        sliderList.style.cursor = 'pointer';
        let interval = this.posFinal - this.posInit;
        this.prevSection = this.currentSection;
        if (interval < 0) {
          this.direction = -100;
          if (this.currentSection < this.sections.length - 1) {
            this.currentSection++;
          } else {
            this.currentSection = 0;
          }
        } else if (interval > 0) {
          this.direction = 100;
          let maxLength = this.sections.length - 1;
          if (this.currentSection === 0) {
            this.currentSection = maxLength;
          } else {
            this.currentSection--;
          }
        } else {
          this.direction = 0;
        }
        this.animationTimer = setTimeout(() => {
          this.prevSection = -1;
        }, 1000)
      }
    },
    touchScrolling() {
      // let sliderList = this.$refs.slider_list;
      // console.log(sliderList)
      // sliderList.addEventListener('mousedown', (e) => {
      //   this.posInit = e.clientX;
      //   sliderList.style.cursor = 'grabbing';
      // });
      // sliderList.addEventListener('touchstart', (e) => {
      //   this.posInit = e.targetTouches[0].clientX;
      // });
      // sliderList.addEventListener('mouseup', (e) => {
      //   if (this.animationTimer) {
      //     clearTimeout(this.animationTimer);
      //   }
      //   this.posFinal = e.clientX;
      //   sliderList.style.cursor = 'pointer';
      //   let interval = this.posFinal - this.posInit;
      //   this.prevSection = this.currentSection;
      //   if (interval < 0) {
      //     this.direction = -100;
      //     if (this.currentSection < this.sections.length - 1) {
      //       this.currentSection++;
      //     } else {
      //       this.currentSection = 0;
      //     }
      //   } else if (interval > 0) {
      //     this.direction = 100;
      //     let maxLength = this.sections.length - 1;
      //     if (this.currentSection === 0) {
      //       this.currentSection = maxLength;
      //     } else {
      //       this.currentSection--;
      //     }
      //   } else {
      //     this.direction = 0;
      //   }
      //   this.animationTimer = setTimeout(() => {
      //     this.prevSection = -1;
      //   }, 1000)
      // });
      // sliderList.addEventListener('touchend', (e) => {
      //   if (this.animationTimer) {
      //     clearTimeout(this.animationTimer);
      //   }
      //   this.posFinal = e.changedTouches[0].clientX;
      //   let interval = this.posFinal - this.posInit;
      //   this.prevSection = this.currentSection;
      //   if (interval < 0) {
      //     this.direction = -100;
      //     if (this.currentSection < this.sections.length - 1) {
      //       this.currentSection++;
      //     } else {
      //       this.currentSection = 0;
      //     }
      //   } else if (interval > 0) {
      //     this.direction = 100;
      //     let maxLength = this.sections.length - 1;
      //     if (this.currentSection === 0) {
      //       this.currentSection = maxLength;
      //     } else {
      //       this.currentSection--;
      //     }
      //   } else {
      //     this.direction = 0;
      //   }
      //   this.animationTimer = setTimeout(() => {
      //     this.prevSection = -1;
      //   }, 1000)
      // });
    },
    prevSlide() {
      this.prevSection = this.currentSection;
      this.direction = 100;
      let maxLength = this.sections.length - 1;
      if (this.currentSection === 0) {
        this.currentSection = maxLength;
      } else {
        this.currentSection--;
      }
      this.animationTimer = setTimeout(() => {
        this.prevSection = -1;
      }, 1000);
    },
    nextSlide() {
      this.prevSection = this.currentSection;
      this.direction = -100;
      if (this.currentSection < this.sections.length - 1) {
        this.currentSection++;
      } else {
        this.currentSection = 0;
      }
      this.animationTimer = setTimeout(() => {
        this.prevSection = -1;
      }, 1000);
    }
  },
  mounted() {
    this.touchScrolling();
  }
}
;
</script>

<style scoped>
.slider {
  position: relative;
  user-select: none;
  margin-bottom: 1rem;
  height: calc(10vw + 180 * (100vw / 1838));

}

.slider-list {
  position: relative;
  width: 100%;
  height: calc(10vw + 180 * (100vw / 1838));
  /*pointer-events: all;*/
  cursor: pointer;
  overflow: hidden;
}

/*.slider-list.grab {*/
/*  cursor: grab;*/
/*}*/

/*.slider-list.grabbing {*/
/*  cursor: grabbing;*/
/*}*/

.slider-track {
  display: flex;
}

.slider-track_section {
  transition: all 1s ease 0s;
  position: absolute;
  top: 0;
  left: 0;
  display: flex;
  opacity: 0;
}

.slider-item {
  position: relative;
  width: calc(10vw + 180 * (100vw / 1838));
  height: calc(10vw + 180 * (100vw / 1838));
  flex-shrink: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  background-size: cover;
}

.slider-item a {
  z-index: 10;
  position: absolute;
  left: 0;
  top: 0;
  height: 100%;
  width: 100%;
  display: flex;
  align-items: center;
  justify-items: center;
}

.slider-item .slider-item__background {
  z-index: 0;
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

.slider-item .slider-item__background:hover {
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


@media screen and (max-width: 768px) {
  .slider,
  .slider-list {
    height: calc(10vw + 180 * (100vw / 1200));
  }

  .slider-item {
    width: calc(10vw + 180 * (100vw / 1200));
    height: calc(10vw + 180 * (100vw / 1200));
  }

  .next,
  .prev {
    top: calc(5vw + 20 * (100vw / 770));
  }
}

@media screen and (max-width: 375px) {
  .slider,
  .slider-list {
    height: calc(10vw + 180 * (100vw / 770));
  }

  .slider-item {
    width: calc(10vw + 180 * (100vw / 770));
    height: calc(10vw + 180 * (100vw / 770));
  }

  .next,
  .prev {
    top: calc(5vw + 20 * (100vw / 770));
  }
}

</style>
