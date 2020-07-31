<template>
  <div class="container-one">
    <el-tabs>
      <el-tab-pane label="Published" v-model="published_list">
        <el-col :span="24" class="show">
          <ul class="chapter_one"  v-for="(item, index) in published_list">
            <li>
              <h3 class="chapter_title" @click="toChapterItem(item.id)">{{item.chapter_title}}</h3>
              <div class="delete_button">
                <el-button type="danger" class="delete_link" @click="updateChapterStatus(index, item.id, published_list, 'Trash')">delete</el-button>
                <el-button type="primary" @click="updateChapterStatus(index, item.id, published_list, 'Draft')">Draft</el-button>
              </div>
              <span class="last_edit">{{item.last_update}}</span>
            </li>
          </ul>
        </el-col>
      </el-tab-pane>
      <el-tab-pane label="Draft" v-model="draft_list">
        <el-col :span="24" class="show">
          <ul class="chapter_one"  v-for="(item, index) in draft_list">
            <li>
              <h3 class="chapter_title" @click="toChapterItem(item.id)">{{item.chapter_title}}</h3>
              <div class="delete_button">
                <el-button type="primary" class="delete_link" @click="updateChapterStatus(index, item.id, draft_list, 'Published')">Publish</el-button>
                <el-button type="danger" class="delete_link" @click="updateChapterStatus(index, item.id, draft_list, 'Trash')">delete</el-button>
              </div>
              <span class="last_edit"> {{item.last_update}}</span>
            </li>
          </ul>
        </el-col>
      </el-tab-pane>
      <el-tab-pane label="Trashed" v-model="trashed_list">
        <el-col :span="24" class="show">
          <ul class="chapter_one"  v-for="(item, index) in trashed_list">
            <li>
              <h3 class="chapter_title">{{item.chapter_title}}</h3>
              <div class="delete_button">
                <el-button type="primary" @click="updateChapterStatus(index, item.id, trashed_list, 'Draft')">Recover</el-button>
                <el-button type="danger" @click="deleteChapterItem(item.id)">delete</el-button>
              </div>
              <span class="last_edit"> {{item.last_update}}</span>
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
  import {listChapterForBook, deleteChapterItemForBook, updateChapterItemForBook} from "../../../../../api/api";

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
        // console.log(this.$route.params.book_id);
        listChapterForBook(this.$route.params.book_id).then((response) => {
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
      updateChapterStatus(index, id, list, BookStatus){
        console.log(index, id,  list,  BookStatus);
        if(BookStatus === 'Trash'){
          alert('do you want to trash this chapter');
        }

        updateChapterItemForBook(this.$route.params.book_id, id, {
          'publish_status': BookStatus
        }).then((response) => {
          let movedItem = list[index];
          this.trashed_list.push(movedItem);
          // console.log(this.trashed_list);
          // console.log(response);
          list.slice(index, 1);
          location.reload();
        }).catch(error =>{
          console.log(error);
        });
      },
      deleteChapterItem(id){
        alert('do you want to delete this chapter');
        deleteChapterItemForBook(this.$route.params.book_id, id).then((response) => {
          //   this.$message{
          //
          // }
        });
      },
      toChapterItem(id){
        this.$router.push({name:'chapter_retrieve', params:{chapter_id:id}})
      }
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
