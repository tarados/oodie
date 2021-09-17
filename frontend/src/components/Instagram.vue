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
// import axios from "axios";

export default {
  name: "Instagram",

  data() {
    return {
      slides: [
        {
          "image": "http://localhost:8000/media/images/insta/image0.jpeg",
          "comment": "❤️ @maryna_fit",
          "shortcode": "CMBtnoJniU1"
        },
        {
          "image": "http://localhost:8000/media/images/insta/image1.jpeg",
          "comment": "Худиялко это самая мягкая, тёплая и уютная одежда, которая у вас когда-либо была☁️",
          "shortcode": "CL69EZzH2CW"
        },
        {
          "image": "http://localhost:8000/media/images/insta/image2.jpeg",
          "comment": "St. Valentine's Day mood ❤️",
          "shortcode": "CLMph2Kn-37"
        },
        {
          "image": "http://localhost:8000/media/images/insta/image3.jpeg",
          "comment": "Keep calm and wear #худиялко ❄️",
          "shortcode": "CLHKMlTHAap"
        },
        {
          "image": "http://localhost:8000/media/images/insta/image4.jpeg",
          "comment": "Let’s get cozy☁️",
          "shortcode": "CLCQP8LH-aF"
        },
        {
          "image": "http://localhost:8000/media/images/insta/image5.jpeg",
          "comment": "#худиялко",
          "shortcode": "CKvw7HdniMS"
        },
        {
          "image": "http://localhost:8000/media/images/insta/image6.jpeg",
          "comment": "Когда за окном -16 настроение спасает ароматное какао, хороший фильм и теплое худиялко☁️",
          "shortcode": "CKJRUmfnztb"
        },
        {
          "image": "http://localhost:8000/media/images/insta/image7.jpeg",
          "comment": "Чтобы праздники были ещё уютнее☁️ #худиялко \nСегодня отправляем посылки Новой почтой по Киеву и отдаём заказы возле Контрактовой площади до 21.00🙌🏻",
          "shortcode": "CJaph_THRx5"
        },
        {
          "image": "http://localhost:8000/media/images/insta/image8.jpeg",
          "comment": "•Все посылки отправляем в день заказа\n•Работаем ежедневно с 10.00 до 20.00 \n•31-го декабря работаем до 16.00, возможен самовывоз возле Контрактовой площади \n•1 января выходной, со 2-го января работаем в обычном режиме",
          "shortcode": "CJTAwIQHkYQ"
        },
        {
          "image": "http://localhost:8000/media/images/insta/image9.jpeg",
          "comment": "A warm hug is inside this bag 🎁",
          "shortcode": "CJQYL1Jnx8F"
        },
        {
          "image": "http://localhost:8000/media/images/insta/image10.jpeg",
          "comment": "В худиялке утро будет комфортным даже в самые морозные дни☁️",
          "shortcode": "CJQYABXnPdr"
        },
        {
          "image": "http://localhost:8000/media/images/insta/image11.jpeg",
          "comment": "Что такое худиялко?\r\nЭто двухслойное домашнее оверсайз худи. Сверхмягкий ворсистый внешний слой в сочетании с легким воздушным внутренним слоем расслабляет и дает ощущение как будто вы в облачке.\n\r\nИдеально подходит:\r\n-Холодным утром, когда так сложно выбраться из под одеяла\r\n-Для просмотра фильмов зимними вечерами\r\n-Во время пикников в прохладное время года\r\n-Для расслабления и отдыха\n-В качестве подарка \nОдин размер, который подходит всем от XXS до 6XL.\n\nЗаказ можно оформить на сайте hoodiyalko.com.ua (активная ссылка в шапке профиля) или написав в директ💌\n\nУспей заказать по акционной цене 1499 грн вместо 2̶1̶0̶0̶ 🔥",
          "shortcode": "CJQQQixnTET"
        }
      ],
    }
  },
  components: {
    Slider
  },
  computed: {},
  methods: {
  //   async getInstagramImages() {
  //     const response = await axios.get(process.env.VUE_APP_INSTA);
  //     console.log(process.env.VUE_APP_INSTA);
  //     this.slides = response.data;
  //   }
  // },
  // mounted() {
  //   console.log(process.env.VUE_APP_INSTA);
  //   this.getInstagramImages();
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
