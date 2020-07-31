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
        <el-select  v-model="book_info.book_type">
          <el-option
            v-for="(element,index) in category_type"
            :key="element.id"
            :label="element.category_name"
            :value="element.id"/>
        </el-select>
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
      <el-form-item label="Avatar">
        <el-upload
          class="avatar-uploader"
          action="cdn"
          :file-list="fileList"
          list-type="picture-card"
          :http-request="uploadImage"
          :on-preview="handlePictureCardPreview"
          :on-exceed="handleExceed"
          :before-upload="beforeCoverUpload"
          :limit="1">
          <i class="el-icon-plus avatar-uploader-icon"/>
        </el-upload>
        <p v-if="alertVisible">You can only upload one image for your book cover</p>
        <el-dialog :visible.sync="dialogVisible">
          <img width="100%" :src="dialogImageUrl" alt="">
        </el-dialog>
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
  import {getBookCategory, getAuthorBookItem, updateAuthorBookItem, deleteAuthorBookItem} from "../../../../../api/api";
  import axios from 'axios';
  export default {
    name: "author_novel_setting",
    data() {

      return {
        centreDialogVisible: false,
        deletionWord:'',
        book_info: {},
        old_info:{
          book_name:''
        },
        category_type:[],
        formData: {},
        fileList:[],
        dialogImageUrl:"",
        dialogVisible: false,
        disabled: false,
        alertVisible: false
      }
    },
    computed:{
      bookId(){
        return this.$route.params.book_id;
      }
    },
    created() {
      this.getAuthorBook();
      this.getCategory();
    },
    methods: {
      getCategory() {
        getBookCategory().then((response) => {
          this.category_type = response.data;
          console.log(response.data)
        })
      },
      getAuthorBook(){
        // console.log(this.bookId);
        getAuthorBookItem(this.bookId).then((response) => {
          console.log(response.data);
          this.book_info = response.data;
          this.fileList.push({name:'book_cover', url:response.data.book_image});
        });
      },
      uploadImage(item){
        console.log(item.file);
        this.formData = new FormData();
        this.formData.append('book_image', item.file);
        console.log(...this.formData);

      },
      handleRemove(file, fileList) {
        console.log(file, fileList);
      },
      handlePictureCardPreview(file) {
        this.dialogImageUrl = file.url;
        this.dialogVisible = true;
      },
      beforeCoverUpload(file) {
        const isJPG = file.type === 'image/jpeg';
        const isLt2M = file.size / 1024 / 1024 < 2;
        if (!isJPG) {
          this.$message.error('The picture should be a JPEG file');
        }
        if (!isLt2M) {
          this.$message.error('The picture size should be less than 2MB!');
        }
        return isJPG && isLt2M;
      },
      handleExceed(file, fileList){
        this.alertVisible = true
      },
      updateAuthorBook(){
        axios.all(
          [updateAuthorBookItem(this.bookId,this.formData, {headers:{
            'Content-type':'multipart/form-data',
          }}),
            updateAuthorBookItem(this.bookId,  {
          'book_type': this.book_info.book_type.id,
          'book_name': this.book_info.book_name,
          'book_short_description': this.book_info.book_short_description,
          'book_description': this.book_info.book_description
        })]).then((response)=>{
          console.log(response);
          this.$router.push('/novel/chapter/'+this.bookId);
        }).catch(err=>{
          console.log(err)
        });
      },
      deleteAuthorBook(){
        deleteAuthorBookItem(this.bookId).then((response) => {
          this.$message({
            message: 'Book deleted',
            type: 'success'
          });
          this.$router.to({name:'/novel/list'})
        });
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
