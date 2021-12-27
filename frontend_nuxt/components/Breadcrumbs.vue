<template>
  <ul class="breadcrumbs">
    <li class="breadcrumbs__item" v-for="(item, index) in breadcrumbs" :key="index">
      <nuxt-link
        v-if="index < breadcrumbCount"
        :to=item.routeName
        class="breadcrumbs__link"
      >
        {{ $t(`${item.title}`) }}
      </nuxt-link>
      <span v-if="index === breadcrumbs.length - 1">{{ $t(`${item.title}`) }}</span>
    </li>
  </ul>
</template>

<script>

export default {
  name: "Breadcrumbs",
  props: {
    currentCategory: {
      type: String
    },
    currentProduct: {
      type: Object
    }
  },
  data() {
    return {
      title: '',
      categoryTitle: ''
    }
  },
  computed: {
    breadcrumbs() {
      const result = [];
      if (this.currentProduct) {
        result.push({title: "MenuHome", routeName: "/"});
        if (this.currentProduct.category !== 1) {
          result.push({title: "MenuBrandsFriends", routeName: "/brands"});
        }
        const category = this.$store.getters['categories/getCategory'](this.currentProduct.category);
        if (category) {
          if (category.title_translate) {
            this.categoryTitle = category.title_translate;
          }
          this.categoryTitle = category.title;
          const idCategory = parseInt(category.id);
          result.push({
            title: this.categoryTitle,
            routeName: "/brands/" + `${idCategory}`,
            routeParams: {slug: category.slug}
          });
        }
        if (this.currentProduct.title_translate) {
          this.title = this.currentProduct.title_translate;
        }
        this.title = this.currentProduct.title;
        result.push({title: this.title});
      }
      return result;
    },
    breadcrumbCount() {
      return this.breadcrumbs.length - 1
    }
  }
}
</script>

<style scoped>
.breadcrumbs {
  display: inline-block;
  padding: 0 0 15px;
}

.breadcrumbs__item {
  display: inline-block;
}

.breadcrumbs__item span {
  text-transform: uppercase;
}

.breadcrumbs__item:not(:last-of-type)::after {
  content: '>';
  margin: 0 5px;
  color: #cccccc;
}

.breadcrumbs__link {
  text-transform: uppercase;
  text-decoration: none;
  color: #777676;
}

.breadcrumbs__link:hover {
  text-decoration: underline;
}

.breadcrumbs__link--active {
  color: black;
}
</style>
