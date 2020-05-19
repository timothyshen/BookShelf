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
            <span class="head_content">Story</span>
          </template>
        </el-page-header>
      </div>
      <div class="button">
        <router-link :to="{name:'book_setting', params:{book_id:this.$route.params.book_id}}">
          <el-button icon="el-icon-setting"></el-button>
        </router-link>
        <el-button icon="el-icon-plus" @click="toCreate">New Chapter</el-button>
      </div>
    </el-col>
  </el-row>
</template>

<script>
  export default {
    name: "book_list_head",
    methods:{
      goBack(){
        window.history.length > 1 ? this.$router.go(-1) : this.$router.push('/')
      },
      toCreate(){
        console.log(this.$route.params.book_id);
        this.$router.push({name:'chapter_create', params:{book_id:this.$route.params.book_id}})
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

        .page_head, .head_content {
          color: white;
          line-height: 50px;
          font-size: 20px;
        }
      }

      .button {
        float: right;
        padding-right: 12px;
      }
    }
  }
</style>
