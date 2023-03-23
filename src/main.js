import { createApp } from 'vue'
import App from './App.vue'
import './registerServiceWorker'
import router from "./router";
import axios from 'axios'
import MyUI from '@/components'
import ElementPlus from 'element-plus'

const app=createApp(App)
app.use(router.router).use(ElementPlus).use(MyUI).mount('#app')
axios.defaults.baseURL=' http://127.0.0.1:8000/'