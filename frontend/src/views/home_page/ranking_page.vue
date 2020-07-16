<template>
  <div>
    <el-row :gutter="20" style="margin-top: 20px">
      <h1>General Ranking</h1>
      <el-col :span="6">
        <Rankingboard v-bind:rank_info="click_board"></Rankingboard>
      </el-col>
      <el-col :span="6">
        <Rankingboard v-bind:rank_info="fav_board"></Rankingboard>
      </el-col>
      <el-col :span="6">
        <Rankingboard v-bind:rank_info="vote_board"></Rankingboard>
      </el-col>
      <el-col :span="6">
        <Rankingboard v-bind:rank_info="tip_board"></Rankingboard>
      </el-col>
    </el-row>
    <el-row :gutter="20" style="margin-top: 20px">
      <h1>Category Ranking</h1>
      <el-col :span="6">
        <category_ranking_board v-bind:rank_info="history_board"></category_ranking_board>
      </el-col>
      <el-col :span="6">
        <Rankingboard v-bind:rank_info="fav_board"></Rankingboard>
      </el-col>
      <el-col :span="6">
        <Rankingboard v-bind:rank_info="click_board"></Rankingboard>
      </el-col>
      <el-col :span="6">
        <Rankingboard v-bind:rank_info="click_board"></Rankingboard>
      </el-col>
    </el-row>
  </div>
</template>

<script>
  import Rankingboard from "./component/Rankingboard";
  import category_ranking_board from "./component/category_ranking_board";

  export default {
    name: "ranking_page",
    components: {Rankingboard, category_ranking_board},
    data() {
      return {
        click_board: {
          title: 'Weekly Top Click',
          rank_param: 'total_click'
        },
        fav_board: {
          title: 'Weekly Top Favour',
          rank_param: 'fav_num'
        },
        vote_board: {
          title: 'Weekly Top Voted',
          rank_param: 'total_vote'
        },
        tip_board: {
          title: 'Weekly Top Tipped',
          rank_param: 'total_vote'
        },
        history_board:{
          title:'Weekly Top History Click',
          rank_param:'total_click',
          cate_param:'History'
        }
      }
    }
  }
</script>

<style scoped>

</style>
