<template>
  <div>
    <h1> ты с нами в instagram?</h1>
    <div class="hello-instagram">
      <img src="../assets/insta.jpg">
    </div>
  </div>
</template>

<script>
export default {
  name: "Instagram"
}
</script>

<style scoped>
.hello-instagram {
  margin-bottom: 5vmin;
 }

h1 {
  margin: 2vmin 0;
  text-align: center;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  font-weight: 100;
}

img {
  width: 100%;
}
</style>