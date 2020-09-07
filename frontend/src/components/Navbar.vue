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
            <router-link :to="{name: 'Card'}">
              <svg
                  aria-hidden="true"
                  focusable="false"
                  role="presentation"
                  class="icon icon-cart"
                  viewBox="0 0 37 40"
              >
                <path
                    d="M36.5 34.8L33.3 8h-5.9C26.7 3.9 23 .8 18.5.8S10.3 3.9 9.6 8H3.7L.5 34.8c-.2 1.5.4 2.4.9 3 .5.5 1.4 1.2 3.1 1.2h28c1.3 0 2.4-.4 3.1-1.3.7-.7 1-1.8.9-2.9zm-18-30c2.2 0 4.1 1.4 4.7 3.2h-9.5c.7-1.9 2.6-3.2 4.8-3.2zM4.5 35l2.8-23h2.2v3c0 1.1.9 2 2 2s2-.9 2-2v-3h10v3c0 1.1.9 2 2 2s2-.9 2-2v-3h2.2l2.8 23h-28z"
                />
              </svg>
            </router-link>
            <div
                class="circle"
                v-show="this.$store.state.productsStore.cardProducts.length > 0"
                v-text="this.$store.state.productsStore.cardProducts.length"
            ></div>
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
  /*transition: all .5s ease-out;*/
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
  p {
    font-size: 0.55rem;
  }

  img {
    width: 10vmax;
  }

  .container-nav {
    height: 10rem;
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
    margin-left: 2rem;
  }
}
</style>
