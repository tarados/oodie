<template>
  <div class="wrapper-brands">
<!--    <div class="brands-info">ТУТ БУДЕТ ТЕКСТ ПРО ОТБОР БРЕНДОВ ДРУЗЕЙ, КАКИЕ ОРИГИНАЛЬНЫЕ ТУТ ТОВАРЫ И КАК ОНИ ХОРОШИ НА ПОДАРОК-->
<!--      ТЕКСТ ПРИМЕРНО НА 500 ЗНАКОВ, О ТВОРЧЕСТВЕ НЕБОЛЬШИХ КОМПАНИЙ И УНИКАЛЬНОСТИ, И ПРО ДОСТАВКУ В ОДНОЙ ПОСЫЛКЕ</div>-->
    <BrandsList/>
  </div>
</template>

<script>
import BrandsList from "@/components/BrandsList";

export default {
  name: "Brands",
  data() {
    return {
      visibleCard: true,
      categoryId: null,
      slug: ''
    }
  },
  components: {
    BrandsList
  },
  computed: {
    activeCategoryId() {
      let a = 0;
      const b = this.slug;
      this.$store.getters.allCategories.forEach(function (item) {
        if (item.slug === b) {
          a = item.id
        }
      });
      return a
    }
  },
  methods: {},
  watch: {
    $route(to) {
      this.slug = to.params.slug;
    }
  },
  mounted() {
    this.slug = this.$route.params.slug;
  }
}
</script>

<style scoped>
.wrapper-brands {
  max-width: 1380px;
  margin: 0 auto;
  padding-top: 40px;
}

.brands-info {
  font-size: calc(1vw + 2 * (100vw / 1338));
  font-family: 'Roboto', sans-serif;
  margin: 2% 5%;
  padding: 6px;
}

/*media queries******************************************************************************************************/
@media screen and (max-width: 1200px) {

}

@media screen and (max-width: 960px) {

}


@media screen and (max-width: 750px) {
  .brands-info {
    font-size: calc(1vw + 10 * (100vw / 750));
    font-family: 'Roboto', sans-serif;
  }
}

@media screen and (max-width: 420px) {

}

@media screen and (max-width: 375px) {

}

@media screen and (max-width: 360px) {

}

@media screen and (max-width: 320px) {

}

@media screen and (max-width: 280px) {

}

</style>
