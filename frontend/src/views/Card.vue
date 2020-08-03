<template>
  <div ref="card" class="card">
    <Navbar/>
    <div class="wrapper-card">
      <div class="header">
        <h1>Your cart</h1>
      </div>
      <div class="grid-container first">
        <div class="item title">Product</div>
        <div class="item price">Price</div>
        <div class="item quantity">Quantity</div>
        <div class="item total">Total</div>
      </div>
      <div v-for="(product, index) in this.$store.state.productsStore.cardProducts" :key="index">
        <div class="grid-container second">
          <div class="item image">
            <img :src="product.image">
          </div>
          <div class="item product">
            {{ product.title }}
            <div class="remove" @click="deleteOrder(index)">Remove</div>
          </div>
          <div class="item price-val">${{ product.price }}</div>
          <div class="item quantity-val">
            {{ product.quantity }}
            <div class="triangle">
              <div class="triangle-up" @click="plusQuantity(index)"></div>
              <div class="triangle-down" @click="minusQuantity(index)"></div>
            </div>
          </div>
          <div class="item total-val">${{ product.total }}</div>
        </div>
        <div class="mobile">
          <div class="mobile-content">
            <div class="image">
              <img :src="product.image">
            </div>
            <div class="product">
              {{ product.title }}
            </div>
            <div class="total-val">${{ product.total }}</div>
          </div>
          <div class="mobile-edit">
            <div class="remove-mobile" @click="deleteOrder(index)">Remove</div>
            <div class="quantity-val-mobile">
              <div class="up">
                <div class="triangle-mobile-up" @click="plusQuantity(index)"></div>
              </div>
              <div class="product-quantity">
                {{ product.quantity }}
              </div>
              <div class="down">
                <div class="triangle-mobile-down" @click="minusQuantity(index)"></div>
              </div>
            </div>
            <div></div>
          </div>
        </div>
      </div>
      <div class="subtotal-mobile-box">
        <div class="subtotal-mobile-title">Subtotal</div>
        <div class="item subtotal-mobile" v-text="getTotalPrice"></div>
      </div>
      <div class="submit-mobile-box">
        <router-link :to="{name: 'Home'}" class="continue-mobile-shopping">Continue shopping</router-link>
        <router-link :to="{name: 'Checkout'}" class="checkout-mobile">Check out</router-link>
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
    <Footer />
  </div>
</template>

<script>
import Navbar from "../components/Navbar";
import Footer from "@/components/Footer";
import {mapGetters} from 'vuex';

export default {
  name: "Card",
  components: {
    Navbar,
    Footer
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
  },
  mounted() {
    // this.$refs.card.style.height = '100%';
    console.log(this.$refs.card.style.clientHeight);
  }
}
</script>

<style scoped>
.card {
  height: 100px;
}
.wrapper-card {
  /*margin: 3vh;*/
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

.mobile,
.subtotal-mobile-box,
.submit-mobile-box {
  display: none;
}

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
  text-align: center;
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
  background: rgba(150, 21, 100, 0.5);
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

/*media queries*************************************************************************************/
@media screen and (max-width: 960px) {
  .wrapper-card {
    margin: 5vw;
  }

  h1 {
    font-size: calc(3.125vw + 10px);
  }

  .title,
  .price,
  .quantity,
  .total,
  .product,
  .price-val,
  .quantity-val,
  .quantity-mobile,
  .quantity-val-mobile,
  .total-val,
  .subtotal-mobile-title,
  .subtotal-mobile,
  .continue-mobile-shopping,
  .checkout-mobile,
  .remove {
    font-size: calc(3.125vw + 2px);
    margin-left: 3%;
  }

  .first,
  .second,
  .submit-box {
    display: none;
  }

  .item {
    margin-left: 10%;
  }

  .mobile {
    display: flex;
    flex-wrap: wrap;
    width: 100%;
    margin-top: 4%;
  }

  .mobile-content {
    width: 100%;
    display: grid;
    grid-template-columns: 20% 60% 20%;
    grid-template-rows: repeat(2, 10vw);
    grid-row-gap: 2%;
  }

  .image,
  .product,
  .total-val {
    grid-row: 1/3;
  }

  .edit button {
    width: 90%;
    height: 60%;
    border-radius: 0;
    border: 1px solid;
    background-color: white;
    text-transform: uppercase;
  }

  .mobile-edit {
    width: 100%;
    height: 10vw;
    display: grid;
    grid-template-columns: 50% 25% 25%;
  }

  .mobile-edit .remove-mobile {
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

  .quantity-mobile {
    align-self: center;
    text-align: center;
  }

  .quantity-val-mobile {
    grid-column: 3/5;
    display: flex;
    flex-wrap: wrap;
    justify-content: flex-end;
    align-self: center;
  }


  .triangle-mobile-up {
    width: 0;
    height: 0;
    margin-bottom: 3px;
    border-left: 5px solid transparent;
    border-right: 5px solid transparent;
    border-bottom: 10px solid black;
  }

  .triangle-mobile-up:hover, .triangle-mobile-down:hover {
    background: rgba(150, 21, 100, 0.5);
  }

  .triangle-mobile-down {
    width: 0;
    height: 0;
    border-left: 5px solid transparent;
    border-right: 5px solid transparent;
    border-top: 10px solid black;
  }

  .up,
  .down,
  .product-quantity {
    flex-grow: 1;
  }

  .subtotal-mobile-box {
    display: flex;
    flex-wrap: wrap;
    align-self: center;
    justify-content: space-between;
    width: 100%;
    border-top: 1px solid grey;
    padding: 5%;
  }

  .submit-mobile-box {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
    align-self: center;
  }

  .continue-mobile-shopping {
    text-transform: uppercase;
    font-weight: 400;
    border-radius: 3px;
    text-decoration: none;
    color: #939393;
    border: 1px solid grey;
    padding: 2%;
    margin: 0;
  }

  .checkout-mobile {
    background-color: #f87c56;
    color: white;
    text-transform: uppercase;
    font-weight: 400;
    border-radius: 3px;
    text-decoration: none;
    height: 9.5vw;
    flex-grow: 1;
    margin-left: 5%;
    display: flex;
    justify-content: center;
    align-items: center
  }
}

@media screen and (max-width: 640px) {

}

@media screen and (max-width: 450px) {

}

@media screen and (max-width: 375px) {

}


@media screen and (max-width: 360px) {
  img {
    width: 10.5vmax;
  }
}

@media screen and (max-width: 325px) {

}
</style>
