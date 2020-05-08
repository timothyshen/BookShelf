<template>
  <div class="container_book">
    <el-backtop :bottom="60" />
    <book_content/>
    <book_index/>
  </div>
</template>

<script>
  import book_content from "./component/book_content";
  import book_index from "./component/book_index";
  import axios from "axios";
    export default {
      name: "book_detail",
      components:{book_content, book_index},
      data() {
        return {
          book_info:{
            book_name:'',
            author:'',
            status:'',
            contracted:'',
            vip:'',
            book_image:'',
            book_short_description: "",
            book_description: "",
            total_words: '',
            chapter_count: '',
            total_vote: '',
            weekly_vote: '',
            total_click: '',
            fav_num: '',
          },
          value: 3.7
        }
      },
      created() {
        this.getChapter();
      },
      methods:{
        getChapter(){
          axios.get(`http://127.0.0.1:8000/book/detail/2`).then((response) => {
          });
        }
      }
    }
</script>

<style scoped>
.container_book{
  margin:0 auto;
  width:900px;
}
</style>
