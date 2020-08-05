<template>
  <div class="top">
    <el-tabs>
      <el-tab-pane label="Description">
        <el-row class="index_wrap">
          <p>{{index_info.description}}</p>
        </el-row>
        <el-row class="index_wrap user_comment_head">
          <el-col :span="6" class="comment_title">
            <h3>User Comments</h3>
          </el-col>
          <el-col :span="6" :offset="12" class="comment_button">
            <el-button @click="dialogVisible = true">Write Comment</el-button>
          </el-col>
        </el-row>
        <el-dialog
          title="User Comment"
          :visible.sync="dialogVisible"
          width="30%"
          >
          <p style="margin-bottom: 20px">Message box</p>
          <el-input
            type="textarea"
            :rows="2"
            placeholder="Please insert your comment"
            v-model="userComment"/>
          <span slot="footer" class="dialog-footer">
            <el-button @click="dialogVisible = false">Cancel</el-button>
            <el-button type="primary" @click="postComment">Confirm</el-button>
          </span>
        </el-dialog>
        <el-row class="index_wrap user_comment_body" v-for="(item, index) in user_comment" :key="index">
          <div class="information_body">
            <div>
              <el-avatar class="block" :src="item.user.profile.icon"/>
              <span style="margin: 10px 5px; display: block">{{item.user.username}}</span>
            </div>
            <div>{{item.message}}</div>
          </div>
        </el-row>
      </el-tab-pane>
      <el-tab-pane label="Chapters">
        <h2 class="chapter_title">All chapters</h2>
        <ul class="chapter_list">
          <li class="chapter_item" v-for="(chapter, index) in index_info.chapters" v-bind="chapter">
            <router-link
              :to="{name: 'chapter', params:{book_id:index_info.book_id, id:chapter.id},query:{position:index}}">
              {{chapter.chapter_title}}
            </router-link>
          </li>
        </ul>


      </el-tab-pane>
    </el-tabs>

  </div>
</template>

<script>
  import axios from "axios";
  import {postUserCommentForBook} from "../../../../api/api";

  export default {
    name: "book_index",
    props: {
      index_info: {
        type: Object
      },
      user_comment: {
        type: Array
      }
    },
    data() {
      return {
        dialogVisible: false,
        userComment:''
      };
    },

    methods: {
      postComment(){
        this.dialogVisible = false;
        postUserCommentForBook(this.$props.index_info.book_id, {
          "message": this.userComment,
          "book": this.$props.index_info.book_id
        }).then((response)=>{
          console.log(response.data)
        }).catch((err)=>{
          console.log(err)
        })
      }
    }
  }
</script>

<style lang="less">
  .chapter_title {
    margin-bottom: 20px;
  }

  .index_wrap {
    margin-top: 20px;
    margin-bottom: 10px;

    .comment_title {
      line-height: 40px;
    }

    .comment_button {
      text-align: center;
    }

    .information_body {
      padding: 0 20px;
    }
  }

  .user_comment_body {
    height: 150px;
    margin-bottom: 10px;
  }

  .user_comment_head {
    margin: 0 20px;
    padding: 20px;
    border-bottom: 1px black solid;
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
