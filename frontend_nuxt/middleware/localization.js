
export default async function ({ context, store, i18n, route }) {
  if (process.server) {
    await store.dispatch('locales/fetch');
    await store.dispatch('messages/fetch');
    i18n._vm.messages = store.getters['messages/messages'];
  } else {
    i18n._vm.messages = store.getters['messages/messages'];
  }
}
