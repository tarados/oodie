<template>
  <div>
    <h2> ты с нами в instagram?</h2>
    <div class="hello-instagram"></div>
  </div>
</template>

<script>
export default {
  name: "Instagram"
}
</script>

<style scoped>
.hello-instagram {
  height: 14rem;
  margin-bottom: 5%;
  background-image: url("../assets/insta.jpg");
  background-repeat: no-repeat;
  background-size: cover;
}

h2 {
  margin-top: 20px;
  text-align: center;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  font-weight: 100;
}
</style>