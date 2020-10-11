<template>
  <div class="wrapper-checkout">
    <div class="header">
      <h1>К оплате:</h1>
    </div>
    <div class="subtotal">
      <div class="subtotal-title">Всего</div>
      <div class="subtotal-val" v-text="totalPrice"></div>
    </div>
    <form class="submit-box" @submit.prevent="submitHandler" autocomplete="off">
      <div class="form-title required">
        <span>Имя:</span>
      </div>
      <div class="username">
        <input
            autocomplete="nope"
            v-model="userName"
            :class="{invalid: invalidName}"
        >
        <small v-show="invalidName">Введите Ваше имя</small>
      </div>
      <div class="form-title required">
        <span>Фамилия:</span>
      </div>
      <div class="user-surname">
        <input
            autocomplete="nope"
            v-model="userSurname"
            :class="{invalid: invalidSurname}"
        >
        <small v-show="invalidSurname">Введите Вашу фамилию</small>
      </div>
      <div class="form-title required">
        <span>Телефон:</span>
      </div>
      <div class="phone">
        <input
            v-model="phone"
            :class="{invalid: invalidPhone || !$v.phone.numeric || !$v.phone.minLength || !$v.phone.maxLength}"
        >
        <small v-if="!$v.phone.numeric"> Вводите только числа!</small>
        <small
            v-else-if="!$v.phone.minLength || !$v.phone.maxLength"
        >
          В номере должно быть {{ $v.phone.$params.maxLength.max }} чисел. Сейчас их {{ phone.length }}!
        </small>
        <small v-show="invalidPhone && $v.phone.numeric && $v.phone.minLength && $v.phone.maxLength">
          Введите номер телефона!
        </small>
      </div>
      <div class="form-title">
        <span>E-mail:</span>
      </div>
      <div class="mail">
        <input
            v-model="email"
            :class="{invalid: !this.$v.email.email}"
        >
        <small v-if="!$v.email.email">Enter E-mail!</small>
      </div>
      <div class="form-title required">
        <span>Способ доставки:</span>
      </div>
      <div class="delivery">
        <select v-model="selected">
          <option disabled value="">Выберите способ доставки</option>
          <option>Новая почта</option>
          <option>Самовывоз</option>
        </select>
      </div>
      <div class="form-title required" v-show="selected === 'Новая почта'">
        <span>Город:</span>
      </div>
      <div class="new-post-city" v-show="selected === 'Новая почта'">
        <autocomplete
            :search="search"
            @submit="setCity"
        ></autocomplete>
      </div>
      <div class="form-title required" v-show="selected === 'Новая почта'">
        <span>Отделение:</span>
      </div>
      <div class="new-post-office" v-show="selected === 'Новая почта'">
        <autocomplete
            class="autocomplete"
            autocomplete="nope"
            :search="searchWarehouse"
            @submit="setWarehouse"
        ></autocomplete>
        <label data-first="Enter post address" data-second="Post address"></label>
      </div>
      <div class="form-title" v-show="selected === 'Самовывоз'">
        <span>Адрес:</span>
      </div>
      <div class="others" v-show="selected === 'Самовывоз'">
                  <textarea
                      id="others"
                      v-model="address"
                  ></textarea>
        <label data-first="Enter address" data-second="delivery address"></label>
      </div>
      <div class="form-title required"
           :class="{visible: isVisible}"
      >
        <span>Способ оплаты:</span>
      </div>
      <div class="payment-content"
           :class="{visible: isVisible}"
      >
        <select v-model="selectedPayment">
          <option disabled value="">Выберите способ оплаты</option>
          <option>Наличными</option>
          <option>На карту</option>
          <option>Наложенным платежем</option>
        </select>
      </div>
      <div class="form-title">
        <span>Комментарий</span>
      </div>
      <div class="description-content">
        <textarea v-model="comment" rows="4"></textarea>
      </div>
      <div class="button-block">
        <button @click="toCard" class="continue-shopping">
          <span>Вернуться в корзину</span>
        </button>
        <button type="submit" class="continue-shipping">
          <span> Купить</span>
        </button>
      </div>
    </form>
  </div>
