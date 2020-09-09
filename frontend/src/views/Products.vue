<template>
  <div>
    <div class="content-text">
      <span>ТУТ БУДЕТ ТЕКСТ ПРО ОТБОР БРЕНДОВ ДРУЗЕЙ, КАКИЕ ОРИГИНАЛЬНЫЕ ТУТ ТОВАРЫ И КАК ОНИ ХОРОШИ НА ПОДАРОК
ТЕКСТ ПРИМЕРНО НА 500 ЗНАКОВ, О ТВОРЧЕСТВЕ НЕБОЛЬШИХ КОМПАНИЙ И УНИКАЛЬНОСТИ, И ПРО ДОСТАВКУ В ОДНОЙ ПОСЫЛКЕ</span>
    </div>
    <ProductsList
        thumbnail="small"
        :category-id="activeCategoryId"
    />
  </div>
</template>

<script>
import ProductsList from "../components/ProductsList";

export default {
  name: "Products",
  data() {
    return {
      visibleCard: true,
      category: '',
      categoryId: null,
      slug: ''
    }
  },
  components: {
    ProductsList
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
.content-text {
  width: 1580px;
  margin: 0 auto;
}

.content-text span {
  line-height: 1.7;
  margin: 1%;
}

</style>