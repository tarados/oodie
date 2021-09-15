
export default async ({ app, store }) => {
  if (process.server) {
    await store.dispatch('locales/fetch');
    await store.dispatch('messages/fetch');
  }
  app.i18n._vm._data.messages = store.getters['messages/messages'];
  if (process.browser) {
    app.store.commit("cart/addProductFromCart");
  }
}
