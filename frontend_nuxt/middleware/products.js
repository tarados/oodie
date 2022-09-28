export default async function ({context, store, i18n, route}) {
  console.log('begin');
  await store.dispatch('products/fetch');
  console.log('products ok');
  await store.dispatch('categories/fetch');
  console.log('categories ok')
  await store.dispatch('home/fetch');
  console.log('home ok')
  await store.dispatch('description/fetch');
  console.log('description ok')
}
