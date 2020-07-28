<template>
  <div>
    <Navbar visible-card="visible-card" />
    <Category />
    <ProductsList thumbnail="small"/>
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
                visibleCard: true
            }
        },
        components: {
            Navbar,
            ProductsList,
            Category
        }
    }
</script>

<style scoped>

</style>