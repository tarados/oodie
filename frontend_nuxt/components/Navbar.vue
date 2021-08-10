<template>
  <div class="navbar">
    <div class="navbar_header">
      <div class="navbar_header__hamburg"></div>
      <div class="navbar_header__phone">
        <img src="~/assets/img/phone-receiver.svg" alt=""/>
        <a href="#" class="phone">
          <span>+380507204066</span>
        </a>
      </div>
      <div class="navbar_header__basket">
<!--        <flag iso="it" />-->
      </div>
    </div>
    <div class="navbar_logo">

    </div>
    <div class="navbar_items">
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
  </div>
</template>

<script>
export default {
  name: "Navbar"
}
</script>

<style scoped>
.navbar {
  width: 100%;
  position: relative;
  display: flex;
  flex-direction: column;
}

.navbar_header {
  padding: 15px;
  height: 60px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  background-color: #f5f5f5;
  font-size: calc(14px + 2 * ((100vw - 320px) / 1518));
  border: 1px solid black;
}

.navbar_header__hamburg {
  width: 50px;
  height: 40px;
  border: 1px solid black;
  background-color: yellow;
  display: none;
}

.navbar_header__phone {
  display: flex;
  flex-wrap: nowrap;
  align-items: center;
  justify-content: space-between;
}

.navbar_header__phone img {
  height: 16px;
}

.navbar_header__phone a {
  font-size: 16px;
  margin-left: 5px;
  text-decoration: none;
  color: #000000;
}

.navbar_header__basket {
  border: 1px solid black;
  background-color: green;
}

.navbar_logo {
}

.navbar_items {
}
</style>
