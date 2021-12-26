<template>
  <div class="home">
    <header class="showcase">
      <div class="container showcase-inner">
        <img alt="banner" src="~/assets/img/banner4.jpg"/>
      </div>
    </header>
    <div class="content-wrapper">
      <div class="info">
        <div class="info-content">
          <div class="wrapper-image">
            <img alt="size" src="~/assets/img/size.png">
          </div>
          <div class="info-title">
            <h4>{{ $t('InfoSize') }}</h4>
            <span>{{ $t('InfoSizeDescription') }}</span>
          </div>
        </div>
        <div class="info-content">
          <div class="wrapper-image cat">
            <img alt="cat" src="~/assets/img/cat.png">
          </div>
          <div class="info-title">
            <h4>{{ $t('InfoCat') }}</h4>
            <span>{{ $t('InfoCatDescription') }}</span>
          </div>
        </div>
        <div class="info-content">
          <div class="wrapper-image footer-content__item">
            <img alt="delivery" src="~/assets/img/delivery.png">
          </div>
          <div class="info-title">
            <h4>{{ $t('InfoDelivery') }}</h4>
            <span>{{ $t('InfoDeliveryDescription') }}</span>
          </div>
        </div>
      </div>
    </div>
    <ProductsList :ctg="1"/>
    <Slider :slides="slides" /><!-- TODO: create component InstagramSlider and move slides to this component -->
  </div>
</template>

<script>

export default {
  name: "Home",
  middleware: ['products'],
  head() {
    return {
      title: this.title,
      meta: [
        {
          hid: 'description',
          name: 'description',
          content: this.description
        },
        {name: 'keywords', content: 'худиялко, бренды друзья'}
      ]
    }
  },
  computed: {
    title() {
      if (!this.$store.getters['home/home']) {
        return '';
      }
      return this.$t(this.$store.getters['home/home']);
    },
    description() {
      if (!this.$store.getters['description/description']) {
        return '';
      }
      return this.$t(this.$store.getters['description/description']);
    },
    slides() {
      if (!this.$store.getters['instagram/slides'].length > 0) {
        return [];
      }
      return this.$store.getters['instagram/slides']
    }
  }
}
</script>
<style scoped>
.home {
  margin: 0 auto 2rem;
}

.content-wrapper {
  max-width: 1240px;
  margin: 40px auto 40px;
  padding: 0 10px;
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
  text-align: start;
}

.info-content + .info-content {
  margin-left: 80px;
  padding-left: 80px;
  border-left: 2px solid #d2d2d2;
}

.info-content .info-title {
  margin: 0 2vmin;
}

.wrapper-image {
  width: 3.5rem;
  height: 2.5rem;
  position: relative;
}

.wrapper-image.footer-content__item {
  margin-right: 1rem;
}

.wrapper-image img {
  position: absolute;
  left: 0;
  top: 0;
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
</style>

