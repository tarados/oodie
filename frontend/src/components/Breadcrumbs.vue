<template>
  <div class="wrapper">
    <ul class="breadcrumbs">
      <li
          class="breadcrumbs__item"
          v-for="(item, index) in categories" :key="index"
          v-show="item.title !== 'oodie'"
      >
        <router-link
            :to="{name: 'Brand', params: {slug: item.slug}}"
            class="breadcrumbs-link"
            :class="{breadcrumbs__link__active: isLast}"
        >
          {{ item.title }}
        </router-link>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: "Breadcrumbs",
  props: {
    categories: {
      type: Array
    },
    selectedCategoryId: {
      type: Number
    }
  },
  data() {
    return {
      isLast: false
    }
  }
}
</script>

<style scoped>

</style>