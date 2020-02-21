<template>
  <el-row :gutter="24" class="container">
    <el-col  :span="20" :offset="2" class="wrapper">
      <el-row :gutter="20">
        <el-col :span="3" class="username_wrap">
          <router-link to="/app/index">
            <el-image :src="src"></el-image>
          </router-link>
        </el-col>
        <el-col :span="6">
          <el-menu
            :default-active="1"
            class="navBar"
            mode="horizontal"
            background-color="#545454"
            text-color="#fff"
            active-text-color="#ffd04b"><!--Save for later -->
            <!--logo and nav-->
            <el-menu-item index="1">Home</el-menu-item>
            <el-menu-item index="2">Creator</el-menu-item>
            <el-menu-item index="3">Completed</el-menu-item>
            <el-menu-item index="4">Library</el-menu-item>
          </el-menu>
        </el-col>
        <el-col :span="6">
          <el-input
            placeholder="Search"
            class="input_nav"
            v-model="input2"
            size="large">
            <el-button slot="append" icon="el-icon-search"></el-button>
          </el-input>
        </el-col>
        <el-col :span="8">
          <el-row type="flex" class="row-bg" justify="end">
            <el-col :span="2"><el-avatar class="block" :size="small" :src="circleUrl"></el-avatar></el-col>
            <el-col :span="4" class="username_wrap">
              <p class="username">User</p>
            </el-col>
            <el-col :span="10">
              <el-menu
                class="navBar"
                mode="horizontal"
                background-color="#545454"
                text-color="#fff"
                active-text-color="#ffd04b"><!--Save for later -->
                <!--logo and nav-->
                <el-menu-item index="1">Bookshelf</el-menu-item>
                <el-menu-item index="2">Log out</el-menu-item>
              </el-menu>
          </el-col>
          </el-row>
        </el-col>


      </el-row>
    </el-col><!--first col layer-->
  </el-row>
</template>

<script>
    export default {
        name: "login_headbar",
      data () {
        return {
          circleUrl: "https://cube.elemecdn.com/3/7c/3ea6beec64369c2642b92c6726f1epng.png",
          squareUrl: "https://cube.elemecdn.com/9/c2/f0ee8a3c7c9638a54940382568c9dpng.png",
          sizeList: ["large", "medium", "small"],
          src: require('../../static/image/logo.png')
        }
      }
    }
</script>

<style>
  .container{
    background-color: #545454;
  }
  .input_nav{
    margin-top: 10px;
  }
  .block{
    margin-top: 10px;
  }

  .username_wrap {
    text-align: center;
    height: 60px;
    line-height: 60px;
    color: #fff;
  }

</style>
