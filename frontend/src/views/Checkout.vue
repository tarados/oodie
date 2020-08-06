<template>
  <div>
    <div class="wrapper-checkout">
      <div class="header">
        <h1>Your checkout</h1>
      </div>
      <div class="grid-container third">
        <div class="item subtotal-title">Subtotal</div>
        <div class="item subtotal-val" v-text="getTotalPrice"></div>
      </div>
      <div class="header-box">
        <h2>Contact information</h2>
      </div>
      <form class="submit-box" @submit.prevent="submitHandler">
        <div class="title-name">
          Name:
        </div>
        <div class="user-name">
          <input
              v-model="userName"
              :class="{invalid: invalidName}"
          >
          <small v-show="invalidName"> Enter your name!</small>
        </div>
        <div class="title-phone">
          Phone:
        </div>
        <div class="phone">
          <input
              v-model="phone"
              :class="{invalid: invalidPhone || !$v.phone.numeric || !$v.phone.minLength || !$v.phone.maxLength}"
          >
          <small v-if="!$v.phone.numeric"> Enter only numeric!</small>
          <small
              v-else-if="!$v.phone.minLength || !$v.phone.maxLength"
          >
            The length of the number should be {{ $v.phone.$params.maxLength.max }}. Now it {{ phone.length }}!
          </small>
          <small v-show="invalidPhone && $v.phone.numeric && $v.phone.minLength && $v.phone.maxLength"> Enter your
            phone!</small>
        </div>
        <div class="title-mail">
          E-mail:
        </div>
        <div class="mail">
          <input
              v-model="email"
              :class="{invalid: this.$v.email.$dirty || !this.$v.email.email || invalidEmail}"
          >
          <small v-if="$v.email.$dirty || !$v.email.email || invalidEmail">Enter E-mail!</small>
<!--          <small v-else-if="!$v.email.required">Enter E-mail!</small>-->
        </div>
        <div class="title-delivery">
          Delivery method:
        </div>
        <div class="delivery">
          <select v-model="selected">
            <option disabled value="">Select delivery method</option>
            <option>Новая почта</option>
            <option>Другие</option>
          </select>
        </div>
        <div class="title-city" v-show="selected === 'Новая почта'">City:</div>
        <div class="new-post-city" v-show="selected === 'Новая почта'">
          <input v-model="city">
        </div>
        <div class="title-office" v-show="selected === 'Новая почта'">Office number:</div>
        <div class="new-post-office" v-show="selected === 'Новая почта'">
          <input
              id="post-office"
              v-model="postOffice"
          >
          <label data-first="Enter post address" data-second="Post address"></label>
        </div>
        <div class="title-others" v-show="selected === 'Другие'">Address:</div>
        <div class="others" v-show="selected === 'Другие'">
        <textarea
            id="others"
            v-model="address"
        ></textarea>
          <label data-first="Enter address" data-second="delivery address"></label>
        </div>
        <div class="button-block" v-if="selected !== 'Другие'">
          <button @click="toCard" class="continue-shopping">Return to card</button>
          <button type="submit" class="continue-shipping">Continue shipping</button>
        </div>
        <div class="button-block-others" v-else>
          <button @click="toCard" class="continue-shopping">Return to card</button>
          <button type="submit" class="continue-shipping">Continue shipping</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import {mapGetters} from 'vuex';
import {required, numeric, minLength, maxLength, email} from 'vuelidate/lib/validators'
import {post} from '../js/send'

export default {
  name: "Checkout",
  data() {
    return {
      selected: '',
      userName: '',
      address: '',
      city: '',
      postOffice: '',
      phone: '',
      email: '',
      invalidName: false,
      invalidEmail: false,
      invalidPhone: false
    }
  },
  validations: {
    userName: {required},
    phone: {required, numeric, minLength: minLength(10), maxLength: maxLength(10)},
    email: {email, required}
  },
  computed: {
    ...mapGetters(["getTotalPrice"])
  },
  methods: {
    async submitHandler() {
      const productsList = [];
      this.$store.state.productsStore.cardProducts.forEach(product => {
        productsList.push({
          'id': product.id,
          'price': product.price,
          'quantity': product.quantity
        });
      });
      let order = {
        'products': productsList,
        'username': this.userName,
        'phone': this.phone,
        'delivery': this.selected,
        'city': this.city,
        'post-office': this.postOffice,
        'others': this.address
      };
      const response = await post("order", order);
      this.invalidName = !this.$v.userName.required;
      this.invalidPhone = !this.$v.phone.required;
      this.invalidEmail = !this.$v.email.required;
      this.delivery = this.selected;
      if (response && !this.$v.$invalid) {
        await this.$router.push({name: 'Successful'});
      }
      if (this.$v.invalid) {
        this.$v.$touch();
        return
      }
    },
    toCard() {
      this.$router.push({name: "Card"})
    }
  },
  watch: {
    userName: function () {
      this.invalidName = this.$v.userName.$invalid;
    },
    phone: function () {
      if (this.$v.phone.$invalid) {
        this.invalidPhone = this.$v.phone.required;
      } else {
        this.invalidPhone = !this.$v.phone.required;
      }
    },
    email: function () {
      if (this.$v.email.$invalid) {
        this.invalidEmail = this.$v.email.required;
      } else {
        this.invalidEmail = !this.$v.email.required;
      }
    }
  }
}
</script>

