<template>
  <div>
    <Navbar visible-card="visible-card" />
    <ProductsList thumbnail="small"/>
  </div>

</template>

<script>
    import Navbar from "../components/Navbar";
    import ProductsList from "../components/ProductsList";

    export default {
        name: "Products",
        data() {
            return {
                visibleCard: true
            }
        },
        components: {
            Navbar,
            ProductsList
        }
    }
</script>

<style scoped>

</style>