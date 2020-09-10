<template>
  <div class="navbar">
    <div class="container-nav">
      <div class="nav-header">
        <div class="contact-info">
          <div class="contact-phone">
            <img src="../assets/phone.jpg"/>
            <p>+380507204066</p>
          </div>
          <div class="contact-email">
            <p>hoodiyalko@gmail.com</p>
          </div>
        </div>
        <div class="card-hamburger">
          <div class="card" v-show="visibleCard">
            <span
                class="item-basket"
                v-show="this.$store.state.productsStore.cardProducts.length > 0"
            >{{this.$store.state.productsStore.cardProducts.length}}
            </span>
            <router-link :to="{name: 'Card'}">
              <img src="../assets/basket.png">
            </router-link>
          </div>
          <div class="item hamburger"></div>
          <Hamburger/>
        </div>
      </div>
      <div class="logo">
        <Logo/>
      </div>
      <div class="linkList">
        <div class="linkList-item">
          <router-link :to="{name: 'Home'}"
          >
            главная
          </router-link>
        </div>
        <div class="linkList-item">
          <router-link :to="{name: 'Brands'}"
          >
            о нас
          </router-link>
        </div>
        <div class="linkList-item"
             @mouseover="mouseover"
             @mouseleave="mouseleave"
        >
          <router-link
              :to="{name: 'Brands'}"
          >
            бренды друзья
          </router-link>
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none"
               stroke-linecap="round" stroke-linejoin="round">
            <path stroke="none" d="M0 0h24v24H0z"/>
            <path d="M9 14l3 3l3 -3"/>
          </svg>
          <transition name="fade" appear>
            <div class="sub-menu" v-if="isOpen">
              <div
                  class="menu-item"
                  v-for="(item, index) in this.$store.getters.allCategories" :key="index"
                  v-show="item.slug !== 'oodie'"
              >
                <router-link :to="{name: 'Brand', params: {slug: item.slug}}">{{ item.title }}</router-link>
              </div>
            </div>
          </transition>
        </div>
        <div class="linkList-item">
          <router-link :to="{name: 'Brands'}">контакты</router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Hamburger from "./Hamburger";
import Logo from "./Logo";

export default {
  name: "NavBar",
  props: {
    visibleCard: Boolean,
  },
  components: {
    Hamburger,
    Logo
  },
  data() {
    return {
      selected: "",
      isOpen: false,
      options: [],
      hamburger: false,
    };
  },
  computed: {},
  methods: {
    mouseover: function () {
      this.isOpen = true
    },
    mouseleave: function () {
      this.isOpen = false
    }
  },
  mounted() {

  }
}

</script>

<style scoped>
.navbar {
  border-bottom: 1px solid grey;
}

.container-nav {
  height: 24.57rem;
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
  height: 3.66rem;
  background-color: #c7d9d8;
}

.contact-info {
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
  align-items: center;
  justify-content: flex-end;
}

.logo {
  width: 100%;
}

span {
  text-transform: uppercase;
}

.linkList {
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
}

.linkList .linkList-item {
  padding: 10px 20px;
  position: relative;
  text-align: center;
  border-bottom: 3px solid transparent;
  display: flex;
  transition: 0.4s;
}

.linkList .linkList-item a:active,
.linkList .linkList-item a:hover {
  color: #c7d9d8;
}

.linkList .linkList-item a {
  color: #3d4246;
  text-transform: uppercase;
  text-decoration: none;
}

.linkList .linkList-item svg {
  width: 18px;
  margin-left: 10px;
}

.linkList-item svg:hover {
  fill: #c7d9d8;
  transition: all .5s ease-out;
}

.linkList-item .sub-menu {
  position: absolute;
  background-color: #c7d9d8;
  top: calc(100% + 0.5rem);
  /*transform: translateX(-50%);*/
  width: 80%;
  display: flex;
  flex-direction: column;
  padding: 3%;
}

.linkList-item .sub-menu .menu-item {
  margin: 3%;
}

.linkList-item .sub-menu .menu-item:hover {
  opacity: 0.5;
}

.linkList-item .sub-menu .menu-item a {
  color: white;
}

.fade-enter-active,
.fade-leave-active {
  transition: all .2s ease-out;
}

.fade-enter,
.fade-leave-to {
  opacity: 0.8;
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
  margin-right: 45%;
  align-items: center;
}

.card span {
  font-size: 2rem;
}

.card img {
  color: #7b786e;
}


/*media queries*************************************************************************************/

@media screen and (max-width: 1024px) {
  .linkList {
    width: auto;
  }

  .container-nav {
    height: 13.7rem;
  }
}

@media screen and (max-width: 750px) {
  .container-nav {
    height: 23.3rem;
  }

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
}

@media screen and (max-width: 450px) {
  .logo img {
    width: 10vmax;
  }

  .container-nav {
    height: 11rem;
  }

  .nav-header {
    justify-content: flex-start;
  }
}

@media screen and (max-width: 375px) {
}

@media screen and (max-width: 360px) {
}

@media screen and (max-width: 325px) {
  p,
  .card span {
    font-size: 0.55rem;
  }

  img {
    width: 10vmax;
  }

  .container-nav {
    height: 10rem;
  }

  .card {
    margin: 0;
  }

  .card img {
    width: 1.5rem;
  }

  .card-hamburger {
    margin-left: 25%;
  }
}

@media screen and (max-width: 280px) {
  .nav-header {
    justify-content: flex-start;
  }

  .card-hamburger {
    justify-content: space-around;
  }

  .card {
   margin-right: 0;
  }
}
</style>
