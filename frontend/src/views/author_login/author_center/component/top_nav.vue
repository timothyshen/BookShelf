<template>
  <el-row class="container_author">
    <el-col :span="24" class="topbar-wrap">
      <div class="topbar-logo topbar-btn">
        <router-link to="/authorManagement">
          <el-image src='../../../../static/image/logo.png'></el-image>
        </router-link>
      </div>
      <div class="topbar-title">
        <el-row v-show="$store.state.topNavState === 'author'">
          <el-col :span="4">

            <h2 style="color: white; text-align: center;">Author</h2>
          </el-col>
          <el-col :span="20">
            <el-menu :default-active="defaultActiveIndex" mode="horizontal" @select="handleSelect" :router="true">
              <el-menu-item index="/authorManagement">Dashboard</el-menu-item>
              <el-menu-item index="/storyManagement">Story</el-menu-item>
              <el-menu-item index="income">Income</el-menu-item>
            </el-menu>
          </el-col>
        </el-row>
        <el-row v-show="$store.state.topNavState === 'story'" :gutter="20">
          <el-col :span="12">
            <h2 style="color: white; text-align: center;">Stories</h2>
          </el-col>
          <el-col :span="12">
            <el-menu :default-active="defaultActiveIndex" mode="horizontal" @select="handleSelect" :router="true">
              <el-menu-item index="/list">Novel</el-menu-item>
              <el-menu-item index="/list">Fanfic</el-menu-item>
            </el-menu>
          </el-col>
        </el-row>
        <el-row v-show="$store.state.topNavState === 'income'">
          <el-col :span="24">
            <el-menu :default-active="defaultActiveIndex" mode="horizontal" @select="handleSelect" :router="true">
              <el-menu-item>Income</el-menu-item>
            </el-menu>
          </el-col>
        </el-row>
      </div>
      <div class="topbar-account topbar-btn" >
        <el-button v-show="$store.state.topNavState === 'story'">
          <router-link to="create">
            <i class="el-icon-plus"></i>
            Create new book
          </router-link>
        </el-button>
        <el-dropdown trigger="click">
          <span class="el-dropdown-link userinfo-inner">
            <i class="iconfont icon-user"></i>{{userInfo.username}}<i class="el-icon-caret-bottom"></i></span>
          <el-dropdown-menu slot="dropdown">
            <el-dropdown-item>
              <div><span style="color: #555;font-size: 14px;">User Info</span></div>
            </el-dropdown-item>
            <el-dropdown-item>
              <div><span style="color: #555;font-size: 14px;">Setting</span></div>
            </el-dropdown-item>
            <el-dropdown-item divided>Log out</el-dropdown-item>
          </el-dropdown-menu>
        </el-dropdown>

      </div>
    </el-col>
  </el-row>
</template>

<script>
  import {mapGetters} from "vuex";

  export default {
    name: "top_nav",
    data() {
      return {
        src: require('../../../../static/image/logo.png'),
        defaultActiveIndex: 'dashboard',
        homeMenu: false,
      }
    },
    computed:{
      ...mapGetters({
        userInfo:'userInfo'
      })
    },
    created() {
      this.fetchNavDate();
    },
    methods: {
      handleSelect(index) {
        this.defaultActiveIndex = index;
      },
      fetchNavDate() {
        let cur_path = this.$route.path; //获取当前路由
        let routers = this.$router.options.routes; // 获取路由对象
        let nav_type = "", nav_name = "";
        for (var i = 0; i < routers.length; i++) {
          let children = routers[i].children;
          if (children) {
            for (let j = 0; j < children.length; j++) {
              if (children[j].path === cur_path) {
                nav_type = routers[i].type;
                nav_name = routers[i].name;
                break;
              }
              // 如果该菜单下还有子菜单
              if (children[j].children) {
                let grandChildren = children[j].children;
                for (let z = 0; z < grandChildren.length; z++) {
                  if (grandChildren[z].path === cur_path) {
                    nav_type = routers[i].type;
                    nav_name = routers[i].name;
                    break;
                  }
                }
              }
            }
          }
        }
        this.$store.state.topNavState = nav_type;
        this.$store.state.leftNavState = nav_name;
        if (nav_type === "author") {
          this.defaultActiveIndex = "dashboard";
        } else {
          this.defaultActiveIndex = "/" + nav_name + "Manager";
        }
      }
    },
    watch: {
      '$route': function (to, from) { // 路由改变时执行
        //console.info("to.path:" + to.path);
        this.fetchNavDate();
      }
    }
  }
</script>

<style lang="less" scoped>
  .container_author {
    width: 100%;
    .topbar-wrap {
      height: 50px;
      line-height: 50px;
      background: #000000;
      padding: 0px;
      .topbar-btn {
        color: #fff;
      }
      .topbar-logo {
        float: left;
        width: 200px;
        line-height: 26px;
      }
      .topbar-title {
        width: 500px;
        float: left;
        text-align: left;
        padding-left: 10px;
        border-bottom: 0;
        border-left: 1px solid #000;
        .el-menu--horizontal {
          background-color: transparent;
        }
        .el-menu--horizontal > .el-menu-item:not(.is-disabled):hover, .el-menu--horizontal > .el-menu-item:not(.is-disabled):focus, .el-menu--horizontal > .el-menu-item.is-active {
          color: black;
          background-color: white;
          border-bottom: 2px solid #409EFF !important;
        }
        .el-menu--horizontal > .el-menu-item {
          height: 50px;
          line-height: 50px;
          color: #fff;
          .iconfont {
            margin-right: 5px;
            display: inline-block;
            width: 24px;
            text-align: center;
            font-size: 18px;
            vertical-align: middle;
          }
        }
      }
      .topbar-account {
        float: right;
        padding-right: 12px;
      }
      .userinfo-inner {
        cursor: pointer;
        color: #fff;
        padding-left: 10px;
      }
    }
  }
</style>
