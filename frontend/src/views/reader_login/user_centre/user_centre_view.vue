<template>
  <el-row>
    <div><user_profile_component/></div>
    <div><msg_table/></div>
    <div><exp_table/></div>
  </el-row>
</template>

<script>
  import exp_table from "./components/exp_table";
  import msg_table from "./components/msg_table";
  import user_profile_component from "./components/user_profile";

  export default {
    name: "user_centre_view",
    components: {
      exp_table,
      msg_table,
      user_profile_component
    }
  }
</script>

<style scoped>

</style>
