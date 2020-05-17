<template>
  <div class="user_profile_background">
    <div class="icon_row">
      <div class="image_name">
        <el-avatar class="user_icon" type="circle"/>
      </div>
      <div class="username_tab">
        <h2 class="username">{{userInfo.username}}</h2>
      </div>
      <el-button-group class="user_button_group">
        <el-button class="user_setting_button" size="small" icon="el-icon-view" round>Profile</el-button>
        <el-button class="user_setting_button" size="small" icon="el-icon-setting" round>Setting</el-button>
      </el-button-group>
    </div>

  </div>
</template>

<script>
  import {getUserDetail} from "../../../../api/api";
  import axios from 'axios';
  import store from "../../../../store/store";

  export default {
    name: "user_profile_component",
    data() {
      return {
        userInfo: {
          username: '',
          password: '',
          gender: '',
          birthday: '',
          email: '',
          avatar: '',
        },
      }
    },
    created() {
      this.getUserInfo();
    },
    methods: {
      getUserInfo() {
        let user_id = store.state.userInfo.user_id;
        console.log(user_id);
        console.log(typeof user_id);
        getUserDetail(user_id).then((response) => {
          console.log(response.data);
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

    .icon_row {
      width: 690px;
      height: 100px;
      display: table;
      table-layout: fixed;
      .image_name {
        display: table-cell;
        .user_icon {
          margin-left: 20px;
          margin-top: 20px;
          width: 100px;
          height: 100px;
        }
      }

      .username_tab {
        display: table-cell;


      }



      .user_button_group {
        display: table-cell;
        .user_setting_button {

          width: 100px;

        }
      }


    }

    .inform_bar {
      height: 100px;
      width: inherit;
      background: #ffc58b;
      border-top: black 1px solid;
    }
  }
</style>
