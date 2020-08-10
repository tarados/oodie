<template>
  <div class="wrapper">
    <div class="item-header" ref="header" >
      <Navbar
          ref="navbar"
      />
    </div>
    <div class="item-body">
      <router-view/>
    </div>
    <div class="item-footer" ref="footer">
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
        },
        data() {
            return {

            }
        },
        methods: {
        },
        mounted() {
        }
    }
</script>

<style scoped>

</style>