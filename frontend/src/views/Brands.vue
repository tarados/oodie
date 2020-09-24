<template>
  <div class="wrapper-brands">
    <h3>ТУТ БУДЕТ ТЕКСТ ПРО ОТБОР БРЕНДОВ ДРУЗЕЙ, КАКИЕ ОРИГИНАЛЬНЫЕ ТУТ ТОВАРЫ И КАК ОНИ ХОРОШИ НА ПОДАРОК
      ТЕКСТ ПРИМЕРНО НА 500 ЗНАКОВ, О ТВОРЧЕСТВЕ НЕБОЛЬШИХ КОМПАНИЙ И УНИКАЛЬНОСТИ, И ПРО ДОСТАВКУ В ОДНОЙ ПОСЫЛКЕ</h3>
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

/*media queries******************************************************************************************************/
@media screen and (max-width: 1200px) {

}

@media screen and (max-width: 960px) {

}


@media screen and (max-width: 750px) {

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