<template>
  <div>
    <el-row class="text_editor_head">
      <el-col>
        <h2>Word count:</h2>
        <span>{{wordCount}}</span>
        <h2>Paragraph count:</h2>
        <span>{{paragraphCount}}</span>
      </el-col>
    </el-row>
    <el-form class="chapter_editor" v-model="chapter_data">
      <el-form-item>
        <el-input
          v-model="chapter_data.chapter_title"
          class="editor_title"
          placeholder="Title">
        </el-input>
      </el-form-item>
      <el-form-item>
        <el-input
          v-model="chapter_data.chapter_body"
          id="chapter_body"
          class="editor_body"
          placeholder="Title"
          type="textarea"
          resize="none"
          show-word-limit
          @input="countingWords"
          :autosize="{minRows: 4, maxRows: 20}"
        >
        </el-input>
      </el-form-item>
      <div>
        <el-button @click="updateChapter('Draft')">Save as draft</el-button>
        <el-button @click="updateChapter('Published')">Publish</el-button>
      </div>
    </el-form>
  </div>
</template>

<script>
  import {getChapterItemForBook, updateChapterItemForBook} from "../../../../../api/api";

  export default {
    name: 'author_chapter_exist',
    data() {
      return {
        wordCount: 0,
        paragraphCount: 0,
        chapter_data:{},
      }
    },
    computed:{
      bookId(){
        return this.$route.params.book_id;
      },
      chapterId(){
        return this.$route.params.chapter_id;
      }
    },
    created() {
      this.getChapter();
    },
    methods: {
      countingWords: function () {
        this.wordCount = this.chapter_data.chapter_body.split(' ').length;
        let paragraphs = this.chapter_data.chapter_body.replace(/\n$/gm, '').split(/\n/);
        this.paragraphCount = paragraphs.length;
        // console.log(this.wordCount);
        // console.log(this.message);
      },
      getChapter() {
        getChapterItemForBook(this.bookId, this.chapterId)
          .then((response) => {
            this.chapter_data = response.data;
            this.wordCount = response.data.word_count;
          console.log(response.data)
        })
      },
      updateChapter(chapterStatus){
        updateChapterItemForBook(this.bookId, this.chapterId, {
          'chapter_title':this.chapter_data.chapter_title,
          'chapter_body':this.chapter_data.chapter_body,
          'word_count': this.wordCount,
          'publish_status': chapterStatus
        }).then((response)=>{
          this.$router.push({name:'chapter_view'})
        }).catch(err =>{
          console.log(err)
        })
      }
    }
  }
</script>

<style lang="less" scoped>
  .text_editor_head {
    height: 50px;
    width: 100%;
  }


  .chapter_editor {
    width: 900px;
    margin: 0 auto;

    .el-form-item {
      margin-bottom: 10px;

      .editor_title /deep/ .el-input__inner {
        border-radius: 0;
        font-size: 24px;
        border: none transparent;
        border-bottom: 1px solid grey;
      }

      .editor_body /deep/ .el-textarea__inner {
        border-radius: 0;
        font-size: 16px;
        border: none transparent;
        min-height: 600px;
      }
    }
  }
</style>
