<template>
  <div class="wrapper">
    <div class="content-about">
      <div class="contact-item">
        <h2>{{ $t('ShippingAndPayment') }}</h2>
      </div>

      <div class="contact-item">
        <p class="title">{{ $t('DeliveryInUkraine') }}</p>
        <ul>
          <li>{{ $t('ShippingAndPaymentDescriptionOne') }}</li>
          <li>{{ $t('ShippingAndPaymentDescriptionTwo') }}</li>
        </ul>
      </div>

      <div class="contact-item">
        <p class="title">{{ $t('DeliveryInKiev') }}</p>
        <ul>
          <li>{{ $t('ShippingAndPaymentDescriptionThree') }}</li>
          <li>{{  $t('ShippingAndPaymentDescriptionFour') }}</li>
          <li>{{ $t('ShippingAndPaymentDescriptionFive') }}</li>
          <li>{{ $t('ShippingAndPaymentDescriptionSix') }}</li>
        </ul>
      </div>

      <div class="contact-item">
        <p class="title">{{ $t('DeliveryInOtherCountry') }}</p>
        <p>{{ $t('ShippingAndPaymentDescriptionSeven') }}</p>
      </div>

      <div class="contact-item">
        <p class="title">{{ $t('DeliveryPayment') }}</p>
        <ul>
          <li>{{ $t('DeliveryPrePayment') }}</li>
          <li>{{ $t('DeliveryCashOn') }}</li>
          <li>{{ $t('DeliveryCashPickup') }}</li>
        </ul>
      </div>

      <div class="contact-item">
        <p class="title">{{ $t('ShippingAndPaymentDescriptionEight') }}</p>
      </div>
    </div>



  </div>

</template>

<script>


export default {
  name: "Contacts"
};
</script>

<style scoped>
.wrapper {
  margin: 0 auto;
  max-width: 800px;
  padding: 16px 16px 40px 16px;
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
