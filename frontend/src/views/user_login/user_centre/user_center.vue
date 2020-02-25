<template>
  <el-col :span="12" :offset="6">
    <el-container class="user_container_body">
      <el-aside
        class="aside"
        width="200px">
        <sidebar/>
      </el-aside>
      <el-container class="user_body">
        <!--          <div class="userInfo">-->
        <!--            <div>-->
        <!--              <el-image type="circle" class="user_icon"/>-->
        <!--              <p>Username</p>-->
        <!--              <div>-->
        <!--                <el-button-group>-->
        <!--                  <el-button>Setting</el-button>-->
        <!--                </el-button-group>-->
        <!--              </div>-->
        <!--            </div>-->
        <!--          </div>-->
        <user_profile/>
        <div>
          <div></div>
        </div>
        <div></div>
        <div></div>
      </el-container>
    </el-container>
  </el-col>
</template>

<script>
  import sidebar from "./components/sidebar";
  import user_profile from "./components/user_profile";

  export default {
    name: "user_center",
    components: {sidebar, user_profile},
    data() {
      return {
        tabPosition: 'left'
      }
    }
  }
</script>

<style lang="less" scoped>
  .user_container_body {
    height: 600px;
    width: 900px;

    .aside {
      width: 200px;
      background-color: #545c64;
    }

    .user_body {
      width: 100%;
    }
  }
</style>
