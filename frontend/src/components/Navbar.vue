<template>
  <div class="navbar">
    <div class="container-nav">
      <div class="hamburg">
        <Hamburger/>
      </div>
      <div class="nav-header">
        <a href="tel:+380507204066" class="phone"><img src="../assets/phone-receiver.svg"/>+380507204066</a>
        <div class="nav-header__lang_basket">
          <Dropdown/>
          <div class="basket" v-if="basketVisible">
            <router-link :to="{name: 'Cart'}">
              <img src="../assets/cart.svg">
              <span
                  v-show="cartProducts.length > 0"
              >{{ cartProducts.length }}
            </span>
            </router-link>
          </div>
        </div>
      </div>
    </div>
    <Logo/>
    <div class="linkList">
      <div class="linkList-item"
           v-for="(item, index) in links" :key="item.route">
        <router-link :to="item.route">
          <p>{{ item.title | localize }}</p>
        </router-link>
        <div class="linkList-item__brands" v-if="links[index].nestedRoutes"
             @mouseover="mouseover"
             @mouseleave="mouseleave"
        >
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor"
               fill="none"
               stroke-linecap="round" stroke-linejoin="round">
            <path stroke="none" d="M0 0h24v24H0z"/>
            <path d="M9 14l3 3l3 -3"/>
          </svg>
          <div
              class="linkList-item__sub-menu"
              v-if="isOpen"
          >
            <div
                class="menu-item"
                v-for="category in categoriesList" :key="category.id"
                v-show="category.slug !== 'hoodiyalko'"
            >
              <router-link
                  :to="{name: 'Brand', params: {slug: category.slug}}"
              >
                <p>{{ category.title }}</p>
              </router-link>
            </div>
          </div>
        </div>
      </div>
    </div>

  </div>
</template>

<script>
import Hamburger from "@/components/Hamburger";
import Dropdown from "@/components/LangSelection";
import Logo from "./Logo";
import links from '@/js/linkList'
import {mapState} from 'vuex'

export default {
  name: "NavBar",
  components: {
    Hamburger,
    Dropdown,
    Logo
  },
  data() {
    return {
      selected: "",
      isOpen: false,
      isDropdown: false,
      basketVisible: true,
      options: [],
      links: [],
      categories: [],
      hamburger: false,
    };
  },
  computed: {
    ...mapState(["categoriesList", "cartProducts"]),
    getBasket() {
      if (this.$router.currentRoute.name === 'Cart') {
        return false;
      } else {
        return true;
      }
    }
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
      this.links = links();
    }
  },
  watch: {
    $route(to) {
      if (to.name === 'Cart' || to.name === 'Checkout') {
        this.basketVisible = false;
      } else {
        this.basketVisible = true;
      }
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
  /*z-index: 2;*/
}

.container-nav {
  display:inline-block;
  width: 100%

}

.nav-header {
  padding: 15px;
  height: 60px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  background-color: var(--overlay-color);
  font-size: calc(14px + 2 * ((100vw - 320px) / 1518));
}

.hamburg {
  display: none;
}

.nav-header__lang_basket {
  display: flex;
  justify-content: space-between;
}

.phone {
  margin-left: 3rem;
  text-decoration: none;
  cursor: pointer;
  color: black;

}

.basket a {
  display: flex;
  justify-content: center;
  align-items: center;
  text-decoration: none;
  cursor: pointer;
  color: black;
}

.basket a span {
  font-size: calc(14px + 2 * ((100vw - 320px) / 1518));
}

.phone img {
  margin-right: 8px;
  height: 16px;
}

.basket a img {
  height: 1.5rem;
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

.linkList .linkList-item a.router-link-active {
  font-weight: bold;
}

.linkList .linkList-item a:hover,
.linkList .linkList-item p:hover {
  font-weight: bold;
}

.linkList .linkList-item a,
.linkList .linkList-item p {
  color: #3d4246;
  text-transform: uppercase;
  text-decoration: none;
}

.linkList .linkList-item p {
  cursor: pointer;
}

.linkList .linkList-item svg {
  width: 18px;
  height: 18px;
  margin-left: 10px;
}

.linkList-item svg:hover {
  fill: #c7d9d8;
  transition: all .5s ease-out;
}

.linkList-item .linkList-item__brands .linkList-item__sub-menu {
  position: absolute;
  background-color: var(--overlay-color);
  top: calc(100% + 0.5rem);
  left: 0;
  width: 80%;
  display: flex;
  align-items: center;
  flex-direction: column;
  padding-top: 3%;
}

.linkList-item .linkList-item__brands .linkList-item__sub-menu .menu-item {
  margin: 3%;
}

.linkList-item .linkList-item__brands .linkList-item__sub-menu .menu-item:hover {
  opacity: 0.5;
}

.linkList-item .linkList-item__brands .linkList-item__sub-menu .menu-item a {
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
    /*grid-template-columns: 3fr 2fr 1fr;*/
  }

  .phone {
    /*grid-column: 2 / 2;*/
  }

  .basket {
    /*position: absolute;*/
    /*top: 15px;*/
    /*right: 10px;*/
  }

  .hamburg {
    /*grid-column: 1 / 2;*/
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

@media screen and (max-width: 300px) {
  .nav-header {
    font-size: 10px;
  }
}
</style>
