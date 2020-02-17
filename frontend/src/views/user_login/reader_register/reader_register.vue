<template>
  <div>
    <head></head><!--最外层-->
    <el-col :span="12" :offset="6">
      <el-form ref="form" v-model="form_data" label-width="180px" :label-position="labelPosition">
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
        <el-form-item label="Gender:">
          <el-radio-group v-model="form_data.gender">
            <el-radio label="m">Male</el-radio>
            <el-radio label="f">Female</el-radio>
          </el-radio-group>
        </el-form-item>
        <el-form-item label="Email:" >
          <el-input type="email" v-model="form_data.email"/>
        </el-form-item>
        <el-form-item label="Date of Birth">
          <el-date-picker
            v-model="form_data.birthday"
            type="date"
            placeholder="pick a date">
          </el-date-picker>
        </el-form-item>
        <el-form-item label="Avatar">
          <el-upload
            :before-upload="beforeAvatarUpload"
            :on-success="handleAvatarSuccess"
            :show-file-list="false"
            action="https://jsonplaceholder.typicode.com/posts/"
            class="avatar-uploader">
            <img v-if="imageUrl" :src="imageUrl" class="avatar">
            <i v-else class="el-icon-plus avatar-uploader-icon"></i>
          </el-upload>
        </el-form-item>
        <el-button type="primary" @click="isRegister">Rgister</el-button>
        <el-button @click="resetForm('form_data')">Reset</el-button>
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
            gender: 'm',
            birthday:'',
            email:''
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
            });
          },
        handleAvatarSuccess(res, file){
            this.imageURL = URL.createObjectURL(file.raw);
        },
        beforeAvatarUploade(file){
            const isJPG = file.type === 'image/jpeg';
            const isLt2M = file.size / 1024 /1024 < 2;
            if(isJPG){
              console('error')
            }
        },
        resetForm(formName) {
          this.$nextTick(()=>{
            this.$refs[formName].resetFields();
          })
        },
      }
    }
</script>

<style scoped>

</style>
