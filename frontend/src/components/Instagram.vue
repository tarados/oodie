<template>
  <div class="instagram-wrapper">
    <div class="slider-title">Мы в Instagram</div>
    <section v-if="gallery">
      <Slider :slides="gallery"/>
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
      gallery: [
        {
          'image': 'https://avatars.mds.yandex.net/get-zen_doc/4364496/pub_6065ee3e6b0f875cb5d158f6_6065eea09f06e15305628b68/scale_1200',
          'index': 1
        },
        {
          'image': 'https://avatars.mds.yandex.net/get-zen_doc/4355093/pub_6065ee3e6b0f875cb5d158f6_6065fa6c09a6b717029b855c/scale_1200',
          'index': 2
        },
        {
          'image': 'https://avatars.mds.yandex.net/get-zen_doc/4432928/pub_6065ee3e6b0f875cb5d158f6_6065eea0608d5c2073ec7c9f/scale_1200',
          'index': 3
        },
        {
          'image': 'https://avatars.mds.yandex.net/get-zen_doc/2352854/pub_6065ee3e6b0f875cb5d158f6_6065eea009a6b7170292180e/scale_1200',
          'index': 4
        },
        {
          'image': 'https://avatars.mds.yandex.net/get-zen_doc/4359735/pub_60554ee389855f0fde266f1b_60555eb78099bd488fa39bc3/scale_1200',
          'index': 5
        },
        {
          'image': 'https://avatars.mds.yandex.net/get-zen_doc/4387796/pub_60554ee389855f0fde266f1b_60555f4c7aafb756838dd662/scale_1200',
          'index': 6
        },
        {
          'image': 'https://avatars.mds.yandex.net/get-zen_doc/3530293/pub_60611e0f7e40c468535e98a9_6061246a038b20790cf47fbb/scale_1200',
          'index': 7
        },
        {
          'image': 'https://avatars.mds.yandex.net/get-zen_doc/1640172/pub_6024ff92cd2cb47e6390cb7c_6024ffaf10b7775b5614fbcc/scale_1200',
          'index': 8
        },
        {
          'image': 'https://avatars.mds.yandex.net/get-zen_doc/1781567/pub_6024ff92cd2cb47e6390cb7c_602501c65a38290c15fd9d93/scale_1200',
          'index': 9
        },
        {
          'image': 'https://avatars.mds.yandex.net/get-zen_doc/2380919/pub_604cca73126a3d455ab04c0c_604cca8d126a3d455ab0874c/scale_1200',
          'index': 10
        },
        {
          'image': 'https://avatars.mds.yandex.net/get-zen_doc/3989805/pub_604cca73126a3d455ab04c0c_604cddd5af41a36641549cc5/scale_1200',
          'index': 11
        },
        {
          'image': 'https://avatars.mds.yandex.net/get-zen_doc/3990034/pub_604cca73126a3d455ab04c0c_604cdddf011181447baebc2e/scale_1200',
          'index': 12
        },
      ]
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
