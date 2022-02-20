export const state = () => ({
  error: null
})

export const mutations = {
  setError(state, e) {
    state.error = e;
  },
  clearError(state) {
    state.error = null;
  }
}

export const getters = {
  getError: state => state.error
}
