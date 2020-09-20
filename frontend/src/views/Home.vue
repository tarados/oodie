<template>
  <div>
    <header class="showcase">
      <div class="container showcase-inner">
        <h1>Winter Sale Now On!</h1>
        <p>One size fits all hooded blanket perfect for those chilly mornings and cold afternoons!</p>
        <router-link :to="{name: 'Brands'}" class="btn">BUY NOW</router-link>
      </div>
    </header>
    <div class="info">
      <div class="info-content size">
        <img src="../assets/size.png">
        <div class="info-title">
          <h4>Один размер</h4>
          <span>Подходит для всех</span>
        </div>
      </div>
      <div class="info-content cat">
        <img src="../assets/cat.png">
        <div class="info-title">
          <h4>теплое и очень мягкое</h4>
          <span>как котик</span>
        </div>
      </div>
      <div class="info-content delivery">
        <img src="../assets/delivery.png">
        <div class="info-title">
          <h4>бесплатная доставка</h4>
          <span>для заказов от 2000 грн</span>
        </div>
      </div>
    </div>
    <ProductsList thumbnail="large" :category-id="categoryId"/>
  </div>
</template>

<script>
import ProductsList from "../components/ProductsList";

export default {
  name: 'Home',
  data() {
    return {
      // visibleCard: true
    }
  },
  components: {
    ProductsList
  },
  computed: {
    categoryId() {
      return 1
    }
  },
  methods: {
    basketVisible() {
      if (this.$store.state.productsStore.basketVisible);
       else (this.$store.dispatch('changeVisibleBasket'));
      }
  },
  mounted() {
    this.basketVisible();
  }
}
</script>

<style scoped>
/*section one - header*****************************************************************************/
.container {
  max-width: 960px;
  margin: auto;
  overflow: hidden;
  padding: 0.3rem;
}

.showcase {
  content: '';
  background: url("../assets/tile.jpg") no-repeat center center/cover;
  width: 100%;
  height: 650px;
}

.showcase .showcase-inner {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  color: white;
  height: 100%;
}

.showcase h1 {
  font-size: 2.5rem;
}

.showcase p {
  font-size: 1.2rem;
}

.btn {
  display: inline-block;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  white-space: normal;
  font-size: 14px;
  border: none;
  border-radius: 3px;
  background-color: white;
  color: black;
  padding: 0.75rem 1.5rem;
  margin-top: 1rem;
  text-decoration: none;
  transition: opacity 1s ease-in;
}

.btn:hover {
  opacity: 0.7;
}


/*section two -  collections oodie******************************************************************/
.collections {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  align-items: center;
}

.wrapper_collections {
  padding: 55px;
}

.item_collections {
  flex: 0 1 50%;
}

.item_collections_image_wrapper {
  max-width: 436px;
  max-height: 545px;
  margin: 0 auto 19px;
  position: relative;
  width: 100%;
}

.item_collections_image {
  max-width: 436px;
  max-height: 545px;
}

.info {
  width: 85%;
  margin: 0 auto;
  height: 10rem;
  display: flex;
  flex-wrap: wrap;
  justify-content: space-around;
  align-items: center;
}

.info .info-content img {
  width: 4vmax;
  margin-right: 2%;
}

.info .delivery img {
  margin-top: 4%;
}

.info-content {
  height: 5vmax;
  display: flex;
  flex-wrap: wrap;
  justify-content: flex-start;
  align-items: center;
}

.size {
  width: 25%;
}

.cat {
  width: 35%
}

.delivery {
  width: 25%;
}

.cat,
.size {
  border-right: 1px solid grey;
}

.info-title {
  height: 4.5rem;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.info-content h4 {
  margin-top: 8%;
  font-size: 0.9vmax;
}

.info-content span {
  font-size: 1vmax;
}

.info-content span,
h4 {
  text-transform: uppercase;
  letter-spacing: 1px;
}


/*media queries********************************************************************************************/

@media screen and (max-width: 1024px) {

  .delivery {
    width: 28%;
  }

  .info-content h4 {
    margin-top: 11%;
    font-size: 0.8vmax;
  }

  .info-content span {
    font-size: 0.7vmax;
  }

  .info-title {
    height: 4vmax;
    justify-content: space-around;
  }
}

@media screen and (max-width: 750px) {
  .showcase {
    height: 490px;
  }
}

@media screen and (max-width: 420px) {
  .info {
    display: none;
  }
}

@media screen and (max-width: 375px) {
  .logo svg {
    width: 34vw;
  }
}

@media screen and (max-width: 360px) {
  .logo svg {
    width: 34vw;
  }
}

@media screen and (max-width: 320px) {
  .info .info-content img {
    width: 1.2rem;
  }

  .info-content h4,
  h5 {
    font-size: 0.3rem;
  }

  .info-title {
    justify-content: space-around;
  }

  .info-content {
    width: auto;
  }
}


</style>
