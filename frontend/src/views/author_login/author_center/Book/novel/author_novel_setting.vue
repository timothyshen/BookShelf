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
      <el-button @click="centreDialogVisible = true">Delete</el-button>
    </el-form>
    <el-dialog
    title="Deletion"
    :visible.sync="centreDialogVisible"
    width="30%"
    center>
      <p>Do you really want to delete this book?</p>
      <p>If you want to delete this book please insert the book name: {{book_info.book_name}} below</p>
      <el-input v-model="deletionWord" />
      <span slot="footer" class="dialog-footer">
        <el-button type="primary" @click="deleteAuthorBook" v-bind:disabled="deletionWord !== this.book_info.book_name">Confirm</el-button>
      </span>
    </el-dialog>
  </div>
</template>

<script>
  import {getAuthorBookItem, updateAuthorBookItem, deleteAuthorBookItem} from "../../../../../api/api";

  export default {
    name: "author_novel_setting",
    data() {
      let validateInput = (rule, value, callback) =>{
        if (value !== this.book_info.book_name){

        }
        };
      return {
        centreDialogVisible: false,
        deletionWord:'',
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
      },
      deleteAuthorBook(){

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
