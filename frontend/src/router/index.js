import Vue from 'vue'
import Router from 'vue-router'
import app from "../views/app/app";
import login from "../views/user_login/login";
import reader_register from "../views/user_login/reader_register/reader_register";
import headbar from "../views/head/headbar";
import login_headbar from "../views/head/login_headbar";
import footerbar from "../views/footer/footer";
import user_center from "../views/user_login/user_centre/user_center";
import home from "../views/app/home";
import home_page from "../views/home_page/home_page";
import cookie from "../static/cookie/cookie";

Vue.use(Router);

let router = new Router({
  routes: [{
    path: '/',
    component: app,
    children: [
      {
        path: 'login',
        name: 'login',
        components: {
          head: headbar,
          content: login,
          footer: footerbar,
        },
        meta: {
          title: 'Log in',
          need_log: false
        }
      },
      {
        path: 'register',
        name: 'register',
        components: {
          content: reader_register,
          head: login_headbar,
          footer: footerbar
        }
      },
      {
        path: 'home',
        components: {
          head: headbar,
          content: home,
          footer: footerbar,
        },
        children: [
          {
            path: 'index',
            name: 'home_page',
            component: home_page
          },
          {
            path: 'user',
            name: 'user',
            component: user_center
          }
        ]
      }
    ]
  }]
});

router.beforeEach((to, from, next)  =>{
  var nextPath = cookie.getCookie('nextPath');
  if (to !== undefined){
    if(to.meta.need_log) {
      console.log(to.meta.need_log);
      if (!store.state.userInfo.token) {
        next({
          path: '/home/index',
        });
      } else {
        next();
      }
    }
  }
});
export default router;
