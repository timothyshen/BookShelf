<template>
  <el-container class="user_container_body">
    <router-view name="aside"></router-view>
    <router-view></router-view>
  </el-container>
</template>

<script>


  export default {
    name: "user_center",
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
