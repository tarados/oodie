<template>
    <ul class="breadcrumbs">
      <li class="breadcrumbs__item" v-for="(item, index) in breadcrumbs" :key="index">
        <router-link
            v-if="index < breadcrumbCount"
            :to="{name: item.routeName, params: item.routeParams}"
             class="breadcrumbs__link"
        >
         {{ $t(`${item.title}`) }}
        </router-link>
        <a v-if="index === breadcrumbs.length - 1" class="breadcrumbs__link breadcrumbs__link--active">{{ item.title}}</a>
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
      type: String
    }
  },
  computed: {
    breadcrumbs() {
      const currentProduct = this.$store.getters['product/product'];
      const categoriesList = this.$store.getters['categories/categories'];
      const result = [];
      if (currentProduct && currentProduct.category === 1) {
        result.push({ title: "MenuHome", routeName: "Home" });
      } else {
        result.push({ title: "MenuBrandsFriends", routeName: "Brands" });

        if (currentProduct) {
          const category = categoriesList.find(category => category.id === currentProduct.category);
          if (category) {
            result.push({ title: category.title, routeName: "Brand", routeParams: { slug: category.slug } });
          }
        }
      }

      if (currentProduct) {
        result.push({ title: currentProduct.title });
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

.breadcrumbs__item:not(:last-of-type)::after {
  content: '>';
  margin: 0 5px;
  color: #cccccc;
}

.breadcrumbs__link {
  text-transform: uppercase;
  text-decoration: none;
  color: #999999;
}

.breadcrumbs__link:hover {
  text-decoration: underline;
}

.breadcrumbs__link--active {
  color: black;
}
</style>
