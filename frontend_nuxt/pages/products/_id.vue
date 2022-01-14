<template>
  <div class="wrapper-product">
    <div class="breadcrumbs-wrapper">
      <Breadcrumbs :current-product="product" :current-category="currentCategory"/>
    </div>
    <Product :product="product" />
  </div>
</template>

<script>

export default {
  name: "productId",
  validate({params}) {
    return /^\d+$/.test(params.id);
  },
  async asyncData({$axios, params, app}) {
   try {
     const data = await $axios.get(process.env.VUE_APP_API + '/products/produc/' + params.id);
     const product = data.data.product;
     return {product}
   } catch (e) {
     await app.store.commit("error/setError", e);
     alert(e);
     await app.router.push('/');
   }
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
    title() {
      if (this.product.title_translate) {
        return this.$t(this.product.title_translate);
      }
      return this.product.title;
    },
    description() {
      if (this.product.description_locale) {
        return this.$t(this.product.description_locale);
      }
      return this.product.description;
    },
    currentCategory() {
      const category = this.$store.getters['categories/getCategory'](this.product.category);
      if (!category) {
        return '';
      }
      if (category.title_translate) {
        return this.$t(category.title_translate);
      }
      return category.title;
    }
  }
};
</script>

<style scoped>
.wrapper-product {
  margin-top: 55px;
  margin-bottom: 40px;
}

.breadcrumbs-wrapper {
  padding-left: 15px;
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
  flex-wrap: wrap;
  justify-content: flex-start;
  align-items: inherit;
  align-content: center;
}

</style>
