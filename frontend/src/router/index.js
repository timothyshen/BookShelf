import Vue from 'vue'
import Router from 'vue-router'
import app from "../views/app/app";
import login from "../views/reader_login/login";
import reader_register from "../views/reader_login/reader_register/reader_register";
import headbar from "../views/head/headbar";
import login_headbar from "../views/head/login_headbar";
import footerbar from "../views/footer/footer";
import user_center from "../views/reader_login/user_centre/user_center";
import home from "../views/app/home";
import home_page from "../views/home_page/home_page";
import cookie from "../static/cookie/cookie";
import book_detail from "../views/book_page/book_detail/book_detail";
import chapter_detail from "../views/book_page/chapter/chapter_detail";
import chapter_index from "../views/book_page/book_index/chapter_index";
import author_login from "../views/author_login/author_login";
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
        path: 'author_register',
        name: 'author_register',
        components: {
          content: author_login,
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
          },
          {
            path: 'book',
            name: 'book',
            component: book_detail,

          },
          {
            path: 'book/chapter-1',
            name: 'chapter',
            component: chapter_detail
          },
          {
            path: 'book/1',
            name: 'chapter',
            component: chapter_index
          }
        ]
      }
    ]
  }]
});

// router.beforeEach((to, from, next)  =>{
//   var nextPath = cookie.getCookie('nextPath');
//   if (to !== undefined){
//     if(to.meta.need_log) {
//       console.log(to.meta.need_log);
//       if (!store.state.userInfo.token) {
//         next({
//           path: '/home/index',
//         });
//       } else {
//         next();
//       }
//     }
//   }
// });
export default router;
