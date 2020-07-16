<template>
  <div class="body">
    <el-row>
      <el-col :span="8" class="block_level">
        <div class="block_image">
          <el-image src="'../../static/image/TD%20Global%2019-20.PNG'"></el-image>
        </div>
        <dl class="block_info">
          <dt class="block_info_head">
            <a>
              Test one
            </a>
            <span>woainia</span>
          </dt>
          <dd class="block_info_description">
             Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean eget nibh vitae lacus placerat consequat.
            Fusce vitae semper felis, at volutpat velit. Vivamus ornare dolor sit amet dui vulputate
          </dd>
        </dl>
      </el-col>
      <el-col :span="8" class="block_level">
        <div class="block_image">
          <el-image></el-image>
        </div>
        <dl class="block_info">
          <dt class="block_info_head">
            <h3>
              <router-link>Test one</router-link>
            </h3>
            <span>woainia</span>
          </dt>
          <dd class="block_info_description">
             Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean eget nibh vitae lacus placerat consequat.
            Fusce vitae semper felis, at volutpat velit. Vivamus ornare dolor sit amet dui vulputate
          </dd>
        </dl>
      </el-col>
      <el-col :span="8" class="block_level">
        <div class="block_image">
          <el-image></el-image>
        </div>
        <dl class="block_info">
          <dt class="block_info_head">
            <h3>
              <router-link>Test one</router-link>
            </h3>
            <span>woainia</span>
          </dt>
          <dd class="block_info_description">
             Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean eget nibh vitae lacus placerat consequat.
            Fusce vitae semper felis, at volutpat velit. Vivamus ornare dolor sit amet dui vulputate
          </dd>
        </dl>
      </el-col>
      <el-col :span="8" class="block_level">
        <div class="block_image">
          <el-image></el-image>
        </div>
        <dl class="block_info">
          <dt class="block_info_head">
            <h3>
              <router-link>Test one</router-link>
            </h3>
            <span>woainia</span>
          </dt>
          <dd class="block_info_description">
             Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean eget nibh vitae lacus placerat consequat.
            Fusce vitae semper felis, at volutpat velit. Vivamus ornare dolor sit amet dui vulputate
          </dd>
        </dl>
      </el-col>
      <el-col :span="8" class="block_level">
        <div class="block_image">
          <el-image></el-image>
        </div>
        <dl class="block_info">
          <dt class="block_info_head">
            <h3>
              <router-link>Test one</router-link>
            </h3>
            <span>woainia</span>
          </dt>
          <dd class="block_info_description">
             Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean eget nibh vitae lacus placerat consequat.
            Fusce vitae semper felis, at volutpat velit. Vivamus ornare dolor sit amet dui vulputate
          </dd>
        </dl>
      </el-col>
      <el-col :span="8" class="block_level">
        <div class="block_image">
          <el-image></el-image>
        </div>
        <dl class="block_info">
          <dt class="block_info_head">
            <h3>
              <router-link>Test one</router-link>
            </h3>
            <span>woainia</span>
          </dt>
          <dd class="block_info_description">
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean eget nibh vitae lacus placerat consequat.
            Fusce vitae semper felis, at volutpat velit. Vivamus ornare dolor sit amet dui vulputate
          </dd>
        </dl>
      </el-col>
    </el-row>
  </div>
</template>

<script>
  export default {
    name: "main_push",
    data() {
      return {}
    }
  }
</script>

<style lang="less" scoped>
  .body {
    .block_level {
      display: table;
      height: 150px;
      padding: 5px 0px 0px 5px;

      .block_image {
        display: inline-block;
        width: 40%;
      }

      .block_info {
        display: inline-block;
        width: 60%;
        padding-right: 5px;

        .block_info_head {
          height: 25px;
          line-height: 25px;
          overflow: hidden;
          border-bottom: dotted 1px #6191D0;
          font-weight: bold;
          span{
            float: right;
            font-weight: normal;
          }
        }

        .block_info_description {

        }
      }
    }
  }
</style>
