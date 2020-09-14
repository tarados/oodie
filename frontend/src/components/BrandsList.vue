<template>
  <div class="wrapper">
    <div class="row">
      <router-link :to="{name: 'Brand', params: {slug: brand.slug} }"
                   v-for="(brand, index) in brands" :key="index"
                   class="brand"
      >
        <img :src="brand.images">
        <div class="brand-title">
          <h4>{{ brand.title }}</h4>
        </div>
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
        if (item.title !== 'oodie') {
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
.wrapper {
  margin-top: 3rem;
}

h4 {
  text-transform: uppercase;
  text-align: center;
}

.row {
  max-width: 1580px;
  margin: 0 auto;
  display: flex;
  flex-wrap: wrap;
  justify-content: flex-start;
  align-items: center;
  align-content: center;
}

.brand {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  padding-bottom: 2rem;
  text-decoration: none;
  color: #3d4246;
  width: calc((100% / 12) * 4 - 30px);
  margin: 0 15px;
}

.brand-title {
  background-color: #c7d9d8;
  width: 72%;
  margin-top: -5rem;
  height: 4.65rem;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-size: 2rem;
}

.brand img {
  width: 100%;
}

/*media queries******************************************************************************************************/
@media screen and (max-width: 1200px) {
  .brand {
    width: auto;
  }

  .brand-title {
    margin-top: -3rem;
    height: 2.72rem;
    font-size: 1rem;
  }
}

@media screen and (max-width: 960px) {
  .brand {
    width: auto;
  }

  .brand-title {
    margin-top: -3rem;
    height: 2.72rem;
    font-size: 1.9rem;
  }
}


@media screen and (max-width: 750px) {
  .brand {
    width: auto;
  }

  .brand-title {
    margin-top: -3rem;
    height: 2.72rem;
    font-size: 1.8rem;
  }
}

@media screen and (max-width: 420px) {
  .brand {
    width: auto;
  }

  .brand-title {
    margin-top: -3rem;
    height: 2.72rem;
    font-size: 1.6rem;
  }
}

@media screen and (max-width: 375px) {
  .brand {
    width: auto;
  }

  .brand-title {
    margin-top: -3rem;
    height: 2.72rem;
    font-size: 1.4rem;
  }
}

@media screen and (max-width: 360px) {
  .brand {
    width: auto;
  }

  .brand-title {
    margin-top: -3rem;
    height: 2.72rem;
    font-size: 1.3rem;
  }
}

@media screen and (max-width: 320px) {
  .brand {
   width: auto;
  }

  .brand-title {
    margin-top: -3rem;
    height: 2.72rem;
    font-size: 1.2rem;
  }
}

@media screen and (max-width: 280px) {
  .brand {
    width: auto;
  }

  .brand-title {
    margin-top: -3rem;
    height: 2.72rem;
    font-size: 1rem;
  }
}


</style>