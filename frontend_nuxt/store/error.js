export const state = () => ({
  error: []
})

export const mutations = {
  setError(state, e) {
    state.error.push(e);
  }
}

export const getters = {
  getError: state => state.error
}
