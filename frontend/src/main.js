import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import './index.css'
import store from './store'
import axios from 'axios'
import VueClickAway from "vue3-click-away";

axios.defaults.baseURL = 'http://127.0.0.1:8000/api/v1'

const app = createApp(App)

app.use(VueClickAway)
app.use(router)
app.use(store)

app.mount('#app')
