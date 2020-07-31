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
        <el-select v-model="book_info.book_type">
          <el-option
            v-for="(element,index) in book_type"
            :key="element.id"
            :label="element.category_name"
            :value="element.id"/>
        </el-select>
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
      <el-form-item label="Book cover" required>
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
        <el-dialog :visible.sync="dialogVisible">
          <img width="100%" :src="dialogImageUrl" alt="">
        </el-dialog>
      </el-form-item>
      <el-button @click="createBook">Create</el-button>
    </el-form>
  </div>
</template>

<script>
  import {getBookCategory, registerAuthorBook} from "../../../../api/api";

  export default {
    name: "book_create",
    data() {
      return {
        imageUrl: '',
        book_info: {
          book_name: '',
          book_type: '',
          book_short: '',
          book_long: '',
          book_image: null
        },
        book_type: [],
        formData: {},
        fileList: [],
        dialogImageUrl: "",
        dialogVisible: false,
        disabled: false,
        alertVisible: false,
        addImage:true
      }
    },
    created() {
      this.getCategory()
    },
    methods: {
      uploadImage(item) {
        console.log(item.file);
        this.formData = new FormData();
        this.formData.append('book_image', item.file);
        this.formData.append('book_name', this.book_info.book_name);
        this.formData.append('book_type', this.book_info.book_type);
        this.formData.append('book_short_description', this.book_info.book_short);
        this.formData.append('book_description', this.book_info.book_long);
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
      handleExceed(file, fileList) {
        this.$message.error('You can only upload one image for your icon');
      },
      createBook() {
        registerAuthorBook(this.formData, {headers:{
            'Content-type':'multipart/form-data',
          }}).then((response) => {
          console.log(response.data);
          this.$router.go(-1);
        })
      },
      getCategory() {
        getBookCategory().then((response) => {
          this.book_type = response.data;
          console.log(response.data)
        })
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
  .book_container {
    width: 600px;
    margin: 0 auto;
  }
</style>
