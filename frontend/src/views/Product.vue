<template>
  <div>
    <Navbar/>
    <div class="wrapper">
      <div class="row">
        <div class="item left">
          <img :src="this.$route.params.image" class="noZoomImg">
        </div>
        <div class="item right">
          <h1>{{this.$route.params.title}}</h1>
          <div class="price">{{this.$route.params.price}} Sale</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
    import Navbar from "../components/Navbar";

    export default {
        name: "Product",
        components: {
            Navbar
        }
    }
</script>

<style scoped>
  .wrapper {
    margin-top: 55px;
  }

  .row {
    max-width: 1200px;
    margin: 0 auto;
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    align-items: inherit;
    align-content: center;
  }

  .item {
    text-align: left;
    font-size: 1.1em;
    font-family: "Roboto", "Lucida Grande", "DejaVu Sans", "Bitstream Vera Sans", Verdana, Arial, sans-serif;
    color:rgb(61, 66, 70);
    border: 1px solid black;
    width: calc((100% / 12) * 6 - 30px);
    margin: 0 15px;
    overflow: hidden;
  }

  .item img {
   width: 100%;
  }

  .item img:hover {
    transform: scale(1.5);

  }

  .price {
    padding-left: 10px;
    color: #eb6f6e;
  }
</style>