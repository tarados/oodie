<template>
  <div class="wrapper-logo" @click="toMain">
    <img src="../assets/logo2.png">
  </div>
</template>

<script>
export default {
  name: "logo",
  methods: {
    toMain() {
      this.$router.push({name: 'Home'})
    }
  }
};
</script>

<style scoped>
.wrapper-logo {
  display: flex;
  justify-content: center;
  align-items: center;
  align-self: center;
  margin-top: 50px;
  margin-bottom: 40px;
  cursor: pointer;

}

img {
  width: 80%;
  max-width: 400px;
  margin: 0 auto;
}

</style>
