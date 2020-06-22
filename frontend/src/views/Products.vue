<template>
  <div>
    <Navbar />
    <Hamburger />
    <ProductsList thumbnail="small"/>
  </div>
  
</template>

<script>
  import Navbar from "../components/Navbar";
  import Hamburger from "../components/Hamburger";
  import ProductsList from "../components/ProductsList";

    export default {
        name: "Products",
        components: {
            Navbar,
            Hamburger,
            ProductsList
        }
    }
</script>

<style scoped>

</style>