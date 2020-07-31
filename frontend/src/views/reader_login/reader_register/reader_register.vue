<template>
  <div class="register_container">
    <el-col :span="12" :offset="6">
      <el-form :model="registerForm" ref="registerForm" :rules="rules" label-width="100px"
               :label-position="labelPosition">
        <el-form-item label="Username" prop="username">
          <el-input type="text" v-model="registerForm.username">username</el-input>
          <p class="error-text" v-show="error.username">{{error.username}}</p>
        </el-form-item>
        <el-form-item label="Password:" prop="password">
          <el-input
            type="password"
            v-model="registerForm.password"
            show-password>password
          </el-input>
          <p class="error-text" v-show="error.password">{{error.password}}</p>
        </el-form-item>
        <el-form-item label="Confirm password:" prop="checkPass">
          <el-input
            type="password"
            v-model="registerForm.checkPass"
            show-password>password
          </el-input>
        </el-form-item>
        <el-form-item label="Gender:" prop="gender">
          <el-radio-group v-model="registerForm.profile.gender">
            <el-radio label="male">Male</el-radio>
            <el-radio label="female">Female</el-radio>
          </el-radio-group>
        </el-form-item>
        <el-form-item label="Email:" prop="email">
          <el-input type="email" v-model="registerForm.email" :rules="email"/>
          <p class="error-text" v-show="error.email">{{error.email}}</p>
        </el-form-item>
        <el-form-item label="Date of Birth" prop="birthday">
          <el-date-picker
            value-format="yyyy-MM-dd"
            v-model="registerForm.profile.birthday"
            type="date"
            placeholder="pick a date">
          </el-date-picker>
        </el-form-item>
        <el-form-item label="Avatar" required>
          <el-upload
            class="avatar-uploader"
            action="https://jsonplaceholder.typicode.com/posts/"
            :http-request="uploadImage"
            :on-success="handleAvatarSuccess"
            :show-file-list="false"
            :before-upload="beforeAvatarUpload"
            :on-exceed="handleExceed">
            <img v-if="this.imageUrl" :src="this.imageUrl" class="avatar">
            <i v-else class="el-icon-plus avatar-uploader-icon"></i>
          </el-upload>
        </el-form-item>
        <el-button type="primary" @click="isRegister">Register</el-button>
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
        } else if (this.registerForm.checkPass !== '') {
          this.$refs.registerForm.validateField('checkPass');
        }
      };
      let validatePass2 = (rule, value, callback) => {
        if (value === '') {
          callback(new Error('Please reenter the password'));
        } else if (value !== this.registerForm.password) {
          callback(new Error('The password is not the same'));
        } else {
          callback();
        }
      };
      let emailValidator = (rule, value, callback) => {
        const mailReg = /^([a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+(.[a-zA-Z0-9_-])+/;
        if (!value) {
          return callback(new Error('Email can not be empty'))
        }
        setTimeout(() => {
          if (mailReg.test(value)) {
            callback()
          } else {
            callback(new Error('Please insert correct email format'))
          }
        }, 100)
      };
      let usernameValidator = (rule, value, callback) => {
        const usernameReg = /(?=[a-zA-Z0-9._]{8,20}$)(?!.*[_.]{2})[^_.].*[^_.]$/;
        if(!value){
          return callback(new Error('Username can not be empty'))
        }
        setTimeout(() => {
          if (usernameReg.test(value)) {
            callback()
          } else {
            callback(new Error('Please insert correct username format'))
          }
        }, 100)
      };
      return {
        labelPosition: 'left',
        imageUrl: '',
        formData: '',
        registerForm: {
          username: '',
          password: '',
          checkPass: '',
          email: '',
          profile: {
            gender: '',
            birthday: '',
            avatar: {},
            role: 'Reader'
          },
        },
        error: {
          password: '',
          username: '',
          email: '',
        },
        rules: {
          password: [{
            validator: validatePass, trigger: 'blur'
          }],
          checkPass: [{
            validator: validatePass2, trigger: 'blur'
          }],
          email: [{
            validator: emailValidator, trigger: 'blur'
          }],
          username:[{
            validator: usernameValidator, trigger:'blur'
          }]
        }
      }
    },
    methods: {
      uploadImage(item) {
        console.log(item.file);
        this.formData = new FormData();
        this.formData.append('profile.icon', item.file);
        this.formData.append('profile.birthday', this.registerForm.profile.birthday);
        this.formData.append('profile.gender', this.registerForm.profile.gender);
        this.formData.append('profile.role', this.registerForm.profile.role);
        this.formData.append('username', this.registerForm.username);
        this.formData.append('password', this.registerForm.password);
        this.formData.append('email', this.registerForm.email);
        console.log(...this.formData);
      },
      isRegister() {
        let that = this;
        register(
          this.formData
        ).then((response) => {
          cookie.setCookie('user_id', response.data.user_id, 7);
          cookie.setCookie('name', response.data.name, 7);
          cookie.setCookie('token', response.data.token, 7);
          cookie.setCookie('role', response.data.role, 7);
          that.$store.dispatch('setInfo');
          that.$router.push({name: 'login'});
          console.log('success')
        }).catch(function (error) {
          console.log(error);
          console.log(error.username[0]);
          that.error.username = error.username ? error.username[0] : '';
          that.error.password = error.password ? error.password[0] : '';
        });
      },
      resetForm(formName) {
        this.$nextTick(() => {
          this.$refs[formName].resetFields();
        })
      },
      handleAvatarSuccess(res, file) {
        this.imageUrl = URL.createObjectURL(file.raw);
      },
      beforeAvatarUpload(file) {
        const isJPG = file.type === 'image/jpeg';
        const isLt2M = file.size / 1024 / 1024 < 2;
        if (!isJPG) {
          this.$message.error('The picture should be a JPEG file');
        }
        if (!isLt2M) {
          this.$message.error('The picture size should be less than 2MB!');
        }
        return isJPG && isLt2M;
      },
      handleExceed(){
        this.$message.error('You can only upload one image for your icon');
      },
    }
  }
</script>

<style>
  .register_container {
    margin: 20px 0;
    height: 600px;
  }
</style>
