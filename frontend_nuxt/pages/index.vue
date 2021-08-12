<template>
  <div class="home">
    <h1>Home</h1>
  </div>
</template>

<script>
export default {
  data() {
    return {
      layouts: 'default',
      arrayOfObjects: ['vbcvbc', 'hhhhhhhhhhhhhhhf'],
      object: {
        name: 'Object Name',
      }
    }
  },
  methods: {
    methodToRunOnSelect(payload) {
      this.object = payload;
    }
  }
}
</script>
<style scoped>
.my-dropdown-toggle {
  border-radius: 5px;
}

.home {
  width: 600px;
  margin: 0 auto;
  text-align: center;
  padding-top: 4rem;
}
</style>

