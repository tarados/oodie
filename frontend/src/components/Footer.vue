<template>
  <div class="wrapper">
    <div class="wrapper-footer">
      <div class="footer">
        <div class="contacts">
          <div class="contacts-item">
            <span>Контакты:</span>
          </div>
          <div class="contacts-item">
            <img src="../assets/phone-receiver.svg"/>
            <router-link to="#">
              <p>+380507204066</p>
            </router-link>
          </div>
          <div class="contacts-item">
            <img src="../assets/email.svg">
            <p>hoodiyalko@gmail.com</p>
          </div>
        </div>
        <div class="social">
          <div class="social-icon">
            <div class="social-content">
<!--              <div class="circl">-->
<!--                <img src="../assets/facebook.png">-->
<!--              </div>-->
              <a href="https://www.facebook.com/hoodiyalko/">
                <p>facebook.com/hoodiyalko/</p>
              </a>
            </div>
            <div class="social-content">
<!--              <div class="circl">-->
<!--                <img src="../assets/instagram.png">-->
<!--              </div>-->
              <a href="https://www.instagram.com/hoodiyalko/">
                <p>instagram.com/hoodiyalko/</p>
              </a>
            </div>
            <div class="social-content">
<!--              <div class="circl">-->
<!--                <img src="../assets/tik-tok.png">-->
<!--              </div>-->
              <a href="https://www.tiktok.com/hoodiyalko/">
                <p>tiktok.com/hoodiyalko/</p>
              </a>
            </div>
          </div>
        </div>
        <div class="delivery">
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
  }
}
</script>

<style scoped>
.wrapper-footer {
  margin: 0;
  background-color: #c3d7d6;
}

.footer {
  display: grid;
  grid-template-columns: 1fr 1fr 2fr;
  grid-template-rows: 9em;
  grid-template-areas: "contacts delivery social";
  align-items: center;
  justify-items: center;
}

.contacts {
  grid-area: contacts;
}

.contacts-item {
  display: flex;
  flex-wrap: nowrap;
  align-items: flex-end;
}

.contacts-item a,
.contacts-item p {
  margin: 0 1.2vmin;
  text-decoration: none;
  cursor: pointer;
  color: black;
}

.contacts-item img {
  width: 3vmin;
}

.delivery {
  grid-area: delivery;
}

.contacts,
.delivery {
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: space-around;
}

.social {
  grid-area: social;
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



.contacts span {
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