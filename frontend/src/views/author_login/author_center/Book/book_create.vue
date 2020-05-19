<template>
  <div class="book_container">
    <div>
      <h2>Let's start</h2>
    </div>
      <el-form :model="book_info" ref="book_info" >
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
                    v-model="book_info.book_short"
                    placeholder="Please insert your text"
                    maxlength="30"
                    show-word-limit/>
        </el-form-item>
        <el-form-item label="Long description">
          <el-input type="textarea"
                    v-model="book_info.book_long"
                    placeholder="Please insert your text"
                    maxlength="200"
                    show-word-limit/>
        </el-form-item>
        <el-button @click="createBook">Create</el-button>
      </el-form>
  </div>
</template>

<script>
  import {registerAuthorBook} from "../../../../api/api";

  export default {
        name: "book_create",
        data(){
          return{
            imageUrl: '',
            book_info:{
              book_name:'',
              book_short:'',
              book_long:'',
              book_image:null
            }
          }
        },
      methods:{
        createBook(){
          registerAuthorBook({
            "book_name": this.book_info.book_name,
            "book_image": this.book_info.book_image,
            "book_short_description": this.book_info.book_short,
            "book_description": this.book_info.book_long
          }).then((response)=>{
            console.log(response.data)
          })
        },
        handleAvatarSuccess(res, file) {
          this.imageURL = URL.createObjectURL(file.raw);
        },
        beforeAvatarUpload(file) {
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
        resetForm(formName) {
          this.$nextTick(() => {
            this.$refs[formName].resetFields();
          })
        }
      }
    }
</script>

<style scoped>
.book_container{
  width: 600px;
  margin: 0 auto;
}
</style>
