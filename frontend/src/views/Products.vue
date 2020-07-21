<template>
  <div>
    <Navbar visible-card="visibleCard"/>
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