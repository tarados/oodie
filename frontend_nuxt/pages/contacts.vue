<template>
  <div class="wrapper">
    <div class="content-about">
      <p>{{ $t('ContactsQuestions') }}</p>
      <p>{{ $t('ContactsMessage') }}</p>

      <div class="contact-row">
        <img class="contact-icon" src="~/assets/img/phone-receiver.svg"/>
        <a href="tel:+380507204066">+380507204066</a>
      </div>

      <div class="contact-row">
        <img class="contact-icon" src="~/assets/img/email.svg">
        <a href="mailto:hoodiyalko@gmail.com" rel="noopener">hoodiyalko@gmail.com</a>
      </div>
      <br>
      <p><strong>{{ $t('ContactsDescriptionOne') }}<br> {{ $t('ContactsDescriptionTwo') }}</strong></p>
      <br>
      <p>{{ $t('ContactsSubscribe') }}</p>
      <p><a target="_blank" href="https://www.facebook.com/hoodiyalko/" rel="noopener">facebook.com/hoodiyalko</a></p>
      <p><a target="_blank" href="https://www.instagram.com/hoodiyalko/" rel="noopener">instagram.com/hoodiyalko</a></p>
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
  padding: 16px 16px 40px 16px;
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
