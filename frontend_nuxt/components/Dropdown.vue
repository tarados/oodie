<template>
  <div class="langSelector"
       @mouseover="mouseoverLang"
       @mouseleave="mouseleaveLang"
  >
    <flag iso="ru"/>
    <div class="langSelector_item">
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
      selectedLanguageIcon: "",
      selectedLanguage: 'ru',
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
      this.selectedLanguageIcon = this.selectedLanguage = locale.toUpperCase();
    }
  }
}
</script>

<style scoped>
.langSelector {
  position: relative;
  margin-right: calc(0rem + 20 * ((100vw - 320px) / 1518));
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

.langSelector .sub-menu {
  position: absolute;
  width: 70%;
}

.langSelector .sub-menu .lang {
  display: flex;
  align-self: center;
  justify-content: space-between;
  background-color: var(--overlay-color);
  margin-top: 10px;
  margin-left: 3px;
}

</style>
