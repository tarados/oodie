<template>
  <div class="wrapper">
    <div class="wrapper-footer">
      <div class="footer">
        <div class="footer-item">
          <p class="contacts">Контакты:</p>
          <p>+380 50 720 40 66</p>
          <p>hoodiyalko@gmail.com</p>
        </div>
        <div class="footer-item">
          <div class="social-icon">
            <div class="social-content">
              <div class="circl">
                <img src="../assets/facebook.png">
              </div>
              <a href="https://www.facebook.com/hoodiyalko/">
                <p>facebook.com/hoodiyalko/</p>
              </a>
            </div>
            <div class="social-content">
              <div class="circl">
                <img src="../assets/instagram.png">
              </div>
              <a href="https://www.instagram.com/hoodiyalko/">
                <p>instagram.com/hoodiyalko/</p>
              </a>
            </div>
            <div class="social-content">
              <div class="circl">
                <img src="../assets/tik-tok.png">
              </div>
              <a href="https://www.tiktok.com/hoodiyalko/">
                <p>tiktok.com/hoodiyalko/</p>
              </a>
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
  justify-content: space-around;
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

.social-content {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: flex-start;
}

.circl {
  margin: 2% 5% 1% 0;
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

p.contacts {
  text-transform: uppercase;
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