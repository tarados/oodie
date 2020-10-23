<template>
  <div class="wrapper-logo">
    <div class="elfsight-app-18f30070-13eb-44cf-9977-e6b9948b7045"></div>
  </div>
</template>

<script>
export default {
  name: "logo",
  methods: {
    toMain() {
      this.$router.push({name: 'Home'})
    },
  },

  mounted() {
    const script = document.createElement('script');
    script.setAttribute('src','https://apps.elfsight.com/p/platform.js');
    document.head.appendChild(script);
  }
};
</script>

<style scoped>
.wrapper-logo {
  display: flex;
  justify-content: center;
  align-items: center;
  align-self: center;
  margin-top: 50px;
  margin-bottom: 40px;
  cursor: pointer;

}
</style>
