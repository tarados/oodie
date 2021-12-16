<template>
  <div class="container">
    <div class="orderSuccessful">
      <p>{{ $t('SuccessfulMessageOne') }}</p>
      <p>{{ $t('SuccessfulMessageTwo') }}</p>
      <button @click="backToMain">{{ $t('SuccessfulToHome') }}</button>
    </div>
  </div>

</template>

<script>

export default {
  name: "Successful",
  head() {
    return {
      title: this.$t('SuccessfulMessageOne')
    }
  },
  components: {},
  methods: {
    backToMain() {
      this.$router.push('/');
    }
  }
}
</script>

<style scoped>

.orderSuccessful {
  text-align: center;
  margin: 20px 0;
  padding: 15px;
  border-radius: 3px;
}

p {
  font-size: 25px;
  font-weight: 600;
}

.thumbnail {
  width: 320px;
  height: 240px;
}

.image {
  width: 100%;
  height: 100%;
}

.image img {
  -webkit-transition: all 1s ease; /* Safari and Chrome */
  -moz-transition: all 1s ease; /* Firefox */
  -ms-transition: all 1s ease; /* IE 9 */
  -o-transition: all 1s ease; /* Opera */
  transition: all 1s ease;
}

.image:hover img {
  -webkit-transform: scale(1.25); /* Safari and Chrome */
  -moz-transform: scale(1.25); /* Firefox */
  -ms-transform: scale(1.25); /* IE 9 */
  -o-transform: scale(1.25); /* Opera */
  transform: scale(1.25);
}

.orderSuccessful button {
  margin-top: 32px;
  padding: 16px 32px;
  background-color: green;
  color: white;
  text-transform: uppercase;
  border: none;
  font-size: 18px;
}

</style>
