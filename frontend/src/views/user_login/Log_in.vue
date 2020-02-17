<template>
  <div>
    <el-form>
      <el-form-item label="Username:">
        <el-input></el-input>
      </el-form-item>
    </el-form>
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
