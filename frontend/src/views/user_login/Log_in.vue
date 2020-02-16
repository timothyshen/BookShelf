<template>
  <div>
    <div class="form-group">
      <p>Username:</p>
      <label>
        <input type="text" name="username"/>
      </label>
    </div>
    <div class="form-group">
      <p>Password:</p>
      <input type="password" name="password"/>
    </div>
    <div class="form-group">
      <button type="submit" @click="isLogin">Login</button>
    </div>
  </div>
</template>

<script>
  import {login_one} from '../../api/api';
    export default {
        name: "Log_in",
        methods:{
          isLogin(){
            let that = this;
            login_one({
              password: that.password,
              username: that.username
            }).catch(function (error) {
              console.log(error.response);
              that.error.username = error.username?error.username[0]:'';
              that.error.password = error.password?error.password[0]:'';
            })
          }
        }
    }
</script>

<style scoped>

</style>
