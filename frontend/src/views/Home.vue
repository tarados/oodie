<template>
  <div>
    <header class="showcase">
      <div class="container showcase-inner">
        <img src="../assets/banner4.jpg"/>
      </div>
    </header>

    <div class="content-wrapper">
      <div class="info">
        <div class="info-content">
          <div class="wrapper-image">
            <img src="../assets/size.png">
          </div>
          <div class="info-title">
            <h4>Один размер</h4>
            <span>Подходит для всех</span>
          </div>
        </div>
        <div class="info-content">
          <div class="wrapper-image cat">
            <img src="../assets/cat.png">
          </div>
          <div class="info-title">
            <h4>теплое и очень мягкое</h4>
            <span>как котик</span>
          </div>
        </div>
        <div class="info-content">
          <div class="wrapper-image footer-content__item">
            <img src="../assets/delivery.png">
          </div>
          <div class="info-title">
            <h4>быстрая доставка</h4>
            <span>1-2 дня по Украине</span>
          </div>
        </div>
      </div>
    </div>
    <ProductsList :category-id="categoryId" />
    <InstaWidget />
  </div>
</template>

<script>
import ProductsList from "../components/ProductsList";
import InstaWidget from "../components/InstaWidget";


export default {
  name: 'Home',
  data() {
    return {
    }
  },
  components: {
    ProductsList,
    InstaWidget
  },
  computed: {
    categoryId() {
      return 1
    }
  },
  methods: {
    basketVisible() {
      if (!this.$store.state.productsStore.basketVisible) {
        this.$store.dispatch('changeVisibleBasket')
      }
    }
  },
  mounted() {
    this.basketVisible();
  }
}
</script>

<style scoped>
.content-wrapper {
  max-width: 1240px;
  margin: 40px auto 40px;
  padding: 0px 10px;
}


.container {
  margin: auto;
  overflow: hidden;
  padding: 0.3rem;
}

.showcase {
  content: '';
  width: 100%;
  margin-bottom: 5vmin;
  text-align: center;
}

.showcase img {
  width: 100%;
  height: auto;

}

.showcase .showcase-inner {
  padding: 0;
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
  display: flex;
  justify-content: center;
}


.info-content {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: center;
}

.info-content + .info-content {
  margin-left: 80px;
  padding-left: 80px;
  border-left: 2px solid #d2d2d2;
}

.info-content:last-child {
  /*margin-right: 5vmin;*/
  /*border-left: 1px solid grey;*/
}

.info-content:first-child {
  /*border-right: 1px solid grey;*/
}

.info-content .info-title {
  margin: 0 2vmin;
}

.wrapper-image {
  width: 40px;
  height: 40px;
  position: relative;
  /*margin-right: 8px;*/
}

.wrapper-image.footer-content__item {
  margin-right: 16px;
}

.wrapper-image.cat {
  /*height: 4px;*/
}

.wrapper-image img {
  position: absolute;
  left: 0;
  top: 0;
  /*width: 100%;*/
  height: 100%;
}

.info-content .info-title h4 {
  font-size: calc(10px + 5 * (100vw / 1838));
  font-weight: 500;
}

.info-content .info-title span {
  font-size: calc(8px + 4 * (100vw / 1838));
  color: #b0b0b0;
}

.info-content .info-title span,
h4 {
  text-transform: uppercase;
  letter-spacing: 1px;
}


/*media queries********************************************************************************************/

@media screen and (max-width: 1240px) {
  .info {
    margin: 0 auto;
  }
}
@media screen and (max-width: 1100px) {
  .info-content + .info-content {
    margin-left: 40px;
    padding-left: 40px;
  }
}

@media screen and (max-width: 960px) {
  .info-content + .info-content {
    margin-left: 40px;
    padding-left: 40px;
  }

  .info-content .info-title h4 {
    font-size: calc(10px + (5 + 5 * 0.7) * ((100vw - 750px) / 1838));
  }

  .info-content .info-title span {
    font-size: calc(8px + (4 + 4 * 0.7) * ((100vw - 750px) / 1838));
  }
}

@media screen and (max-width: 850px) {
  .info-content + .info-content {
    margin-left: 20px;
    padding-left: 20px;
  }
}

@media screen and (max-width: 750px) {
  .info {
    display: none;
  }

}

@media screen and (max-width: 420px) {

}

@media screen and (max-width: 375px) {
  /*.logo svg {*/
  /*  width: 34vw;*/
  /*}*/
}

@media screen and (max-width: 360px) {
  /*.logo svg {*/
  /*  width: 34vw;*/
  /*}*/
}

@media screen and (max-width: 320px) {

}


</style>
