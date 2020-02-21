import Vue from 'vue'
import Router from 'vue-router'
import app from "../views/app/app";
import login from "../views/user_login/login";
import reader_register from "../views/user_login/reader_register/reader_register";
import headbar from "../views/head/headbar";
import login_headbar from "../views/head/login_headbar";
import footer from "../views/footer/footer";

Vue.use(Router);

let router = new Router({
  routes: [{
    path:'/app',
    component: app,
    children:[
      {
        path: 'login',
        name: 'login',
        components: {
          head: headbar,
          content: login,
          footer: footer,
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
/*router.beforeEach((to, from, next)  =>{
  var nextPath = cookie.getCookie('nextPath');
  if (to != undefined){
    if(to.meta.need_log) {
      console.log(to.meta.need_log);
      if (!store.state.userInfo.token) {
        next({
          path: '/login',
        });
      } else {
        next();
      }
    }
  }
});*/
export default router;
