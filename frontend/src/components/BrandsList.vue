<template>
  <div class="wrapper-brandlist">
    <div class="row">
      <router-link :to="{name: 'Brand', params: {slug: brand.slug} }"
                   v-for="(brand, index) in brands" :key="index"
                   class="brand"
      >
        <img :src="brand.images">
        <div class="brand-title">{{ brand.title }}</div>
      </router-link>
    </div>
  </div>
</template>

<script>
import {mapGetters} from 'vuex'

export default {
  name: "Brands",
  computed: {
    ...mapGetters(["allProducts", "allCategories"]),
    brands() {
      let brandsList = [];
      this.allCategories.forEach(item => {
        if (item.title !== 'hoodiyalko') {
          const brand = {
            'title': item.title,
            'images': this.allProducts.find(product => product.category === item.id).image,
            'slug': item.slug
          };
          brandsList.push(brand);
        }
      });
      return brandsList;
    }
  },
  methods: {},
  mounted() {
    this.$store.dispatch('loadProducts');
  }
}
</script>

<style scoped>
.wrapper-brandlist {
  max-width: 1580px;
  margin: 0 auto;
}

h4 {

}

.row {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-gap: 1em;
  grid-auto-flow: row;
}

.brand {
  position: relative;
  text-decoration: none;
  color: #3d4246;
}

.brand-title {
  position: absolute;
  background-color: #c7d9d8;
  width: 72%;
  height: 12vmin;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  text-transform: uppercase;
  text-align: center;
  font-size: calc(22px + 10 * (100vw / 1580));
  font-family: 'Arial', sans-serif;
  bottom: 3vmin;
  left: 14%;
}

.brand-image {

}

img {
  width: 100%;
}

/*media queries******************************************************************************************************/
@media screen and (max-width: 1024px) {

}

@media screen and (max-width: 960px) {

}


@media screen and (max-width: 767px) {
  .brand-title {
    font-size: calc(24px + (16 + 16 * 0.7) * (100vw / 1580));
  }

  .row {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media screen and (max-width: 420px) {
  .row {
    grid-template-columns: 1fr;
  }
}

@media screen and (max-width: 375px) {

}

@media screen and (max-width: 360px) {

}

@media screen and (max-width: 320px) {
}

@media screen and (max-width: 280px) {

}


</style>