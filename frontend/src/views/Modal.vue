<template>
  <transition name="modal-fade">
    <div class="modal-backdrop">
      <div class="modal">
        <div class="modal_item" v-for="(warning, index) in warningList" :key="index">
          {{warning.title}}
          <div class="modal_item__title">{{ warning.title }}</div>
          <div class="modal_item__title">{{ warning.currentAvailability }}</div>
        </div>
        <button
            type="button"
            class="btn-green"
            @click="close"
        >
          Close me!
        </button>
      </div>
    </div>
  </transition>
</template>

<script>
export default {
  name: 'modal',
  props: {
    warningList: {
      type: Array
    }
  },
  methods: {
    close() {
      this.$router.go(-1);
    },
  },
  mounted() {
    this.warningList;
    console.log('modal: ', this.warningList);
  }
};
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
  width: 70vw;
  height: 50%;
  background: #FFFFFF;
  box-shadow: 2px 2px 20px 1px;
  overflow-x: auto;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.modal-header,
.modal-footer {
  padding: 15px;
  display: flex;
}

.modal-footer {
  border-top: 1px solid #eeeeee;
  justify-content: flex-end;
}

.modal-body {
  position: relative;
  padding: 20px 10px;
}

.btn-green {
  margin: 2rem;
  width: 12vw;
  height: 2rem;
  color: white;
  background: #4AAE9B;
  border: 1px solid #4AAE9B;
  border-radius: 2px;
}

.modal-fade-enter,
.modal-fade-leave-active {
  opacity: 0;
}

.modal-fade-enter-active,
.modal-fade-leave-active {
  transition: opacity .5s ease
}
</style>
