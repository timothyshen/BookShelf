<template>
  <el-main class="container_body">
    <div class="login_body">
      <h2>Author Login</h2>
      <el-form :model="loginForm">
        <el-form-item>
          <div class="login_text">
            Username
          </div>
          <el-input type="text" v-model="loginForm.username">username</el-input>
        </el-form-item>
        <el-form-item>
          <div class="login_text">
            password
          </div>
          <el-input type="password" v-model="loginForm.password">password</el-input>
        </el-form-item>
        <el-form-item>
          <div>
            <el-link class="forget_link" type="primary">Forget?</el-link>
          </div>
        </el-form-item>
        <el-form-item class="button_group">
          <el-button type="primary" @click="isLogin">Login</el-button>
          <el-button type="primary"><router-link to="/author_register">register</router-link></el-button>

        </el-form-item>
      </el-form>
    </div>
  </el-main>
</template>

<script>

  import {login} from "../../api/api";
  import cookie from "../../static/cookie/cookie";

  export default {
    name: "author_login",
    data() {
      return {
        loginForm: {
          username: '',
          password: ''
        },
        autoLogin: false,
        error: false,
        userNameError: '',
        parseWordError: ''
      }
    },
    methods: {
      isLogin: function () {
        let that = this;
        login({
          password: that.loginForm.password,
          username: that.loginForm.username
        }).then((response) => {
          console.log(response.data);

          cookie.setCookie('user_id', response.data.user_id, 7);
          cookie.setCookie('name', response.data.name, 7);
          cookie.setCookie('token', response.data.token, 7);
          cookie.setCookie('role', response.data.role, 7);

          that.$store.dispatch('setInfo');
          this.$router.push({name: 'author'})
        }).catch(function (error) {
          if ("non_field_errors" in error) {
            that.error = error.non_field_errors[0];
          }
          if ("username" in error) {
            that.userNameError = error.username[0];
          }
          if ("password" in error) {
            that.parseWordError = error.password[0];
          }
        });
      }
    }
  }
</script>

<style lang="less" scoped>
  .container_body{
    margin: 100px auto;
    width: 900px;

    h2{
      text-align: center;
      margin-bottom:20px;
    }
    .button_group{
      margin:0 auto;
      width: inherit;
      justify-content: center;
    }

  }
</style>
