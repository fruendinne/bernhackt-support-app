import Vue from 'vue';
import VueRouter from 'vue-router';
import Onboarding from '../views/Onboarding'
import Troubleshooting from '../views/Troubleshooting'

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    component: Onboarding,
  },
  {
    path: '/troubleshooting',
    component: Troubleshooting,
  }
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;
