<template>
  <div class="navbar">
    <div class="container-nav">
      <div class="nav-header">
        <div class="hamburg">
          <Hamburger/>
        </div>
        <div class="phone">
          <router-link to="#"><img src="../assets/phone-receiver.svg"/>+380507204066</router-link>
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
            <p>{{ links['1'] }}</p>
          </router-link>
        </div>
        <div class="linkList-item">
          <router-link
              :to="{name: 'About'}"
          >
            <p>{{ links['2'] }}</p>
          </router-link>
        </div>
        <div class="linkList-item"
             @mouseover="mouseover"
             @mouseleave="mouseleave"
        >
          <router-link
              :to="{name: 'Brands'}"
          >
            <p>{{ links['3'] }}</p>
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
            <p>{{ links['4'] }}</p>
          </router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Hamburger from "./Hamburger";
import Logo from "./Logo";
import linkList from '../js/linkList'

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
      links: {},
      hamburger: false,
    };
  },
  computed: {
  },
  methods: {
    clearTimer: function () {
      if (this.timer) clearTimeout(this.timer);
      this.timer = -1;
    },

    mouseover: function () {
      this.clearTimer();
      this.isOpen = true;
    },
    mouseleave: function () {
      this.clearTimer();

      this.timer = setTimeout(() => {
        this.isOpen = false;
      }, 500);

    },
    getLinkList() {
      this.links = linkList();
    }
  },
  mounted() {
    this.$store.dispatch('changeVisibleBasket');
    this.getLinkList();
  }
}

</script>

<style scoped>

.navbar {
  position: relative;
  z-index: 2;
}


.nav-header {
  width: 100%;
  padding: 15px;
  height: 60px;

  display: flex;
  flex-direction: row;
  background-color: var(--overlay-color);
}

.hamburg {
  display: none;
  flex:1 1 auto;
}

.phone {
  flex:1 1 auto;
  height: 30px;
  line-height: 30px;
  align-self: flex-start;
}

.basket {
  flex:1 1 auto;
  align-self: flex-end;
  line-height: 30px;
}

.phone a,
.basket a {
  display: flex;
  text-decoration: none;
  cursor: pointer;
  color: black;
}

.basket a {
  justify-content: flex-end;
}

.phone a img {
  margin-top: 4px;
  height: 20px;
}

.basket a img {
  height: 30px;
}

.basket a img {
}

.phone a p,
.basket a span {
  padding-left: 8px;
  font-size: 20px;
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
  display: flex;
  transition: 0.4s;
}

.linkList .linkList-item a:active,
.linkList .linkList-item a:hover {
  font-weight: bold;
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
  background-color: var(--overlay-color);
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
  color: black;
}

/*media queries*************************************************************************************/
@media screen and (max-width: 1200px) {
  .linkList .linkList-item {
    padding: 0 calc(1vw + 12 * (100vw / 1200));
  }
}

@media screen and (max-width: 750px) {
  .nav-header {
    display: block;
    text-align: center;
  }

  .phone {
    display: inline-block;
  }

  .basket {
    position: absolute;
    top: 15px;
    right: 10px;
  }

  .hamburg {
    position: absolute;
    top: 15px;
    left: 10px;
    display: block;
  }

  .hamburger {
    display: inline;
    width: 15px;
    height: 50px;
    opacity: 0;
  }

  .linkList {
    display: none;
  }
}
</style>
