<template>
  <div class="wrapper">
    <div class="content-about">
      <p>{{ 'ContactsQuestions' | localize }}</p>
      <p>{{ 'ContactsMessage' | localize }}</p>

      <div class="contact-row">
        <img class="contact-icon" src="../assets/phone-receiver.svg"/>
        <a href="tel:+380507204066">+380507204066</a>
      </div>

      <div class="contact-row">
        <img class="contact-icon" src="../assets/email.svg">
        <a href="mailto:hoodiyalko@gmail.com">hoodiyalko@gmail.com</a>
      </div>
      <br>
      <p><strong>{{ 'ContactsDescriptionOne' | localize }}<br> {{ 'ContactsDescriptionTwo' | localize }}</strong></p>
      <br>
      <p>{{ 'ContactsSubscribe' | localize }}</p>
      <p><a target="_blank" href="https://www.facebook.com/hoodiyalko/">facebook.com/hoodiyalko</a></p>
      <p><a target="_blank" href="https://www.instagram.com/hoodiyalko/">instagram.com/hoodiyalko</a></p>
    </div>


  </div>

</template>

<script>
export default {
  name: "Contacts"
}
</script>

<style scoped>
.wrapper {
  margin: 0 auto;
  max-width: 800px;
  padding: 16px;
  padding-bottom: 40px;
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
