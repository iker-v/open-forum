import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import ThreadView from '../views/ThreadView.vue'
import CreateThreadView from '../views/CreateThreadView.vue'
import SettingsView from '../views/SettingsView.vue'
import ThreadListView from '../views/ThreadListView.vue'
import store from '../store'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/thread/:id',
      name: 'ThreadView',
      component: ThreadView,
    },
    {
      path: '/create-thread/:categoryid',
      name: 'createThread',
      component: CreateThreadView,
    },
    {
      path: '/settings',
      name: 'settings',
      component: SettingsView,
    },
    {
      path: '/c/:category',
      name: 'threadList',
      component: ThreadListView,
    },    
  ]
})

router.beforeEach((to, from, next) => {

  store.commit('initializeStore')
  next()
})

export default router
