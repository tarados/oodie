<template>
  <div class="wrapper">
    <Navbar visible-card />
    <router-view/>
    <Footer/>
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
    return {}
  },
  methods: {},
  mounted() {
  }
}
</script>

<style scoped>

</style>