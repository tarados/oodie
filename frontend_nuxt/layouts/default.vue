<template>
  <div class="default">
    <Navbar/>
    <nuxt/>
    <Footer/>
    <ModalError
      v-show="showModal"
      @close="closeModal"
      :warning-content="warningContent"
      :header-text="headerText"
    />
  </div>
</template>

<script>

export default {
  name: "default",
  data() {
    return {
      isModalVisible: false,
      warningContent: '',
      headerText: 'ErrorHeaderText'
    };
  },
  created() {
    this.$nuxt.$on('close', () => {
      this.isModalVisible = false;
      this.$store.commit('error/clearError');
    });
  },
  computed: {
    showModal() {
      if (this.$store.getters['error/getError']) {
        this.warningContent = String(this.$store.getters['error/getError']);
        return true;
      }
      return false;
    }
  },
  methods: {
    closeModal() {
      this.isModalVisible = !this.isModalVisible;
    }
  }
}
</script>

<style scoped>
.default {
  position: relative;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  overflow-x: hidden;
}

</style>
