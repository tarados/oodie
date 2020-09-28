<template>
  <div class="wrapper">
    <div class="content-about">
      <h1>Есть вопросы?</h1>
      <h2>Мы будем рады получить твое сообщение:</h2>
      <p>jhkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk</p>
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
  grid-template: repeat(8, 1fr) / 1fr;
  grid-row-gap: 1vmin;
}

h1 {
  font-size: calc(16px + 16 * (100vw / 1600));
}

h2 {
  font-size: calc(12px + 12 * (100vw / 1600));
}

p {
  font-size: calc(10px + 14 * (100vw / 1600));
}

.test {
  font-size: 18px;
}

@media screen and (max-width: 320px) {
  h1 {
    font-size: calc(16px + (16 + 16 * 0.7) * ((100vw - 320px) / 1600));
  }

  h2 {
    font-size: calc(12px + (12 + 12 * 0.7) * ((100vw - 320px) / 1600));
  }

  p {
    font-size: calc(10px + (14 + 14 * 0.7) * ((100vw - 320px) / 1600));
  }
}
</style>