<template>
  <div>
    <div class="content-text">
      <span>ТУТ БУДЕТ ТЕКСТ ПРО ОТБОР БРЕНДОВ ДРУЗЕЙ, КАКИЕ ОРИГИНАЛЬНЫЕ ТУТ ТОВАРЫ И КАК ОНИ ХОРОШИ НА ПОДАРОК
ТЕКСТ ПРИМЕРНО НА 500 ЗНАКОВ, О ТВОРЧЕСТВЕ НЕБОЛЬШИХ КОМПАНИЙ И УНИКАЛЬНОСТИ, И ПРО ДОСТАВКУ В ОДНОЙ ПОСЫЛКЕ</span>
    </div>
    <BrandsList/>
  </div>
</template>

<script>
import BrandsList from "@/components/BrandsList";

export default {
  name: "Brands",
  data() {
    return {
      visibleCard: true,
      categoryId: null,
      slug: ''
    }
  },
  components: {
    BrandsList
  },
  computed: {
    activeCategoryId() {
      let a = 0;
      const b = this.slug;
      this.$store.getters.allCategories.forEach(function (item) {
        if (item.slug === b) {
          a = item.id
        }
      });
      return a
    }
  },
  methods: {},
  watch: {
    $route(to) {
      this.slug = to.params.slug;
    }
  },
  mounted() {
    this.slug = this.$route.params.slug;
  }
}
</script>

<style scoped>
.content-text {
  width: 1580px;
  margin: 0 auto;
  padding: 20px;
  text-align: justify;
}

.content-text span {
  line-height: 1.7;
}

/*media queries******************************************************************************************************/
@media screen and (max-width: 1200px) {
  .content-text {
    width: auto;
  }

  .content-text span {
    font-size: 0.7rem;
    line-height: normal;
  }
}

@media screen and (max-width: 960px) {
  .content-text {
    width: auto;
  }

  .content-text span {
    font-size: 0.7rem;
    line-height: normal;
  }
}


@media screen and (max-width: 750px) {
  .content-text {
    width: auto;
  }

  .content-text span {
    font-size: 0.7rem;
    line-height: normal;
  }
}

@media screen and (max-width: 420px) {
  .content-text {
    width: auto;
  }

  .content-text span {
    font-size: 0.7rem;
    line-height: normal;
  }
}

@media screen and (max-width: 375px) {
  .content-text {
    width: auto;
  }

  .content-text span {
    font-size: 0.7rem;
    line-height: normal;
  }
}

@media screen and (max-width: 360px) {
  .content-text {
    width: auto;
  }

  .content-text span {
    font-size: 0.7rem;
    line-height: normal;
  }
}

@media screen and (max-width: 320px) {
  .content-text {
    width: auto;
  }

  .content-text span {
    font-size: 0.7rem;
    line-height: normal;
  }
}

@media screen and (max-width: 280px) {

}

</style>