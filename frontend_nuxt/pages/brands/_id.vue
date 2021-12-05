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
    }
  },
  head() {
    let categoryTitle = '';
    this.$store.getters['categories/categories'].forEach(item => {
      if (item.id === this.ctgId) {
        categoryTitle = item.title
      }
    });
    if (this.$t(`${this.title}`)) {
      categoryTitle = this.$t(`${this.title}`)
    }
    return {
      title: categoryTitle,
      meta: [
        {
          hid: 'description',
          name: 'description',
          content: 'My custom description'
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
        return category.title;
      } else {
        return "";
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
