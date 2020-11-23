<template>
  <div class="wrapper-card" ref="card">
    <div class="header">
      <h1 v-if="this.$store.state.productsStore.cardProducts.length > 0">Корзина</h1>
      <h1 v-else>Ваша корзина пуста!</h1>
    </div>
    <div v-for="(product, index) in this.$store.state.productsStore.cardProducts" :key="index">
      <div class="grid-container second">
        <div class="item image">
          <img :src="product.image">
        </div>
        <div class="item product">
          <div class="name">
            {{ product.title }}
            <strong v-if="needShowSize(product)">
              {{ product.size }}
            </strong>
          </div>
        </div>
        <div class="item quantity-val">
          <div>
            {{ product.quantity }}
          </div>
          <div class="triangle">
            <div class="triangle-up" @click="plusQuantity(index)"></div>
            <div class="triangle-down" @click="minusQuantity(index)"></div>
          </div>
        </div>
        <div class="item total-val">{{ product.total }} грн</div>
        <div class="item close"><button @click="deleteOrder(index)">X</button></div>
      </div>
      <div class="mobile">
        <div class="mobile-content">
          <div class="image">
            <img :src="product.image">
          </div>
          <div class="product"><span>{{ product.title }}</span><span v-if="needShowSize(product)">{{ product.size }}</span></div>
          <div class="total-val">{{ product.total }} грн</div>
        </div>
        <div class="mobile-edit">
          <div class="remove-mobile" @click="deleteOrder(index)">Удалить</div>
          <div class="quantity-val-mobile">
            <div class="down">
              <div class="quantity-button" @click="minusQuantity(index)">-</div>
            </div>
            <div class="product-quantity">
              {{ product.quantity }}
            </div>
            <div class="up">
              <div class="quantity-button" @click="plusQuantity(index)">+</div>
            </div>
          </div>
          <div></div>
        </div>
      </div>
    </div>
    <div class="subtotal-mobile-box" v-show="this.$store.state.productsStore.cardProducts.length > 0">
      <div class="subtotal-mobile-title">Итого:</div>
      <div class="item subtotal-mobile" v-text="totalPrice"></div>
    </div>
    <div class="container container-border">
      <div class="subtotal-box" v-show="this.$store.state.productsStore.cardProducts.length > 0">
        <span>Итого </span>
        <span v-text="totalPrice"></span>
      </div>
    </div>
    <div class="container" v-if="isPreorder">
      <p>В Вашей корзине есть товар по предзаказу!
      Отправка этого товара будет ориентировочно 20-го декабря. Мы свяжемся с вами когда товар появится
        в наличии для подтверждения и отправим ваш заказ в первую очередь.</p>
    </div>
    <div class="container checkout-buttons">
        <router-link :to="{name: 'Home'}" class="checkout-button continue-shopping button">Продолжить покупки</router-link>
        <router-link
            :to="{name: 'Checkout'}"
            class="checkout-button checkout button"
            v-show="this.$store.state.productsStore.cardProducts.length > 0"
        >Оформить заказ</router-link>
    </div>
  </div>
</template>

<script>
import {mapGetters} from 'vuex';
import settings from "@/settings";


export default {
  name: "Card",
  data() {
    return {
      availability: null,
    }
  },
  computed: {
    ...mapGetters(["totalPrice"]),
    isPreorder() {
      let el = false
      this.$store.state.productsStore.cardProducts.forEach(product => {
        if (product.preorder) {
          el = true
        }
      })
      return el
    }
  },
  methods: {
    needShowSize(product) {
      const result = product.size && product.size !== settings.hideSize;
      return result;
    },
    deleteOrder(index) {
      this.$store.commit('delProduct', index);
    },
    minusQuantity(index) {
      const item = this.$store.state.productsStore.cardProducts[index];
      let newAvailability = item.quantity - 1;
      if (newAvailability > 0) {
        this.$store.commit('decrement', index);
      }
    },
    plusQuantity(index) {
      const item = this.$store.state.productsStore.cardProducts[index];
      let newAvailability = item.quantity + 1;
      if (newAvailability <= item.availability) {
        this.$store.commit('increment', index);
      } else {
        alert("В наличии только " + item.availability);
      }
    },
    basketVisible() {
      if (this.$store.state.productsStore.basketVisible) {
        this.$store.dispatch('changeVisibleBasket')
      }
    }
  },
  mounted() {
    this.basketVisible();
  }
}
</script>

