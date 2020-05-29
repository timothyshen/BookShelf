<template>
  <el-main>
    <el-form v-model="user_info">
      <el-form-item label="Username" prop="username">
        <el-input
          v-model="user_info.username"
          type="text">username
        </el-input>
      </el-form-item>
      <el-form-item label="Gender:">
        <el-radio-group v-model="user_info.profile.gender">
          <
          <el-radio label="male">Male</el-radio>
          <el-radio label="female">Female</el-radio>
        </el-radio-group>
      </el-form-item>
      <el-form-item label="Email:" prop="email">
        <el-input type="email" v-model="user_info.email"/>
      </el-form-item>
      <el-form-item label="Date of Birth" prop="birthday">
        <el-date-picker
          v-model="user_info.profile.birthday"
          type="date"
          placeholder="pick a date">
        </el-date-picker>
      </el-form-item>
      <el-form-item label="Avatar">
        <el-upload
          class="avatar-uploader"
          action="cdn"
          :file-list="fileList"
          list-type="picture-card"
          :http-request="uploadImage"
          :on-preview="handlePictureCardPreview"
          :on-exceed="handleExceed"
          :limit="1">
          <i class="el-icon-plus avatar-uploader-icon"/>
        </el-upload>
        <p v-if="alertVisible">You can only upload one image for your icon</p>
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

  export default {
    name: "user_setting",
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
        alertVisible: false
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
        this.formData.append('profile.birthday', this.user_info.profile.birthday);
        this.formData.append('profile.gender', this.user_info.profile.gender);
        this.formData.append('username', this.user_info.username);
        updateUserDetail(this.getUserId, this.formData).then((response) => {
          console.log(response.data)
        }).catch(err=>{
          console.log(err)
        })
      },
      handleRemove(file, fileList) {
        console.log(file, fileList);
      },
      handlePictureCardPreview(file) {
        this.dialogImageUrl = file.url;
        this.dialogVisible = true;
      },
      handleExceed(file, fileList){
        this.alertVisible = true
      }
    }
  }
</script>

<style scoped>
  .avatar{
    height: inherit;
    width: inherit;
    font-family: Jokerman,serif;
  }
</style>
