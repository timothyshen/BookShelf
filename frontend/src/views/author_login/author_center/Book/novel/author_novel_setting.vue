<template>
  <div class="book_container">
    <div>
      <h2>Let's start</h2>
    </div>
    <el-form :model="book_info" ref="book_info">
      <el-form-item label="Book name">
        <el-input type="text" v-model="book_info.book_name"/>
      </el-form-item>
      <el-form-item label="Book style">
        <el-select>
          <el-option label="History"/>
          <el-option label="Romance"/>
        </el-select>
      </el-form-item>
      <el-form-item label="Book image">
        <el-upload
          v-model="book_info.book_image"
          :before-upload="beforeAvatarUpload"
          :on-success="handleAvatarSuccess"
          :show-file-list="false"
          action="https://jsonplaceholder.typicode.com/posts/"
          class="avatar-uploader">
          <img v-if="imageUrl" :src="imageUrl" class="avatar" alt="user_icon">
          <i v-else class="el-icon-plus avatar-uploader-icon"/>
        </el-upload>
      </el-form-item>
      <el-form-item label="Short description">
        <el-input type="textarea"
                  v-model="book_info.book_short_description"
                  placeholder="Please insert your text"
                  maxlength="30"
                  show-word-limit/>
      </el-form-item>
      <el-form-item label="Long description">
        <el-input type="textarea"
                  v-model="book_info.book_description"
                  placeholder="Please insert your text"
                  maxlength="200"
                  show-word-limit/>
      </el-form-item>
      <el-button @click="updateAuthorBook">Save</el-button>
      <el-button>Delete</el-button>
    </el-form>
  </div>
</template>

<script>
  import {getAuthorBookItem, updateAuthorBookItem} from "../../../../../api/api";

  export default {
    name: "author_novel_setting",
    data() {
      return {
        imageUrl: '',
        book_info: {},
        new_info:{
          book_name:'',
          book_short:'',
          book_long:''
        }
      }
    },
    computed:{
      bookId(){
        return this.$route.params.book_id;
      }
    },
    created() {
      this.getAuthorBook();
    },
    methods: {
      getAuthorBook(){
        // console.log(this.bookId);
        getAuthorBookItem(this.bookId).then((response) => {
          console.log(response.data);
          this.book_info = response.data
        });
      },
      updateAuthorBook(){
        console.log(this.book_info);
        updateAuthorBookItem(this.bookId,{
          'book_name': this.book_info.book_name,
          'book_short_description': this.book_info.book_short_description,
          'book_description': this.book_info.book_description
        }).then((response)=>{
          console.log(response.data);
          console.log('success')
        })

      }
    }
  }
</script>

<style scoped>
  .book_container {
    width: 600px;
    margin: 0 auto;
  }
</style>
