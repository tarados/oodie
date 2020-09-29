<template>
  <div class="wrapper-brandlist">
    <div class="row">
      <router-link :to="{name: 'Brand', params: {slug: brand.slug} }"
                   v-for="(brand, index) in brands" :key="index"
                   :style="{'background': 'url(' + brand.images + ') center no-repeat', 'background-size': 'cover'}"
                   class="brand"
      >
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
        const firstProduct = this.allProducts.find(product => product.category === item.id);

        if (!firstProduct) return;

        if (item.title !== 'hoodiyalko') {
          const brand = {
            'title': item.title,
            'images': firstProduct.image,
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
  margin: 0 auto;
}

.row {
  margin: 0 0 2% 0;
  display: grid;
  grid-template: 400px / repeat(3, 400px);
  grid-auto-rows: 400px;
  grid-gap: 1em;
  grid-auto-flow: row;
  justify-content: center;
}

.brand {
  position: relative;
  text-decoration: none;
  color: #3d4246;
}

.brand-title {
  position: absolute;
  background-color: rgba(0, 0, 0, 0.5);
  width: 60%;
  height: calc(5vmin + 10 * (100vw / 1838));
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  text-transform: uppercase;
  text-align: center;
  font-size: calc(3.5vmin + 3 * (100vw / 1838));
  font-family: 'Roboto', sans-serif;
  bottom: 3vmin;
  left: 20%;
}

img {
  width: 100%;
}

/*media queries******************************************************************************************************/
@media screen and (max-width: 1260px) {
  .row {
    grid-template: 400px / repeat(2, 400px);
  }
}

@media screen and (max-width: 1024px) {

}


@media screen and (max-width: 860px) {
  .row {
    grid-template: 400px / 400px;
  }
}


@media screen and (max-width: 767px) {
  .brand-title {
    height: calc(5vmin + 10 * (100vw / 767));
    font-size: calc(3.5vmin + 3 * (100vw / 767));
  }
}

@media screen and (max-width: 420px) {
  .row {
    grid-template: 360px / 360px;
    grid-auto-rows: 360px;
  }

  .brand-title {
    height: calc(5vmin + 10 * (100vw / 420));
    font-size: calc(3.5vmin + 3 * (100vw / 420));
  }

}

@media screen and (max-width: 375px) {
  .row {
    grid-template: 320px / 320px;
    grid-auto-rows: 320px;
  }
}

@media screen and (max-width: 360px) {
  .row {
    grid-template: 300px / 300px;
    grid-auto-rows: 300px;
  }
}

@media screen and (max-width: 320px) {
  .row {
    grid-template: 260px / 260px;
    grid-auto-rows: 260px;
  }
}

@media screen and (max-width: 280px) {
  .row {
    grid-template: 220px / 220px;
    grid-auto-rows: 220px;
  }
}


</style>
