<template>
  <div id="root">
    <div class="wrapper">
      <Navbar class="nav" :visible-card="visible"/>
      <router-view class="content" @cardVisible="cardVisible"/>
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
    /*min-height: 100%;*/
    /*display: grid;*/
    /*grid-template: minmax(100px, auto) 1fr minmax(70px, auto) / 1fr;*/
    display: flex;
    flex-flow: column;
    flex: 1;
  }

  .content {
    flex: 1;
  }


</style>