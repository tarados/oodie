<template>
  <div class="wrapper-layout" id="content-wrapper">
    <div id="content">
      <Navbar/>
      <router-view/>
    </div>
    <div id="footer">
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
.wrapper-layout {
  overflow-x: hidden;
}
</style>