<template>
  <div class="wrapper-brand">
    <ProductsList :ctg="ctgId" size="small"/>
  </div>
</template>

<script>

export default {
  name: "Brand",
  middleware: ['products'],
  validate({params}) {
    return /^\d+$/.test(params.id);
  },
  async asyncData({$axios, app, $i18n, params}) {
    const data = await $axios.get(process.env.VUE_APP_API + '/categories/category/' + params.id);
    const category = data.data.category;
    app.head.title = category.title;
    app.head.meta.push(
      {
        hid: 'description',
        name: 'description',
        content: category.description
      }
    )
    return {category}
  },
  computed: {
    ctgId() {
      return Number(this.$route.params.id);
    },
  }
}
</script>

<style scoped>
.wrapper-brand {
  display: flex;
  flex-direction: column;
  align-self: center;
}
</style>
