<template>
  <div>
    <div>
      <h2>All genre</h2>
    </div>
    <div v-for="(element, index) in category_type">
      <i class="el-icon-edit">{{element.category_name}}</i>
      <p>Total:{{element.total_number}}</p>
    </div>
  </div>
</template>

<script>
  import {getBookCategory} from "../../../api/api";

  export default {
    name: "category_table",
    data() {
      return {
        category_type:[]
      }
    },
    created() {
      this.getCategory();
    },
    methods: {
      getCategory() {
        getBookCategory().then((response) => {
          this.category_type = response.data;
          console.log(response.data)
        })
      },
    }
  }
</script>

<style scoped>

</style>
