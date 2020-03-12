<template>
  <div class="user_profile_background">
    <div class="icon_row">
      <div>
        <el-avatar class="user_icon" type="circle"/>
        <h2 v-model="userInfo.username"/>
      </div>
      <el-button-group class="user_button_group">
        <el-button class="user_setting_button" size="small" icon="el-icon-view" round>Profile</el-button>
        <el-button class="user_setting_button" size="small" icon="el-icon-setting" round>Setting</el-button>
      </el-button-group>

    </div>
    <div class="inform_bar">

    </div>
  </div>
</template>

<script>
  import {getUserDetail} from "../../../../api/api";

  export default {
    name: "user_profile",
    data() {
      return {
        userInfo: {
          username: '',
          password: '',
          checkPass: '',
          gender: '',
          birthday: '',
          email: '',
          avatar: '',
        }
      }
    },
    created() {
      this.getUserInfo();
    },
    methods: {
      getUserInfo() {
        getUserDetail().then((response) => {
          this.userInfo = response.data;
        }).catch(function (error) {
          console.log(error);
        })

      }
    }
  }
</script>

<style scoped lang="less">
  .user_profile_background {
    background: linear-gradient(top, #e66465, #9198e5);
    width: 100%;
    height: 200px;
    margin: 10px;

    .icon_row {
      position: relative;
      top: 30px;
      height: 100px;

      .user_icon {
        margin-left: 20px;
        width: 90px;
        height: 90px;
      }

      .user_button_group {
        position: relative;
        bottom: 40px;
        left: 60%;
      }

      .user_setting_button {
        width: 100px;

      }
    }

    .inform_bar {
      height: 100px;
      width: inherit;
      background: black;
      border-top: black 1px solid;
    }
  }
</style>