</template>

<script>
import {mapGetters} from 'vuex';
import {required, numeric, minLength, maxLength, email} from 'vuelidate/lib/validators';
import {clearLocalStorage} from "@/js/card";
import {post} from '../js/send';
import Autocomplete from '@trevoreyre/autocomplete-vue';

export default {
  name: "Checkout",
  components: {
    Autocomplete
  },
  data() {
    return {
      selected: '',
      selectedPayment: '',
      isVisible: true,
      userName: '',
      userSurname: '',
      address: '',
      city: '',
      postOffice: '',
      phone: '',
      email: '',
      comment: '',
      invalidName: false,
      invalidSurname: false,
      invalidEmail: false,
      invalidPhone: false
    }
  },
  validations: {
    userName: {required},
    userSurname: {required},
    phone: {required, numeric, minLength: minLength(10), maxLength: maxLength(10)},
    email: {email}
  },
  computed: {
    ...mapGetters(["totalPrice", "allCities", "allWarehouses"])
  },
  methods: {
    async submitHandler() {
      const productsList = [];
      this.$store.state.productsStore.cardProducts.forEach(product => {
        productsList.push({
          'id': product.id,
          'price': product.price,
          'quantity': product.quantity,
          'size': product.size
        });
      });
      let order = {
        'products': productsList,
        'username': this.userName,
        'userSurname': this.userSurname,
        'phone': this.phone,
        'payment': this.selectedPayment,
        'delivery': this.selected,
        'city': this.city,
        'post-office': this.postOffice,
        'others': this.address,
        'comment': this.comment
      };
      const response = await post("order", order);
      this.invalidName = !this.$v.userName.required;
      this.invalidSurname = !this.$v.userSurname.required;
      this.invalidPhone = !this.$v.phone.required;
      this.invalidEmail = !this.$v.email.required;
      this.delivery = this.selected;
      if (response && !this.$v.$invalid) {
        await this.$router.push({name: 'Successful'});
        clearLocalStorage();
        this.$store.commit('clearBasket');
      }
      if (this.$v.invalid) {
        this.$v.$touch();
        return
      }
    },
    toCard() {
      this.$router.push({name: "Card"})
    },
    cardVisible() {
      this.$emit('cardVisible', false);
    },
    deliveryState() {
      this.$store.dispatch('loadCities');
    },
    search(input) {
      let cityList = this.allCities.map(city => {
        return city.name
      });
      if (input.length < 1) {
        return []
      }
      return cityList.filter(city => {
        return city.toLowerCase()
            .startsWith(input.toLowerCase())
      });
    },
    searchWarehouse(input) {
      let warehouseList = this.allWarehouses.map(warehouse => {
        return warehouse
      });
      if (input.length < 1) {
        return []
      }
      return warehouseList.filter(warehouse => {
        return warehouse.toLowerCase()
            .match(input.toLowerCase())
      });
    },
    setCity(city) {
      this.city = city;
    },
    setWarehouse(warehouse) {
      this.postOffice = warehouse;
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
    },
    city: function () {
      let cityId = this.allCities.find(city => city.name === this.city).id;
      this.$store.dispatch('loadWarehouses', cityId);
    },
    selected: function () {
      if(this.selected) {
        this.isVisible = false;
      }
    }
  },
  mounted() {
    this.cardVisible();
    this.deliveryState();
  }
}
</script>

<style scoped>
.wrapper-checkout {
  max-width: 600px;
  margin: 0 auto;
  padding-bottom: 64px;
}

.subtotal {
  display: grid;
  margin: 30px 0 30px;
  grid-template: 1fr / 1fr 1fr;
}

.header {
  text-align: center;
}

