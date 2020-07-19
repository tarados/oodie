<template>
  <div class="container">
    <div class="orderSuccessful">
      <p>Ваша заявка принята! Спасибо за покупку!</p>
      <button @click="backToMain">Вернуться на главную страницу</button>
    </div>
    <div>
      <span class="red">Red</span>
    </div>
    <div>
      <span class="green">Green</span>
    </div>
    <div>
      <span class="blue">Blue</span>
    </div>
  </div>

</template>

<script>
    // import Logo from '../components/Logo'

    export default {
        name: "Successful",
        components: {
            // Logo
        },
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
  }

  .red, .green, .blue {
    position: absolute;
    width: 50px;
    height: 50px;
  }
  .red {
    background: red;
    z-index: 1;
  }
  .green {
    background: green;
  }
  .blue {
    background: blue;
  }
</style>