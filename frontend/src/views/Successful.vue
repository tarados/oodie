<template>
  <div class="container">
    <div class="orderSuccessful">
      <p>Ваша заявка принята! Спасибо за покупку!</p>
      <button @click="backToMain">Вернуться на главную страницу</button>
    </div>
    <Logo />
  </div>

</template>

<script>
    import Logo from '../components/Logo'

    export default {
        name: "Successful",
        components: {
            Logo
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
    /*font-style: italic;*/
  }

  .current-font {
    font-family: "Roboto", fantasy;
    color: blue;
    font-size: 25px;
    /*font-weight: 600;*/
  }

  .current-font2 {
    font-family: "montreal-serialbold", sans-serif;
    font-size: 25px;
    /*font-weight: 600;*/
  }
</style>