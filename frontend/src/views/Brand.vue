<template>
  <div>
    <ProductsList thumbnail="large" :category-id="activeCategoryId"/>
  </div>
</template>

<script>
import ProductsList from "@/components/ProductsList";

export default {
  name: "Brand",
  data() {
    return {
      visibleCard: true,
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