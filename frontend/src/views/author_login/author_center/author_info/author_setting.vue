<template>
  <el-main style="width: 50%">
    <el-form v-model="user_info">
      <el-form-item label="Username" prop="username">
        <el-input
          v-model="user_info.username"
          type="text"
          :disabled="true">username
        </el-input>
      </el-form-item>
      <el-form-item label="Gender:">

        <el-radio-group v-model="user_info.profile.gender">

          <el-radio label="male">Male</el-radio>
          <el-radio label="female">Female</el-radio>
        </el-radio-group>
      </el-form-item>
      <el-form-item label="Email:" prop="email">
        <p class="error-text" v-show="error">{{error}}</p>
        <el-input type="email" v-model="user_info.email"/>
      </el-form-item>
      <el-form-item label="Date of Birth" prop="birthday">
        <p class="error-text" v-show="error">{{error}}</p>
        <el-date-picker
          v-model="user_info.profile.birthday"
          type="date"
          placeholder="pick a date"
          value-format="yyyy-MM-dd">
        </el-date-picker>
      </el-form-item>
      <el-form-item label="Avatar">
        <p class="error-text" v-show="error">{{error}}</p>
        <el-upload
          class="avatar-uploader"
          action="cdn"
          :file-list="fileList"
          list-type="picture-card"
          :http-request="uploadImage"
          :on-preview="handlePictureCardPreview"
          :on-exceed="handleExceed"
          :before-upload="beforeAvatarUpload"
          :limit="1">
          <i class="el-icon-plus avatar-uploader-icon"/>
        </el-upload>
        <el-dialog :visible.sync="dialogVisible">
          <img width="100%" :src="dialogImageUrl" alt="">
        </el-dialog>
      </el-form-item>
      <el-button type="primary" @click="updateUser">Save</el-button>
    </el-form>
  </el-main>
</template>

<script>
  import {getUserDetail, updateUserDetail} from "../../../../api/api";
  import axios from "axios";

  export default {
    name: "author_setting",
    computed: {
      getUserId() {
        return this.$store.state.userInfo.user_id;
      }
    },
    data() {
      return {
        user_info: {},
        formData: {},
        fileList:[],
        dialogImageUrl:"",
        dialogVisible: false,
        disabled: false,
        alertVisible: false,
        noticeVisible: false,
        error:false
      }
    },
    created() {
      this.getUser()
    },
    methods: {
      getUser() {
        getUserDetail(this.getUserId).then((response) => {
          console.log(response.data);
          this.user_info = response.data;
          this.fileList.push({name:'user_icon', url:response.data.profile.icon})
        })
      },
      uploadImage(item){
        console.log(item.file);
        this.formData = new FormData();
        this.formData.append('profile.icon', item.file);
        console.log(...this.formData);
      },
      updateUser() {
        axios.all([
          updateUserDetail(this.getUserId, this.formData, {headers:{
              'Content-type':'multipart/form-data'
            }}),
          updateUserDetail(this.getUserId, {
            "email": this.user_info.email,
            "profile": {
              "gender": this.user_info.profile.gender,
              "birthday": this.user_info.profile.birthday
            }
          })]).then((response) => {
          console.log(response);
          this.$message({
            message: 'User update completed',
            type: 'success'
          })

        }).catch(err=>{
          console.log(err);
          if (err){
            this.error = "Please re-enter your detail"
          }
        })
      },
      handleRemove(file, fileList) {
        console.log(file, fileList);
      },
      handlePictureCardPreview(file) {
        this.dialogImageUrl = file.url;
        this.dialogVisible = true;
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
      }
    }
  }
</script>

<style scoped>

</style>
