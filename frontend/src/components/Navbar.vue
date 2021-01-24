<template>
  <div class="navbar">
    <div class="container-nav">
      <div class="nav-header">
        <div class="hamburg">
          <Hamburger/>
        </div>
        <div class="phone">
          <a href="tel:+380507204066"><img src="../assets/phone-receiver.svg"/>+380507204066</a>
        </div>
        <div class="langSelector"
             @mouseover="mouseoverLang"
             @mouseleave="mouseleaveLang"
        >
          <div class="langSelector_item">
            <flag :iso="selectedLanguageIcon"></flag>
            <span>{{selectedLanguage}}</span>
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none"
                 stroke-linecap="round" stroke-linejoin="round">
              <path stroke="none" d="M0 0h24v24H0z"/>
              <path d="M9 14l3 3l3 -3"/>
            </svg>
          </div>
          <transition name="fade" appear>
            <div class="sub-menu" v-if="isOpenLang">
              <div
                  class="menu-item lang"
                  v-for="(item, index) in langList" :key="index"
                  @click="getLocale(index)"
              >
                <flag :iso="item.slug"></flag>
                <p>{{ item.title }}</p>
              </div>
            </div>
          </transition>
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
          <router-link :to="{name: 'Home'}" exact
          >
            <p>{{ links['1'] | localize }}</p>
          </router-link>
        </div>
        <div class="linkList-item">
          <router-link
              :to="{name: 'About'}"
          >
            <p>{{ links['2'] | localize }}</p>
          </router-link>
        </div>
        <div class="linkList-item"
             @mouseover="mouseover"
             @mouseleave="mouseleave"
        >
          <router-link
              :to="{name: 'Brands'}"
          >
            <p>{{ links['3'] | localize  }}</p>
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
            <p>{{ links['4'] | localize }}</p>
          </router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Hamburger from "./Hamburger";
import Logo from "./Logo";
import links from '../js/linkList'
import {langList} from '../js/linkList'
import {mapGetters} from 'vuex'

export default {
  name: "NavBar",
  components: {
    Hamburger,
    Logo
  },
  data() {
    return {
      selected: "",
      selectedLanguageIcon: "",
      selectedLanguage: "",
      isOpen: false,
      isOpenLang: false,
      options: [],
      links: {},
      langList: [],
      hamburger: false,
    };
  },
  computed: {...mapGetters(["getLocales",])},
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
    mouseoverLang: function () {
      this.clearTimer();
      this.isOpenLang = true;
    },
    mouseleaveLang: function () {
      this.clearTimer();

      this.timer = setTimeout(() => {
        this.isOpenLang = false;
      }, 500);

    },
    getLinkList() {
      this.links = links();
      this.langList = langList();
      this.selectedLanguage = window.navigator.language.slice(0, 2);
      this.selectedLanguageIcon = window.navigator.language.slice(0, 2);
    },
    getLocale(index) {
      const locale = this.langList[index].name;
      this.$store.commit('setLocale', locale);
      this.selectedLanguageIcon = this.langList[index].slug;
      this.selectedLanguage = this.langList[index].title;
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
  padding: 15px;
  height: 60px;
  display: grid;
  grid-template-columns: 1fr 15fr 1fr 1fr;
  background-color: var(--overlay-color);
}

.hamburg {
  display: none;
}

.phone {
  height: 30px;
  line-height: 30px;
  grid-column: 1 / 3;
}

.langSelector {
  width: 70%;
  grid-column: 3 / 4;
  justify-self: end;
  align-self: start;
}

.langSelector .langSelector_item {
  margin-top: 8px;
}

.langSelector .langSelector_item span {
  margin-left: 3px;
}

.nav-header .langSelector svg {
  width: 18px;
  height: 18px;
}

.nav-header .langSelector .sub-menu .lang {
  width: 70%;
  display: flex;
  align-self: center;
  justify-content: space-between;
  background-color: var(--overlay-color);
  margin-top: 10px;
  margin-left: 3px;
}

.basket {
  line-height: 30px;
  grid-column: 4 / 5;
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
  margin-top: 6px;
  height: 16px;
}

.phone img {
  margin-right: 8px;
  height: 16px;
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

.linkList-item .sub-menu {
  position: absolute;
  background-color: var(--overlay-color);
  top: calc(100% + 0.5rem);
  width: 80%;
  display: flex;
  align-items: center;
  flex-direction: column;
  padding-top: 3%;
}

.linkList-item .sub-menu .menu-item {
  margin: 3%;
}

.langSelector .sub-menu {
  /*display: grid;*/
  /*grid-template-columns: 1fr 1fr;*/
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
    grid-template-columns: 1fr 3fr 1fr 1fr;
  }

  .phone {
    grid-column: 2 / 2;
  }

  .basket {
    position: absolute;
    top: 15px;
    right: 10px;
  }

  .hamburg {
    grid-column: 1 / 2;
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
