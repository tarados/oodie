<template>
  <div id="app">
    <modal-vue
        modalSize="md"
        @on-close="$vm2.close('modal-4')"
        name="modal-4"
        :headerOptions="{
          title: 'vasya',
          closeIcon: ' '
        }"
        :footerOptions="{
        btn1: 'Ok ',
        disableBtn2: true,
        btn1OnClick: () => {
          $vm2.close('modal-4');
        },
        justify: 'center'
      }"
    >
      <p></p>
      <div v-for="(warning, index) in warningList" :key="index">
        <p>{{ warning.title }}</p>
      </div>
    </modal-vue>
  </div>
</template>

<script>
export default {
  name: 'modal',
  props: {
    warningList: {
      type: Array
    }
  },
  methods: {
    close() {
      this.$vm2.close("modal-4");
    }
  },
  mounted() {
    console.log("modal", this.warningList);
  }
};
</script>

<style scoped>
#app {
  /*font-family: "Avenir", Helvetica, Arial, sans-serif;*/
  /*-webkit-font-smoothing: antialiased;*/
  /*-moz-osx-font-smoothing: grayscale;*/
  /*text-align: center;*/
  /*color: #2c3e50;*/
  /*margin-top: 60px;*/
}
</style>
