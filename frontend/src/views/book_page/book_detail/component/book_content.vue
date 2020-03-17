<template>
    <el-row :gutter="10" class="container_book">
      <el-col :span="6" class="image">
        <el-image></el-image>
      </el-col>
      <el-col :span="18" class="detail">
        <div class="title">
          <h1>
            <strong>Book title</strong>
            <span>Author</span>
          </h1>
        </div>
        <div class="tag">
          <el-tag effect="dark">Contracted</el-tag>
          <el-tag>Ongoing</el-tag>
          <el-tag>VIP</el-tag>
        </div>
        <p class="short_des">
          Lorem ipsum dolor sit amet, in modus lucilius delicatissimi mei.
        </p>
        <div class="number_detail">
          <ul class="number_list">
            <li>Word count</li>
            <li>Word count</li>
            <li>Word count</li>
          </ul>
        </div>
        <div class="button">
          <el-button>Read trail</el-button>
          <el-button>Tip it</el-button>
          <el-button>Vote it</el-button>
          <el-button>Add to favor</el-button>
        </div>
        <el-rate
        v-model="value"
        disabled
        show-score
        text-color="#ff9900"
        score-template="{value}">
        </el-rate>
      </el-col>
    </el-row>
</template>

<script>
    export default {
        name: "book_content",
      data(){
          return{
            value:3.7
          }
      }
    }
</script>

<style lang="less" scoped>
  .container{
    padding-top:200px;
  }
  .image{
    background-color: blue;
  }
  .detail{
    padding-left:10px;
    background-color: snow;

    .title {
      padding-bottom: 10px;
      h1 {
        display: inline;
        span {
          display: inline-block;
          padding-left: 20px;
          font-size: 18px;
        }
      }
    }
    .tag{
      padding-bottom: 10px;
    }
    .short_des {
      padding-bottom: 10px;
    }
    .number_detail {
      padding-bottom:10px;
      font-size: 20px;
      height: 50px;
      width: 100%;
      .number_list{
        column-count: 3;
        column-gap: 40px;
        column-rule: 4px double #ff00ff;
        li {
        text-decoration: none;
        display: inline-block;
        }
      }

      span{
        display: inline-block;
        padding: 0 10px;
      }
    }
    .button {
      padding-bottom: 10px;
    }
  }

</style>
