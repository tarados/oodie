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
  width: 60%;
  height: calc(5vmin + 10 * (100vw / 1838));
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  text-transform: uppercase;
  text-align: center;
  font-size: calc(3.5vmin + 3 * (100vw / 1838));
  font-family: 'Arial', sans-serif;
  bottom: 3vmin;
  left: 20%;
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
    height: calc(5vmin + 10 * (100vw / 767));
    font-size: calc(3.5vmin + 3 * (100vw / 767));
  }

  .row {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media screen and (max-width: 420px) {
  .row {
    grid-template-columns: 1fr;
  }

  .brand-title {
    height: calc(5vmin + 10 * (100vw / 420));
    font-size: calc(3.5vmin + 3 * (100vw / 420));
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