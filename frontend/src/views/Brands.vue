<template>
  <div class="wrapper-brands">
    <BrandsList/>
  </div>
</template>

<script>
import BrandsList from "@/components/BrandsList";

export default {
  name: "Brands",
  data() {
    return {
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
  methods: {
    basketVisible() {
      if (!this.$store.state.productsStore.basketVisible) {
        this.$store.dispatch('changeVisibleBasket')
      }
    }
  },
  watch: {
    $route(to) {
      this.slug = to.params.slug;
    }
  },
  mounted() {
    this.slug = this.$route.params.slug;3
    this.basketVisible();
  }
}
</script>

<style scoped>
.wrapper-brands {
  max-width: 1380px;
  margin: 0 auto;
  padding-top: 40px;
  padding-bottom: 40px;
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
