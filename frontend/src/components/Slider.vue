<template>
  <div class="slider" ref="slider">
    <div class="slider-list" ref="slider_list">
      <div class="slider-track" ref="slider_track">
        <div
            class="slider-item"
            ref="slider_item"
            v-for="(slider, index) in slides" :key="index"
            :style="{backgroundImage: `url(${slider.image})`}"
        >
          {{slider.index}}
          <div class="slider-item__background">
            <span>{{ slider.comment }}</span>
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
      counter: 1,
      posInit: 0,
      posX1: 0,
      posX2: 0,
      posY1: 0,
      posY2: 0,
      posFinal: 0,
      isSwipe: false,
      isScroll: false,
      allowSwipe: true,
      transition: true,
      slideIndex: 0,
      slider: this.$refs.slider,
      slideWidth: this.slides[0].offsetWidth,
      trfRegExp: /([-0-9.]+(?=px))/
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
    touchScrolling() {
      let sliderList = this.$refs.slider_list;
      // let  sliderTrack = this.$refs.slider_track;
      let sliderItems = this.$refs.slider_item;
      sliderList.addEventListener('mousedown', (e) => {
        this.posInit = e.clientX;
        sliderList.style.cursor = 'grabbing';
      });
      sliderList.addEventListener('mouseup', (e) => {
        this.posFinal = e.clientX;
        sliderList.style.cursor = 'pointer';
        let interval = this.posFinal - this.posInit;
        if (interval < 0) {
          let widthItem = 0;
          for (let i = 0; i < this.sectionCount; i++) {
            let first = this.slides.shift();
            this.slides.push(first);
            widthItem += sliderItems[i].clientWidth;
          }
          let bias = '-' + widthItem + 'px';
          sliderList.style.transform = `translateX(-${widthItem * this.counter}px)`;
          console.log(bias);
          console.log(sliderList.style.transform);
          this.counter++;
        } else {
          for (let i = 0; i < this.sectionCount; i++) {
            let last = this.slides.pop();
            this.slides.unshift(last);
          }
        }
      });
    },
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
  background-color: yellow;
  height: calc(10vw + 180 * (100vw / 1838));

}

.slider-list {
  width: 100%;
  height: calc(10vw + 180 * (100vw / 1838));
  pointer-events: all;
  cursor: pointer;
  transition: all 2s ease 0s;
}

.slider-list.grab {
  cursor: grab;
}

.slider-list.grabbing {
  cursor: grabbing;
}

.slider-track {
  display: flex;
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
  color: white;
  font-size: 40px;
}

.slider-item .slider-item__background {
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


@media screen and (max-width: 1200px) {

}

@media screen and (max-width: 450px) {

}

@media screen and (max-width: 375px) {

}

@media screen and (max-width: 320px) {

}
</style>
