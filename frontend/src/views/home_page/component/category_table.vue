<template>
  <div class="genre_table">
    <div class="genre_title">
      <h2>All genre</h2>
    </div>
    <!--    <div v-for="(element, index) in category_type">-->
    <!--      <i class="el-icon-edit">{{element.category_name}}</i>-->
    <!--      <p>Total:{{element.total_number}}</p>-->
    <!--    </div>-->
    <div class="tab_box">
      <p class="genre_name"><i class="el-icon-edit"/>History</p>
      <p class="genre_number">10000</p>
    </div>
    <div class="tab_box">
      <p class="genre_name"><i class="el-icon-edit"/>History</p>
      <p class="genre_number">10000</p>
    </div>
    <div class="tab_box">
      <p class="genre_name"><i class="el-icon-edit"/>History</p>
      <p class="genre_number">10000</p>
    </div>
    <div class="tab_box">
      <p class="genre_name"><i class="el-icon-edit"/>History</p>
      <p class="genre_number">10000</p>
    </div>
  </div>
</template>

<script>
  import {getBookCategory} from "../../../api/api";

  export default {
    name: "category_table",
    data() {
      return {
        category_type: []
      }
    },
    created() {
      this.getCategory();
    },
    methods: {
      getCategory() {
        getBookCategory().then((response) => {
          this.category_type = response.data;
          console.log(response.data)
        })
      },
    }
  }
</script>

<style lang="less" scoped>
  .genre_table {
    display: table;
    width: 100%;
    background-color: lightgrey;
    border: 1px solid black;
    font-family: 'Avenir', Helvetica, Arial, sans-serif;

    .genre_title {
      display: block;
      height: 50px;
      line-height: 50px;
      text-align: center;
      border: 1px solid black;
    }

    .tab_box {
      display: table-row;
      width: 50%;
      float: left;
      box-sizing: border-box;
      text-align: center;
      padding: 10px;
      border: 1px solid black;
    }


  }
</style>
