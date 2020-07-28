<template>
  <div>
    <Navbar visible-card="visible-card"/>
    <Category :categories="categories"/>
    <ProductsList
        thumbnail="small"
        @productsList="productsList"
    />
  </div>

</template>

<script>
import Navbar from "../components/Navbar";
import ProductsList from "../components/ProductsList";
import Category from "../components/Category";

export default {
  name: "Products",
  data() {
    return {
      visibleCard: true,
      categories: []
    }
  },
  components: {
    Navbar,
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
      this.categories = Object.keys(productsGroupedByCategory)
    }
  }
}
</script>

<style scoped>

</style>