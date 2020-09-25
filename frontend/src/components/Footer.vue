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
          <div class="social-title">
            <span>Мы в соцсетях:</span>
          </div>
          <div class="social-icons">
            <div class="social-content">
              <div class="circl">
                <a href="https://www.facebook.com/hoodiyalko/">
                  <img src="../assets/facebook.png">
                </a>
              </div>
            </div>
            <div class="social-content">
              <div class="circl">
                <a href="https://www.instagram.com/hoodiyalko/">
                  <img src="../assets/instagram.png">
                </a>
              </div>
            </div>
            <div class="social-content">
              <div class="circl">
                <a href="https://www.tiktok.com/hoodiyalko/">
                  <img src="../assets/tik-tok.png">
                </a>
              </div>
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
  grid-template-rows: calc(15vmin + 15 * (100vw / 1838));
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

.contacts-item img,
.circl img {
  width: calc(2vmin + 8 * (100vw / 1838));
}

.circl img {
  margin-top: calc(1vmin + 1 * (100vw / 1838));
}

.delivery {
  grid-area: delivery;
}

.contacts,
.delivery,
.social {
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: space-around;
}

.social {
  grid-area: social;
  width: calc(15vmin + 15 * (100vw / 1838));
}

.social-icons {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
}

.social-content {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: flex-start;
}

.circl {
  margin: 2% 5% 1% 0;
  width: calc(3vmin + 14 * (100vw / 1838));
  height: calc(3vmin + 14 * (100vw / 1838));
  text-align: center;
  background: white;
  border-radius: 50%;
}

span,
p {
  font-size: calc(1vmin + 12 * (100vw / 1838));
}

.contacts span {
  text-transform: uppercase;
}

/*media queries*****************************************/
@media screen and (max-width: 1200px) {

}

@media screen and (max-width: 750px) {
  .footer {
    grid-template-rows: calc(15vmin + 15 * (100vw / 750));
  }

  span,
  p {
    font-size: calc(1vmin + 6 * (100vw / 750));
  }

  .social {
    width: calc(15vmin + 15 * (100vw / 750));
  }

  .contacts-item img,
  .circl img {
    width: 3vmin;
  }

  .circl img {
    margin-top: calc(1vmin + 1 * (100vw / 750));
  }

  .circl {
    width: calc(3vmin + 14 * (100vw / 750));
    height: calc(3vmin + 14 * (100vw / 750));
  }
}

@media screen and (max-width: 450px) {

}

@media screen and (max-width: 320px) {

}

</style>