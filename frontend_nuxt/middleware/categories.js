export default async function ({app, store, param1, param2}) {
  await store.dispatch('categories/fetch');
  app.head.title = param1;
  app.head.meta.push({
    hid: 'description',
    name: 'description',
    content: 'param2'
  })
  console.log(app.head.meta);
}
