<template>
  <el-carousel indicator-position="outside" height="410px">
    <el-carousel-item v-for="(item, key) in category_image_list" :key="key">
      <h3 class="medium">
        <router-link :to="{name:'book', params:{book_id:item.book}}">
          <el-image
            :src="item.book_image"
            :alt="item.text"
            :key="item.id"
          />
        </router-link>
      </h3>
    </el-carousel-item>
  </el-carousel>
</template>

<script>
  import {categoryImageRender} from "../../../api/api";

  export default {
    name: "category_carousel",
    data(){
      return{
        category_image_list:[]
      }
    },
    props: {
      rank_info: {
        type: Object
      }
    },
    created() {
      this.getMainPush()
    },
    methods: {
      getMainPush() {
        categoryImageRender(this.rank_info.cate_param).then((response) => {
          console.log(response.data);
          this.category_image_list = response.data;
        }).catch((err) => {
          console.log(err)
        })
      }
    }
  }
</script>

<style scoped>

</style>
