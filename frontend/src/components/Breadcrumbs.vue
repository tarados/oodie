<template>
    <ul class="breadcrumbs">
      <li class="breadcrumbs__item" v-for="(item, index) in breadcrumbs" :key="index">
        <router-link
            v-if="index === 0"
            :to="{name: item.routeName, params: item.routeParams}"
             class="breadcrumbs__link">{{ item.title | localize }}</router-link>
        <router-link
            v-if="index === 1"
            :to="{name: item.routeName, params: item.routeParams}"
             class="breadcrumbs__link">{{ item.title }}</router-link>

        <a v-if="index === breadcrumbs.length - 1" class="breadcrumbs__link breadcrumbs__link--active">{{ item.title}}</a>
      </li>
    </ul>
</template>

<script>
import { mapGetters } from 'vuex'

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

    },
    ...mapGetters(["breadcrumbs"])
  }
}
</script>

<style scoped>
.breadcrumbs {
  ;
  display: inline-block;
  padding: 0px 0px 15px;
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
