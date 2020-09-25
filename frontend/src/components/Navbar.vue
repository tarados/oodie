<template>
  <div class="navbar">
    <div class="container-nav">
      <div class="nav-header">
        <div class="hamburg">
          <Hamburger/>
        </div>
        <div class="phone">
          <router-link to="#">
            <img src="../assets/phone-receiver.svg"/>
            <p>+380507204066</p>
          </router-link>
        </div>
        <div class="basket" v-show="this.$store.state.productsStore.basketVisible">
          <router-link :to="{name: 'Card'}">
            <img src="../assets/cart.svg">
            <span
                v-show="this.$store.state.productsStore.cardProducts.length > 0"
            >{{ this.$store.state.productsStore.cardProducts.length }}
            </span>
          </router-link>
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
                <router-link
                    :to="{name: 'Brand', params: {slug: item.slug}}"
                >
                  <p>{{ item.title }}</p>
                </router-link>
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
  height: calc(20vw + 29 * (100vw / 1838));
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: flex-start;
}

.nav-header {
  width: 100%;
  display: grid;
  grid-template-columns: 1fr 1fr;
  grid-template-rows: calc(3vw + 4 * (100vw / 1838));
  grid-template-areas: "phone basket";
  background-color: #c7d9d8;
  align-items: center;
  align-content: center;
  justify-items: center;
}

.hamburg {
  grid-area: hamburg;
}

.phone {
  grid-area: phone;
  justify-self: flex-start;
  margin: 0 2vmin;
}

.basket {
  grid-area: basket;
  justify-self: flex-end;
  margin: 0 5vmin;
}

.phone a,
.basket a {
  display: flex;
  flex-wrap: wrap;
  justify-content: flex-end;
  align-items: center;
  text-decoration: none;
  cursor: pointer;
  color: black;
}

.phone a img,
.basket a img {
  width: 3vmin;
  margin: 0 1.5vmin;
}

.phone a p,
.basket a span {
  font-size: calc(11px + 8 * (100vw / 1580));
}

span {
  text-transform: uppercase;
}

.linkList {
  margin-bottom: 7vmin;
  align-self: center;
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: center;
}

.linkList .linkList-item {
  padding: 0 calc(3vw + 12 * (100vw / 1838));
  position: relative;
  /*border-bottom: 3px solid transparent;*/
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
  width: 80%;
  display: flex;
  align-items: center;
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

/*media queries*************************************************************************************/
@media screen and (max-width: 1600px) {
  .container-nav {
    height: calc(20vw + 22 * (100vw / 1600));
  }
}

@media screen and (max-width: 1200px) {
  .linkList .linkList-item {
    padding: 0 calc(1vw + 12 * (100vw / 1200));
  }
}

@media screen and (max-width: 750px) {
  .nav-header {
    grid-template-columns: 1fr 2fr 1fr;
    grid-template-areas: "hamburg phone basket";
    justify-items: center;
  }

  .nav-header {
    height: calc(59px + 7 * (100vw / 1580));
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

@media screen and (max-width: 325px) {
  .phone a p,
  .basket a span {
    font-size: calc(14px + 6 * (100vw / 1580));
  }
}

</style>
