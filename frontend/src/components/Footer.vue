<template>
  <div class="wrapper">
    <h2> ты с нами в instagram?</h2>
    <div class="hello-instagram"></div>
    <div class="wrapper-footer">
      <div class="footer">
        <div class="footer-item">
          <p>Контакты:</p>
          <p>+380 50 720 40 66</p>
          <p>hoodiyalko@gmail.com</p>
        </div>
        <div class="footer-item">
          <div class="social-icon">
          <p>Подписывайтесь на нас:</p>
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
        <div class="footer-item">
          <p>Доставка и оплата</p>
          <p>Сотрудничество</p>
          <p>Обмен и возврат</p>
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
  margin: 0;
  background-color: #c3d7d6;
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
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  margin: 0 1rem;
  padding: 1%;
  width: calc((100% / 12) * 4 - 2rem);
  height: 100%;
  color: black;
}

.social-icon {
  display: flex;
  flex-direction: column;
}

.circl {
  margin: 1% 1% 1% 20%;
  width: 1.8rem;
  height: 1.8rem;
  text-align: center;
  background: white;
  border-radius: 50%;
}

img {
  width: 0.9rem;
  margin-top: 25%;
}

h2 {
  text-align: center;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  font-weight: 100;
}

.hello-instagram {
  height: 14rem;
  margin-bottom: 1%;
  background-image: url("../assets/insta.jpg");
  background-repeat: no-repeat;
  background-size: cover;
}

p {
  font-weight: bold;
}

/*media queries*****************************************/
@media screen and (max-width: 1200px) {
  .footer {
    width: auto;
  }

  h2 {
    font-size: calc((100vw - 30rem) / 50 * 0.5 + 1rem);
  }
}

@media screen and (max-width: 750px) {
  h2 {
    font-size: calc((100vw - 30rem) / 50 * 0.5 + 1rem);
  }

  .hello-instagram {
    height: 4.15rem;
  }
}

@media screen and (max-width: 450px) {
  h2 {
    font-size: calc((100vw - 30rem) / 50 * 0.5 + 1rem);
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
  p,
  h2 {
    font-size: 0.55rem;
    margin-bottom: 5%;
  }

  .footer-item {
    justify-content: center;
  }

  .circl {
    margin: 3%;
  }

  .hello-instagram {
    height: 4.15rem;
  }
}
</style>