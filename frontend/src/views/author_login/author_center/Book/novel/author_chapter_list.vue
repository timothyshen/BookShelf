<template>
  <div class="container-one">
    <el-tabs>
      <el-tab-pane label="Published" v-model="published_list">
        <el-col :span="24" class="show">
          <ul class="chapter_one"  v-for="(item, index) in published_list">
            <li @click="">
              <h3 class="chapter_title">{{item.chapter_title}}</h3>
              <div class="delete_button">
                <el-link class="delete_link">delete</el-link>
              </div>
              <span class="last_edit"> date</span>
            </li>
          </ul>
        </el-col>
      </el-tab-pane>
    </el-tabs>
    <el-pagination
      class="pagination"
      background
      layout="prev, pager, next"
      :total="1000">
    </el-pagination>
  </div>
</template>

<script>
  import {listChapterForBook} from "../../../../../api/api";

  export default {
    name: "author_chapter_list",
    data() {
      return {
        draft_list:[],
        trashed_list:[],
        published_list:[]
      }
    },
    created() {
      this.getBookChapter()
    },
    methods: {
      getBookChapter() {
        console.log(this.$route.params.book_id);
        listChapterForBook(this.$route.params.book_id).then((response) => {
          console.log(response.data);
          let chapters = response.data;
          chapters.forEach(element =>{
            if (element.publish_status === 'Published'){
              this.published_list.push(element);
            }else if (element.publish_status === 'Draft'){
              this.draft_list.push(element);
            }else{
              this.trashed_list.push(element)
            }
          })
        })
      },
    }
  }
</script>

<style scoped>
  .container-one {
    padding: 40px;
  }

  .show:hover div {
    display: block;
  }

  .el-tabs.el-tabs--top {
    margin-bottom: 40px;
  }

  .pagination {
    float: right;
  }
</style>
