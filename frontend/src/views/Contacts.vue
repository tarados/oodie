<template>
  <div class="wrapper">
    <div class="content-about">
      <p>Есть вопросы?</p>
      <p>Мы будем рады получить твое сообщение:</p>

      <div class="contact-row">
        <img class="contact-icon" src="../assets/phone-receiver.svg"/>
        <a href="tel:+380507204066">+380507204066</a>


<!--        <img class="contact-icon extra" src="../assets/media.png">-->
<!--        <img class="contact-icon" src="../assets/phone.png">-->
      </div>

      <div class="contact-row">
        <img class="contact-icon" src="../assets/email.svg">
        <a href="mailto:hoodiyalko@gmail.com">hoodiyalko@gmail.com</a>
      </div>
      <br>
      <p><strong>Возможен самовывоз возле м.Контрактовая площадь по предварительной договоренности.</strong></p>
      <br>
      <p>Подписывайся на наши страницы:</p>
      <p><a target="_blank" href="https://www.facebook.com/hoodiyalko/">facebook.com/hoodiyalko</a></p>
      <p><a target="_blank" href="https://www.instagram.com/hoodiyalko/">instagram.com/hoodiyalko</a></p>
      <a target="_blank" href="https://www.tiktok.com/hoodiyalko">tiktok.com/@hoodiyalko</a>
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
