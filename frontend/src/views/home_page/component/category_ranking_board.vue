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
            <p class="rank_table_bookname">1. <router-link :to="{name:'book', params:{book_id:rank_one.id}}">{{rank_one.book_name}}</router-link></p>
            <p class="rank_table_author">{{rank_one.book_author}}</p>
          </div>
          <div class="rank_table_description">
            <p>{{rank_one.book_short_description}}</p>
          </div>

        </li>
        <li class="ranking_board_item" v-for="(item,index) in ranking_board.slice(1)">
          <h3 class="rank_table_bookname">{{index + 2}}.<router-link :to="{name:'book', params:{book_id:item.id}}">{{item.book_name}}</router-link></h3>
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
        height: 150px;
        width: 35%;
      }

      .rank_one_description {
        float: left;
        align-items: baseline;
        list-style-type: decimal;
        list-style-position: inside;
        color: black;
        height: 40%;
        width: 65%;
        padding: 5px;
        p{
          height: 50%;
          width: 100%;
          margin-left: 10px;
        }

        p:first-child{
          font-size: 16pt;
         a{
           text-decoration: underline black;

         }
        }

        p:nth-child(2){

          margin-left: 50px;
        }
      }
      .rank_table_description{
        float: left;
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
        color: black;
      }

      .rank_table_author {
        float: right;
      }
    }

    .rank_one {

    }


  }
</style>
