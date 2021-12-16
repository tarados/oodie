<template>
  <div class="wrapper-brand">
    <ProductsList :ctg="ctgId" size="small"/>
  </div>
</template>

<script>

export default {
  name: "Brand",
  middleware: ['products'],
  data() {
    return {
      title: '',
      description: '',
    }
  },
  head() {
    return {
      title: this.$t(`${this.title}`),
      meta: [
        {
          hid: 'description',
          name: 'description',
          content: this.$t(`${this.title}`)
        }
      ]
    }
  },
  computed: {
    ctgId() {
      return Number(this.$route.params.id);
    },
    categoryForHead() {
      const category = this.$store.getters['categories/categories'].find(category => category.id === this.ctgId);
      if (category) {
        if (category.title_translate) {
          this.title = category.title_translate;
        }  else {
          this.title = category.title;
        }
        if (category.category_description) {
          this.description = category.category_description;
        }
      }
    }
  },
  mounted() {
    this.categoryForHead;
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
