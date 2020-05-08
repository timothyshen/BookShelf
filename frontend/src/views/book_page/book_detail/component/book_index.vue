<template>
  <div class="top">
    <el-tabs>
      <el-tab-pane label="Description">
        <p>{{description}}</p>
      </el-tab-pane>
      <el-tab-pane label="Chapters">
        <h2 class="chapter_title">All chapters</h2>
        <ul class="chapter_list">
          <li class="chapter_item" v-for="(chapter, index) in chapters" v-bind="chapter">
            {{chapter.id}}. {{chapter.chapter_title}}
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
    data() {
      return {
        description:'',
        chapters:''
      }
    },
    created() {
      this.getChapter();
    },
    methods:{
      getChapter(){
        axios.get(`http://127.0.0.1:8000/book/detail/2`).then((response) => {
          console.log(typeof response.data);
          this.description = response.data.book_description;
          let chapter_item = response.data.Chapter;
          this.chapters = Object.values(chapter_item)
          console.log(this.chapters);
        })
      }
    }
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
