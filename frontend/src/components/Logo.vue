<template>
  <div class="wrapper-logo">
    <img src="../assets/logo2.png">
  </div>
</template>

<script>
export default {
  name: "logo",
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

}

img {
  width: 80%;
  max-width: 400px;
  margin: 0 auto;
}

</style>
