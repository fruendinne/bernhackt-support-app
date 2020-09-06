import Vue from 'vue';
import Vuex from 'vuex';
import { startFlow } from '../services/api'

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    flow: null,
    problem: null,
  },
  mutations: {
    setFlow(state, flow) {
      state.flow = flow
    },
    setProblem(state, problem) {
      state.problem = problem
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
