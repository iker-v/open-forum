import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import './index.css'
import store from './store'
import axios from 'axios'
import VueClickAway from "vue3-click-away";

axios.defaults.baseURL = 'https://api.ikerv.me'

const app = createApp(App)

app.use(VueClickAway)
app.use(router)
app.use(store)

app.mount('#app')
