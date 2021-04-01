<template>
  <div id="app">
    <modal-vue
        modalSize="md"
        @on-close="$vm2.close('modal-4')"
        name="modal-4"
        :footerOptions="{
        btn1: 'Ok ',
        disableBtn2: true,
        btn1OnClick: () => {
          $vm2.close('modal-4');
        },
        justify: 'center'
      }"
    >
      <template v-slot:header>
        <div class="modal_title">
          Указанные количества неактуальны!
        </div>
      </template>
      <section>
        <div class="container-modal"
             v-for="(warning, index) in warningList" :key="index"
        >
          <p>{{ warning.title }}</p>
          <p>В наличии - {{ warning.currentAvailability }}</p>
        </div>
      </section>
      <div class="modal_petition">
        <span>Пожалуйста, удалите данный товар из корзины и закажите что-нибудь, что есть в наличии!</span>
      </div>
    </modal-vue>
  </div>
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
      this.$vm2.close("modal-4");
    }
  }
};
</script>

<style>
#app .modal_title {
  text-align: center;
  margin-top: 10px;
  font-weight: 600;
  text-transform: uppercase;
}

.container-modal {
  padding: 10px;
  display: grid;
  grid-template-columns: 55% 45%;
  grid-template-rows: 2rem;
}

.container-modal p {
  padding-left: 1rem;
  text-transform: uppercase;
}

div > div > div#vm2_box_modal-4.vm2_modal-content {
  padding: 10px;
}

.modal_petition span {
  text-transform: uppercase;
  text-align: justify;
  color: green;
}
</style>
