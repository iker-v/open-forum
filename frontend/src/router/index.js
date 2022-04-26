import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import ThreadView from '../views/ThreadView.vue'
import CreateThreadView from '../views/CreateThreadView.vue'
import SettingsView from '../views/SettingsView.vue'
import ThreadListView from '../views/ThreadListView.vue'
import PanelView from '../views/PanelView.vue'
import store from '../store'

const checkAuth = (to, from, next) => {
  if (store.state.auth.isAuthenticated) next()
  else next({ name: 'home' })
}

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/thread/:idthread',
      name: 'ThreadView',
      component: ThreadView,
    },
    {
      path: '/create-thread/:categoryid',
      name: 'createThread',
      component: CreateThreadView,
      beforeEnter: checkAuth,
    },
    {
      path: '/settings',
      name: 'settings',
      component: SettingsView,
      beforeEnter: checkAuth,
    },
    {
      path: '/panel',
      name: 'panel',
      component: PanelView,
      beforeEnter: checkAuth,
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
