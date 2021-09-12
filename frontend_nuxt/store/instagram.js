import axios from "axios";

export const state = () => ({
  slides: []
})

export const mutations = {
  setSlides(state, slides) {
    state.slides = slides
  }
}

export const actions = {
  async fetch({commit}) {
    const data = await axios.get(process.env.VUE_APP_INSTA);
    const slides = data.data;
    commit('setSlides', slides);
  }
}

export const getters = {
  slides: s => s.slides
}