<style scoped>

.wrapper-card {
  margin: 5vw;
}


.header {
  margin: 2% auto;
  text-align: center;
}

h1 {
  font-size: 2rem;
  color: rgb(61, 66, 70);
  text-transform: uppercase;
  letter-spacing: 0;
}

.grid-container {
  display: grid;
  max-width: 900px;
  margin: 15px auto;
  grid-template-columns: 10% 55% 10% 19% 6%;
}

.container-border {
  border-top: 1px solid black;
}

.container {
  width: 100%;
  display: flex;
  max-width: 900px;
  margin: auto;
  align-items: flex-end;
  justify-content: flex-end;
  padding: 0px 16px;
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
  text-transform: uppercase;
  letter-spacing: 0.8px;
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
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-around;
  padding-left: 16px;
}

.product .name {
  flex-grow: 2;
}

.remove {
  padding: 8px;
  height: 1.65vmax;
  display: flex;
  justify-content: center;
  align-items: center;
  border: 1px solid #e8e9eb;
  text-transform: uppercase;
  cursor: pointer;
  font-size: 12px;
  color: rgb(31, 66, 70);
  letter-spacing: 0.96px;
}

.remove:hover {
  opacity: 0.6;
  transition: all 0.7s ease;
}

p {
  margin: 25px 0;
  color: #f1410b;
  letter-spacing: 0.96px;
  line-height: 25px;
  text-transform: uppercase;
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

.quantity-val > div {
  margin-top: 2%;
  padding-top: 5%;
  padding-right: 5%;
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

.item.close {
  text-align: center;
  align-self: center;
}

.item.close button {
  border: none;
  background: transparent;
  font-size: 20px;
  color: #a3a4a5;
  cursor: pointer;
  width: 100%;
  height: 100%;
}

.item.close button:hover {
  color: black;
}

.item.close button:focus {
  outline: none;
}

.triangle {
  opacity: 0.2;
  margin-left: 8px;
  margin-right: 6px;
}

.quantity-val:hover > .triangle {
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
  margin-top: 20px;
  font-weight: bold;
  text-transform: uppercase;
}

.submit-box {
  display: grid;
  max-width: 1200px;
  margin: 20px auto;
  grid-template-columns: 60% 40%;
  grid-template-rows: 38px;
  border-top: none;
  border-bottom: none;
}

.checkout-buttons {
  margin-top: 32px;
  margin-bottom: 64px;
}

.checkout-button {
  display: flex;
  padding: 16px;
  text-transform: uppercase;
  font-size: 14px;
  font-weight: bold;
  text-decoration: none;
}

.checkout-button + .checkout-button {
  margin-left: 16px;
}

.checkout {
  background-color: #f87c56;
  color: white;
}

.continue-shopping {
  border: 1px solid black;
  color: black;
}

/*media queries*************************************************************************************/

@media screen and (max-width: 680px) {
  .wrapper-card {
    margin: 5vw;
  }

  .container {
    padding: 0;
    justify-content: space-between;
  }

  h1 {
    font-size: calc(2.5vw + 10px);
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
    font-size: 16px;
  }

  .product {

    justify-content: left;
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


  .quantity-button {
    width: 24px;
    font-weight: bold;
    text-align: center;
    font-size: 20px;
    border: 1px solid rgb(61, 66, 70);
    color: rgb(61, 66, 70);
  }

  .product-quantity {
    min-width: 24px;
    text-align: center;
    line-height: 24px;
  }
  .subtotal-mobile-box {
    display: flex;
    flex-wrap: wrap;
    align-self: center;
    justify-content: space-between;
    width: 100%;
    border-top: 1px solid grey;
    padding: 16px 0px;
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
    text-decoration: none;
    height: 9.5vw;
    flex-grow: 1;
    margin-left: 5%;
    display: flex;
    justify-content: center;
    align-items: center
  }

  .subtotal-box {
    display: none;
  }

  .container-border {
    display: none;
  }
}

@media screen and (max-width: 450px) {
  .checkout-buttons a {
    font-size: 12px;
  }
}

@media screen and (max-width: 360px) {
  img {
    width: 10.5vmax;
  }
}

@media screen and (max-width: 320px) {
  .checkout-button {
    padding: 8px;
  }
}
</style>
