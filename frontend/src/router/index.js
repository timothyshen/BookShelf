import Vue from 'vue'
import Router from 'vue-router'
import app from "../views/app/app";
import HelloWorld from '@/components/HelloWorld'
import top_chart from '@/views/Chart/top_chart'
import login from "../views/user_login/login";
import reader_register from "../views/user_login/reader_register/reader_register";
import headbar from "../views/head/headbar";
import login_headbar from "../views/head/login_headbar";
Vue.use(Router)

// export default new Router({
//   routes: [
//     {
//       path: '/',
//       name: 'login',
//       components:{
//           head: headbar,
//           content: login,
//
//         }
//     },
//     {
//       path: '/index',
//       name: 'top_chart',
//       component: top_chart
//     },
//     {
//       path: '/register',
//       name: 'register',
//       component: reader_register
//     },
//     {
//       path:'/headbar',
//       name:'headbar',
//       component: headbar
//     }
//   ]
// })

let router = new Router({
  routes: [{
    path:'/app',
    component: app,
    children:[
      {
        path: 'login',
        name: 'login',
        components:{
          head: headbar,
          content: login,

        },
        meta:{
          title:'Log in',
          need_log:false
        }
      },
      {
        path: 'reader/register',
        name: 'register',
        components: {
          content: reader_register,
          head:login_headbar,
        }
      }

      ]
  }]
});

export default router;
