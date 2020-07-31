<template>
  <div class="container_body">
    <el-col :offset="6" :span="18" class="banner">
      <el-image></el-image>
    </el-col>
    <el-row class="main_body">
      <h1>Sign in</h1>
      <el-col :span="6" :offset="6">
        <el-form :model="loginForm">
          <el-form-item>
            <div class="login_text">
              Username
            </div>
            <el-input type="text" v-model="loginForm.username">username</el-input>
            <p class="error-text" v-show="userNameError">{{userNameError}}</p>
          </el-form-item>
          <el-form-item>
            <div class="login_text">
              password
            </div>
            <el-input type="password" v-model="loginForm.password">password</el-input>
            <p class="error-text" v-show="parseWordError">{{parseWordError}}</p>
          </el-form-item>
          <el-form-item>
            <div>
              <el-link class="forget_link" type="primary">Forget?</el-link>
            </div>
          </el-form-item>
          <el-form-item>
            <p class="error-text" v-show="error">{{error}}</p>
            <el-button type="primary" @click="isLogin">Login</el-button>
            <router-link :to="'/register'" target = _blank><el-button type="primary">register</el-button></router-link>
          </el-form-item>
        </el-form>
      </el-col>
      <el-col :span="6">
        <div class="button_wrap">
          <el-button class="selfButton" type="primary" icon="" size="medium"><span>Google login</span></el-button>
        </div>
        <div class="button_wrap">
          <el-button class="selfButton" type="primary" icon="el-icon-google"><span>Facebook Login</span></el-button>
        </div>
        <div class="button_wrap">
          <el-button class="selfButton" type="primary" icon="el-icon-google"><span>Twitter Login</span></el-button>
        </div>
      </el-col>
    </el-row>
  </div>
</template>
<script>
  import {login} from '../../api/api';
  import cookie from "../../static/cookie/cookie";
  export default {
    name: "login",
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
          //save the userinfo to local
          cookie.setCookie('user_id', response.data.user_id, 7);
          cookie.setCookie('name', response.data.name, 7);
          cookie.setCookie('token', response.data.token, 7);
          cookie.setCookie('role', response.data.role, 7);

          // update store info
          that.$store.dispatch('setInfo');
          // add token to refresh
          that.$store.commit('updateToken', response.data.token);
          console.log('success');
          // jump to home page
          this.$router.push({name: 'user'})
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

<style>
  h1 {
    font-weight: bold;
    margin: 0;
    text-align: center;
  }

  .login_text, .forget_link {
    font-size: 20px;
    font-weight: 100;
    line-height: 20px;
    letter-spacing: 0.5px;
    margin: 20px 0 30px;
  }

  .button_wrap {
    padding: 20px;
  }

  .selfButton {
    height: 70px;
    width: 450px;
  }
  .container_body{
    margin-top: 20px;
  }
  .main_body{
    top: 50%;
  }

</style>
