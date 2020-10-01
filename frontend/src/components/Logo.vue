<template>
  <div class="wrapper-logo">
    <router-link :to="{name: 'Home'}">
      <img src="../assets/logo2.png">
    </router-link>
  </div>
</template>

<script>
export default {
  name: "logo",
};
</script>

<style scoped>
.wrapper-logo {
  display: flex;
  justify-content: center;
  align-items: center;
  align-self: center;
  margin-top: 50px;
  margin-bottom: 40px;

}

img {
  width: 80%;
  max-width: 400px;
  margin: 0 auto;
}


/*media queries*************************************************************************************/
@media screen and (max-width: 1024px) {
  /*.wrapper-logo {*/
  /*  margin-bottom: 1.7rem;*/
  /*}*/

}

@media screen and (max-width: 750px) {
  .wrapper-logo {
    margin-bottom: calc(1vw + 16 * (100vw / 750));
  }

}

@media screen and (max-width: 420px) {
  .wrapper-logo {
    margin-bottom: calc(6vw + 12 * (100vw / 420));
  }

}

@media screen and (max-width: 375px) {
  .wrapper-logo {
    margin-bottom: calc(6vw + 12 * (100vw / 375));
  }

}

@media screen and (max-width: 360px) {
  .wrapper-logo {
    margin-bottom: calc(6vw + 12 * (100vw / 360));
  }
}

@media screen and (max-width: 325px) {
  .wrapper-logo {
    margin-bottom: calc(6vw + 12 * (100vw / 325));
  }

}

@media screen and (max-width: 280px) {
  .wrapper-logo {
    margin-bottom: calc(6vw + 12 * (100vw / 280));
  }
}
</style>
