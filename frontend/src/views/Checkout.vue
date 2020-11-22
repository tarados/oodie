<template>
  <div class="wrapper-checkout">
    <form @submit.prevent="submitHandler">
      <div class="submit-box">
        <div class="form-title required">
          <span>Имя:</span>
        </div>
        <div class="form-content username">
          <input
              v-model="userName"
              :class="{invalid: invalidName}"
          >
          <small v-show="invalidName">Введите Ваше имя</small>
        </div>
        <div class="form-title required">
          <span>Фамилия:</span>
        </div>
        <div class="form-content user-surname">
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
        <div class="form-content phone">
          <div class="form-content__phone">
            <input
                v-model="country"
                class="country"
                @input="handleUserInputCountry"
            >
            <input
                v-model="phone"
                placeholder="__-___-__-__"
                :class="{invalid: invalidPhone}"
                class="phone-context"
                @input="handleUserInput"
            >
          </div>
          <small v-show="invalidPhone">
            Введите номер телефона
          </small>
        </div>
        <div class="form-title">
          <span>E-mail:</span>
        </div>
        <div class="form-content mail">
          <input
              v-model="email"
              :class="{invalid: !this.$v.email.email}"
          >
          <small v-if="!$v.email.email">Enter E-mail!</small>
        </div>
        <div class="form-title required">
          <span>Способ доставки:</span>
        </div>
        <div class="form-content footer-content__item">
          <select v-model="deliveryMethod" :class="{invalid: invalidDelivery}">
            <option disabled value="">Выберите способ доставки</option>
            <option>Новая почта</option>
            <option>Курьером Новой почты</option>
            <option>Самовывоз</option>
          </select>
          <small v-if="invalidDelivery">Нужно выбрать способ доставки</small>
        </div>
        <div class="form-title required" v-if="deliveryMethod === 'Новая почта'">
          <span>Город:</span>
        </div>
        <div class="" v-if="deliveryMethod === 'Новая почта'" :class="{invalid: invalidCity}">
          <autocomplete
              placeholder="Начните вводить название города"
              autocomplete="nope"
              :search="search"
              @submit="setCity"
          ></autocomplete>
          <small v-if="invalidCity">Выберите город</small>
        </div>
        <div class="form-title required" v-if="deliveryMethod === 'Новая почта'">
          <span>Отделение:</span>
        </div>
        <div class="new-post-office" v-if="deliveryMethod === 'Новая почта'" :class="{invalid: invalidOffice}">
          <autocomplete
              class="autocomplete"
              placeholder="Начните вводить номер или адрес отделения"
              autocomplete="nope"
              :search="searchWarehouse"
              @submit="setWarehouse"
          ></autocomplete>
          <small v-if="invalidOffice">Нужно выбрать склад Новой Почты</small>
          <label data-first="Enter post address" data-second="Post address"></label>
        </div>
        <div class="form-title required" v-if="deliveryMethod === 'Курьером Новой почты'">
          <span>Адрес:</span>
        </div>
        <div class="adress required" v-if="deliveryMethod === 'Курьером Новой почты'" :class="{invalid: invalidAdress}">
          <textarea v-model="adress" rows="4"></textarea>
          <small v-if="invalidAdress">Нужно указать адрес доставки</small>
        </div>
        <div class="form-title required">
          <span>Способ оплаты:</span>
        </div>
        <div class="payment-content" :class="{invalid: invalidPayment}">
          <select v-model="selectedPayment">
            <option disabled value="">Выберите способ оплаты</option>
            <option>На карту</option>
            <option>Наложенный платеж</option>
          </select>
          <small v-if="invalidPayment">Нужно выбрать способ оплаты</small>
        </div>
        <div class="form-title">
          <span>Комментарий</span>
        </div>
        <div class="description-content">
          <textarea v-model="comment" rows="4"></textarea>
        </div>
        <div class="button-block" v-if="deliveryMethod === 'Самовывоз'">
          <strong>Вы сможете забрать заказ возле метро Контрактовая. После оформления заказа, наш менеджер свяжется с
            вами для уточнения деталей.</strong>
        </div>
      </div>
      <div class="subtotal">
        <div class="subtotal-title">К оплате</div>
        <div class="subtotal-val" v-text="totalPrice"></div>
      </div>
      <div class="submit-box">
        <div class="button-block">
          <button @click="toCard" class="continue-shopping">
            <span>Вернуться в корзину</span>
          </button>
          <button type="submit" class="continue-shipping">
            <span> Купить</span>
          </button>
        </div>
      </div>
    </form>
  </div>
</template>

