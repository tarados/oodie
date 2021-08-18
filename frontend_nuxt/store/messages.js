export const state = () => ({
  messages: {}
})

export const mutations = {
  setMessages(state, data) {
    state.messages = data
  }
}

export const actions = {
  async fetch({commit}) {
    console.log("fetch messages");
    const data = await this.$axios.$get('https://hoodiyalko.avallon.im/app/locales');
    const messages = processLocalization(data);
    commit('setMessages', messages);
    console.log("fetch success");
  }
}

export const getters = {
  messages: s => s.messages
}

function processLocalization(data) {
  const result = {};

  for (let localeKey in data) {
    result[localeKey.slice(0, 2)] = data[localeKey];
  }

  return result;
}
