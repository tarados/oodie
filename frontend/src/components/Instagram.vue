<template>
  <div class="instagram-wrapper">
    <div class="slider-title">Мы в Instagram</div>
    <Slider :slides="slides"/>
  </div>
</template>

<script>
import Slider from "../components/Slider";
import axios from "axios";

export default {
  name: "Instagram",

  data() {
    return {
      slides: []
    }
  },
  components: {
    Slider
  },
  computed: {},
  methods: {
    async getInstagramImages() {
      const response = await axios.get(process.env.VUE_APP_INSTA);
      console.log(response.data[0]);
      response.data.forEach(item => {
        this.slides.push(item);
      });
    },
  },
  mounted() {
    this.getInstagramImages();
  }
};
</script>

<style>
.instagram-wrapper .slider-title {
  font-size: 24px;
  font-weight: 600;
  text-align: center;
  line-height: 32px;
  padding: 24px 10px;
}


</style>
