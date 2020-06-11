<template>
  <div>
    <Navbar />
    <Hamburger />
    <Collections set-style="small"/>
  </div>
  
</template>

<script>
  import Navbar from "../components/Navbar";
  import Hamburger from "../components/Hamburger";
  import Collections from "../components/Collections";

    export default {
        name: "Products",
        components: {
            Navbar,
            Hamburger,
            Collections
        }
    }
</script>

<style scoped>

</style>