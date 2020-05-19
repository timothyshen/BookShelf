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
    <el-form class="chapter_editor">
      <el-form-item>
        <el-input
          class="editor_title"
          placeholder="Title">
        </el-input>
      </el-form-item>
      <el-form-item>
        <el-input
          v-model="message"
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
        <el-button>Save as draft</el-button>
        <el-button>Publish</el-button>
      </div>
    </el-form>
  </div>
</template>

<script>
  export default {
    name: "author_chapter_create",
    data(){
      return {
        wordCount: 0,
        paragraphCount:0,
        message:''
      }
    },
    methods:{
      countingWords: function () {
        this.wordCount = this.message.length;
        let paragraphs = this.message.replace(/\n$/gm, '').split(/\n/);
        this.paragraphCount = paragraphs.length;
        // console.log(this.wordCount);
        // console.log(this.message);
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
