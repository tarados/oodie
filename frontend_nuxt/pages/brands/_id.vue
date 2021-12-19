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
  async asyncData({$axios, params}) {
    const data = await $axios.get(process.env.VUE_APP_API + '/categories/category/' + params.id);
    const category = data.data.category;
    return {category}
  },
  head() {
    return {
      title: this.title,
      meta: [
        {
          hid: 'description',
          name: 'description',
          content: this.description
        }
      ]
    }
  },
  computed: {
    ctgId() {
      return Number(this.$route.params.id);
    },
    title() {
      if (!this.category) {
        return '';
      }
      if (this.category.title_translate) {
        return this.$t(this.category.title_translate);
      }
      return this.category.title;
    },
    description() {
      if (!this.category) {
        return '';
      }
      if (this.category.description_locale) {
        return this.$t(this.category.description_locale);
      }
      return this.category.description;
    }
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
