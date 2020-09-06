import Vue from 'vue';
import VueRouter from 'vue-router';
import Onboarding from '../views/Onboarding'

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    component: Onboarding
  }
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;
