<template>
  <div id="root">
    <div class="wrapper">
      <Navbar class="nav"/>
      <router-view class="content"/>
      <Footer/>
    </div>
  </div>
</template>

<script>
    import Navbar from "../components/Navbar";
    import Footer from "../components/Footer";

    export default {
        name: "MainLayout",
        components: {
            Navbar,
            Footer
        }
    }
</script>

<style>
  #root {
    position: relative;
    display: flex;
    flex-flow: column;
    min-height: 100vh;
    margin: 0;
    padding: 0;
  }

  .wrapper {
    display: flex;
    flex-flow: column;
    flex: 1;
  }

  .content {
    flex: 1;
  }


</style>