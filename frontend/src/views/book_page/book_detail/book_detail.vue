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
    export default {
        name: "book_detail",
      components:{book_content, book_index}
    }
</script>

<style scoped>
.container_book{
  margin:0 auto;
  width:900px;
}
</style>
