<template>
  <div>
    <Navbar/>
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
        <div class="item product">
          {{product.title}}
          <div class="remove" @click="deleteOrder(index)">Remove</div>
        </div>
        <div class="item price-val">${{product.price}}</div>
        <div class="item quantity-val">
          {{product.quantity}}
          <div class="triangle">
            <div class="triangle-up" @click="plusQuantity(index)"></div>
            <div class="triangle-down" @click="minusQuantity(index)"></div>
          </div>
        </div>
        <div class="item total-val">${{product.total}}</div>
      </div>
      <div class="grid-container second subtotal-box">
        <div class="item subtotal-title">Subtotal</div>
        <div class="item subtotal" v-text="getTotalPrice"></div>
      </div>
      <div class="grid-container submit-box">
        <router-link :to="{name: 'Home'}" class="item continue-shopping">Continue shopping</router-link>
        <router-link :to="{name: 'Checkout'}" class="item checkout">Check out</router-link>
      </div>
    </div>
  </div>
</template>

<script>
    import Navbar from "../components/Navbar";
    import {mapGetters} from 'vuex';

    export default {
        name: "Card",
        components: {
            Navbar
        },
        computed: {
            ...mapGetters(["getTotalPrice"])
        },
        methods: {
            deleteOrder(index) {
                this.$store.commit('delProduct', index);
            },
            minusQuantity(index) {
                this.$store.commit('decrement', index);
            },
            plusQuantity(index) {
                this.$store.commit('increment', index);
            }
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

  .title, .price, .quantity, .total {
    font-weight: 600;
  }

  .second {
    grid-template-rows: 147px;
    border-top: 1px solid #e8e9eb;
  }

  .second:last-child {
    border-bottom: 1px solid #e8e9eb;
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

  .product {
    display: block;
  }

  .remove {
    margin-top: 10px;
    width: 12%;
    height: 1.65vmax;
    display: flex;
    justify-content: center;
    align-items: center;
    border: 1px solid #e8e9eb;
    text-transform: uppercase;
    text-decoration: none;
    font-size: 12px;
    color: rgb(31, 66, 70);
    letter-spacing: 0.96px;
  }

  .remove:hover {
    opacity: 0.6;
    transition: all 0.7s ease;
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
    display: flex;
    flex-wrap: wrap;
    align-content: center;
    justify-content: flex-end;
    border: 1px solid #e8e9eb;
    transition: all 0.7s ease;
    width: 60px;
    height: 41px;
    margin-left: 25%;
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

  .triangle {
    opacity: 0;
    margin-left: 8px;
    margin-right: 6px;
  }

  .triangle:hover {
    opacity: 1;
    transition: all 0.7s ease;
  }

  .triangle-up {
    width: 0;
    height: 0;
    margin-bottom: 3px;
    border-left: 5px solid transparent;
    border-right: 5px solid transparent;
    border-bottom: 10px solid black;
  }

  .triangle-up:hover, .triangle-down:hover {
    background: rgba(150,21,100, 0.5);
  }

  .triangle-down {
    width: 0;
    height: 0;
    border-left: 5px solid transparent;
    border-right: 5px solid transparent;
    border-top: 10px solid black;
  }

  .subtotal-title {
    grid-column: 1/5;
    justify-self: flex-end;
    align-self: center;
    margin-right: 3%;
    font-size: 18px;
    font-weight: 600;
    color: #3d4246;
  }

  .subtotal {
    font-weight: 600;
    align-self: center;
    justify-self: center;
  }

  .subtotal-box {
    border-bottom: none;
  }

   .submit-box {
     grid-template-rows: 38px;
     border-top: none;
     border-bottom: none;
   }

  .checkout {
    grid-column: 5/5;
    justify-self: center;
    align-self: center;
    width: 92%;
    height: 100%;
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    align-items: center;
    background-color: #f87c56;
    color: white;
    text-transform: uppercase;
    font-size: 14px;
    font-weight: 400;
    border-radius: 3px;
    text-decoration: none;
  }

  .checkout:hover,
  .continue-shopping:hover {
    opacity: 0.5;
    transition: opacity 0.7s ease;
  }

  .continue-shopping {
    grid-column: 1/4;
    justify-self: flex-end;
    align-self: center;
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    align-items: center;
    width: 21%;
    height: 100%;
    border: 1px solid #e8e9eb;
    text-transform: uppercase;
    font-size: 14px;
    font-weight: 600;
    border-radius: 3px;
    text-decoration: none;
  }
</style>
