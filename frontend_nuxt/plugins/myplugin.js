export default async ({ app, store }) => {
  app.i18n._vm._data.messages = store.getters['messages/messages'];
  if (process.browser) {
    app.store.commit("cart/addProductFromCart");
  }
}
