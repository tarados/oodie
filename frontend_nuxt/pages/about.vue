<template>
  <div class="wrapper">
    <img src="~/static/sewer_cat.gif"/>
  </div>
</template>

<script>
export default {
  name: "About",
  head() {
    return {
      title: this.$t('AboutPage'),
      meta: [
        {
          hid: 'description',
          name: 'description',
          content: 'My custom description'
        }
      ]
    }
  }
}
</script>

<style scoped>
.wrapper {
  text-align: center;
  padding-bottom: 40px;
}

img {
  width: 100%;
  max-width: 500px;
}
</style>
