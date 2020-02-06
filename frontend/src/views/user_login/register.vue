<template>
  <div><!--最外层-->
    <div>
      <div>
        <form type="submin">
          <h2>Username:</h2>
          <input type="text" v-model="username"></input>
          <h2>Password:</h2>
          <input type="password" v-model="password"></input>
          <h2>Confirm Password</h2>
          <input type="password" v-model="password_two"></input>
          <button type="submit" @click="isRegister">register</button>
        </form>

      </div>
    </div>
  </div>
</template>

<script>
  import {login} from '../../api/api'
  import cookie from "../../static/cookie/cookie";
    export default {
        name: "register",
      data() {
        return {
          username: '',
          password: '',
          password_two: '',
          error: {
            password: '',
            username: ''
          }
        }
      },
      methods:{
          isRegister(){
            var that = this
            login({
              password: that.password,
              username: that.username,
              password_two: that.password_two

            }).then((response)=>{
              cookie.setCookie('name',response.data.username,7);
              cookie.setCookie('token',response.data.token,7);
              that.$router.push({name:'login'});
              console.log('success')
            }).catch(function (error) {
              that.error.mobile = error.username?error.username[0]:'';
              that.error.password = error.password?error.password[0]:'';
            })
          }
      }
    }
</script>

<style scoped>

</style>
