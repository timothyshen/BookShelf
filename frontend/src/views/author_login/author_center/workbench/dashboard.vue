<template>
  <el-row class="wrap">
    <el-collapse>
      <el-collapse-item name="1">
        <template slot="title">
          <h3>Message</h3>
        </template>
        <el-alert
          title="Important notice"
          type="info"
          show-icon
          :closable="false"
          description="">
        </el-alert>
        <template slot="default">
          <div>This is a message tab for global message</div>
        </template>
      </el-collapse-item>
      <div>
        <div>
          <img/>
        </div>
        <div>
          <h2>{{bookItem.book_name}}</h2>
        </div><div>
          <h2>Number of clicks</h2>
          <span>{{bookItem.total_click}}</span>
        </div>
        <div>
          <h2>Number of Word</h2>
          <span>{{bookItem.total_words}}</span>
        </div>
        <div>
          <h2>Number of Favorite</h2>
          <span>{{bookItem.fav_num}}</span>
        </div>
      </div>
    </el-collapse>

  </el-row>
</template>

<script>
  import {getAuthorBook} from "../../../../api/api";

  export default {
    name: "dashboard",
    data() {
      return {
          bookItem:[]
      }
    },
    methods:{
      getBook(){
        getAuthorBook().then((response)=>{
          let bookList = response.data;
          this.bookItem = bookList[bookList.length-1];
        })
      }
    },
    created() {
      this.getBook();
    }
  }
</script>

<style scoped>

</style>
