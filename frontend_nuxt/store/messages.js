import {get} from '~/assets/js/api'

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
    const data = await get('locales');
    const messages = processLocalization(data);
    commit('setMessages', messages);
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
