<template>
    <div>
      <div></div>
      <div>
        <el-carousel indicator-position="outside">
          <el-carousel-item v-for="item in 4" :key="item">
            <h3>{{ item }}</h3>
          </el-carousel-item>
        </el-carousel>
      </div>
    </div>
</template>

<script>
    export default {
        name: "carousel"
    }
</script>

<style scoped>

</style>
