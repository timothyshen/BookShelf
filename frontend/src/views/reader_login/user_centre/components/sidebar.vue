<template>
  <el-menu
    :default-active="defaultActiveIndex"
    mode="vertical"
    background-color="#545c64"
    text-color="#fff"
    active-text-color="#ffd04b"
    style="width: 200px" :router="true">
    <el-menu-item index="/userManager">
      <i class="el-icon-setting"/>
      <span slot="title">Home</span>
    </el-menu-item>
    <el-menu-item index="2" route="bookcase">
      <i class="el-icon-setting"/>
      <span slot="title">Bookcase</span>
    </el-menu-item>
    <el-menu-item index="3">
      <i class="el-icon-setting"/>
      <span slot="title">My comment</span>
    </el-menu-item>
    <el-menu-item index="4">
      <i class="el-icon-setting"/>
      <span slot="title">VIP</span>
    </el-menu-item>
    <el-menu-item index="security">
      <i class="el-icon-setting"/>
      <span slot="title">Security</span>
    </el-menu-item>
    <el-menu-item index="setting">
      <i class="el-icon-setting"/>
      <span slot="title">Profile</span>
    </el-menu-item>
  </el-menu>
</template>

<script>
  export default {
    name: "sidebar",
    data() {
      return{
        defaultActiveIndex: '/userManager'
      }
    }
  }
</script>

<style scoped>

</style>
