<template>
  <div class="navbar">
    <div class="container-nav ">
      <div class="item logo">
        <Logo/>
      </div>
      <div class="item link">
        <div class="linkList">
          <a href="/">Home</a>
          <router-link
              :to="{name: 'Products'}"
          >
            Sale Products
          </router-link>
          <a href="/">Contact us</a>
        </div>
      </div>
      <div class="card">
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
    </div>
    <Hamburger/>
  </div>
</template>

<script>
import Hamburger from "./Hamburger";
import Logo from "./Logo"

export default {
  name: 'NavBar',
  components: {
    Hamburger,
    Logo
  },
  data() {
    return {
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
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  align-items: center;
}

.item {
  flex-grow: 1;
}

.link {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
}

.link a {
  margin: 25px;
  color: #3d4246;
  text-decoration: none;
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

@media screen and (max-width: 640px) {

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
  img {
    width: 10vmax;
  }

  .card {
    margin-left: 25%;
  }
}

</style>
