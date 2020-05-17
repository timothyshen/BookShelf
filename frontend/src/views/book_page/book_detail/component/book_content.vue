<template>
  <el-row :gutter="10" class="container_book">
    <el-col :span="6" class="image">
      <el-image src="#"/>
    </el-col>
    <el-col :span="18" class="detail">
      <div class="title">
        <h1>
          <strong>{{book_info.book_name}}</strong>
          <span>{{book_info.author}}</span>
        </h1>
      </div>
      <div class="tag">
        <el-tag effect="dark" v-if="book_info.contracted">Contracted</el-tag>
        <el-tag v-if="book_info.status">{{book_info.status}}</el-tag>
        <el-tag v-if="book_info.vip">VIP</el-tag>
      </div>
      <p class="short_des">
        {{book_info.book_short_description}}
      </p>
      <p class="short_des">
        {{book_info.book_description}}
      </p>
      <div class="number_detail">
        <ul class="number_list">
          <li>Total word: {{book_info.total_words}}</li>
          <li>Total click: {{book_info.total_click}}</li>
          <li>Total vote: {{book_info.total_vote}}</li>
          <li>Total favor: {{book_info.fav_num}}</li>
        </ul>
      </div>
      <div class="button">
          <el-button @click="toChapter">
            Read
          </el-button>
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
  import axios from 'axios';
  export default {
    name: "book_content",
    props:{
      book_info:{
        type: Object
      }
    },
    data() {
      return {
          value: ''
      }
    },
    created() {
      this.getBookRate()
    },
    methods:{
      toChapter(){
        this.$router.push({name: 'chapter', params:{book_id: this.$props.book_info.book_id, id: '1'}})
      },
      getBookRate(){
        let book_value = this.$props.book_info;
        this.value = book_value.value;
      }
    }
  }
</script>

<style lang="less" scoped>
  .container {
    padding-top: 200px;
  }

  .image {
    background-color: blue;
  }

  .detail {
    padding-left: 10px;
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

    .tag {
      padding-bottom: 10px;
    }

    .short_des {
      padding-bottom: 10px;
    }

    .number_detail {
      padding-bottom: 10px;
      font-size: 20px;
      height: 50px;
      width: 100%;

      .number_list {
        column-count: 3;
        column-gap: 40px;
        column-rule: 4px double #ff00ff;

        li {
          text-decoration: none;
          display: inline-block;
        }
      }

      span {
        display: inline-block;
        padding: 0 10px;
      }
    }

    .button {
      padding-bottom: 10px;
    }
  }

</style>
