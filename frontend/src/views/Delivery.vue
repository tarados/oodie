<template>
  <div class="wrapper">
    <div class="content-about">
      <div class="contact-item">
        <h2>{{ 'ShippingAndPayment' | localize }}</h2>
      </div>

      <div class="contact-item">
        <p class="title">{{ 'DeliveryInUkraine' | localize }}</p>
        <ul>
          <li>{{ 'ShippingAndPaymentDescriptionOne' | localize }}</li>
          <li>{{ 'ShippingAndPaymentDescriptionTwo' | localize }}</li>
        </ul>
      </div>

      <div class="contact-item">
        <p class="title">{{ 'DeliveryInKiev' | localize }}</p>
        <ul>
          <li>{{ 'ShippingAndPaymentDescriptionThree' | localize }}</li>
          <li>{{  'ShippingAndPaymentDescriptionFour' | localize }}</li>
          <li>{{ 'ShippingAndPaymentDescriptionFive' | localize }}</li>
          <li>{{ 'ShippingAndPaymentDescriptionSix' | localize }}</li>
        </ul>
      </div>

      <div class="contact-item">
        <p class="title">{{ 'DeliveryInOtherCountry' | localize }}</p>
        <p>{{ 'ShippingAndPaymentDescriptionSeven' | localize }}</p>
      </div>

      <div class="contact-item">
        <p class="title">{{ 'DeliveryPayment' | localize }}</p>
        <ul>
          <li>{{ 'DeliveryPrePayment' | localize }}</li>
          <li>{{ 'DeliveryCashOn' | localize }}</li>
          <li>{{ 'DeliveryCashPickup' | localize }}</li>
        </ul>
      </div>

      <div class="contact-item">
        <p class="title">{{ 'ShippingAndPaymentDescriptionEight' | localize }}</p>
      </div>
    </div>



  </div>

</template>

<script>
export default {
  name: "Contacts",
  methods: {
    basketVisible() {
      if (!this.$store.state.productsStore.basketVisible) {
        this.$store.dispatch("changeVisibleBasket");
      }
    },
  },
  mounted() {
    this.basketVisible();
    console.log(this.$router.currentRoute.name);
  },
};
</script>

<style scoped>
.wrapper {
  margin: 0 auto;
  max-width: 800px;
  padding: 16px;
  padding-bottom: 40px;
}

.contact-item {
  margin-bottom: 16px;
  line-height: 24px;
}

.contact-item .title {
  font-weight: bold;
}

.contact-item ul {
  padding-left: 24px;
}
.content-about {
  /*margin: 6vmin;*/
  /*display: grid;*/
  /*grid-template: repeat(8, auto) / 1fr;*/
  /*grid-row-gap: 3vmin;*/

  font-size: 16px;
}

.content-about p, .contact-row {
  margin-bottom: 8px;
}

.contact-row {
  display: flex;
}

.content-about a {
  color: black;
  text-decoration: none;
}

.content-about a:hover {
  text-decoration: underline;
}

.contact-icon {
  display: inline-block;
  width: 20px;
  height: 20px;
  margin-right: 8px;
}

.extra {
  margin-left: 16px;
}

</style>
