<template>
  <div>
    <el-row :gutter="20">
      <el-col :span="4">
        <category_table></category_table>
      </el-col>
      <el-col :span="16">
        <carousel></carousel>
      </el-col>
      <el-col :span="4">
        <news_board></news_board>
      </el-col>
    </el-row>
    <el-row :gutter="20" style="margin-top: 20px">
      <el-col :span="5">
        <Rankingboard v-bind:rank_info="click_board"></Rankingboard>
      </el-col>
      <el-col :span="14">
        <main_push v-bind:rank_info="main_book_push"/>
      </el-col>
      <el-col :span="5">
        <Rankingboard v-bind:rank_info="click_board"></Rankingboard>
      </el-col>
    </el-row>
  </div>
</template>

<script>
  import category_table from "./component/category_table";
  import carousel from "./component/carousel";
  import news_board from "./component/news_board";
  import Rankingboard from "./component/Rankingboard";
  import main_push from "./component/main_push";
  export default {
    name: "home_page",
    components:{category_table, carousel, news_board, Rankingboard, main_push},
    data(){
      return{
        click_board:{
          title:'Weekly Top Click',
          rank_param:'total_click'
        },
        fav_board:{
          title:'Weekly Top Favour',
          rank_param:'fav_num'
        },
        main_book_push: {
          cate_param:'Index'
        }
      }
    }
  }
</script>

<style scoped>

</style>
