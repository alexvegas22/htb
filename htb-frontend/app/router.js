// router.js
import { createRouter, createWebHashHistory } from 'vue-router';

import General from './components/general.vue';
import Sock from './components/sock.vue';
import Image from './components/image.vue';

const routes = [
    {
	path: '/',
	component: General,
    },
    {
	name: 'sock',
	path: '/sock',
	component: Sock,
    },
    {
	name : 'image',
	path: '/image/:boardName/:imageName',
	component: Image,
    },
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

export default router;
