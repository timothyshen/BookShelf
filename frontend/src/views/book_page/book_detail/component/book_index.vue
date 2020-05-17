<template>
  <div class="top">
    <el-tabs>
      <el-tab-pane label="Description">
        <p>{{index_info.description}}</p>
      </el-tab-pane>
      <el-tab-pane label="Chapters">
        <h2 class="chapter_title">All chapters</h2>
        next
        <ul class="chapter_list">
          <li class="chapter_item" v-for="(chapter, index) in index_info.chapters" v-bind="chapter">
            <router-link :to="{name: 'chapter', params:{book_id:index_info.book_id, id:'1', url: chapter.url}}">{{chapter.id}}. {{chapter.chapter_title}}</router-link>
          </li>
        </ul>


      </el-tab-pane>
    </el-tabs>

  </div>
</template>

<script>
  import axios from "axios";

  export default {
    name: "book_index",
    props:{
      index_info:{
        type: Object
      }
    },
    created() {

    },
    methods: {}
  }
</script>

<style lang="less" scoped>
  .chapter_title {
    margin-bottom: 20px;
  }

  .chapter_list {
    column-count: 3;
    margin: 0 10px;

    .chapter_item {
      border-bottom: 2px solid black;
      text-decoration: none;
      display: inline-block;
      height: 40px;
      width: 100%;
      font-size: 18px;
      text-align: center;
      padding-top: 10px;
      line-height: 40px;
    }
  }
</style>
