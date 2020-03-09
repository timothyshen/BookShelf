<template>
  <div class="register_container">
    <el-col :span="12" :offset="6">
      <el-form :model="registerForm" ref="registerForm" :rules="rules" label-width="100px" :label-position="labelPosition">
        <el-form-item label="Username" prop="username">
          <el-input type="text" v-model="registerForm.username">username</el-input>
        </el-form-item>
        <el-form-item label="Password:" prop="password">
          <el-input
            type="password"
            v-model="registerForm.password"
            show-password>password</el-input>
        </el-form-item>
        <el-form-item label="Confirm password:" prop="checkPass">
          <el-input
            type="password"
            v-model="registerForm.checkPass"
            show-password>password</el-input>
        </el-form-item>
        <el-form-item label="Gender:" prop="gender">
          <el-radio-group v-model="registerForm.gender">
            <el-radio label="m">Male</el-radio>
            <el-radio label="f">Female</el-radio>
          </el-radio-group>
        </el-form-item>
        <el-form-item label="Email:" prop="email">
          <el-input type="email" v-model="registerForm.email"/>
        </el-form-item>
        <el-form-item label="Date of Birth" prop="birthday">
          <el-date-picker
            v-model="registerForm.birthday"
            type="date"
            placeholder="pick a date">
          </el-date-picker>
        </el-form-item>
        <el-form-item label="Avatar" prop="avatar">
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
        <el-button @click="resetForm('registerForm')">Reset</el-button>
      </el-form>
    </el-col>
  </div>
</template>

<script>
  import {register} from '../../../api/api'
  import cookie from "../../../static/cookie/cookie";
    export default {
      name: "register",
      data() {
        let validatePass = (rule, value, callback) => {
          if (value === '') {
            callback(new Error('Please enter the password'));
          } else if (this.registerForm.checkPass !== ''){
            this.$refs.registerForm.validateField('checkPass');
          }
        };
        let validatePass2 = (rule, value, callback) => {
          if (value === ''){
            callback(new Error('Please reenter the password'));
          } else if(value !== this.registerForm.password){
            callback(new Error('The password is not the same'));
          } else {
            callback();
          }
        }
        return{
          labelPosition: 'left',
          imageUrl: '',
          registerForm: {
            username: '',
            password: '',
            checkPass: '',
            gender: 'm',
            birthday: '',
            email: '',
            avatar: ''
          },
          error: {
            password: '',
            username: ''
          },
          rules: {
            password: [{
              validator: validatePass, trigger: 'blur'
            }],
            checkPass:[{
              validator: validatePass2, trigger:'blur'
            }]
          }
        }
      },
      methods:{
          isRegister(){
            let that = this;
            register({
              password: that.registerForm.password,
              username: that.registerForm.username,
            }<!--,{
              auth:{
                username: 't.shen',
                password: 'bookshelf'
              }
            }-->).then((response)=>{
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
          beforeAvatarUpload(file){
              const isJPG = file.type === 'image/jpeg';
              const isLt2M = file.size / 1024 /1024 < 2;
            if (!isJPG) {
              this.$message.error('The picture should be a JPEG file');
            }
            if (!isLt2M) {
              this.$message.error('The picture size should be less than 2MB!');
            }
            return isJPG && isLt2M;
          },
        resetForm(formName) {
          this.$nextTick(() => {
            this.$refs[formName].resetFields();
          })
        }
      }
    }
</script>

<style>
.register_container{
  margin-bottom: 20px;
  height: 600px;
}
</style>
