<template>
  <div class="menu-wrap">
    <input value="toggler" type="checkbox" class="toggler" v-model="checked"/>
    <div class="hamburger">
      <div></div>
    </div>
    <div class="menu">
      <div>
        <div>
          <ul>
            <li class="menu-item"
                v-for="item in links" :key="item.route"
                @click="closeHamburger"
            >
              <router-link :to="item.route">{{ $t(`${item.title}`) }}</router-link>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

export default {
  name: "Hamburger",
  data() {
    return {
      checked: false,
      links: [{route: "/", title: "MenuHome"},
        {route: "/about", title: "MenuAboutUs"},
        {
          route: "/brands", title: "MenuBrandsFriends",
          nestedRoutes: [
            {route: "/some-route-1", title: "SomeRoute1"},
            {route: "/some-route-1", title: "SomeRoute2"},
          ]
        },
        {route: "/contacts", title: "MenuContacts"}]
    };
  },
  methods: {
    closeHamburger() {
      this.checked = false;
    }
  }
};
</script>

<style scoped>
.menu-wrap {
  position: fixed;
  left: 0;
  z-index: 1;
}

.menu-wrap .label {
  position: relative;
}

.menu-wrap .label label {
  position: absolute;
  left: 10px;
}

.menu-wrap .toggler {
  position: fixed;
  z-index: 2;
  cursor: pointer;
  width: 50px;
  height: 40px;
  opacity: 0;
}

.menu-wrap .hamburger {
  position: fixed;
  left: 0;
  z-index: 1;
  width: 50px;
  height: 40px;
  padding: 1.2rem 1rem 1rem 1rem;
  background-color: #f5f5f5;
  display: flex;
  align-items: center;
  justify-content: center;
}

.menu-wrap .hamburger > div {
  position: relative;
  width: 100%;
  height: 2px;
  background-color: black;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.4s ease;
}

.menu-wrap .hamburger > div:before,
.menu-wrap .hamburger > div::after {
  content: "";
  position: absolute;
  z-index: 1;
  top: -8px;
  width: 100%;
  height: 2px;
  background: inherit;
}

.menu-wrap .hamburger > div:after {
  top: 8px;
}

.menu-wrap .toggler:checked + .hamburger > div {
  transform: rotate(135deg);
}

.menu-wrap .toggler:checked + .hamburger > div:before,
.menu-wrap .toggler:checked + .hamburger > div:after {
  top: 0;
  transform: rotate(90deg);
}

.menu-wrap .toggler:checked:hover + .hamburger > div {
  transform: rotate(225deg);
}

.menu-wrap .toggler:checked ~ .menu {
  visibility: visible;
}

.menu-wrap .toggler:checked ~ .menu > div {
  transform: scale(1);
  transition-duration: var(--menu-speed);
}

.menu-wrap .toggler:checked ~ .menu > div > div {
  opacity: 1;
  transition: opacity 0.4s ease;
}

.menu-wrap .menu {
  position: fixed;
  left: 0;
  width: 100%;
  height: 164px;
  visibility: hidden;
  overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: center;
}

.menu-wrap .menu > div {
  background: var(--overlay-color);
  border-radius: 50%;
  width: 200vw;
  height: 200vw;
  display: flex;
  flex: none;
  align-items: center;
  justify-content: center;
  transform: scale(0);
  transition: all 0.4s ease;
}

.menu-wrap .menu > div > div {
  text-align: center;
  max-width: 90vw;
  max-height: 100vh;
  opacity: 0;
  transition: opacity 0.4s ease;
}

.menu-wrap .menu > div > div > ul > li {
  list-style: none;
  color: #000;
  font-size: 16px;
  padding: 0.65rem;
}

.menu-item + .menu-item {
  border-top: 1px solid #000;
}

.menu-wrap .menu > div > div > ul > li > a {
  color: inherit;
  text-decoration: none;
  text-transform: uppercase;
  transition: color 0.4s ease;
}

@media screen and (max-width: 280px){
  .menu-wrap .hamburger {
    left: -10px;
    /*width: 45px;*/
  }
}

</style>
