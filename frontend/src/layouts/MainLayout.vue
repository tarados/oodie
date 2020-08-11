<template>
  <div class="wrapper">
    <Navbar class="nav" :visible-card="visible"/>
    <router-view class="content" @cardVisible="cardVisible"/>
    <Footer class="footer"/>
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
                visible: true
            }
        },
        methods: {
            cardVisible() {
                this.visible = false;
            }
        },
        mounted() {
        }
    }
</script>

<style scoped>


</style>