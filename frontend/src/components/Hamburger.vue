<template>
  <div class="menu-wrap">
    <input type="checkbox" class="toggler" v-model="checked"/>
    <div class="hamburger">
      <div></div>
    </div>
    <div class="menu">
      <div>
        <div>
          <ul>
            <li @click="closeHamburger">
              <router-link :to="{name: 'Home'}">Худиялки</router-link>
            </li>
            <li @click="closeHamburger">
              <router-link :to="{name: 'About'}">О нас</router-link>
            </li>
            <li @click="closeHamburger">
              <router-link :to="{name: 'Brands'}">Дружеские бренды</router-link>
            </li>
            <li @click="closeHamburger">
              <router-link :to="{name: 'Contacts'}">Контакты</router-link>
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
    };
  },
  methods: {
    closeHamburger() {
      this.checked = false;
    },
  },
  mounted() {
  },
};
</script>

<style scoped>
.menu-wrap {
  display: none;
  position: fixed;
  top: 8px;
  left: 0;
  z-index: 1;
}

.menu-wrap .toggler {
  position: fixed;
  /*top: 1.55vw;*/
  /*left: 1vw;*/
  z-index: 2;
  cursor: pointer;
  width: 50px;
  height: 40px;
  opacity: 0;
}

.menu-wrap .hamburger {
  position: fixed;
  /*top: 1.55vw;*/
  left: 1vw;
  z-index: 1;
  width: 50px;
  height: 40px;
  padding: 1.2rem 1rem 1rem 1rem;
  background-color: #f5f5f5;
  display: flex;
  align-items: center;
  justify-content: center;
}

/* Hamburger line*/
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
  font-size: 1.11rem;
  border-bottom: 1px solid #000;
  padding: 0.65rem;
}

.menu-wrap .menu > div > div > ul > li > a {
  color: inherit;
  text-decoration: none;
  transition: color 0.4s ease;
}

.close {
  display: none;
}

/*media queries******************************************************************************************/

@media screen and (max-width: 750px) {
  .menu-wrap {
    display: inline;
  }

}

@media screen and (max-width: 640px) {

}

@media screen and (max-width: 540px) {

}

@media screen and (max-width: 450px) {

}

@media screen and (max-width: 420px) {

}

@media screen and (max-width: 375px) {

}

@media screen and (max-width: 360px) {

}

@media screen and (max-width: 325px) {


}

@media screen and (max-width: 285px) {

}
</style>
