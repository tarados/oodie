<template>
  <div id="demo">
    <button v-on:click="show = !show">
      Переключить
    </button>
    <transition name="fade">
      <div v-if="show">
        <div class="linkContent">
          <ul>
            <li><a href="#">Home</a></li>
            <li>
              <a href="#">Sale Products</a>
            </li>
            <li>
              <a href="#">Contact us</a>
            </li>
          </ul>
        </div>
      </div>
    </transition>
  </div>
</template>

<script>

    export default {
        name: "Hamburger",
        components: {},
        data() {
            return {
                show: true
            }
        }
    }
</script>

<style scoped>
  .fade-enter-active, .fade-leave-active {
    transition: opacity .5s;
  }

  .fade-enter, .fade-leave-to /* .fade-leave-active до версии 2.1.8 */
  {
    opacity: 0;
  }

  .linkContent {
    background-color: yellow;
  }
</style>