<template>
  <div>
    <Category
        :categories="categories"
        :slugs="slugList"
        @onChoice="onChoice"
    />
    <ProductsList
        thumbnail="small"
        @productsList="productsList"
        :category="category"
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
                categories: [],
                slugList: [],
                category: '',
                slug: ''
            }
        },
        components: {
            ProductsList,
            Category
        },
        methods: {
            productsList(val) {
                const groupBy = (array, key) => {
                    return array.reduce((result, currentValue) => {
                        (result[currentValue[key]] = result[currentValue[key]] || []).push(
                            currentValue
                        );
                        return result;
                    }, {});
                };
                const productsGroupedByCategory = groupBy(val, 'category');
                for (let key in productsGroupedByCategory) {
                    this.categories.push(key.split(',')[0]);
                    this.slugList.push(key.split(',')[1]);
                }
            },
            onChoice(index) {
                if (this.category === this.categories[index]) {
                    this.category = '';
                } else {
                    this.category = this.categories[index];
                    this.slug = this.slugList[index];
                }
            }
        },
        watch: {
            categories: function () {
                // console.log(this.categories);
            }
        }
    }
</script>

<style scoped>

</style>