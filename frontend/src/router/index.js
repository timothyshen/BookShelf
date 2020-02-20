import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import top_chart from '@/views/Chart/top_chart'
import login from "../views/user_login/login";
import reader_register from "../views/user_login/reader_register/reader_register";
import headbar from "../views/head/headbar";
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'login',
      component: login
    },
    {
      path: '/index',
      name: 'top_chart',
      component: top_chart
    },
    {
      path: '/register',
      name: 'register',
      component: reader_register
    },
    {
      path:'/headbar',
      name:'headbar',
      component: headbar
    }
  ]
})
