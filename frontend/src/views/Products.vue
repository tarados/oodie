<template>
  <div>
    <Category
        :categories="this.$store.getters.allCategories"
        @onChoice="onChoice"
    />
    <ProductsList
        thumbnail="small"
        :category-id="activeCategoryId"
    />
  </div>
</template>

<script>
import ProductsList from "../components/ProductsList";
import Category from "../components/Category";

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
    ProductsList,
    Category
  },
  computed: {
    activeCategoryId() {
      // const activeCategory = this.$store.getters.allCategories.filter(item => item.slug === this.slug)[0];
      // console.log(activeCategory);
      let a = 0;
      const b = this.slug;
      this.$store.getters.allCategories.forEach(function (item) {
        if (item.slug === b) {
          a = item.id
        }
      });
      console.log(a);
      return a
    }
  },
  methods: {
    onChoice(index) {
      if (this.category === this.$store.getters.allCategories[index].title) {
        this.category = '';
        this.categoryId = null;
        this.$router.push({path: '/brands'}).catch(() => {
        });
      } else {
        this.category = this.$store.getters.allCategories[index].title;
        this.categoryId = this.$store.getters.allCategories[index].id;
        this.slug = this.$store.getters.allCategories[index].slug;
        this.$router.push({path: '/brands/' + this.slug}).catch(() => {
        });
      }
    },
    currentState() {
      this.activeCategoryId;
    }
  },
  watch: {
    $route(to, from) {
      console.log(from.params.slug);
      this.slug = to.params.slug;
    }
  },
  mounted() {
    this.currentState();
  }
}
</script>

<style scoped>

</style>