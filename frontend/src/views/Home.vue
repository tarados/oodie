<template>
  <div>
    <header class="showcase">
      <div class="container showcase-inner">
        <img src="../assets/banner3.jpg"/>
<!--        <h1>Winter Sale Now On!</h1>-->
<!--        <p>One size fits all hooded blanket perfect for those chilly mornings and cold afternoons!</p>-->
<!--        <router-link :to="{name: 'Brands'}" class="btn">BUY NOW</router-link>-->
      </div>
    </header>
    <div class="info">
      <div class="info-content">
        <img src="../assets/size.png">
        <div class="info-title">
          <h4>Один размер</h4>
          <span>Подходит для всех</span>
        </div>
      </div>
      <div class="info-content">
        <img src="../assets/cat.png">
        <div class="info-title">
          <h4>теплое и очень мягкое</h4>
          <span>как котик</span>
        </div>
      </div>
      <div class="info-content">
        <img src="../assets/delivery.png">
        <div class="info-title">
          <h4>бесплатная доставка</h4>
          <span>для заказов от 2000 грн</span>
        </div>
      </div>
    </div>
    <ProductsList :category-id="categoryId" />
    <Instagram/>
  </div>
</template>

<script>
import ProductsList from "../components/ProductsList";
import Instagram from "@/components/Instagram";

export default {
  name: 'Home',
  data() {
    return {
    }
  },
  components: {
    ProductsList,
    Instagram
  },
  computed: {
    categoryId() {
      return 1
    }
  },
  methods: {
    basketVisible() {
      if (this.$store.state.productsStore.basketVisible) ;
      else (this.$store.dispatch('changeVisibleBasket'));
    }
  },
  mounted() {
    this.basketVisible();
  }
}
</script>

<style scoped>
.container {
  /*max-width: 960px;*/
  margin: auto;
  overflow: hidden;
  padding: 0.3rem;
}

.showcase {
  content: '';
  /*background: url("../assets/banner.png") no-repeat center;*/
  width: 100%;
  /*height: 35vmax;*/
  margin-bottom: 5vmin;
  text-align: center;
}

.showcase img {
  width: 100%;
  max-width: 1200px;
  height: auto;
}

.showcase .showcase-inner {
  /*display: flex;*/
  /*flex-direction: column;*/
  /*align-items: center;*/
  /*justify-content: center;*/
  /*text-align: center;*/
  /*color: white;*/
  /*height: 100%;*/
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

.info {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  align-items: center;
  margin: 0 15%;
}


.info-content {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: center;
}

.info-content:last-child {
  margin-right: 5vmin;
  border-left: 1px solid grey;
}

.info-content:first-child {
  border-right: 1px solid grey;
}

.info-content .info-title {
  margin: 0 2vmin;
}

.info-content img {
  width: calc(5vmin + 5 * (100vw / 1838));
}

.info-content .info-title h4 {
  padding: 1.1vmin 0;
  font-size: calc(1.8vmin + 2 * (100vw / 1838));
  font-weight: 500;
}

.info-content .info-title span {
  font-size: calc(1.5vmin + 2 * (100vw / 1838));
  color: #b0b0b0;
}

.info-content .info-title span,
h4 {
  text-transform: uppercase;
  letter-spacing: 1px;
}


/*media queries********************************************************************************************/

@media screen and (max-width: 1240px) {
  .info-content .info-title h4 {
    font-size: calc(1.3vmin + 2 * (100vw / 1240));
  }

  .info-content .info-title span {
    font-size: calc(1vmin + 2 * (100vw / 1240));
  }

  .info-content img {
    width: calc(3.5vmin + 3 * (100vw / 1240));
  }

  .info {
    /*margin: 0 16%;*/
  }
}

@media screen and (max-width: 1040px) {
  .info-content .info-title h4 {
    font-size: calc(1.3vmin + 2 * (100vw / 1024));
  }

  .info-content .info-title span {
    font-size: calc(1vmin + 2 * (100vw / 1024));
  }

  .info-content img {
    width: calc(3.5vmin + 3 * (100vw / 1024));
  }
}

@media screen and (max-width: 960px) {
  .info-content .info-title h4 {
    font-size: calc(0.8vmin + 1 * (100vw / 960));
  }

  .info-content .info-title span {
    font-size: calc(0.6vmin + 1 * (100vw / 960));
  }

  .info-content img {
    width: calc(2vmin + 2 * (100vw / 960));
  }

  .info {
    /*margin: 0 18%;*/
  }
}

@media screen and (max-width: 750px) {
  .info {
    display: none;
  }

  /*.showcase {*/
  /*  height: 490px;*/
  /*}*/
}

@media screen and (max-width: 420px) {

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

}


</style>
