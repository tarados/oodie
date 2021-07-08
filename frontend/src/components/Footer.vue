<template>
  <div class="wrapper-footer">
    <div class="container">
      <div class="footer-content">
        <div class="footer-content__item">
          <div class="footer-content__item--contacts">
            <span>{{ 'FooterContacts' | localize }}:</span>
          </div>
          <div class="footer-content__item--contacts">
            <img src="../assets/phone-receiver.svg"/>
            <a href="tel:+380507204066">
              <span>+380507204066</span>
            </a>
          </div>
          <div class="footer-content__item--contacts">
            <img src="../assets/email.svg">
            <a href="mailto:hoodiyalko@gmail.com" rel="noopener">
              <span>hoodiyalko@gmail.com</span>
            </a>
          </div>
        </div>
        <div class="footer-content__item">
          <div class="footer-content__item--delivery">
            <router-link :to="{name: 'Delivery' }">
              <span>{{ 'FooterShipping' | localize }}</span>
            </router-link>
          </div>
          <div
              class="footer-content__item--delivery"
              @click="errorForSentry"
          >
            <span>{{ 'FooterCooperation' | localize }}</span>
          </div>
          <div class="footer-content__item--delivery">
            <span>{{ 'FooterExchange' | localize }}</span>
          </div>
        </div>
        <div class="footer-content__item">
          <div class="footer-content__item--social">
            <span>{{ 'FooterSocial' | localize }}</span>
          </div>
          <div class="footer-content__item--social">
            <div class="icon">
              <div class="icon__circl">
                <a target="_blank" href="https://www.facebook.com/hoodiyalko/" rel="noopener">
                  <img src="../assets/facebook.png">
                </a>
              </div>
            </div>
            <div class="icon">
              <div class="icon__circl">
                <a target="_blank" href="https://www.instagram.com/hoodiyalko/" rel="noopener">
                  <img src="../assets/instagram.png">
                </a>
              </div>
            </div>
            <div class="icon">
              <div class="icon__circl">
                <a target="_blank" href="https://vm.tiktok.com/ZS9y5cnx/" rel="noopener">
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
  methods: {
    errorForSentry() {
      throw Error('123');
    }
  }
}
</script>

<style scoped>
.wrapper-footer {
  background-color: var(--overlay-color);
  padding: 32px;
}

.container {
  max-width: 1240px;
  margin: 0 auto;
}

.footer-content {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
}

.footer-content__item {
  min-height: 120px;
  min-width: 136px;
  padding: 15px 0;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.footer-content__item:nth-child(1) .footer-content__item--contacts:nth-child(1) span {
  text-transform: uppercase;
}

.footer-content__item:nth-child(3) {
  min-width: 150px;
  align-items: center;
}

.footer-content__item--contacts {
  display: flex;
  flex-wrap: nowrap;
}

.footer-content__item span {
  padding: 0;
  text-decoration: none;
  cursor: pointer;
  color: black;
}

.footer-content__item--contacts img {
  margin-right: 15px;
}

.footer-content__item--contacts img,
.icon__circl img {
  width: 22px;
}

.icon__circl img {
  margin-top: 8px;
}

.footer-content__item--social {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
}

.footer-content__item--social:nth-child(2) {
  width: 100%;
}

.icon__circl {
  margin: 2% 5% 1% 0;
  width: 40px;
  height: 40px;
  text-align: center;
  background: white;
  border-radius: 50%;
}

.footer-content__item a {
  color: black;
  text-decoration: none;
}

.footer-content__item a:hover {
  text-decoration: underline;
}

@media screen and (max-width: 750px) {
  .footer-content__item:nth-child(1) {
    display: none;
  }

  span {
    font-size: 14px;
  }
}

@media screen and (max-width: 375px) {
  .wrapper-footer {
    padding: 32px 0;
  }
}

@media screen and (max-width: 320px) {
  .footer-content__item {
    padding: 10px 0;
    min-height: 100px;
  }

  .footer-content__item:nth-child(2) {
    min-width: 120px;
  }

  span {
    font-size: 12px;
  }
}

@media screen and (max-width: 280px) {
  .footer-content__item:nth-child(3) {
    min-width: 120px;
  }

  span {
    font-size: 11px;
  }
}
</style>
