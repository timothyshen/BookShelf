<template>
    <el-table :data="books"
    style="width: 100%">
      <el-table-column prop="id" label="ID"/>
      <el-table-column prop="book_name" label="Book name"/>
      <el-table-column prop="newest_chapter" label="Newest update"/>
      <el-table-column prop="book_mark" label="Book Mark"/>
      <el-table-column prop="last_update_time" label="Last update time"/>
      <el-table-column label="Edit">
        <template slot-scope="scope">
          <el-button
            size="mini"
            type="danger"
            >Remove</el-button>
        </template>
      </el-table-column>

    </el-table>
</template>

<script>
    export default {
        name: "bookcase",
     data(){
          return{
            books:[{
              id:'',
              book_name:"",
              newest_chapter:"",
              last_update:"",
              book_mark:'',
              last_updated_time:''
            }]
          }
     }
    }
</script>

<style scoped>

</style>
