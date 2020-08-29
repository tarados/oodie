<template>
  <div class="wrapper">
    <img src="../assets/logo.jpg">
  </div>
</template>

<script>
export default {
  name: "logo"
}
</script>

<style scoped>
.wrapper {

}

img {
  width: 45rem;
  margin: 0 auto;
}

/*media queries*************************************************************************************/
@media screen and (max-width: 750px) {

}

@media screen and (max-width: 640px) {

}

@media screen and (max-width: 420px) {
  .logo img {
    width: 18rem;
  }
}

@media screen and (max-width: 375px) {

}


@media screen and (max-width: 360px) {

}

@media screen and (max-width: 325px) {
  .logo img {
    width: 16rem;
  }
}

@media screen and (max-width: 280px) {
  .logo img {
    width: 14rem;
  }
}
</style>