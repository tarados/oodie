<template>
  <div>
    <Category
        :categories="this.$store.getters.allCategories"
        @onChoice="onChoice"
    />
    <ProductsList
        thumbnail="small"
        :category-id="categoryId"
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
                slug: '',
                routPath: ''
            }
        },
        components: {
            ProductsList,
            Category
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
                this.slug = this.$route.params.slug;
            }
        },
        watch: {
            $route(to, from) {
                console.log(to.params);
                console.log(from);
                this.slug = this.$route.params.slug;
            }
        },
        mounted() {
            this.currentState();
            console.log(this.slug);
        }
    }
</script>

<style scoped>

</style>