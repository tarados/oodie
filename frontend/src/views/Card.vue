<template>
  <div>
    <Navbar />
    <div class="wrapper">
      <div class="header">
        <h1>Your cart</h1>
      </div>
      <div class="grid-container first">
        <div class="item title">Product</div>
        <div class="item price">Price</div>
        <div class="item quantity">Quantity</div>
        <div class="item total">Total</div>
      </div>
      <div class="grid-container second" v-for="(product, index) in this.$store.state.productsStore.cardProducts" :key="index">
        <div class="item image">
          <img :src="product.image">
        </div>
        <div class="item product">{{product.title}}</div>
        <div class="item price-val">{{product.price}}</div>
        <div class="item quantity-val">{{product.quantity}}</div>
        <div class="item total-val">sdf</div>
      </div>
    </div>
  </div>
</template>

<script>
  import Navbar from "../components/Navbar";

    export default {
        name: "Card",
        components: {
            Navbar
        }
    }
</script>

<style scoped>
  .wrapper {
    margin-top: 55px;
  }

  .header {
    text-align: center;
  }

  h1 {
    font-size: 2.5em;
    color: rgb(61, 66, 70);;
    text-transform: none;
    letter-spacing: 0;
  }

  .grid-container {
    display: grid;
    max-width: 1200px;
    margin: 15px auto;
    grid-template-columns: 10% 58% 10% 11% 11%;
    /*grid-template-areas:*/
    /*"header header"*/
  }

  .first {
    grid-template-rows: 78px;
  }

  .second {
    grid-template-rows: 147px;
    border-top: 1px solid grey;
  }

  .second:last-child {
    border-bottom: 1px solid grey;
  }

  /*Просто оформление*/
  .item {
    color: black;
  }

  img {
    width: 5vmax;
  }

  .title {
    grid-column: 1/3;
    align-self: end;
    padding: 28px 0;
  }

  .product, .image {
    align-self: center;
  }

  .price {
    align-self: end;
    padding: 28px 0;

  }

  .price-val {
    align-self: center;
  }

  .quantity {
    text-align: center;
    align-self: end;
    padding: 28px 0;

  }

  .quantity-val {
    text-align: center;
    align-self: center;
  }

  .total {
    text-align: center;
    align-self: end;
    padding: 28px 0;

  }

  .total-val {
    text-align: center;
    align-self: center;
  }
</style>