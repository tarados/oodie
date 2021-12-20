export default async function ({context, store, i18n, route}) {
  await store.dispatch('products/fetch');
  await store.dispatch('categories/fetch');
  await store.dispatch('home/fetch');
  await store.dispatch('description/fetch');
}
