export default async function ({context, store, i18n, route}) {
  if (process.server) {
    await store.dispatch('products/fetch');
    await store.dispatch('categories/fetch');
  }
}
