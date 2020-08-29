<template>
  <div class="navbar">
    <div class="container-nav ">
      <div class="nav-header">
        <div class="contact-info">
          <div class="contact-phone">
            <img src="../assets/phone.jpg">
            <p>+380507204066</p>
          </div>
          <div class="contact-email">
            <p>hoodiyalko@gmail.com</p>
          </div>
        </div>
        <div class="card-hamburger">
          <div class="card" v-show="visibleCard">
            <router-link :to="{name: 'Card'}">
              <svg aria-hidden="true" focusable="false" role="presentation" class="icon icon-cart"
                   viewBox="0 0 37 40">
                <path
                    d="M36.5 34.8L33.3 8h-5.9C26.7 3.9 23 .8 18.5.8S10.3 3.9 9.6 8H3.7L.5 34.8c-.2 1.5.4 2.4.9 3 .5.5 1.4 1.2 3.1 1.2h28c1.3 0 2.4-.4 3.1-1.3.7-.7 1-1.8.9-2.9zm-18-30c2.2 0 4.1 1.4 4.7 3.2h-9.5c.7-1.9 2.6-3.2 4.8-3.2zM4.5 35l2.8-23h2.2v3c0 1.1.9 2 2 2s2-.9 2-2v-3h10v3c0 1.1.9 2 2 2s2-.9 2-2v-3h2.2l2.8 23h-28z"></path>
              </svg>
            </router-link>
            <div class="circle"
                 v-show="this.$store.state.productsStore.cardProducts.length > 0"
                 v-text="this.$store.state.productsStore.cardProducts.length"
            >
            </div>
          </div>
          <div class="item hamburger"></div>
          <Hamburger/>
        </div>
      </div>
      <div class="logo">
        <Logo/>
      </div>
      <div class="link">
        <div class="linkList">
          <a href="/">
            <span>главная</span>
          </a>
          <router-link
              :to="{name: 'Brands'}"
          >
            <span>о нас</span>
          </router-link>
          <select v-model="selected">
            <option disabled value="">
              <span>бренды друзья</span>
            </option>
            <option v-for="(option, index) in options" :key="index">
              {{option}}
            </option>
          </select>
          <router-link
              :to="{name: 'Brands'}"
          >
            <span>контакты</span>
          </router-link>
        </div>
      </div>
    </div>

  </div>
</template>

<script>
import Hamburger from "./Hamburger";
import Logo from "./Logo"

export default {
  name: 'NavBar',
  props: {
    visibleCard: Boolean
  },
  components: {
    Hamburger,
    Logo
  },
  data() {
    return {
      selected: '',
      options: ['a', 's', 'd'],
      hamburger: false
    }
  },
  methods: {},
  mounted() {

  }
}
</script>

<style scoped>
.navbar {
  border-bottom: 1px solid grey;
}

.container-nav {
  height: 33rem;
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  align-items: flex-start;
}

.nav-header {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  align-items: center;
  width: 100%;
  height: 5rem;
  background-color: #c7d9d8;
}

.contact-info {
  margin: 1%;
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-between;
}

.contact-info img {
  width: 2rem;
}

.contact-phone {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  margin: 0 1rem;
}

.contact-phone p {
  margin: 0 0.35rem;
}

.card-hamburger {
  display: flex;
  flex-wrap: wrap;
  width: 45%;
  align-items: center;
  justify-content: flex-end;
}

.logo {
  width: 100%;
}

span {
  text-transform: uppercase;
}

.link {
  height: 15%;
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: center;
  flex: auto;
}

.link a {
  margin: 25px;
  color: #3d4246;
  text-decoration: none;
}

.link .linkList select span {
  text-transform: uppercase;
}
select {
  border: none;
  background-color: white;
  text-transform: uppercase;
  font-size: 1.1875rem;
  color: rgb(61, 66, 70);
}

.icon {
  display: inline-block;
  width: 20px;
  height: 30px;
  vertical-align: middle;
  fill: currentColor;
}

.hamburger {
  display: none;
}

.card {
  display: flex;
  margin-right: 2%;
}

.card svg {
  color: #7b786e;
}

.circle {
  width: 18px;
  height: 18px;
  background: red;
  -moz-border-radius: 50px;
  -webkit-border-radius: 50px;
  border-radius: 50px;
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  align-self: center;
  margin-bottom: 23%;
  margin-left: -5%;
  align-items: center;
  color: white;
  position: relative;
  font-size: 12px;
}

/*media queries*************************************************************************************/
@media screen and (max-width: 750px) {
  .contact-info {
    flex-flow: column;
  }

  .contact-info img {
    width: 0.9rem;
  }

  p {
    font-size: 0.71rem;
  }

  .hamburger {
    display: inline;
    width: 15px;
    height: 50px;
    opacity: 0;
    margin-left: 1vw;
  }

  .linkList {
    display: none;
  }

  .card {
    margin-right: 0;
    margin-left: 50%;
  }
}

@media screen and (max-width: 450px) {
  .logo img {
    width: 10vmax;
  }

  .card {
    margin-left: 40%;
  }
}

@media screen and (max-width: 375px) {
  .card {
    margin-left: 35%;
  }
}


@media screen and (max-width: 360px) {
  .card {
    margin-left: 30%;
  }
}

@media screen and (max-width: 325px) {
  p {
    font-size: 0.65rem;
  }

  img {
    width: 10vmax;
  }

  @media screen and (max-width: 280px) {
    .card {
      margin-left: 20%;
    }
  }
}

</style>
