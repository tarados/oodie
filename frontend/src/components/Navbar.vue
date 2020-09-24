<template>
  <div class="navbar">
    <div class="container-nav">
      <div class="nav-header">
        <div class="contact-info">
          <router-link to="#" class="contact-phone">
            <img src="../assets/phone-receiver.svg"/>
            <p>+380507204066</p>
          </router-link>
        </div>
        <div class="card-hamburger">
          <div class="card" v-show="this.$store.state.productsStore.basketVisible">
            <router-link :to="{name: 'Card'}">
              <img src="../assets/cart.svg">
            </router-link>
            <span
                class="item-basket"
                v-show="this.$store.state.productsStore.cardProducts.length > 0"
            >{{ this.$store.state.productsStore.cardProducts.length }}
            </span>
          </div>
          <div class="item hamburger"></div>
          <Hamburger/>
        </div>
      </div>
      <Logo/>
      <div class="linkList">
        <div class="linkList-item">
          <router-link :to="{name: 'Home'}"
          >
            <p>главная</p>
          </router-link>
        </div>
        <div class="linkList-item">
          <router-link
              :to="{name: 'About'}"
          >
            <p>о нас</p>
          </router-link>
        </div>
        <div class="linkList-item"
             @mouseover="mouseover"
             @mouseleave="mouseleave"
        >
          <router-link
              :to="{name: 'Brands'}"
          >
            <p>бренды друзья</p>
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
                  v-show="item.slug !== 'hoodiyalko'"
              >
                <router-link :to="{name: 'Brand', params: {slug: item.slug}}">{{ item.title }}</router-link>
              </div>
            </div>
          </transition>
        </div>
        <div class="linkList-item">
          <router-link
              :to="{name: 'Contacts'}"
          >
            <p>контакты</p>
          </router-link>
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
    this.$store.dispatch('changeVisibleBasket');
    console.log(this.$store.state.productsStore.basketVisible);
  }
}

</script>

<style scoped>
.navbar {
  border-bottom: 2px solid #9a9a9a;
}

.container-nav {
  height: 20.58vmax;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: flex-start;
}

.nav-header {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  align-items: center;
  width: 100%;
  height: 7.5vmin;
  background-color: #c7d9d8;
}

.contact-info {
 margin-left: 2vmin;
}

.contact-info img {
  width: 3vmin;
}

.contact-phone {
  text-decoration: none;
  cursor: pointer;
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  margin: 0 1rem;
}

.contact-phone p {
  color: black;
  margin: 1vmin;
}

.card-hamburger {
  margin-right: 4vmin;
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
  margin-bottom: 7vmin;
  align-self: center;
  display: flex;
  align-items: center;
  justify-content: center;
}

.linkList .linkList-item {
  padding: 0 10.1vmin;
  position: relative;
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
  align-items: center;
}

.card span {
  font-size: 1.1em;
  margin-left: 2vmin;
}

.card a img {
  width: 4.5vmin;
}


/*media queries*************************************************************************************/

@media screen and (max-width: 1024px) {
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

  .card-hamburger {
    margin-left: 20%;
  }

  .card-hamburger span {
    font-size: 1.7rem;
    margin: 0;
  }
}

@media screen and (max-width: 540px) {
  .nav-header {
    justify-content: normal;
  }

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
    margin-left: 53%;
  }

  .card-hamburger span {
    font-size: 1.7rem;
    margin: 0;
  }
}

@media screen and (max-width: 450px) {
  .nav-header {
    justify-content: normal;
  }

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
    margin-left: 39%;
  }

  .card-hamburger span {
    font-size: 1.7rem;
    margin: 0;
  }
}

@media screen and (max-width: 375px) {
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
    margin-left: 33%;
  }

  .card-hamburger span {
    font-size: 1.7rem;
    margin: 0;
  }
}

@media screen and (max-width: 360px) {
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
    margin-left: 30%;
  }

  .card-hamburger span {
    font-size: 1.7rem;
    margin: 0;
  }
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
    margin-left: 20%;
  }

  .card-hamburger span {
    font-size: 1.7rem;
    margin: 0;
  }
}

@media screen and (max-width: 280px) {
  .nav-header {
    justify-content: flex-start;
  }

  .card-hamburger {
    margin-left: 12%;
  }

  .card {
    margin-right: 0;
  }

  .card-hamburger span {
    font-size: 1.7rem;
    margin: 0;
  }
}
</style>
