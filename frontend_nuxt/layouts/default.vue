<template>
  <div class="default">
    <Navbar/>
    <nuxt/>
    <Footer/>
  </div>
</template>

<script>

export default {
  name: "default"
}
</script>

<style scoped>
.default {
  position: relative;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  overflow-x: hidden;
}

</style>
