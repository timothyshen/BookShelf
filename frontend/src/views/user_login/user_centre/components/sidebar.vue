<template>
  <el-menu
    default-active="1"
    mode="vertical"
    background-color="#545c64"
    text-color="#fff"
    active-text-color="#ffd04b">
    <el-menu-item index="1">
      <i class="el-icon-setting"/>
      <span slot="title">Home</span>
    </el-menu-item>
    <el-menu-item index="2">
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
    <el-menu-item index="5">
      <i class="el-icon-setting"/>
      <span slot="title">Security</span>
    </el-menu-item>
    <el-menu-item index="6">
      <i class="el-icon-setting"/>
      <span slot="title">Profile</span>
    </el-menu-item>
  </el-menu>
</template>

<script>
  export default {
    name: "sidebar"
  }
</script>

<style scoped>

</style>
