<template>
  <div>
    <el-row :gutter="20">
      <category_carousel v-bind:rank_info="main_book_push"></category_carousel>
    </el-row>
    <el-row style="margin-top:20px" :gutter="20">
      <el-col :span="5">
        <category_ranking_board v-bind:rank_info="history_board"></category_ranking_board>
      </el-col>
      <el-col :span="14">
        <main_push v-bind:rank_info="main_book_push"></main_push>
      </el-col>
      <el-col :span="5">
        <category_ranking_board v-bind:rank_info="history_board"></category_ranking_board>
      </el-col>
    </el-row>
  </div>
</template>

<script>
  import category_ranking_board from "./component/category_ranking_board";
  import category_carousel from "./component/category_carousel";
  import main_push from "./component/main_push";
  export default {
    name: "category_page",
    components: {category_ranking_board, category_carousel,main_push},
    data() {
      return {
        history_board:{
          title:'Weekly Top ' + this.$route.params.categoryname + ' Click',
          rank_param:'total_click',
          cate_param:this.$route.params.categoryname
        },
        main_book_push:{
          cate_param:this.$route.params.categoryname
        }
      }
    }
  }
</script>

<style scoped>

</style>
