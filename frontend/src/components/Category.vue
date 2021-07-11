<template>
  <div class="wrapper-category">
    <div class="container-flex">
      <div
          ref="category"
          v-show="category.id !== 1"
          class="category-item"
          :class="{active: selectedCategoryId === category.id}"
          v-for="category in categories" :key="category.id"
          @click="onChoice(category)"
      >
        {{ category.title }}
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Category",
  props: {
    categories: {
      type: Array
    },
    selectedCategoryId: {
      type: Number
    }
  },
  methods: {
    onChoice(category) {
      if (this.selectedCategoryId === category.id) {
        this.$router.push({path: '/brands'}).catch(() => {
        });
      } else {
        this.$router.push({path: '/brands/' + category.slug}).catch(() => {
        });
      }
    }
  }
}
</script>

<style scoped>
.wrapper-category {
  max-width: 1200px;
  margin: 0 auto;
  padding: 1%;
}

.container-flex {
  margin-top: 1%;
  height: 2rem;
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
}

.header {
  margin: 0;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  font-size: 1.4375em;
  align-self: center;
}

.categories {
  width: 40%;
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  align-items: center;
}

.category-item {
  margin-left: 1rem;
  background-color: white;
  cursor: pointer;
  user-select: none;
  font-size: 1rem;
  text-transform: uppercase;
  padding: 2%;
  outline: none;
}

.category-item:hover,
.category-item.active {
  background: #e8bd67;
  border-radius: 3rem;
}

.target {
  background: #e8bd67;
  border-radius: 3rem;
}

@media screen and (max-width: 960px) {
  .header {
    font-size: calc((100vw - 30rem) / 50 * 0.5 + 1rem);
    text-align: center;
    margin: 5% auto;
  }

  .category-item {
    font-size: calc((100vw - 30rem) / 50 + 1rem);
  }
}

@media screen and (max-width: 750px) {

}

@media screen and (max-width: 650px) {

}

@media screen and (max-width: 420px) {
  .container-flex {
    display: block;
  }

  .categories {
    justify-content: space-around;
    width: 100%;
  }
}
</style>