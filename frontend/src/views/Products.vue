<template>
  <div>
    <Category
        :categories="categories"
        :slugs="slugList"
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
                categories: [],
                slugList: [],
                category: '',
                slugIndex: '0'
            }
        },
        components: {
            ProductsList,
            Category
        },
        computed: {
            ...mapGetters(["allProducts"])
        },
        methods: {
            productsList() {
                const groupBy = (array, key) => {
                    return array.reduce((result, currentValue) => {
                        (result[currentValue[key]] = result[currentValue[key]] || []).push(
                            currentValue
                        );
                        return result;
                    }, {});
                };
                const productsGroupedByCategory = groupBy(this.allProducts, 'category');
                for (let key in productsGroupedByCategory) {
                    this.categories.push(key.split(',')[0]);
                    this.slugList.push(key.split(',')[1]);
                }
            },
            onChoice(index) {
                this.slugIndex = index;
                if (this.category === this.categories[index]) {
                    this.category = '';
                } else {
                    this.category = this.categories[index];
                    this.slug = this.slugList[index];
                }
            }
        },
        mounted() {
            this.productsList();
            // this.onChoice(this.slugIndex);
        }
    }
</script>

<style scoped>

</style>