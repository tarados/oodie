<template>
  <div>
    <Category
        :categories="this.$store.getters.allCategories"
        :selected-category-id="activeCategoryId"
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

</style>