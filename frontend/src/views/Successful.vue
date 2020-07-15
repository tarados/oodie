<template>
  <div class="container">
    <div class="orderSuccessful">
      <p>Ваша заявка принята! Спасибо за покупку!</p>
      <button @click="backToMain">Вернуться на главную страницу</button>
    </div>
    <div class="current-font">
      We use ultra soft flannel fleece paired with warm sherpa fleece so you don't have to worry about the cold. Some think it's a blanket. Some think it's a hoodie. Either way we know you're going to be cosiest in The Oodie.* Now the top rated wearable blanket on Facebook and Product
      Ваша заявка принята! Спасибо за покупку!
    </div>
    <div class="current-font2">
      Ваша заявка принята! Спасибо за покупку!
      We use ultra soft flannel fleece paired with warm sherpa fleece so you don't have to worry about the cold. Some think it's a blanket. Some think it's a hoodie. Either way we know you're going to be cosiest in The Oodie.* Now the top rated wearable blanket on Facebook and Product
    </div>
  </div>

</template>

<script>
export default {
  name: "Successful",
  methods: {
    backToMain() {
      this.$router.push('/');
    }
  }
}
</script>

<style scoped>

.orderSuccessful {
  text-align: center;
  margin: 20px 0;
  padding: 15px;
  border: 1px solid green;
  background-color: #f2f2f2;
  border-radius: 3px;
}

p {
  font-size: 25px;
  font-weight: 600;
  /*font-style: italic;*/
}

.current-font {
  font-family: "Work Sans", "HelveticaNeue", "Helvetica Neue", sans-serif;
  font-size: 25px;
  /*font-weight: 600;*/
}

.current-font2 {
  font-family: "montreal-serialbold", sans-serif;
  font-size: 25px;
  /*font-weight: 600;*/
}
</style>