<template>
  <div class="modal-backdrop">
    <div class="modal">
      <header class="modal-header">
        {{ $t(`${headerText}`) }}
      </header>
      <section class="modal-body">
        {{ message }}
      </section>
      <footer class="modal-footer">
        <button @click="close">
          OK
        </button>
      </footer>
    </div>
  </div>
</template>

<script>
export default {
  name: "error",
  data() {
    return {
      message: '',
      headerText: 'ErrorHeaderText'
    }
  },
  created() {
    this.message = this.$nuxt.nuxt.err.message;
  },
  methods: {
    close() {
      this.$router.push('/');
    }
  }
}
</script>

<style scoped>
.modal-backdrop {
  position: fixed;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  background-color: rgba(0, 0, 0, 0.3);
  display: flex;
  justify-content: center;
  align-items: center;
}

.modal {
  background: #FFFFFF;
  box-shadow: 2px 2px 20px 1px;
  overflow-x: auto;
  display: flex;
  flex-direction: column;
  margin: 0 15px;
  border-radius: 3px;
}

.modal-header,
.modal-footer {
  padding: 15px;
  display: flex;
}

.modal-header {
  border-bottom: 1px solid #eeeeee;
  color: black;
  text-transform: uppercase;
  justify-content: center;
}

.modal-footer {
  border-top: 1px solid #eeeeee;
  justify-content: center;
}

.modal-body {
  position: relative;
  padding: 20px 10px;
  text-transform: uppercase;
}

button {
  height: 5vh;
  width: 10vh;
  color: black;
  background: rgb(75, 218, 70);
  border: none;
  border-radius: 3px;
}
</style>
