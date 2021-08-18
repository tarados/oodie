export const state = () => ({
  locales: []
})

export const mutations = {
  setLocales(state, data) {
    state.locales = data
  }
}

export const actions = {
  nuxtServerInit ({ commit }, { req }) {
    // console.log("nuxtServerInit!!")
    // if (req.session.user) {
    //   commit('user', req.session.user)
    // }
  },
  async fetch({commit}) {
    const data = await this.$axios.$get('https://hoodiyalko.avallon.im/app/locales');
    let localesKey = Object.keys(data);
    let locales = [];
    localesKey.forEach(item => {
      locales.push(item.slice(0, 2));
    })
    commit('setLocales', locales);
  }
}

export const getters = {
  locales: s => s.locales
}
