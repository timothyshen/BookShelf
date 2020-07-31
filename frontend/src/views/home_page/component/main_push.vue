<template>
  <div class="body">
    <el-row>
      <el-col :span="8" class="block_level" v-for="(item,index) in main_push_book" v-bind:key="item.id">
        <div class="block_image">
          <el-image :src="item.book.book_image"/>
        </div>
        <dl class="block_info">
          <dt class="block_info_head">
            <a>
              <router-link :to="{name:'book', params:{book_id:item.book.id}}">{{item.book.book_name}}</router-link>
            </a>

          </dt>
          <dd class="block_info_description">
            Lorem ipsum dolor sit amet, eos modo hinc cetero ne, ad vim sumo cetero, in eum fabellas percipitur. Summo congue molestie mel ex. Pri no wisi oportere,
          </dd>
        </dl>
      </el-col>
    </el-row>
  </div>
</template>

<script>
  import {categoryBookRender} from "../../../api/api";

  export default {
    name: "main_push",
    data() {
      return {
        main_push_book:[]
      }
    },
    props:{
      rank_info:{
        type: Object
      }
    },
    created() {
      this.getMainPush();
    },
    methods:{
      getMainPush(){
        categoryBookRender(this.rank_info.cate_param).then((response)=>{
          console.log(response.data);
          this.main_push_book = response.data;
        }).catch((err)=>{
          console.log(err)
        })
      }
    }
  }
</script>

<style lang="less" scoped>
  .body {
    .block_level {
      display: table;
      height: 150px;
      padding: 5px 0px 0px 5px;

      .block_image {
        display: inline-block;
        width: 40%;
      }

      .block_info {
        display: inline-block;
        width: 50%;
        padding-right: 5px;
        height: 150px;

        .block_info_head {
          height: 25px;
          line-height: 25px;
          overflow: hidden;
          border-bottom: dotted 1px #6191D0;
          font-weight: bold;
          span{
            float: right;
            font-weight: normal;
          }
        }

        .block_info_description {
          text-align: justify;
        }
      }
    }
  }
</style>
