<template>
  <div class="ranking_table">
    <div class="ranking_header">
      <h2>{{rank_info.title}}</h2>
    </div>
    <div>
      <ul>
        <li class="ranking_one" v-model="rank_one">
          <img :src="rank_one.book_image">
          <div class="rank_one_description">
            <h3 class="rank_table_bookname"><router-link :to="{name:'book', params:{book_id:rank_one.id}}">1. {{rank_one.book_name}}</router-link></h3>
            <span class="rank_table_author">{{rank_one.book_author}}</span>
          </div>
          <div class="rank_table_description">
            <p>{{rank_one.book_short_description}}</p>
          </div>

        </li>
        <li class="ranking_board_item" v-for="(item,index) in ranking_board.slice(1)">
          <h3 class="rank_table_bookname">{{index + 2}}.{{item.book_name}}</h3>
          <span class="rank_table_author">[{{item.book_author}}]</span>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
  import {CateRankingBoardBooks} from "../../../api/api";

  export default {
    name: "Rankingboard",
    props:{
      rank_info:{
        type: Object
      }
    },
    data() {
      return {
        ranking_board:[],
        rank_one:{},
        variableName:'total_click'
      }
    },
    created() {
      this.getRankingBooks();
    },
    methods:{
      getRankingBooks(){
        CateRankingBoardBooks(this.$props.rank_info.cate_param, this.$props.rank_info.rank_param).then((response)=>{
          console.log(response.data);
          this.ranking_board = response.data;
          this.rank_one = this.ranking_board[0]
        })
      }
    }

  }
</script>

<style lang="less" scoped>

  .ranking_table {

    border: 1px solid black;
    background-color: lightgrey;

    .ranking_header {
      height: 40px;
      line-height: 30px;
      padding: 5px;
      border-bottom: 1px solid black;
    }

    .ranking_one {
      padding: 5px;
      height: 150px;

      img {
        float: left;
        height: inherit;
        width: 35%;
      }

      .rank_one_description {
        display: flex;
        align-items: baseline;
        list-style-type: decimal;
        list-style-position: inside;
        text-decoration: underline black;
        height: 40%;
        line-height: 50px;
        padding: 10px;

        h3{
          a{
            text-decoration: none;
          }
          padding-right: 10px;
        }
      }
      .rank_table_description{
        display: flex;
        padding: 10px;
      }
    }

    .ranking_board_item {
      margin-top: 10px;
      padding-left: 5px;
      display: flex;
      align-items: baseline;
      list-style-type: decimal;
      list-style-position: inside;
      text-align: left;

      h3 {
        margin-right: 10px;
        font-size: 20px;
      }

      .rank_table_author {
        float: right;
      }
    }

    .rank_one {

    }


  }
</style>
