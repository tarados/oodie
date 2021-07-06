<template>
  <div class="wrapper-brand">
    <ProductsList :category-id="activeCategoryId" size="small"/>
  </div>
</template>

<script>
import ProductsList from "@/components/ProductsList";
import {mapState} from 'vuex'

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
    ...mapState(["categoriesList"]),
    activeCategoryId() {
      this.categoriesList.forEach(function (item) {
        if (item.slug === this.slug) {
          return item.id
        }
      });
    }
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
</style>
