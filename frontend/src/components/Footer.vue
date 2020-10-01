<template>
  <div class="wrapper-footer">
    <div class="container">
      <div class="footer_row">
        <div class="contacts">
          <div class="contacts-item">
            <span>Контакты:</span>
          </div>
          <div class="contacts-item phone">
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
        <div class="delivery">
          <p>Доставка и оплата</p>
          <p>Сотрудничество</p>
          <p>Обмен и возврат</p>
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
  background-color: var(--overlay-color);
}

.container {
  max-width: 1240px;
  margin: 0 auto;
}

.footer_row {
  display: flex;
}

.contacts,
.delivery,
.social {
  padding: 50px 0;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.contacts {
  width: 40%;
}

.delivery {
  width: 35%;
}

.contacts-item {
  display: flex;
  flex-wrap: nowrap;
  align-items: flex-end;
}

.phone {
  padding-bottom: 10px;
}

.contacts-item a,
.contacts-item p {
  text-decoration: none;
  cursor: pointer;
  color: black;
}

.contacts-item img{
  margin-right: 15px;
}

.contacts-item img,
.circl img {
  width: 22px;
}

.circl img {
  margin-top: 8px;
}

.social {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.social-icons {
  display: flex;
  flex-wrap: wrap;
}

.social-content {
  margin-right: 15px;
}

.circl {
  margin: 2% 5% 1% 0;
  width: 40px;
  height: 40px;
  text-align: center;
  background: white;
  border-radius: 50%;
}

span,
p {
  font-size: calc(10px + 8 * (100vw / 1838));
}

.contacts-item span {
  padding-bottom: 10px;
  text-transform: uppercase;
}

/*media queries*****************************************/

@media screen and (max-width: 750px) {
  .container {
    width: calc(100vw - 20px);
    margin: 0 auto;
  }

  .footer_row {
    justify-content: space-between;
  }

  .contacts {
    display: none;
  }

  span,
  p {
    font-size: calc(10px + (8 + 8 * 0.7) * ((100vw - 320px) / 1838));
  }

  .delivery {
    width: auto;
  }

  .social {
    width: auto;
  }

}
</style>
