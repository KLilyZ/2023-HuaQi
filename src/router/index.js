import {createRouter,createWebHashHistory} from 'vue-router'


const routes = [
  {
    path:'/',
    name:'home',
    component:()=>import ("@/components/HelloWorld")
  },
  {
    path:'/detail/:name',
    name:'detail',
    component: ()=>import ("@/components/chart")
  },
  {
    path:'/detail/:name/:species/:score',
    name:'species',
    component: ()=>import ("@/components/Environment")
  }
]
const router = createRouter({
  history:createWebHashHistory(),
  routes
})

export default {router};