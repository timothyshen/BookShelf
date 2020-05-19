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
          v-model="chapter_data.title"
          class="editor_title"
          maxlength="100"
          placeholder="Title">
        </el-input>
      </el-form-item>
      <el-form-item>
        <el-input
          v-model="chapter_data.body"
          id="chapter_body"
          class="editor_body"
          placeholder="Title"
          type="textarea"
          resize="none"
          show-word-limit
          @input="countingWords"
          minlength="200"
          :autosize="{minRows: 4, maxRows: 20}"
        >
        </el-input>
      </el-form-item>
      <div>
        <el-button @click="saveDraft">Save as draft</el-button>
        <el-button @click="savePublish">Publish</el-button>
      </div>
    </el-form>
  </div>
</template>

<script>
  import {createChapterForBook} from "../../../../../api/api";

  export default {
    name: "author_chapter_create",
    data(){
      return {
        wordCount: 0,
        paragraphCount:0,
        chapter_data:{
          title:'',
          body:''
        },

      }
    },
    methods:{
      countingWords: function () {
        this.wordCount = this.chapter_data.body.split(' ').length;

        let paragraphs = this.chapter_data.body.replace(/\n$/gm, '').split(/\n/);
        this.paragraphCount = paragraphs.length;
        // console.log(this.wordCount);
        // console.log(this.message);
      },
      saveDraft(){
        let book_id = this.$route.params.book_id;
        createChapterForBook(book_id, {
          'chapter_title': this.chapter_data.title,
          'chapter_body': this.chapter_data.body,
          'word_count': this.wordCount,
          'publish_status':'Draft'
        }).then((response)=>{
          console.log(response.data);
          this.$router.go(-1);
        })
      },
      savePublish(){
        let book_id = this.$route.params.book_id;
        createChapterForBook(book_id, {
          'chapter_title': this.chapter_data.title,
          'chapter_body': this.chapter_data.body,
          'word_count': this.wordCount,
          'publish_status':'Published',

        }).then((response)=>{
          console.log(response.data);
          this.$router.go(-1);
        })
      },
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
