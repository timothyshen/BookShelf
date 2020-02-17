<template>
  <div>
    <head></head><!--最外层-->
    <el-col :span="12" :offset="6">
      <el-form ref="form" :model="form_data" label-width="180px" :label-position="labelPosition">
        <el-form-item label="username:">
          <el-input type="text" v-model="form_data.username">username</el-input>
        </el-form-item>
        <el-form-item label="Password:">
          <el-input
            type="password"
            v-model="form_data.password"
            show-password>password</el-input>
        </el-form-item>
        <el-form-item label="Confirm password:">
          <el-input
            type="password"
            v-model="form_data.password_two"
            show-password>password</el-input>
        </el-form-item>
        <el-button type="primary" @click="isRegister">register</el-button>
      </el-form>
    </el-col>
  </div>
</template>

<script>
  import {login} from '../../../api/api'
  import cookie from "../../../static/cookie/cookie";
  import head from "../../../components/head";
    export default {
      components: {head},
      name: "register",
      data() {
        return {
          labelPosition: 'left',
          form_data:{
            username: '',
            password: '',
            password_two: '',
          },
          error: {
            password: '',
            username: ''
          }
        }
      },
      methods:{
          isRegister(){
            let that = this;
            login({
              password: that.form_data.password,
              username: that.form_data.username,
              role: that.form_data.role
            },{
              auth:{
                username: 't.shen',
                password: 'bookshelf'
              }
            }).then((response)=>{
              cookie.setCookie('name',response.data.username,7);
              cookie.setCookie('token',response.data.token,7);
              that.$router.push({name:'login'});
              console.log('success')
            }).catch(function (error) {
              console.log(error.response)
              that.error.mobile = error.username?error.username[0]:'';
              that.error.password = error.password?error.password[0]:'';
            })

          }
      }
    }
</script>

<style scoped>

</style>
