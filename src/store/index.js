import Vue from 'vue';
import Vuex from 'vuex';
import { startFlow } from '../services/api'

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    flow: null,
  },
  mutations: {
    setFlow(state, flow) {
      state.flow = flow
    }
  },
  actions: {
    async startFlow({ commit }, userQuery) {
      commit('setFlow', await startFlow(userQuery))
    }
  },
  modules: {
  },
});
