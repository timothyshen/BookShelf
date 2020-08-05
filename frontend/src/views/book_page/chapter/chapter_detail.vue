<template>
  <div class="chapter_container">
    <header class="chapter_header">
      <div class="header_top">
        <div class="text_setting">
          <el-select v-model="choices.font_size" style="width: 100px" placeholder="Size">
            <el-option label="16pt" value="16"/>
            <el-option label="18pt" value="18"/>
            <el-option label="20pt" value="20"/>
            <el-option label="22pt" value="22"/>
            <el-option label="24pt" value="24"/>
          </el-select><!--font-->
          <el-select v-model="choices.background" style="width: 100px" placeholder="Background">
            <el-option style="background-color: lightyellow" label="lightyellow" value="lightyellow"/>
            <el-option style="background-color: lightsteelblue" label="lightsteelblue" value="lightsteelblue"/>
            <el-option style="background-color: lightskyblue" label="lightskyblue" value="lightskyblue"/>
          </el-select><!--background color-->
          <el-select v-model="choices.font_family" style="width: 100px" placeholder="Font">
            <el-option label="Arial" value="Arial"/>
            <el-option label="Roboto" value="Roboto"/>
            <el-option label="Courier" value="Courier"/>
          </el-select><!--font-family-->
          <el-select v-model="choices.text_color" style="width: 150px" placeholder="Text color">
            <el-option label="Default" value="#000"/>
            <el-option label="Purple" value="#9370DB"/>
            <el-option label="Green" value="#2E8B57"/>
            <el-option label="DarkSlateGray" value="#2F4F4F"/>
            <el-option label="Steel blue" value="#778899"/>
            <el-option label="Maroon" value="#800000"/>
            <el-option label="Cyan" value="#6A5ACD"/>
            <el-option label="Rosy brown" value="#BC8F8F"/>
            <el-option label="Brown" value="#F4A460"/>
            <el-option label="Beige" value="#F5F5DC"/>
            <el-option label="White" value="#F5F5F5"/>
          </el-select><!---->
        </div>
      </div>
      <div class="chapter_info">
        <h2 class="chapter_name">{{this.chapter.chapter_title}}</h2>
        <div class="button_group">
          <el-button-group>
            <el-button>Previous</el-button>
            <el-button>
              <router-link :to="{name:'book'}">Index</router-link>
            </el-button>
            <el-button @click="goToNext">Next</el-button>
            <el-button>Bookmark</el-button>
          </el-button-group>
        </div>
      </div>
    </header>
    <el-main>

      <p v-bind:style="changeStyle()" class="default_text">
        {{this.chapter.chapter_body}}
      </p>
    </el-main>
    <div class="chapter_info">
      <div class="button_group">
        <el-button-group>
          <el-button @click="goToPrevious">Previous</el-button>
          <el-button>
            <router-link :to="{name:'book'}">Index</router-link>
          </el-button>
          <el-button @click="goToNext">Next</el-button>
          <el-button @click="addBookMarkFunction">Bookmark</el-button>
        </el-button-group>
      </div>
    </div>
  </div>
</template>

<script>
  import axios from 'axios';
  import {addBookMark, getChapterItem, getChapterList} from "../../../api/api";

  export default {
    name: "chapter_detail",
    data() {
      return {
        chapter: {},
        choices: {
          font_size: '',
          background: '',
          font_family: '',
          text_color: ''
        },
        listOfChapter: []
      }
    },
    beforeRouteUpdate(to, from, next) {
      console.log(to, from, next);
      next();
      this.getChapter();

    },
    props: {
      book_id: Number,
      id: Number,
      position: Number
    },
    created() {
      this.getChapter()
    },
    methods: {
      getChapter() {
        getChapterItem(this.$route.params.book_id, this.$route.params.id).then((response) => {
          // console.log(response.data);
          this.chapter = response.data;
        }).catch((error) => {
          console.log(error)
        });
        getChapterList(this.$route.params.book_id).then((response) => {
          console.log(response.data);
          this.listOfChapter = response.data
        }).catch((error) => {
          console.log(error)
        });
      },
      changeStyle() {
        return {
          fontSize: this.choices.font_size + 'px',
          backgroundColor: this.choices.background,
          fontFamily: this.choices.font_family,
          color: this.choices.text_color
        }
      },
      addBookMarkFunction() {
        addBookMark({
          chapter: this.chapter.id,
        }).then((response) => {
          console.log(response);
          this.$message({
            message: 'The book mark has been added',
            type: 'success'
          })
        }).catch((error) => {
          console.log(error)
        })
      },
      goToPrevious() {
        // console.log(this.listOfChapter[this.$route.query.position]);
        if (this.$route.query.position === 0) {
          this.$router.push({name: 'book'})
        } else {
          this.$router.push({
            name: 'chapter',
            params: {
              book_id: this.listOfChapter[this.$route.query.position - 1].book,
              id: this.listOfChapter[this.$route.query.position - 1].id,
            },
            query: {
              position: this.$route.query.position - 1
            }
          })

        }

      },
      goToNext() {
        console.log(this.listOfChapter[this.$route.query.position + 1]);
        if (this.$route.query.position === (this.listOfChapter.length - 1)) {
          this.$router.push({name: 'book'})
        } else {
          this.$router.push({
            name: 'chapter',
            params: {
              book_id: this.listOfChapter[this.$route.query.position + 1].book,
              id: this.listOfChapter[this.$route.query.position + 1].id,
            },
            query: {
              position: this.$route.query.position + 1
            }
          })
        }
      }
    }
  }
</script>

<style lang="less" scoped>

  .chapter_container {
    .chapter_header {
      height: 100%;
      padding: 0 20px;
      display: block;

      .header_top {
        height: 30px;
        margin-bottom: 20px;

        .breadcrumb_set {
          display: block;
          float: left;

          .el-breadcrumb__item span {
            font-size: 20px;
            line-height: 30px;
          }
        }

        .text_setting {
          float: right;
        }
      }
    }

    .chapter_info {
      .chapter_name {
        text-align: center;
        margin-bottom: 10px;
      }

      .button_group {
        margin: 0 auto;
        width: 400px;

        .el-button {
          width: 100px;
        }
      }
    }

    .default_text {
      font-size: 20px;
      font-family: Calibri Light, sans-serif;
      background-color: white;
      color: black;
    }
  }
</style>
<style>

</style>
