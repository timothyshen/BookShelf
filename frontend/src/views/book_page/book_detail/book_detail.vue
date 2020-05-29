<template>
  <div class="container_book">
    <el-backtop :bottom="60" />
    <book_content
      v-bind:book_info="book_info"/>
    <book_index v-bind:index_info="index_info"/>
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
            book_id:'',
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
            value: 3.7
          },
          index_info:{
            book_id:'',
            description:'',
            chapters:''
          },
        }
      },
      created() {
        this.getChapter();
      },
      methods:{
        getChapter(){
          axios.get(`http://127.0.0.1:8000/book/detail/9`).then((response) => {
            console.log(response.data)
            this.book_info.book_id = response.data.id;
            this.book_info.book_name = response.data.book_name;
            this.book_info.author = response.data.book_author;
            this.book_info.status = response.data.book_status;
            this.book_info.book_image = response.data.book_image;
            this.book_info.book_short_description = response.data.book_short_description;
            this.book_info.book_description = response.data.book_description;
            this.book_info.total_words = response.data.total_words;
            this.book_info.chapter_count = response.data.chapter_count;
            this.book_info.total_vote = response.data.total_vote;
            this.book_info.weekly_vote = response.data.weekly_vote;
            this.book_info.total_click = response.data.total_click;
            this.book_info.fav_num = response.data.fav_num;
            this.index_info.book_id = response.data.id;
            this.index_info.description = response.data.book_description;
            let chapter_item = response.data.chapter;
            this.index_info.chapters = Object.values(chapter_item);
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
