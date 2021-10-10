export default async ({ app, store }) => {
  app.i18n._vm._data.messages = await store.getters['messages/messages'];
  if (process.browser) {
    await app.store.commit("cart/addProductFromCart");
  }
  if (process.server) {
    await app.store.dispatch('instagram/fetch');
  }
}
