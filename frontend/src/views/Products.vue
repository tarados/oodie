<template>
  <div>
    <Category
        @onChoice="onChoice"
    />
    <ProductsList
        thumbnail="small"
        :category="category"
    />
  </div>
</template>

<script>
import ProductsList from "../components/ProductsList";
import Category from "../components/Category";
import {mapGetters} from 'vuex'

export default {
  name: "Products",
  data() {
    return {
      visibleCard: true,
      category: '',
      slug: '',
      routPath: ''
    }
  },
  components: {
    ProductsList,
    Category
  },
  computed: {
    ...mapGetters(["getCategoryList"]),
    ...mapGetters(["getSlugList"])
  },
  methods: {
    onChoice(index) {
      if (this.category === this.getCategoryList[index]) {
        this.category = '';
        this.$router.push({path: '/brands'}).catch(() => {
        });
      } else {
        this.category = this.getCategoryList[index];
        this.slug = this.getSlugList[index]
        this.$router.push({path: '/brands/' + this.slug}).catch(() => {
        });
      }
    },
    currentState() {
      const currentSlug = this.$route.path.split('/');
      if (currentSlug.length === 3) {
        let slug = this.$route.params.slug;
        console.log(slug);
      }

    }
  },
  mounted() {
    this.currentState();
    console.log(this.$route.params.slug);
  }
}
</script>

<style scoped>

</style>