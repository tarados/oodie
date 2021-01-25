<template>
  <div class="wrapper-brand">
    <ProductsList :category-id="activeCategoryId" size="small"/>
  </div>
</template>

<script>
import ProductsList from "@/components/ProductsList";

export default {
  name: "Brand",
  data() {
    return {
      slug: ''
    }
  },
  components: {
    ProductsList,
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
    },
    activeCategoryTitle() {
      try {
        return this.$store.getters.allCategories.find(item => item.id === this.activeCategoryId).title
      } catch (TypeError) {
        return ''
      }

    }
  },
  methods: {
    // basketVisible() {
    //   if (!this.$store.state.productsStore.basketVisible) {
    //     this.$store.dispatch('changeVisibleBasket')
    //   }
    // }
  },
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
.wrapper-brand {
  display: flex;
  flex-direction: column;
  align-self: center;
}

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
