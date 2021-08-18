export const state = () => ({
  test: "initial"
})

export const mutations = {
  setTest(state, value) {
    state.test = value;
  }
}

export const actions = {
  async nuxtServerInit ({ commit, dispatch }, { req }) {
    console.log("nuxtServerInit");
    commit("setTest", "foo");
    // await dispatch('locales/fetch');
    // await dispatch('messages/fetch');
    // console.log("sss");
  },

  nuxtClientInit (context) {
    console.log("nuxtClientInit", context);
    // i18n._vm.messages = store.getters['messages/messages'];
  }
}
