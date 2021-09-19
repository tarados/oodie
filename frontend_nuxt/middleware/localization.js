export default async function ({context, store, i18n, route}) {
  if (process.server) {
    await store.dispatch('locales/fetch');
    await store.dispatch('messages/fetch');
    i18n._vm._data.messages = store.getters['messages/messages'];
  }
}
