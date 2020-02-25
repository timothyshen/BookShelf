<template>
  <el-container class="container_body">
    <el-aside class="aside">
      <el-tabs :tab-position="tabPosition" class="tabs">
        <el-tab-pane label="Home">Home</el-tab-pane>
        <el-tab-pane label='Bookcase'>Bookcase</el-tab-pane>
        <el-tab-pane label="My comment">My comment</el-tab-pane>
      </el-tabs>
      <el-tabs :tab-position="tabPosition" class="tabs">
        <el-tab-pane>Vip centre</el-tab-pane>
        <el-tab-pane>Security</el-tab-pane>
        <el-tab-pane>Setting</el-tab-pane>
      </el-tabs>
    </el-aside>
    <el-container>
      <el-header>
        <div class="userInfo">
          <div>
            <el-image type="circle" class="user_icon"></el-image>
            <p>Username</p>
            <div>
              <el-button-group>
                <el-button>Settring</el-button>
              </el-button-group>
            </div>
          </div>
        </div>
      </el-header>
      <el-main>
        <div>
          <div></div>
        </div>
        <div></div>
        <div></div>
      </el-main>
    </el-container>
  </el-container>
</template>

<script>
    export default {
        name: "user_center",
      data(){
          return {
            tabPosition:'left'
          }
      }
    }
</script>

<style lang="less">
.aside{
  width: 300px;
}
</style>