<script>
import {mapGetters} from 'vuex';
import {required, email} from 'vuelidate/lib/validators';
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
      "deliveryMethod": "",
      "selectedPayment": '',
      "isVisible": true,
      "userName": "",
      "userSurname": "",
      "adress": '',
      "city": '',
      "country": '+(380)',
      "postOffice": '',
      "phone": "",
      "email": '',
      "comment": '',
      "invalidName": false,
      "invalidSurname": false,
      "invalidCity": false,
      "invalidOffice": false,
      "invalidEmail": false,
      "invalidPhone": false,
      "invalidDelivery": false,
      "invalidPayment": false,
      "invalidAdress": false
    }
  },
  validations: {
    userName: {required},
    userSurname: {required},
    selectedPayment: {required},
    deliveryMethod: {required},
    phone: {required},
    email: {email}
  },
  computed: {
    ...mapGetters(["totalPrice", "allCities", "allWarehouses"]),
  },
  methods: {
    async submitHandler() {
      this.invalidName = this.$v.userName.$invalid;
      this.invalidSurname = this.$v.userSurname.$invalid;
      this.invalidPhone = this.$v.phone.$invalid;
      this.invalidEmail = this.$v.email.$invalid;
      this.invalidDelivery = this.$v.deliveryMethod.$invalid;
      this.invalidPayment = this.$v.selectedPayment.$invalid;
      if (this.deliveryMethod === 'Новая почта') {
        this.invalidAdress = false;
      } else if (this.adress === '') {
        this.invalidAdress = true;
      } else {
        this.invalidAdress = false;
      }

      const productsList = [];

      this.$store.state.productsStore.cardProducts.forEach(product => {
        productsList.push({
          'id': product.id,
          'price': product.price,
          'quantity': product.quantity,
          'size': product.size,
          'preorder': product.preorder
        });
      });
      let order = {
        'products': productsList,
        'username': this.userName,
        'userSurname': this.userSurname,
        'phone': this.country + this.phone,
        'payment': this.selectedPayment,
        'delivery': this.deliveryMethod,
        'city': this.city,
        'post-office': this.postOffice,
        'others': this.adress,
        'comment': this.comment
      };

      if (!this.$v.$invalid) {
        if (!this.invalidAdress || this.deliveryMethod === 'Самовывоз') {
          const response = await post("order", order);
          if (response) {
            await this.$router.push({name: 'Successful'});
            clearLocalStorage();
            this.$store.commit('clearBasket');
          }
        }
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
      this.invalidCity = false;
    },
    setWarehouse(warehouse) {
      this.postOffice = warehouse;
      this.invalidOffice = false;
    },
    handleUserInput(e) {
      let replacedInput = e.target.value.replace(/\D/g, '').match(/(\d{0,2})(\d{0,3})(\d{0,2})(\d{0,2})/);
      this.phone = !replacedInput[2] ? replacedInput[1] : replacedInput[1] + '-' + replacedInput[2]
          + (replacedInput[3] ? '-' + replacedInput[3]: '') + (replacedInput[4] ?'-' + replacedInput[4] : '');
    },
    handleUserInputCountry(e) {
      let replacedInput = e.target.value.replace(/\D/g, '').match(/(\d{0,1})(\d{0,1})(\d{0,1})/);
      this.country = !replacedInput[2] ? replacedInput[1] : '+' + '(' + replacedInput[1] + replacedInput[2] +(replacedInput[3] ? replacedInput[3] +')' : '');
    }
  },
  watch: {
    userName: function (newValue) {
      this.invalidName = this.$v.userName.$invalid;
      localStorage.setItem('userName', newValue);
    },
    userSurname: function (newValue) {
      this.invalidSurname = !newValue;
      localStorage.setItem('userSurname', newValue);
    },
    phone: function (newValue) {
      if (this.$v.phone.$invalid) {
        this.invalidPhone = this.$v.phone.required;
      } else {
        this.invalidPhone = !this.$v.phone.required;
        localStorage.setItem('phone', newValue);
      }
    },
    email: function () {
      if (this.$v.email.$invalid) {
        this.invalidEmail = this.$v.email.required;
      } else {
        this.invalidEmail = !this.$v.email.required;
      }
    },
    adress: function (newValue) {
      this.invalidAdress = !newValue;
    },
    city: function () {
      let cityId = this.allCities.find(city => city.name === this.city).id;
      this.$store.dispatch('loadWarehouses', cityId);
    },
    deliveryMethod: function (newValue) {
      this.invalidDelivery = !newValue;
    },
    selectedPayment: function (newValue) {
      this.invalidPayment = !newValue;
    },
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
  padding: 0px 16px;
  padding-bottom: 64px;

}

.subtotal {
  margin-top: 32px;
  width: 100%;
  display: flex;
  justify-content: space-between;
  padding-top: 8px;

  border-top: 1px solid black;
  /*margin: 30px 0 30px;*/
  /*grid-template: 1fr / 1fr 1fr;*/
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
  grid-template: repeat(auto-fit, minmax(35px, auto)) / 0.7fr 2fr;
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

.form-content {
  height: 100%;
}

.form-content__phone {
  display: flex;
  flex-wrap: nowrap;
}

.form-content__phone input.country {
  border-right: none;
  width: 15%;
}

.form-content__phone input.phone-context {
  border-left: none;
  margin: 0;
  padding: 0;
}

input {
  padding: 0 2%;
  align-self: center;
  width: 100%;
  height: 35px;
  font-size: 0.81rem;
  color: #555;
  outline: none;
  border: 1px solid #bbb;
}

.autocomplete {
  width: 100%;
}

.autocomplete-input {
  border-color: red;
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
  padding-left: 8px;
  position: relative;
  top: 4px;
  right: 0;
}

.footer-content__item,
.payment-content {
  height: 100%;
}

.visible {
  display: none;
}

select {
  height: 35px;
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
    /*margin: 0 10%;*/
  }
}

@media screen and (max-width: 960px) {
  .submit-box {
    /*margin: 0 8%;*/
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
    /*margin: 0 5%;*/
  }

  .form-title {
    font-size: 14px;
  }

  button span {
    font-size: 10px;
  }
}


</style>