<style scoped>
.wrapper-checkout {
  margin: 0 15px;
}

.grid-container {
  display: grid;
  max-width: 600px;
  grid-template-columns: 27% 58% 15%;
}

.logo svg {
  width: 115px;
  margin: 0 5px
}

.header {
  grid-column: 2/4;
  text-align: center;
}

.header h1 {
  color: rgb(61, 66, 70);
  margin-top: 1%;
  margin-bottom: 1%;
}

.third {
  margin: 2vw auto;
}

.subtotal-title {
  grid-column: 1/3;
  color: rgb(48, 48, 48);
  font-weight: 600;
}

.subtotal-val {
  color: rgb(48, 48, 48);
  font-weight: 600;
  font-size: 20px;
}

.item {
  align-self: center;
}

/*Contact information*************************************************************************/
.submit-box {
  max-width: 600px;
  display: grid;
  max-width: 600px;
  grid-template-columns: 40% 60%;
  grid-template-rows: repeat(7, 38px);
  grid-gap: 1vw;
  margin: 0 auto 15vh;
}

.header-box {
  width: 600px;
  margin: 1% auto;
}

h2 {
  text-align: left;
}

.title-name,
.title-delivery,
.title-phone,
.title-mail,
.title-city,
.title-office,
.title-others {
  align-self: center;
}

.user-name,
.phone,
.mail,
.new-post-city,
.new-post-office {
  display: flex;
  flex-wrap: wrap;
  justify-content: flex-end;
}

input {
  align-self: center;
  width: 100%;
  height: 100%;
  font-size: 13px;
  color: #555;
  outline: none;
  border: 1px solid #bbb;
  border-radius: 5px;
}

.invalid {
  border-color: red;
}

small {
  color: red;
  padding-left: 1%;
}

.delivery {
  height: 100%;
}

select {
  height: 100%;
  width: 45%;
  border: 1px solid #bbb;
  border-radius: 5px;
  color: rgb(80, 80, 80);
  background-color: white;
  padding-left: 1%;
}

.button-block,
.button-block-others {
  grid-column: 1/3;
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
}

.button-block-others {
  grid-row: 7/7;
}

.continue-shopping {
  width: 32%;
  background-color: white;
  border: 1px solid #bbbbbb;
  border-radius: 5px;
  text-transform: uppercase;
  font-size: 14px;
  font-weight: 600;
  text-decoration: none;
}

.continue-shipping {
  width: 32%;
  background-color: green;
  border: 0;
  border-radius: 5px;
  color: white;
  text-transform: uppercase;
  text-decoration: none;
  font-size: 14px;
  font-weight: 400;
}

.others {

}

textarea {
  width: 100%;
  height: 5vmax;
  border: 1px solid #bbb;
  border-radius: 5px;
  color: rgb(80, 80, 80);
}

/*media queries*****************************************************************************/
@media (max-width: 620px) {
  .header h1 {
    font-size: calc(3.125vw + 10px);
  }

  .logo svg {
    width: calc(3.125vw + 80px);
  }

  .title-name,
  .title-phone,
  select,
  .title-city,
  .title-office,
  .title-others,
  .continue-shipping,
  .continue-shopping {
    font-size: 2.7vw;
  }

  textarea {
    height: 10vmax;
  }

  .third .subtotal-title,
  .third .subtotal-val {
    font-size: calc(3.125vw + 4px);
  }

  .header-box h2 {
    font-size: calc(3.125vw + 5px);
  }

  .submit-box {
    margin-top: 10%;
    margin-bottom: 20%;
  }

  .submit-box label {
    font-size: calc(1.5vw + 1px);
  }
}

</style>