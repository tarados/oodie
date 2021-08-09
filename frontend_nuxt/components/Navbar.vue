<template>
  <div class="navbar">
    <div class="navbar-item">
      <nuxt-link to="/">
        Home
      </nuxt-link>
    </div>
    <div class="navbar-item">
      <nuxt-link to="/products">
        Products
      </nuxt-link>
    </div>
    <div class="navbar-item">
      <nuxt-link to="/about">
        About
      </nuxt-link>
    </div>
    <div class="navbar-item">
      <nuxt-link to="/Contacts">Contacts</nuxt-link>
    </div>
  </div>
</template>

<script>
export default {
  name: "Navbar"
}
</script>

<style scoped>
.navbar {
  background-color: #dedada;
  height: 4rem;
  display: flex;
  flex-wrap: nowrap;
  justify-content: space-around;
  align-items: center;
}
</style>
