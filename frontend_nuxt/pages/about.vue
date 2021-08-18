<template>

<div class="about">
  <h1>About {{test}} {{date}}</h1>
  <Test/>
</div>
</template>

<script>
import moment from 'moment';

export default {
  name: "about",
  computed: {
    test() { return this.$store.state.test },
    date() {
      return moment().format('MMMM Do YYYY, h:mm');
    }
  },
  mounted() {
    console.log("moment", moment().format('MMMM Do YYYY, h:mm:ss a'));
    console.log("state", this.$store.state.test, JSON.stringify(this.$store.state.messages.messages));
  },
}
</script>

<style scoped>
.about {
  width: 600px;
  margin: 0 auto;
  text-align: center;
  padding-top: 4rem;
}

</style>
