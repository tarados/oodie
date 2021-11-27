<template>
  <ul class="breadcrumbs">
    <li class="breadcrumbs__item" v-for="(item, index) in breadcrumbs" :key="index">
      <nuxt-link
        v-if="index < breadcrumbCount"
        :to= item.routeName
        class="breadcrumbs__link"
      >
        {{ $t(`${item.title}`) }}
      </nuxt-link>
      <span v-if="index === breadcrumbs.length - 1">{{ $t(`${item.title}`) }}</span>
    </li>
  </ul>
</template>

<script>

import About from "@/pages/about";

export default {
  name: "Breadcrumbs",
  components: {About},
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
      const categoriesList = this.$store.getters['categories/categories'];
      const result = [];
      if (this.currentProduct && this.currentProduct.category === 1) {
        result.push({title: "MenuHome", routeName: "/"});
      } else {
        result.push({title: "MenuBrandsFriends", routeName: "/brands"});
        if (this.currentProduct) {
          const category = categoriesList.find(category => category.id === this.currentProduct.category);
          if (category) {
            if (category.title_translate) {
              this.categoryTitle = category.title_translate;
            }  else {
              this.categoryTitle = category.title;
            }
            const idCategory = parseInt(category.id);
            result.push({title: this.categoryTitle, routeName: "/brands/" + `${idCategory}`, routeParams: {slug: category.slug}});
          }
        }
      }
      if (this.currentProduct) {
        if (this.currentProduct.title_translate) {
          this.title = this.currentProduct.title_translate;
        }  else {
          this.title = this.currentProduct.title;
        }
        result.push({title: this.title});
      }

      return result;
    },
    slug() {
      try {
        return this.$store.getters['categories/categories'].find(item => item.title === this.currentCategory).slug;
      } catch (TypeError) {
        return ''
      }
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
