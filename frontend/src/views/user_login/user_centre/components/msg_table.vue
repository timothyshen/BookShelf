<template>
  <div class="msg_table_block">
    <ul class="home_msg_table">
      <li>
        <div class="msg_table_title">Balance</div>
        <div class="msg_table_data">
          <span>0</span>
          Coins
        </div>
        <el-link type="primary" class="msg_table_link">Top Up</el-link>
      </li>
      <li>
        <div class="msg_table_title">Bookcase</div>
        <div class="msg_table_data">
          <span>0</span>
          of Books
        </div>
        <el-link type="primary" class="msg_table_link">Check now</el-link>
      </li>
      <li>
        <div class="msg_table_title">Book List</div>
        <div class="msg_table_data">
          <span>0</span>
          of Follow
        </div>
        <el-link type="primary" class="msg_table_link">Check now</el-link>
      </li>
      <li>
        <div class="msg_table_title">Book List</div>
        <div class="msg_table_data">
          <span>0</span>
          of Follow
        </div>
        <el-link type="primary" class="msg_table_link">Check now</el-link>
      </li>
    </ul>
  </div>

</template>

<script>
  export default {
    name: "msg_table"
  }
</script>

<style lang="less">

  * {
    margin: 0px;
    padding: 0px;
  }

  .msg_table_block {
    width: 100%;

    font-size: 0px;
    margin-left: 10px;
    /*border: #545454 1px solid;*/
    /*border-bottom: none;*/

    li {
      display: inline-block;
      width: 130px;
      padding: 10px 20px 0 20px;

      .msg_table_title {
        margin-left: 10px;
        font-size: 20px;
        text-align: left;
      }

      .msg_table_data {
        margin-left: 10px;
        padding: 20px 0;
        font-size: 12px;
      }

      .msg_table_link {
        display: block;
        border-top: black 1px solid;
        padding: 14px 10px 0 10px;
        font-size: 16px;
        text-align: center;
        height: 40px;
      }
    }
  }
</style>
