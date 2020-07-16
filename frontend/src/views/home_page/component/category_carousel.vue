<template>
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
</template>

<script>
    export default {
        name: "category_carousel"
    }
</script>

<style scoped>

</style>
