import Vue from 'vue'
import Router from 'vue-router'
import app from "../views/app/app";
import login from "../views/reader_login/login";
import reader_register from "../views/reader_login/reader_register/reader_register";
import login_headbar from "../views/head/login_headbar";
import footerbar from "../views/footer/footer";
import user_center from "../views/reader_login/user_centre/user_center";
import home from "../views/app/home";
import home_page from "../views/home_page/home_page";
import book_detail from "../views/book_page/book_detail/book_detail";
import chapter_detail from "../views/book_page/chapter/chapter_detail";
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
import author_chapter_list from "../views/author_login/author_center/Book/novel/author_chapter_list";
import author_chapter_create from "../views/author_login/author_center/Book/novel/author_chapter_create";
import author_chapter_exist from "../views/author_login/author_center/Book/novel/author_chapter_exist";
import author_novel_setting from "../views/author_login/author_center/Book/novel/author_novel_setting";
import book_create_header from "../views/author_login/author_center/Book/novel/component/book_create_header";
import book_setting_head from "../views/author_login/author_center/Book/novel/component/book_setting_head";
import chapter_create_head from "../views/author_login/author_center/Book/novel/component/chapter_create_head";
import book_list_head from "../views/author_login/author_center/Book/novel/component/book_list_head";
import author_setting from "../views/author_login/author_center/author_info/author_setting";
import author_setting_header from "../views/author_login/author_center/author_info/author_setting_header";
import store from "../store/store";
import category_page from "../views/home_page/category_page";
import ranking_page from "../views/home_page/ranking_page";
import user_comment from "../views/reader_login/user_centre/components/user_comment";
import book_comment from "../views/author_login/author_center/Book/novel/book_comment";
import comment_head from "../views/author_login/author_center/Book/novel/component/comment_head";

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
          head: login_headbar,
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
        },
        meta: {
          title: 'Reader Register',
          need_log: false
        }
      },
      {
        path: 'author_login',
        name: 'author_login',
        components: {
          content: author_login,
          head: login_headbar,
          footer: footerbar
        },
        meta: {
          title: 'Author Log in',
          need_log: false
        }
      },
      {
        path: 'author_register',
        name: 'author_register',
        components: {
          content: author_register,
          head: login_headbar,
          footer: footerbar
        },
        meta: {
          title: 'Author Register',
          need_log: false
        }
      },
      {
        path: '/',
        name: 'home',
        redirect: 'index',
        components: {
          head: login_headbar,
          content: home,
          footer: footerbar,
        },
        children: [{
          path: 'index',
          name: 'index',
          component: home_page,
          meta: {
            title: 'Home',
            need_log: false
          }
        },
          {
            path: 'category/:categoryname',
            name: 'category_page',
            component: category_page,
            meta: {
              title: 'page',
              need_log: false
            }
          }, {
            path: 'ranking',
            name: 'ranking_page',
            component: ranking_page,
            meta: {
              title: 'page',
              need_log: false
            }
          }, {
            path: 'ranking',
            name: 'ranking',
            component: ranking_page,
            meta: {
              title: 'Ranking',
              need_log: false
            }
          }, {
            path: 'book/:book_id',
            name: 'book',
            component: book_detail,
            props: true,
            meta: {
              title: 'Book detail',
              need_log: false
            }
          }, {
            path: 'book/item/:book_id/:id',
            name: 'chapter',
            component: chapter_detail,
            props: true,
            params: true,
            meta: {
              title: 'Chapter',
              need_log: false
            }
          },
        ]
      },
      {
        path: '/userManager',
        name: 'user',
        redirect: '/user/usercenter',
        components: {
          head: login_headbar,
          content: user_center,
          footer: footerbar
        },
        children: [
          {
            path: '/user/usercenter',
            name: 'user centre',
            components: {
              aside: sidebar,
              default: user_centre_view
            },
            meta: {
              title: 'User centre',
              need_log: true
            }
          },
          {
            path: '/user/bookcase',
            name: 'bookcase',
            components: {
              aside: sidebar,
              default: bookcase
            },
            meta: {
              title: 'User bookcase',
              need_log: true
            }
          },{
            path: '/user/comment',
            name: 'user_comment',
            components: {
              aside: sidebar,
              default: user_comment
            },
            meta: {
              title: 'User Comment',
              need_log: true
            }
          },
          {
            path: '/user/setting',
            name: 'user_setting',
            components: {
              aside: sidebar,
              default: user_setting
            },
            meta: {
              title: 'User Setting',
              need_log: true
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
        menuShow: true,
        meta: {
          title: 'Author centre',
          need_log: true
        }
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
        menuShow: true,
        meta: {
          title: 'Author dashboard',
          need_log: true
        }
      }
    ]
  }, {
    path: '/storyManagement',
    type: 'story',
    name: 'story',
    redirect: '/novel/list',
    component: author_centre_view,
    children: [{
      path: '/novel/list',
      name: 'Novel_list',
      components: {
        content: author_case,
        top: top_nav,
        aside: left_nav
      },
      leaf: true,
      menuShow: false,
      props: true,
      meta: {
        title: 'Author Book',
        need_log: true
      }
    },{
      path: '/novel/comment',
      name: 'Novel comment',
      components: {
        content: book_comment,
        top: comment_head,
        aside: left_nav
      },
      leaf: true,
      menuShow: false,
      iconCls: 'el-icon-user-solid',
      props: true,
      meta: {
        title: 'Book Comment',
        need_log: true
      }
    }, {
      path: '/author/setting',
      name: 'author_setting',
      components: {
        content: author_setting,
        top: author_setting_header,
        aside: left_nav
      },
      leaf: true,
      menuShow: false,
      props: true,
      meta: {
        title: 'Author setting',
        need_log: true
      }
    },
      {
        path: '/novel/create',
        name: 'New_novel',
        components: {
          content: book_create,
          top: book_create_header,
          aside: left_nav
        },
        leaf: true,
        menuShow: false,
        meta: {
          title: ' Author Novel create',
          need_log: true
        }

      },
      {
        path: '/novel/chapter/:book_id',
        name: 'chapter_view',
        components: {
          content: author_chapter_list,
          top: book_list_head,
          aside: left_nav
        },
        leaf: true,
        menuShow: false,
        props: true,
        meta: {
          title: 'Author Novel chapter',
          need_log: true
        }
      },
      {
        path: '/novel/chapter/:book_id/:chapter_id',
        name: 'chapter_retrieve',
        components: {
          content: author_chapter_exist,
          top: chapter_create_head,
          aside: left_nav
        },
        leaf: true,
        menuShow: false,
        meta: {
          title: 'Author chapter view',
          need_log: true
        }
      }, {
        path: '/novel/chapter/create/:book_id',
        name: 'chapter_create',
        components: {
          content: author_chapter_create,
          top: chapter_create_head,
          aside: left_nav
        },
        leaf: true,
        menuShow: false,
        meta: {
          title: 'Author chapter create',
          need_log: true
        }
      },
      {
        path: '/novel/book/setting',
        name: 'book_setting',
        components: {
          content: author_novel_setting,
          top: book_setting_head,
          aside: left_nav
        },
        leaf: true,
        menuShow: false,
        meta: {
          title: 'Author Novel setting',
          need_log: true
        }
      }]
  }, {
    path: '/incomeManagement',
    type: 'income',
    name: 'income',
    redirect: '/novel/income',
    component: author_centre_view,
  }]
});
//router authorization
router.beforeEach((to, from, next) => {
  console.log(to.meta.need_log, to.meta.title);
  if (to.meta.need_log) {
    console.log(to.meta.need_log);
    if (!store.state.userInfo.token) {
      next({
        path: '/login'
      })
    } else {
      next();
    }
  } else {
    if (to.path === '/') {
      next({
        path: '/index',
      });
    } else {
      next();
    }
  }
});
//for web page title
router.afterEach((to, from, next) => {
  document.title = to.matched[to.matched.length - 1].meta.title;
});
export default router;
