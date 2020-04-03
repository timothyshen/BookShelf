<template>
  <el-row class="wrap">
    <el-collapse>
      <el-collapse-item name="1">
        <template slot="title">
          <h3>Message</h3>
        </template>
        <el-alert
          title="Important notice"
          type="info"
          show-icon
          :closable="false"
        description="">
        </el-alert>
        <template slot="default">
          <div>This is a message tab for global message</div>
        </template>
      </el-collapse-item>
      <div>
        <img/>
        <div>
          <h2>Number of clicks</h2>
          <span>0</span>
        </div>
        <div>
          <h2>Number of reader</h2>
          <span>0</span>
        </div>
        <div>
          <h2>Number of Favorate</h2>
          <span>0</span>
        </div>
      </div>
    </el-collapse>

  </el-row>
</template>

<script>
    export default {
        name: "dashboard"
    }
</script>

<style scoped>

</style>
