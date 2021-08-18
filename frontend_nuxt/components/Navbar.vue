<template>
  <div class="navbar">
    <div class="navbar_header">
      <div class="navbar_header__hamburg">
        <Hamburger/>
      </div>
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
          {{ $t('MenuHome') }}
        </nuxt-link>
      </div>
      <div class="navbar-item">
        <nuxt-link to="/products">
          {{ $t('ProductBrand') }}
        </nuxt-link>
      </div>
      <div class="navbar-item">
        <nuxt-link to="/about">
          {{ $t('MenuAboutUs') }}
        </nuxt-link>
      </div>
      <div class="navbar-item">
        <nuxt-link to="/Contacts">{{ $t('MenuContacts') }}</nuxt-link>
      </div>
    </div>
  </div>
</template>

<script>


export default {
  name: "Navbar",
  mounted() {
    console.log('navbar', this.$i18n.locale)
  }
}
</script>

<style scoped>
.navbar {
  width: 100%;
  margin: 0 auto 20px;
  position: relative;
}

.navbar_header {
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
  padding-left: calc(60 * ((100vw - 500px) / 1837));
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
  padding-right: calc(16px + 32 * ((100vw - 375px) / 1837));
}

.navbar_header__basket img {
  height: 1.5rem;
}

.navbar_header__lang {
  position: relative;
}

.navbar_logo {
  text-align: center;
  margin-top: 2rem;
  margin-bottom: 3rem;
  max-height: 3rem;

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

@media screen and (max-width: 750px) {
  .navbar_items {
    display: none;
  }
  .navbar_header__hamburg {
    display: inline;
  }
  .navbar_header__phone {
    padding-left: 0;
    padding-right: calc(0.7 * 60 * ((100vw + 375px) / 1838));
  }

}
</style>
