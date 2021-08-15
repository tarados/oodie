export const state = () => ({
  locales: [],
  messages: {}
})

export const mutations = {
  setLocales(state, data) {
    state.locales = data
  },
  setMessages(state, data) {
    state.messages = data
  }
}

export const actions = {
  async fetch({commit}) {
    const data = await this.$axios.$get('https://hoodiyalko.avallon.im/app/locales');
    let localesKey = Object.keys(data);
    let locales = [];
    const messages = processLocalization(data);
    localesKey.forEach(item => {
      locales.push(item.slice(0, 2));
    })
    commit('setLocales', locales);
    commit('setMessages', messages);
  }
}

export const getters = {
  locales: s => s.locales
}

function processLocalization(data) {
  const result = {};

  for (let localeKey in data) {
    result[localeKey.slice(0, 2)] = data[localeKey];
  }

  return result;
}
