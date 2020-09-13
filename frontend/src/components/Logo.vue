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
  margin-top: 2rem;
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;

}

img {
  width: 41.495rem;
  margin: 0 auto;
}


/*media queries*************************************************************************************/
@media screen and (max-width: 1024px) {
  .wrapper-logo {
    margin-bottom: 1.7rem;
  }

  img {
    width: 45vmax;
  }
}

@media screen and (max-width: 640px) {
  .wrapper-logo {
    margin-bottom: 1.7rem;
  }

  img {
    width: 45vmax;
  }
}

@media screen and (max-width: 420px) {
  .wrapper-logo {
    margin-bottom: 1.7rem;
  }

  img {
    width: 45vmax;
  }
}

@media screen and (max-width: 375px) {
  .wrapper-logo {
    margin-bottom: 1.6rem;
  }

  img {
    width: 45vmax;
  }
}

@media screen and (max-width: 360px) {
  .wrapper-logo {
    margin-bottom: 1.7rem;
  }

  img {
    width: 45vmax;
  }
}

@media screen and (max-width: 325px) {
  .wrapper-logo {
    margin-bottom: 1.7rem;
  }

  img {
    width: 45vmax;
  }
}

@media screen and (max-width: 280px) {
  img {
    width: 40vmax;
  }
}
</style>