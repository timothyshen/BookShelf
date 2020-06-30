<template>
  <div>
    <div>
      <h2>Top of the week</h2>
    </div>
    <el-row :gutter="20">
      <el-col :span="14">
        <el-carousel indicator-position="outside">
          <el-carousel-item v-for="(item, key) in index_image_list" :key="key">
            <h3 class="medium">
              <router-link :to="{name:'book', params:{book_id:item.book}}"><el-image
                :src="item.book_image"
                :alt="item.text"
                :key="item.id"
                /></router-link>
            </h3>
          </el-carousel-item>
        </el-carousel>
      </el-col>
      <el-col :span="10">
        <ul class='news_list'>
          <li v-for="(item, index) in index_link_list">
            <router-link :to="{name:'book', params:{book_id:item.book.id}}">
              <h3>{{item.book.book_name}}</h3>
              <span>{{item.book.book_short_description}}</span>
            </router-link>
          </li>
        </ul>
      </el-col>
    </el-row>

  </div>
</template>

<script>
  import{indexLinkRender, indexImageRender} from "../../../api/api";

  export default {
    name: "carousel",
    data(){
      return{
        index_link_list:[],
        index_image_list:[]
      }
    },
    methods:{
      getIndexLink(){
        indexLinkRender().then(response=>{
          console.log(response.data);
          this.index_link_list = response.data
        }).catch(err =>{
          console.log(err)
        });
        indexImageRender().then((response) => {
          console.log(response.data);
          this.index_image_list = response.data
        });
      }
    },
    created() {
      this.getIndexLink();
    }
  }
</script>

<style lang="less" scoped>
  .news_list {
    li {
      display: block;
      text-align: left;
      margin-top: 5px;
      padding-bottom: 10px;
      border-bottom: 1px dotted lightgrey;

      h3 {
        margin-bottom: 5px;
      }
    }
  }
</style>
