import { createApp } from 'vue'
import App from './App.vue'
import './registerServiceWorker'
import router from "./router";
import axios from 'axios'
import MyUI from '@/components'

const app=createApp(App)
app.use(router.router).use(MyUI).mount('#app')
axios.defaults.baseURL=' http://127.0.0.1:8000/'