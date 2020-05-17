<template>
  <el-row :gutter="24" class="container">
    <el-col :span="20" :offset="2" class="wrapper">
      <el-row :gutter="20">
        <el-col :span="3" class="username_wrap">
          <router-link to="/">
            <el-image :src="src"></el-image>
          </router-link>
        </el-col>
        <el-col :span="6">
          <el-menu
            default-active="1"
            class="navBar"
            mode="horizontal"
            background-color="#545454"
            text-color="#fff"
            active-text-color="#ffd04b"><!--Save for later -->
            <!--logo and nav-->
            <el-menu-item index="1">
              <router-link to="/">Home</router-link>
            </el-menu-item>
            <el-menu-item index="2">Creator</el-menu-item>
            <el-menu-item index="3">Completed</el-menu-item>
            <el-menu-item index="4">Library</el-menu-item>
          </el-menu>
        </el-col>
        <el-col :span="6">
          <el-input
            placeholder="Search"
            class="input_nav"
            size="large">
            <el-button slot="append" icon="el-icon-search"/>
          </el-input>
        </el-col>
        <el-col :span="8">
          <el-row type="flex" class="row-bg" justify="end" v-if="userInfo.role === 'reader'">
            <el-col :span="2">
              <el-avatar class="block" :size="small" :src="circleUrl"/>
            </el-col>
            <el-col :span="4" class="username_wrap">
              <p class="username">{{userInfo.name}}</p>
            </el-col>
            <el-col :span="10">
              <el-menu
                class="navBar"
                mode="horizontal"
                background-color="#545454"
                text-color="#fff"
                active-text-color="#ffd04b"><!--Save for later -->
                <!--logo and nav-->
                <el-menu-item index="1">
                  <router-link to="/userManager">Bookshelf</router-link>
                </el-menu-item>
                <el-menu-item index="2">
                  [<a @click="signOut()">Sign out</a>]
                </el-menu-item>
              </el-menu>
            </el-col>
          </el-row>
          <el-row type="flex" class="row-bg" justify="end" v-else-if="userInfo.role === 'Author'">
            <el-col :span="2">
              <el-avatar class="block" :size="small" :src="circleUrl"/>
            </el-col>
            <el-col :span="4" class="username_wrap">
              <p class="username">{{userInfo.name}}</p>
            </el-col>
            <el-col :span="10">
              <el-menu
                class="navBar"
                mode="horizontal"
                background-color="#545454"
                text-color="#fff"
                active-text-color="#ffd04b"><!--Save for later -->
                <!--logo and nav-->
                <el-menu-item index="1">
                  <router-link to="/authorManagement">Author Hub</router-link>
                </el-menu-item>
                <el-menu-item index="2">
                  [<a @click="signOut()">Sign out</a>]
                </el-menu-item>
              </el-menu>
            </el-col>
          </el-row>
          <el-row type="flex" class="row-bg" justify="end" v-else>
            <el-menu
              class="navBar"
              mode="horizontal"
              background-color="#545454"
              text-color="#fff"
              default-active="1"
              active-text-color="#ffd04b">
              <!--logo and nav-->
              <el-menu-item index="1">
                <router-link to="/login">Login</router-link>
              </el-menu-item>
              <el-menu-item index="2">
                <router-link to="/register">SignUp</router-link>
              </el-menu-item>
            </el-menu>
          </el-row>
        </el-col>


      </el-row>
    </el-col><!--first col layer-->
  </el-row>
</template>

<script>
  import {mapGetters} from 'vuex';
  import cookie from "../../static/cookie/cookie";
  import {getUserDetail} from "../../api/api";
  import store from "../../store/store";

  export default {
    name: "login_headbar",
    data() {
      return {
        circleUrl: "https://cube.elemecdn.com/3/7c/3ea6beec64369c2642b92c6726f1epng.png",
        src: '../../static/image/logo.png',

      }
    },
    computed:{
      ...mapGetters({
        userInfo:'userInfo'
      })
    },
    methods: {
      signOut() {
        cookie.delCookie('token');
        cookie.delCookie('name');
        cookie.delCookie('role');
        cookie.delCookie('user_id');
        this.$store.dispatch('setInfo');
        this.$store.commit('removeToken');
        this.$router.push('/')
      }
    }
  }
</script>

<style>
  .container {
    background-color: #545454;
  }

  .input_nav {
    margin-top: 10px;
  }

  .block {
    margin-top: 10px;
  }

  .username_wrap {
    text-align: center;
    height: 60px;
    line-height: 60px;
    color: #fff;
  }

</style>
