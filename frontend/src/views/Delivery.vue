<template>
  <div class="wrapper">
    <div class="content-about">
      <div class="contact-item">
        <h2>{{ 'ShippingAndPayment' | localize }}</h2>
      </div>

      <div class="contact-item">
        <p class="title">Доставка по Украине</p>
        <ul>
          <li>Новой Почтой до ближайшего отделения. Заказы оформленные до 17.00 отправляем в тот же день</li>
          <li>Курьером Новой почты по адресу</li>
        </ul>
      </div>

      <div class="contact-item">
        <p class="title">Доставка по Киеву</p>
        <ul>
          <li>Новой почтой до ближайшего отделения</li>
          <li>Курьером Новой почты по адресу</li>
          <li>Самовывоз возле Контрактовой площади, по предварительной договорённости</li>
          <li>На такси (возможно только для предварительно оплаченных заказов)</li>
        </ul>
      </div>

      <div class="contact-item">
        <p class="title">Доставка в другие страны:</p>
        <p>Осуществляется по индивидуальному запросу. Свяжитесь с нами и мы просчитаем стоимость доставки вашего заказа в любой уголок мира.</p>
      </div>

      <div class="contact-item">
        <p class="title">Оплата</p>
        <ul>
          <li>Предоплата на карту (Приват, Моно)</li>
          <li>Наложенным платежом при получении</li>
          <li>Наличными при самовывозе</li>
        </ul>
      </div>

      <div class="contact-item">
        <p class="title">Обмен и возврат возможен в течении 14 дней после покупки</p>
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
