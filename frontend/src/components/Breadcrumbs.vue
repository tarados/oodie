<template>
  <div>
    <ul class="breadcrumbs">
      <li class="breadcrumbs__item">
        <router-link :to="{name: 'Brands'}" class="breadcrumbs__link">Бренды друзья</router-link>
      </li>
      <li class="breadcrumbs__item">
        <router-link :to="{name: 'Brand', params: {slug: this.slug}}" class="breadcrumbs__link">{{
            currentCategory
          }}
        </router-link>
      </li>
      <li class="breadcrumbs__item">
        <a class="breadcrumbs__link breadcrumbs__link--active">{{ currentProduct }}</a>
      </li>
    </ul>
  </div>
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
    slug() {
      try {
        return this.$store.getters.allCategories.find(item => item.title === this.currentCategory).slug;
      } catch (TypeError) {
        return ''
      }

    }
  }
}
</script>

<style scoped>
.breadcrumbs {
  padding: 15px;
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
  color: #009578;
  font-weight: 500;
}
</style>