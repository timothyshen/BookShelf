<template>
    <el-table
      type="index"
      :data="books"
      style="width: 100%">
      <el-table-column prop="id" label="ID"/>
      <el-table-column prop="name" label="Book name"/>
      <el-table-column prop="new_update" label="Newest update"/>
      <el-table-column prop="book_mark" label="Book Mark"/>
      <el-table-column prop="created_time" label="Last update time"/>
      <el-table-column label="Edit">
        <template slot-scope="scope">
          <el-button
            size="mini"
            type="danger"
            @click="delFavFromShelves(scope.$index, scope.row.book_id)"
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
            books:[
              {
                id:'',
                name:'',
                new_update:'',
                book_mark:null,
                created_time:'',
                book_id:''
              }
            ]
          }
     },
     created() {
       getBookShelves().then((response)=>{
         console.log(response.data);
         this.book = response.data;
         console.log(this.books);
         let row = 0;
         this.book.forEach(element => {
           //console.log(element.id);
           this.books[row].id = element.id;
           this.books[row].book_id = element.book.id;
           this.books[row].name = element.book.book_name;
           let last_chapter = element.book.Chapter.slice(-1)[0];
           console.log(last_chapter);
           this.books[row].new_update = last_chapter.chapter_title;
           console.log(last_chapter.created_time.split("T")[0]);
           this.books[row].created_time = last_chapter.created_time.split("T")[0];
           row++
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
