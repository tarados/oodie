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
      <div class="navbar_header__lang">
        <Dropdown/>
      </div>
      <div class="navbar_header__basket">
        <img src="~/assets/img/cart.svg">
      </div>
    </div>
    <div class="navbar_logo">
      <img src="~/assets/img/logo2.png">
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
  name: "Navbar",
  data: () => ({
    arrayOfObjects: ['ru', 'ua'],
    object: {
      name: 'Object Name',
    }
  }),
}
</script>

<style scoped>
.navbar {
  width: 1660px;
  margin: 0 auto;
  position: relative;
}

.navbar_header {
  width: 95%;
  margin-left: 3rem;
  height: 4rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
  background-color: #f5f5f5;
  font-size: calc(14px + 2 * ((100vw - 320px) / 1518));
}

.navbar_header__hamburg {
  width: 50px;
  height: 40px;
  display: none;
}

.navbar_header__phone {
  display: flex;
  flex-wrap: nowrap;
  align-items: center;
  justify-content: space-between;
}

.navbar_header__phone img {
  height: 1rem;
}

.navbar_header__phone a {
  font-size: 16px;
  margin-left: 5px;
  text-decoration: none;
  color: #000000;
}

.navbar_header__basket {

}

.navbar_header__basket img {
  height: 1.5rem;
}

.navbar_header__lang {
  width: 5rem;
}

.navbar_logo {
  text-align: center;
  margin-top: 2rem;
  margin-bottom: 3rem;

}

.navbar_logo img {
  width: 80%;
  max-width: 400px;
}

.navbar_items {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
}

.navbar_items .navbar-item {
  padding: 0 calc(3vw + 12 * (100vw / 1838));
  position: relative;
  display: flex;
  transition: 0.4s;
}

.navbar_items .navbar-item a {
  text-decoration: none;
  text-transform: uppercase;
}
</style>
