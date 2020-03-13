<template>
  <el-col :span="12" :offset="6">
    <el-container class="user_container_body">
      <el-aside
        class="aside"
        width="200px">
        <sidebar/>
      </el-aside>
      <el-container class="user_body">

        <user_profile/>
        <msg_table/>
      </el-container>
    </el-container>
  </el-col>
</template>

<script>
  import sidebar from "./components/sidebar";
  import user_profile from "./components/user_profile";
  import msg_table from "./components/msg_table";

  export default {
    name: "user_center",
    components: {sidebar, user_profile, msg_table},
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
      display: block;

      .user_body * {
        margin: 10px;
      }
    }
  }
</style>
