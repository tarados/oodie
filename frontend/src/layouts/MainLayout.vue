<template>
  <div class="wrapper">
    <div class="item-header">
      <Navbar/>
    </div>
    <div class="item-body">
      <router-view/>
    </div>
    <div class="item-footer">
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
        methods: {
            heightContent() {
                console.log(document.documentElement.clientHeight);
                // let heightString = (document.documentElement.clientHeight - this.calcHeight) + 'px';
                // this.styleContent.height = heightString;
            }
        },
        mounted() {
            this.heightContent();
        }
    }
</script>

<style scoped>
  .wrapper {
    /*min-height: 100%;*/
    /*display: flex;*/
    /*flex-direction: column;*/
  }

  .item-header,
  .item-footer {
    /*flex-shrink: 0;*/
  }

  .item-body {
    /*flex-grow: 1;*/
  }
  /*media queries**************************************************************/

</style>