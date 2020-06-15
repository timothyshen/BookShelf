<template>
  <div class="news">
    <h3 class="news_title">Recent news</h3>
    <ul>
      <li class="news_item">[News] Lorem ipsum dolor sit amet</li>
      <li class="news_item">[News] Lorem ipsum dolor sit amet</li>
      <li class="news_item">[News] Lorem ipsum dolor sit amet</li>
    </ul>
  </div>
</template>

<script>
  export default {
    name: "news_board"
  }
</script>

<style lang="less" scoped>
.news{
  padding:20px;
  .news_title{
    text-align: center;
    margin-bottom:10px;
  }
  ul .news_item{
    padding-bottom: 5px;
    margin-bottom: 5px;
    border-bottom: 1px dotted lightgrey;
  }
}
</style>
