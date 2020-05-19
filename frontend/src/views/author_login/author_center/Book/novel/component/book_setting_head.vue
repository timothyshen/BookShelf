<template>
  <el-row class="container_author">
    <el-col :span="24" class="topbar-wrap">
      <div class="topbar-logo topbar-btn">
        <router-link to="/authorManagement">
          <el-image src='../../../../../../static/image/logo.png'></el-image>
        </router-link>
      </div>
      <div class="topbar-title">
        <el-page-header class="page_head" @back="goBack">
          <template slot="content">
            <span class="head_content">Setting</span>
          </template>
        </el-page-header>
      </div>
    </el-col>
  </el-row>
</template>

<script>
    export default {
        name: "book_create_head",
      methods:{
          goBack(){
            this.$router.go(-1);
          }
      }
    }
</script>

<style lang="less" scoped>
  .container_author {
    width: 100%;

    .topbar-wrap {
      height: 50px;
      line-height: 50px;
      background: #000000;
      padding: 0px;

      .topbar-btn {
        color: #fff;
      }

      .topbar-logo {
        float: left;
        width: 200px;
        line-height: 26px;
      }

      .topbar-title {
        width: 500px;
        float: left;
        text-align: left;
        padding-left: 10px;
        border-bottom: 0;
        border-left: 1px solid #000;
        .page_head, .head_content{
          color: white;
          line-height: 50px;
          font-size: 20px;
        }
      }
      .button{
        float: right;
        padding-right: 12px;
      }
    }
  }
</style>
