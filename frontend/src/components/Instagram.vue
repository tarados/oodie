<template>
  <div class="instagram-wrapper">
    <div class="slider-title">Мы в Instagram</div>
    <section v-if="slides">
      <Slider :slides="slides"/>
    </section>
  </div>
</template>

<script>
import Slider from "../components/Slider";
import axios from "axios";

export default {
  name: "Instagram",

  data() {
    return {
      slides: null,
    }
  },
  components: {
    Slider
  },
  computed: {},
  methods: {
    async getInstagramImages() {
      const response = await axios.get(process.env.VUE_APP_INSTA);
      this.slides = response.data.public_list;
    }
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
