<template>
  <el-main style="width: 50%">
    <el-form v-model="user_info">
      <el-form-item label="Username" prop="username">
        <el-input
          v-model="user_info.username"
          type="text">username
        </el-input>
      </el-form-item>
      <el-form-item label="Gender:">
        <el-radio-group v-model="user_info.profile.gender">
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
      <el-button type="primary" @click="updateUser">Save</el-button>
    </el-form>
  </el-main>
</template>

<script>
  import {getUserDetail, updateUserDetail} from "../../../../api/api";

  export default {
    name: "author_setting",
    computed:{
      getUserId(){
        return this.$store.state.userInfo.user_id;
      }
    },
    data() {
      return {
        user_info:{},

      }
    },
    created() {
      this.getUser()
    },
    methods:{
      getUser(){
        getUserDetail(this.getUserId).then((response) =>{
          console.log(response.data);
          this.user_info = response.data;
        })
      },
      updateUser(){
        updateUserDetail(this.getUserId,{
          'username': this.user_info.username,
          'email': this.user_info.email,
          "profile": {
            "gender": this.user_info.profile.gender,
            "birthday": this.user_info.profile.birthday,
          }
        }).then((response)=>{
          console.log(response.data)
        })
      }
    }
  }
</script>

<style scoped>

</style>
