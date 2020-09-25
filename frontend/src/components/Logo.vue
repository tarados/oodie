<template>
  <div class="wrapper-logo">
    <img src="../assets/logo.jpg">
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

}

img {
  width: calc(35vw + 16 * (100vw / 1835));
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
  /*.wrapper-logo {*/
  /*  margin-bottom: 1.7rem;*/
  /*}*/

}

@media screen and (max-width: 375px) {
  /*.wrapper-logo {*/
  /*  margin-bottom: 1.6rem;*/
  /*}*/

}

@media screen and (max-width: 360px) {
  /*.wrapper-logo {*/
  /*  margin-bottom: 1.7rem;*/
  /*}*/

}

@media screen and (max-width: 325px) {
  /*.wrapper-logo {*/
  /*  margin-bottom: 1.7rem;*/
  /*}*/

}

@media screen and (max-width: 280px) {

}
</style>