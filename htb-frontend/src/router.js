// router.js
import { createRouter, createWebHashHistory } from 'vue-router';

import General from './components/general.vue';
import Sock from './components/sock.vue';

const routes = [
  {
    path: '/',
    component: General,
  },
  {
    path: '/sock',
    component: Sock,
  },
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

export default router;
