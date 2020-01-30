import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import top_chart from '@/views/Chart/top_chart'
import Log_in from '@/views/user_login/login'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'login',
      component: Log_in
    },
    {
      path: '/home',
      name: 'top_chart',
      component: top_chart
    }
  ]
})
