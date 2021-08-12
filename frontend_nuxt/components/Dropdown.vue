<template>
  <div class="langSelector"
       @mouseover="mouseoverLang"
       @mouseleave="mouseleaveLang">
    <flag :iso="selectedLanguageIcon"/>
    <span>{{ selectedLanguage }}</span>
    <div class="langSelector_item">
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
          <flag :iso="item.slug"/>
          <p>{{ item.title }}</p>
        </div>
      </div>
    </transition>
  </div>
</template>

<script>


export default {
  name: "Dropdown",
  data() {
    return {
      langList: [{
        'title': 'RU',
        'name': 'ru-RU',
        'slug': 'ru'
      },
        {
          'title': 'UA',
          'name': 'ua-UA',
          'slug': 'ua'
        }],
      selectedLanguageIcon: "ru",
      selectedLanguage: "RU",
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
    setLocale(index) {
      const locale = this.langList[index];
      this.selectedLanguageIcon = locale.slug
      this.selectedLanguage = locale.title;
    }
  }
}
</script>

<style scoped>
.langSelector {
  width: 3.5rem;
  position: relative;
  padding-left: 85rem;
  display: grid;
  grid-template-columns: repeat(3, 1.1rem);
  grid-template-rows: 1.5rem;
  grid-gap: 1%;
}

.langSelector svg {
  width: 18px;
  height: 18px;
}

.langSelector .sub-menu {
  padding-left: 85rem;
  position: absolute;
  width: 100%;
  top: calc(60% + 18px);

}

.langSelector .sub-menu .lang {
  display: grid;
  grid-template-columns: repeat(2, 1.1rem);
  grid-auto-rows: auto;
  background-color: var(--overlay-color);
}

</style>
