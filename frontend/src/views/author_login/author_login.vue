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
          <el-button type="primary">Login</el-button>
          <el-button type="primary">register</el-button>

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
