<template>
    <el-table :data="books" type="index">
      <el-table-column
        type="index"
        width="50"/>
      <el-table-column label="Book Name">
        <template slot-scope="scope">
          <router-link :to="{name:'book', params:{book_id:scope.row.id}}">{{scope.row.book.book_name}}</router-link>
        </template>
      </el-table-column>

      <el-table-column prop="book.book_author" label="Book author"/>
      <el-table-column  label="Bookmark">
        <template slot-scope="scope">
          <router-link :to="{name:'chapter', params:{book_id:scope.row.book.id, id:scope.row.bookmark.chapter.id}}">{{scope.row.bookmark.chapter.chapter_title}}</router-link>
        </template>
      </el-table-column>
      <el-table-column prop="book.last_update" label="Last updated"/>
      <el-table-column prop="book.book_name" label="Book Name"/>
      <el-table-column label="Removal">
        <template slot-scope="scope">
          <el-button
            size="mini"
            type="danger"
            @click="delFavFromShelves(scope.$index, scope.row.book.id)"
          >Remove</el-button>
        </template>
      </el-table-column>
    </el-table>
</template>

<script>
  import {getBookShelves, deleteBook} from "../../../../api/api";

  export default {
     name: "bookcase",
     data(){
          return{
            books:[],
            bookmarks:[]
          }
     },
     created() {
       getBookShelves().then((response)=>{
         console.log(response.data);
         let book = response.data;
         book.forEach(element =>{
           this.books.push(element);

       })
       }).catch((error)=>{
         console.log(error);
       })
     },
     methods:{
      delFavFromShelves(index, id){
        alert('Do you want to remove the book from the shelf?');
        console.log(index, id);
        deleteBook(id).then((response)=>{
          this.books.splice(index,1);
          alert('Book removed');
        }).catch((error)=>{
          console.log(error);
        })
      }
     }
    }
</script>

<style scoped>

</style>
