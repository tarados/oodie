
export default async function ({ context, store, i18n, route }) {
  if (process.server) {
    console.log("localization middleware");
  //   console.log("start");
    await store.dispatch('locales/fetch');
    await store.dispatch('messages/fetch');
    i18n._vm.messages = store.getters['messages/messages'];
    console.log("end");
  } else {
    console.log("client!!!");
    i18n._vm.messages = store.getters['messages/messages'];
  }
}
