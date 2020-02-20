<template>
  <el-row :gutter="24" class="container_head">
    <el-col  :span="18" :offset="3" class="wrapper">
      <el-row :gutter="20">
        <el-col :span="3" class="logo">
          <p style="color: white">
            This is a logo
          </p>
<!--              <img/>-->
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
            <img/>
            <el-menu-item index="1">Creator</el-menu-item>
            <el-menu-item index="2">Completed</el-menu-item>
            <el-menu-item index="3">Library</el-menu-item>
          </el-menu>
        </el-col>
        <el-col :span="8">
          <el-input
            placeholder="Search"
            class="input_nav"
            v-model="input2"
            size="large">
            <el-button slot="append" icon="el-icon-search"></el-button>
          </el-input>
        </el-col>
        <el-col :span="4" :offset="2">
          <el-menu
            :default-active="1"
            class="navBar"
            mode="horizontal"
            background-color="#545454"
            text-color="#fff"
            active-text-color="#ffd04b"><!--Save for later -->
            <!--logo and nav-->
            <el-menu-item index="1">Login</el-menu-item>
            <el-menu-item index="2">SignUp</el-menu-item>
          </el-menu>
        </el-col>
      </el-row>
    </el-col><!--first col layer-->
  </el-row>
</template>

<script>
    export default {
        name: "headbar"
    }
</script>

<style>
.container_head{
  background-color: #545454;
}
.input_nav{
  margin-top: 10px;
}



</style>
