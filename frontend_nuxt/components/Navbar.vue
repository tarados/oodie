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
      <div class="navbar_header__lang-basket">
        <div class="navbar_header__lang">
          <Dropdown/>
        </div>
        <div class="navbar_header__basket">
          <img src="~/assets/img/cart.svg">
        </div>
      </div>
    </div>
    <div class="navbar_logo">
      <img src="~/assets/img/logo2.png">
    </div>
    <div class="navbar_items">
      <div class="navbar-item"
           v-for="(item, index) in links" :key="index">
        <nuxt-link :to="item.route">
          <p>{{ $t(`${item.title}`) }}</p>
        </nuxt-link>
        <div class="navbar-item__brands" v-if="links[index].nestedRoutes"
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
            class="navbar-item__sub-menu"
            v-if="isOpen"
          >
            <div
              class="menu-item"
              v-for="category in categories" :key="category.id"
              v-show="category.slug !== 'hoodiyalko'"
            >
              <nuxt-link
                to="/"
              >
                <p>{{ category.title }}</p>
              </nuxt-link>
            </div>
          </div>
        </div>
      </div>

    </div>
  </div>
</template>

<script>
import links from '~/assets/js/linkList'
export default {
  name: "Navbar",
  data() {
    return {
      selected: "",
      isOpen: false,
      basketVisible: false
    };
  },
  computed: {
    links() {
      const lnk = links();
      return lnk
    },
    categories() {
      return this.$store.getters['categories/categories']
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
    }
  },
  mounted() {
    // console.log(this.categories)
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

.navbar_header__lang-basket {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 10%;
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
  align-items: baseline;
  transition: 0.4s;
}

.navbar_items .navbar-item a {
  text-decoration: none;
  text-transform: uppercase;
}

.navbar_items .navbar-item a:hover {
  font-weight: bold;
}

.navbar_items .navbar-item .nuxt-link-exact-active {
  font-weight: bold;
}

.navbar_items .navbar-item svg {
  width: 18px;
  height: 18px;
  margin-left: 10px;
}

.navbar-item .navbar-item__brands .navbar-item__sub-menu {
  position: absolute;
  background-color: white;
  top: calc(100% + 0.5rem);
  left: 0;
  width: 80%;
  display: flex;
  align-items: center;
  flex-direction: column;
  padding: 0 calc(3vw + 12 * (100vw / 1838));
}

.navbar-item .navbar-item__brands .navbar-item__sub-menu p {
  font-weight: normal;
}

.navbar-item .navbar-item__brands .navbar-item__sub-menu p:hover {
  font-weight: bold;
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