.header h1 {
  color: rgb(61, 66, 70);
  margin-top: 1%;
  margin-bottom: 1%;
  font-size: calc(22px + 10 * (100vw / 1835));
  text-transform: uppercase;
  letter-spacing: 0.8px;
}

span,
.button-block {
  font-size: 16px;
}

.button-block button {
  padding: 8px;
}

select {
  font-size: calc(8px + 2 * (100vw / 1835));
}

.subtotal-title {
  color: rgb(48, 48, 48);
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.8px;
}

.subtotal-val {
  justify-self: end;
  color: rgb(48, 48, 48);
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.8px;
}

/*Contact information*************************************************************************/
.submit-box {
  display: grid;
  grid-template: repeat(10, minmax(35px, auto)) / 0.7fr 2fr;
  grid-gap: 20px;
}

h2 {
  text-align: left;
  text-transform: uppercase;
  letter-spacing: 0.8px;
  margin-top: 1rem;
}

.form-title {
  align-self: center;
}

.form-title.required {
  /*font-weight: bold;*/
}

input {
  padding: 0 2%;
  align-self: center;
  width: 100%;
  height: 100%;
  font-size: 0.81rem;
  color: #555;
  outline: none;
  border: 1px solid #bbb;
}

.autocomplete {
  width: 100%;
}

.description-content input {
  padding-left: 10px;
}

textarea {
  resize: none;
  padding: 10px;
}

.invalid {
  border-color: red;
}

small {
  color: red;
  padding-left: 1%;
  position: relative;
  top: 20px;
  right: 0;
}

.delivery,
.payment-content {
  height: 100%;
}

.visible {
  display: none;
}

select {
  height: 100%;
  width: 100%;
  border: 1px solid #bbb;
  color: rgb(80, 80, 80);
  background-color: white;
  padding-left: 8px;
  padding-right: 8px;
  font-size: 14px;
}


input,
select,
textarea {
  background-repeat: no-repeat;
  background-position: 12px;
}

input:focus,
select:focus,
textarea:focus {
  border-color: #c7d9d8;
  background-color: #fff;
  outline: none;
  box-shadow: 0 2px 2px #c7d9d8;
}

.button-block {
  grid-column: 1/3;
  display: flex;
  justify-content: space-between;
  margin: 32px 0 0 0;
}

.continue-shopping {
  flex: 1;
  margin-right: 20px;
  background-color: white;
  border: 1px solid #bbbbbb;
  text-transform: uppercase;
  font-weight: 600;
  text-decoration: none;
}

.continue-shipping {
  flex: 1;
  background-color: green;
  border: 0;
  color: white;
  text-transform: uppercase;
  text-decoration: none;
  font-weight: 400;
}

textarea {
  width: 100%;
  border: 1px solid #bbb;
  color: rgb(80, 80, 80);
}

.logo svg {
  width: 7.19rem;
  margin: 0 5px
}

/*autocomplete*****************************************************************************/
.new-post-city div {
  width: 100%;
}

/*media queries*****************************************************************************/
@media screen and (max-width: 1200px) {
  .submit-box {
    margin: 0 10%;
  }
}

@media screen and (max-width: 960px) {
  .submit-box {
    margin: 0 8%;
  }

  select {
    width: 100%;
  }

  small {
    font-size: 0.75rem;
  }

  .logo svg {
    width: 3.6rem;
  }

  span,
  .button-block {
    font-size: calc(12px + (4 * 0.7) * ((100vw - 320px) / 1835));
  }

  select {
    /*font-size: calc(8px + (2 * 0.7) * ((100vw - 320px) / 1835));*/
  }


  header h1 {
    font-size: calc(22px + 7 * ((100vw - 320px) / 1835));
  }
}

@media (max-width: 450px) {
  .submit-box {
    margin: 0 5%;
  }

  .form-title {
    font-size: 14px;
  }

  button span {
    font-size: 10px;
  }
}


</style>
