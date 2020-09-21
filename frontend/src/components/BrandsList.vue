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
  position: relative;
  max-height: 31rem;
  overflow: hidden;
  text-decoration: none;
  color: #3d4246;
  width: calc((100% / 12) * 4 - 30px);
  margin: 10px 10px;
}

.brand-title {
  position: absolute;
  background-color: #c7d9d8;
  width: 72%;
  height: 4.65rem;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-size: 2rem;
  left: 14%;
  top: 83%;
}

.brand img {
  width: 100%;
}

/*media queries******************************************************************************************************/
@media screen and (max-width: 1024px) {
  .brand {
    width: calc((100% / 12) * 6- 30px);
    max-height: 19rem;
  }

  .brand-title {
    top: 82%;
    height: 2.72rem;
    font-size: 1rem;
  }
}

@media screen and (max-width: 960px) {
  .brand {
    width: calc((100% / 12) * 6- 30px);
  }

  .brand-title {
    top: 89%;
    height: 2.72rem;
    font-size: 1.9rem;
  }
}


@media screen and (max-width: 770px) {
  .brand {
    width: calc((100% / 12) * 6 - 30px);
  }

  .brand-title {
    top: 85%;
    height: 2.72rem;
    font-size: 1.8rem;
  }
}

@media screen and (max-width: 420px) {
  .brand {
    width: auto;
  }

  .brand-title {
    top: 86%;
    height: 2.72rem;
    font-size: 1.6rem;
  }
}

@media screen and (max-width: 375px) {
  .brand {
    width: auto;
  }

  .brand-title {
    top: 85%;
    height: 2.72rem;
    font-size: 1.4rem;
  }
}

@media screen and (max-width: 360px) {
  .brand {
    width: auto;
  }

  .brand-title {
    top: 84%;
    height: 2.72rem;
    font-size: 1.3rem;
  }
}

@media screen and (max-width: 320px) {
  .brand {
   width: auto;
  }

  .brand-title {
    top: 82%;
    height: 2.72rem;
    font-size: 1.2rem;
  }
}

@media screen and (max-width: 280px) {
  .brand {
    width: auto;
  }

  .brand-title {
    top: 79%;
    height: 2.72rem;
    font-size: 1rem;
  }
}


</style>