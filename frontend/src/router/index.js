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
import author_register from "../views/author_login/author_register/author_register";
import bookcase from "../views/reader_login/user_centre/components/bookcase";
import sidebar from "../views/reader_login/user_centre/components/sidebar";
import user_centre_view from "../views/reader_login/user_centre/user_centre_view";
import user_setting from "../views/reader_login/user_centre/components/user_setting";
import author_centre_view from "../views/author_login/author_center/author_centre_view";
import top_nav from "../views/author_login/author_center/component/top_nav";
import left_nav from "../views/author_login/author_center/component/left_nav";
import dashboard from "../views/author_login/author_center/workbench/dashboard";
import book_create from "../views/author_login/author_center/Book/book_create";
import author_case from "../views/author_login/author_center/Book/author_case";
import author_chapter_view from "../views/author_login/author_center/Book/novel/author_chapter_view";
import author_chapter_create from "../views/author_login/author_center/Book/novel/author_chapter_create";
import author_novel_setting from "../views/author_login/author_center/Book/novel/author_novel_setting";
Vue.use(Router);

let router = new Router({
  routes: [{
    path: '/',
    component: app,
    redirect: 'index',
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
        path: 'author_login',
        name: 'author_login',
        components: {
          content: author_login,
          head: login_headbar,
          footer: footerbar
        }
      },
      {
        path: 'author_register',
        name: 'author_register',
        components: {
          content: author_register,
          head: login_headbar,
          footer: footerbar
        }
      },
      {
        path: '/',
        name: 'home',
        redirect: 'index',
        components: {
          head: headbar,
          content: home,
          footer: footerbar,
        },
        children: [{
          path: 'index',
          name: 'index',
          component: home_page
        }]
      },
      {
        path: '/userManager',
        name: 'user',
        redirect: '/user/usercentre',
        components: {
          head: headbar,
          content: user_center,
          footer: footerbar
        },
        children: [
          {
            path: '/user/usercentre',
            name: 'user centre',
            components: {
              aside: sidebar,
              default: user_centre_view
            }
          },
          {
            path: '/user/bookcase',
            name: 'user centre',
            components: {
              aside: sidebar,
              default: bookcase
            }
          },
          {
            path: '/user/setting',
            name: 'user setting',
            components: {
              aside: sidebar,
              default: user_setting
            }
          }
        ]
      }
    ]
  }, {
    path: '/authorManagement',
    type: 'author',
    name: 'author',
    redirect: '/novel/dashboard',
    component: author_centre_view,
    children: [
      {
        path: '/novel/dashboard',
        name: 'Author Home',
        components: {
          content: dashboard,
          top: top_nav,
          aside: left_nav
        },
        leaf: true,
        iconCls: 'el-icon-s-home',
        menuShow: true
      },
      {
        path: '/novel/readerdashboard',
        name: 'Reader Data',
        components: {
          content: user_setting,
          top: top_nav,
          aside: left_nav
        },
        leaf: true,
        iconCls: 'el-icon-user-solid',
        menuShow: true
      }
    ]
  }, {
    path: '/storyManagement',
    type: 'story',
    name: 'story',
    redirect: '/novel/list',
    component: author_centre_view,
    children:[{
      path:'/novel/list',
      name: 'Novel list',
      components:{
        content:author_case,
        top:top_nav,
        aside:left_nav
      },
      leaf:true,
      menuShow:false
    },
      {
      path:'/novel/create',
      name: 'New novel',
      components:{
        content:book_create,
        top:top_nav,
        aside:left_nav
      },
      leaf:true,
      menuShow:false
    },
      {
      path:'/novel/chapter',
      name: 'New novel',
      components:{
        content:author_chapter_view,
        top:top_nav,
        aside:left_nav
      },
      leaf:true,
      menuShow:false
    },
      {
      path:'/novel/chapter/create',
      name: 'New novel',
      components:{
        content:author_chapter_create,
        top:top_nav,
        aside:left_nav
      },
      leaf:true,
      menuShow:false
    },
      {
      path:'/novel/book/setting',
      name: 'Novel setting',
      components:{
        content:author_novel_setting,
        top:top_nav,
        aside:left_nav
      },
      leaf:true,
      menuShow:false
    }]
  }, {
    path: '/incomeManagement',
    type: 'income',
    name: 'income',
    redirect: '/novel/income',
    component: author_centre_view,
  }]
});

export default router;
