<template>
  <el-row class='author_centre'>
    <el-col :span="24"><router-view name="top"/></el-col>
    <el-col :span="24" class="main">
      <router-view name="aside"/>
      <section class="content-container">
        <div class="grid-content bg-purple-light">
          <transition name="fade" mode="out-in">
            <router-view name="content"/>
          </transition>
        </div>
      </section>
    </el-col>
  </el-row>
</template>

<script>
    export default {
        name: "author_centre_view"
    }
</script>

<style lang="less" scoped>
.author_centre{
  position: absolute;
  top: 0px;
  bottom: 0px;
  width: 100%;
  .main {
    display: -ms-flexbox;
    display: flex;
    position: absolute;
    top: 50px;
    bottom: 0px;
    overflow: hidden;
  }
  .content-container {
    background: #f2f2f2;
    -ms-flex: 1;
    flex: 1;
    overflow-y: auto;
    padding: 10px;
    .grid-content {
      border-radius: 2px;
      background-color: #fff;
    }
  }
}
</style>
