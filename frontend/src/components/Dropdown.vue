<template>
  <div class="linkList-item" @click="isOpen = !isOpen">
    <a href="#">{{title}}</a>
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round">
      <path stroke="none" d="M0 0h24v24H0z"/>
      <path d="M9 14l3 3l3 -3" />
    </svg>
    <transition name="fade" appear>
      <div class="sub-menu" v-if="isOpen">
        <div
            class="menu-item"
            v-for="(item, index) in items" :key="index"
        >
          <a :href="item.link">{{item.title}}</a>
        </div>
      </div>
    </transition>
  </div>
</template>

<script>
export default {
  name: "Dropdown",
  props: ['title', 'items'],
  data() {
    return {
      isOpen: false
    }
  }
}
</script>

<style>
.linkList .linkList-item svg {
  width: 18px;
  margin-left: 10px;
}

.linkList-item svg:hover {
  fill: #c7d9d8;
}

.sub-menu {
  position: absolute;
  background-color: white;
  top: calc(100% + 18px);
  transform: translateX(-50%);
  width: 100%;
}

.fade-enter-active,
.fade-leave-active {
  transition: all .5s ease-out;
}

.fade-enter,
.fade-leave-to {
  opacity: 0;
}

</style>