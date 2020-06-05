<template>
  <div class="home">
    <Navbar/>
    <Hamburger/>
    <div class="shopContent">
      <div class="mainImage">ss</div>
    </div>
  </div>
</template>

<script>
    import Navbar from "../components/Navbar";
    import Hamburger from "../components/Hamburger"

    export default {
        name: 'Home',
        components: {
            Navbar,
            Hamburger
        }
    }
</script>

<style>
  .shopContent {
    position: absolute;
    width: 100%;
    height: 650px;
  }

  .mainImage {
    width: 100%;
    height: 100%;
    position: relative;
    background-image: url("../assets/tile.jpg");
    background-size: cover;
    background-position: center center;
  }

  @media screen and (max-width: 750px) {
    shopContent {
      height: calc(1512 / 1008 * 45vw);
    }

    .mainImage {
      height: calc(1512 / 1008 * 45vw);
    }
  }

</style>
