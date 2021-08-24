import Vue from "vue";

export default ({store}) => {
  console.log('from locales', store.getters['messages/messages'])
}
// Vue.i18n._vm.messages = Vue.store.getters['messages/messages'];


