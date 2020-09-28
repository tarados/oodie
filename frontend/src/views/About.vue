<template>
  <div class="wrapper">
    <div class="content-about">
      <h1>Есть вопросы?</h1>
      <h2>Мы будем рады получить твое сообщение:</h2>
      <div class="messengers">
        <div class="phone">
          <img src="../assets/phone-receiver.svg"/>
          <router-link class="link" to="#">
            <p>+380507204066</p>
          </router-link>
        </div>
        <div class="mail">
          <img src="../assets/email.svg">
          <p>hoodiyalko@gmail.com</p>
        </div>
        <div class="icons-messengers">
          <img src="../assets/media.png">
          <img src="../assets/messenger.png">
          <img src="../assets/phone.png">
        </div>
      </div>
      <h2>Подписывайся на наши страницы:</h2>
      <p>facebook.com/hoodiyalko/</p>
      <p>instagram.com/hoodiyalko/</p>
      <p>tiktok.com/@hoodiyalko/</p>
      <h2>Возможен самовывоз возле м.Контрактовая площадь по предварительной договоренности.</h2>
    </div>
  </div>
</template>

<script>
export default {
  name: "About"
}
</script>

<style scoped>
.wrapper {
  margin: 0 auto;
  max-width: 1200px;
}

.content-about {
  margin: 6vmin;
  display: grid;
  grid-template: repeat(8, auto) / 1fr;
  grid-row-gap: 3vmin;
}

.messengers {
  display: grid;
  grid-template: repeat(2, auto) / repeat(2, 1fr);
  grid-template-areas:
      "phone icons"
      "mail mail";
}

.phone {
  grid-area: phone;
  display: flex;
  flex-wrap: wrap;
  align-items: center;
}

.phone p,
.mail p {
  margin: 0 3%;
}

.phone .link {
  text-decoration: none;
  color: black;
}

.icons-messengers {
  grid-area: icons;
  display: flex;
  flex-wrap: wrap;
  align-items: center;
}

.mail {
  grid-area: mail;
  display: flex;
  flex-wrap: wrap;
  align-items: center;
}

.messengers img {
  width: 6vmin;
}

h1 {
  font-size: calc(18px + 14 * (100vw / 1600));
}

h2 {
  font-size: calc(14px + 10 * (100vw / 1600));
}

p {
  font-size: calc(12px + 12 * (100vw / 1600));
}

.test {
  font-size: 18px;
}

@media screen and (max-width: 320px) {
  h1 {
    font-size: calc(18px + (14 + 14 * 0.7) * ((100vw - 320px) / 1600));
  }

  h2 {
    font-size: calc(14px + (10 + 10 * 0.7) * ((100vw - 320px) / 1600));
  }

  p {
    font-size: calc(12px + (12 + 12 * 0.7) * ((100vw - 320px) / 1600));
  }
}
</style>