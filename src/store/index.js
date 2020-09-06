import Vue from 'vue';
import Vuex from 'vuex';
import { getNextTLB, setSuccess, startFlow } from '../services/api'

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
    },
    async nextTLB({ state, commit }) {
      commit('setFlow', await getNextTLB(state.flow))
    },
    async setSuccess({ state, commit }) {
      commit('setFlow', await setSuccess(state.flow))
    },
  },
  modules: {
  },
});
