<template>
  <div>
    <Navbar />
    <ProductsList thumbnail="small"/>
  </div>
  
</template>

<script>
  import Navbar from "../components/Navbar";
  import ProductsList from "../components/ProductsList";

    export default {
        name: "Products",
        components: {
            Navbar,
            ProductsList
        }
    }
</script>

<style scoped>

</style>