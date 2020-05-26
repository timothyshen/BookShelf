<template>
  <div>
    <p>tim</p>
    <a href="/admin">admin</a>
    <a href="/api-auth/login">api</a>
    <el-link><router-link to="/novel/create">author</router-link></el-link>
    <category_table></category_table>
    <carousel></carousel>
  </div>
</template>

<script>
  import category_table from "./component/category_table";
  import carousel from "./component/carousel";
  export default {
    name: "home_page",
    components:{category_table, carousel}
  }
</script>

<style scoped>

</style>
