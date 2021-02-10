<template>
  <div class="slider-wrapper">
    <div class="slider">
      <div class="slider_item" v-for="(slider, index) in allProducts" :key="index">
        <img :src="slider.image" alt="">
      </div>
    </div>
  </div>
</template>

<script>
import {mapGetters} from 'vuex'

export default {
  name: "Slider",
  data() {
    return {
    }
  },
  computed: {
    ...mapGetters(["allProducts"])
  },
  methods: {
    // setHover() {
    //   const sliderItems = [...document.querySelectorAll('.vueperslide--visible')];
    //   const toggleActivity = function (index) {
    //     for (let i = 0; i < sliderItems.length; i++) {
    //       if (i === Number(index)) {
    //         sliderItems[i].classList.add('hover-slider');
    //       } else {
    //         sliderItems[i].classList.remove('hover-slider');
    //       }
    //     }
    //   };
    //   document.querySelector('.vueperslides__track').addEventListener('mouseover', (event) => {
    //     if (event.target.classList.contains('vueperslide--visible')) {
    //       toggleActivity(event.target.dataset.index);
    //     }
    //   });
    // }
  },
  mounted() {
  }
};
</script>

<style>
.slider-wrapper {
  margin: 20px auto;
  width: 90%;
  height: 370px;
}

.slider {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-between;
  overflow: hidden;
}

.slider .slider_item {
  flex-grow: 1;
}

.slider .slider_item img {
  width: 360px;
  height: 100%;
}

</style>
