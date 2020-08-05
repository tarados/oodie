<template>
  <div class="wrapper-footer">
    <div class="footer">
      <div class="footer-item">
        <div class="contact-title">Контакты</div>
        <div class="contact-phone">
          <p>Телефон</p>
          <p>+380 50 720 40 66</p>
        </div>
      </div>
      <div class="footer-item">
        <div class="follow-us-title">
          <p>Подписывайтесь на нас</p>
        </div>
        <div class="social-icon">
          <div class="circl">
            <img src="../assets/facebook.png">
          </div>
          <div class="circl">
            <img src="../assets/instagram.png">
          </div>
          <div class="circl">
            <img src="../assets/tik-tok.png">
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Footer",
  data() {
    return {
      iconList: [
        "../assets/instagram.png",
        "../assets/instagram.png"
      ]
    }
  },
  mounted() {
    // console.log(this.iconList);
  }
}
</script>

<style scoped>
.wrapper-footer {
  margin: 4vh 0 0;
  background-color: rgb(134, 168, 213);
}

.footer {
  width: 1200px;
  margin: 0 auto;
  height: 9rem;
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
}

.footer-item {
  margin: 0 1rem;
  width: calc((100% / 12) * 6 - 2rem);
  height: 100%;
  color: white;
}

.contact-title,
.follow-us-title {
  font-size: 1.5rem;
  font-weight: 700;
  margin: 1rem 0;
}

.contact-phone {
  font-size: 1.2rem;
  line-height: 1.9rem;
}

.social-icon {
  display: flex;
  flex-wrap: wrap;
}

.circl {
  margin: 0 1rem;
  width: 40px;
  height: 40px;
  text-align: center;
  background: white;
  border-radius: 50%;
}

img {
  width: 20px;
  margin-top: 25%;
}

/*media queries*****************************************/
@media screen and (max-width: 1200px) {
  .footer {
    width: auto;
  }

  .footer-item {
    width: 44%;
    margin: 0;
  }

  .contact-title,
  .follow-us-title {
    font-size: calc((100vw - 30rem) / 50 * 0.5 + 1rem);
  }
}

@media screen and (max-width: 750px) {
  .contact-title {
    font-size: calc((100vw - 30rem) / 50 * 0.5 + 1rem);
  }
}

@media screen and (max-width: 650px) {

}

@media screen and (max-width: 450px) {
  .footer-item {
    width: 44%;
    margin: 0;
  }

  .contact-title {
    font-size: calc((100vw - 30rem) / 50 * 0.5 + 1rem);
  }

  .contact-phone {
    font-size: calc((100vw - 30rem) / 50 * 0.2 + 1rem);
    line-height: 1.4rem;
  }

  .circl {
    margin: 4%;
    width: 2rem;
    height: 2rem;
  }

  img {
    width: 1rem;
    margin-top: 25%;
  }

}

@media screen and (max-width: 320px) {
  .contact-phone {
    font-size: calc((100vw - 30rem) / 51 + 1rem);
  }

  .circl {
    margin: 3%;
  }
}
</style>