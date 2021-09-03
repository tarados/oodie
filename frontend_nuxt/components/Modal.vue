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
        justify: 'center',
        btn1Style: {width: '15vh', textTransform: 'uppercase'}
      }"
    >
      <template v-slot:header>
        <div class="modal_title">
          {{ $t(headerText) }}
        </div>
      </template>
      <section>
        <div class="container-modal"
             v-for="(warning, index) in warningList" :key="index"
        >
          <p>{{ warning.title }}</p>
          <p>{{ $t(inStock) }} - {{ warning.currentAvailability }}</p>
        </div>
      </section>
      <div class="modal_petition">
        <span>{{ $t(commitText) }}</span>
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
    },
    headerText: {
      type: String
    },
    commitText: {
      type: String
    },
    inStock: {
      type: String
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
  margin: 10px;
  font-weight: 600;
  text-transform: uppercase;
}

.container-modal {
  padding: 1rem;
  display: grid;
  grid-template-columns: 55% 45%;
  grid-template-rows: 2rem;
}

.container-modal p {
  text-transform: uppercase;
}

div > div > div#vm2_box_modal-4.vm2_modal-content {
  padding: 10px;
}

.modal_petition {
  /*text-transform: uppercase;*/
  text-align: justify;
  padding: 1rem;
  /*color: green;*/
}
</style>
