<template>
  <el-main class="container_body">
    <div class="login_body">
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
        <el-form-item>
          <el-button type="primary">Login</el-button>
          <router-link target=_blank>
            <el-button type="primary">register</el-button>
          </router-link>
        </el-form-item>
      </el-form>
    </div>
  </el-main>
</template>

<script>
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
    }
  }
</script>

<style scoped>
  .container_body{
    margin: 100px auto;
    width: 900px;
  }
</style>
