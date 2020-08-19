<template>
  <div class="wrapper-checkout">
    <div class="header">
      <h1>Your checkout</h1>
    </div>
    <div class="subtotal">
      <div class="subtotal-title">Subtotal</div>
      <div class="subtotal-val" v-text="getTotalPrice"></div>
      <div class="header-box">
        <h2>Contact information</h2>
      </div>
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
            },
            cardVisible() {
                this.$emit('cardVisible', false);
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
        },
        mounted() {
            this.cardVisible();
        }
    }
</script>

<style scoped>
  .wrapper-checkout {
    margin: 0 1rem;
  }

  .subtotal {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
    max-width: 37rem;
    margin: 3% auto;

  }

  .header {
    text-align: center;
  }

  .header h1 {
    color: rgb(61, 66, 70);
    margin-top: 1%;
    margin-bottom: 1%;
    font-size: 2rem;
  }

  .subtotal-title {
    color: rgb(48, 48, 48);
    font-weight: 600;
    font-size: 1.25rem;
  }

  .subtotal-val {
    color: rgb(48, 48, 48);
    font-weight: 600;
    font-size: 1.25rem;
  }

  /*Contact information*************************************************************************/
  .submit-box {
    max-width: 37rem;
    display: grid;
    grid-template-columns: 40% 60%;
    grid-template-rows: repeat(7, 2.36rem);
    grid-gap: 1vw;
    margin: 0 auto 15vh;
  }

  .header-box {
    width: 37rem;
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
    font-size: 0.81rem;
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
    font-size: 0.875rem;
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
    font-size: 0.875rem;
    font-weight: 400;
  }

  textarea {
    width: 100%;
    height: 5vmax;
    border: 1px solid #bbb;
    border-radius: 5px;
    color: rgb(80, 80, 80);
  }

  .logo svg {
    width: 7.19rem;
    margin: 0 5px
  }

  /*media queries*****************************************************************************/
  @media screen and (max-width: 960px) {
    h1 {
      font-size: 2rem;
    }

    .subtotal {
      max-width: 20rem;
    }

    .subtotal-title,
    .subtotal-val {
      font-size: 0.78rem;
    }

    .header-box {
      margin-top: 5%;
    }

    h2 {
      font-size: 1.1rem;
    }

    .submit-box {
      grid-template-rows: repeat(7, 2rem);
      grid-gap: 1rem;
      margin-top: 10%;
    }

    select {
      width: 100%;
    }

    .continue-shipping {
      width: 43.95%;
    }

    .continue-shopping {
      width: 42%;
    }

    small {
      font-size: 0.75rem;
    }

    .logo svg {
      width: 3.6rem;
    }

    .title-name,
    .title-phone,
    select,
    .title-city,
    .title-office,
    .title-others,
    .title-delivery,
    .title-mail,
    .continue-shipping,
    .continue-shopping {
      font-size: 0.71rem;
    }

    textarea {
      height: 10vmax;
    }

  }

  @media (max-width: 450px) {
    .wrapper-checkout {
      margin: 0 1.7rem
    }

    .header h1 {
      font-size: 1.25rem;
      margin-top: 5%;
      margin-bottom: 5%
    }

    h2 {
      font-size: 1rem;
    }
  }

</style>