<template>
    <ul class="breadcrumbs">
      <li class="breadcrumbs__item" v-for="(item, index) in breadcrumbs" :key="index">
        <router-link
            v-if="index < breadcrumbCount"
            :to="{name: item.routeName, params: item.routeParams}"
             class="breadcrumbs__link"
        >
         {{ item.title | localize }}
        </router-link>

        <a v-if="index === breadcrumbs.length - 1" class="breadcrumbs__link breadcrumbs__link--active">{{ item.title}}</a>
      </li>
    </ul>
</template>

<script>
import { mapGetters, mapState } from 'vuex'

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
    ...mapGetters(["breadcrumbs"]),
    ...mapState(["categoriesList"]),
    slug() {
      try {
        return this.categoriesList.find(item => item.title === this.currentCategory).slug;
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
