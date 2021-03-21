<template>
  <div class="langSelector"
       @mouseover="mouseoverLang"
       @mouseleave="mouseleaveLang"
  >
    <div class="langSelector_item">
      <flag :iso="selectedLanguageIcon"></flag>
      <span>{{ selectedLanguage }}</span>
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor"
           fill="none"
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
            @click="setLocale(index)"
        >
          <flag :iso="item.slug"></flag>
          <p>{{ item.title }}</p>
        </div>
      </div>
    </transition>
  </div>
</template>

<script>

import {langList} from '@/js/linkList';

export default {
  name: "Dropdown",
  data() {
    return {
      langList: [],
      selectedLanguageIcon: "",
      selectedLanguage: "",
      isOpenLang: false
    }
  },
  methods: {
    clearTimer: function () {
      if (this.timer) clearTimeout(this.timer);
      this.timer = -1;
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
    getlangList() {
      this.langList = langList();
      this.selectedLanguage = window.navigator.language.slice(0, 2).toUpperCase();
      this.selectedLanguageIcon = window.navigator.language.slice(0, 2);
    },
    setLocale(index) {
      const locale = this.langList[index].slug;
      this.$store.commit('setLocale', locale);
      this.selectedLanguageIcon = this.langList[index].slug;
      this.selectedLanguage = this.langList[index].title;
    }
  },
  mounted() {
    this.getlangList();
  }
}
</script>

<style scoped>
.langSelector {
  /*width: 70%;*/
  grid-column: 3 / 4;
  justify-self: end;
  align-self: start;
}

.langSelector .langSelector_item span {
  margin-left: 3px;
}

.langSelector svg {
  width: 18px;
  height: 18px;
}

.langSelector .sub-menu .lang {
  width: 70%;
  display: flex;
  align-self: center;
  justify-content: space-between;
  background-color: var(--overlay-color);
  margin-top: 10px;
  margin-left: 3px;
}

</style>