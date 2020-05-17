<template>
  <el-container class="user_container_body">
    <router-view name="aside"></router-view>
    <router-view></router-view>
  </el-container>
</template>

<script>
  import sidebar from "./components/sidebar";
  import user_profile_component from "./components/user_profile";
  import msg_table from "./components/msg_table";
  import exp_table from "./components/exp_table";
  import bookcase from "./components/bookcase";

  export default {
    name: "user_center",
    components: {sidebar, user_profile_component, msg_table, exp_table, bookcase},
    data() {
      return {
        tabPosition: 'left',
        index: 1
      }
    }
  }
</script>

<style lang="less" scoped>
  .user_container_body {
    margin: 0 auto;
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
