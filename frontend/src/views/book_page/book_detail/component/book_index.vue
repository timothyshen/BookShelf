<template>
  <div class="top">
    <el-tabs>
      <el-tab-pane label="Description">
        <p>description</p>
      </el-tab-pane>
      <el-tab-pane label="Chapters">
        <h2 class="chapter_title">All chapters</h2>
        <ul class="chapter_list">
          <li class="chapter_item" v-for="chapter in chapters" v-bind="chapter">
            {{chapter.id}}. {{chapter.name}}
          </li>
        </ul>


      </el-tab-pane>
    </el-tabs>

  </div>
</template>

<script>
  export default {
    name: "book_index",
    data() {
      return {
        chapters: [{
          id: 1,
          name: 'one'
        }, {
          id: 2,
          name: 'one'
        }, {
          id: 3,
          name: 'one'
        }, {
          id: 4,
          name: 'one'
        }, {
          id: 5,
          name: 'one'
        }, {
          id: 6,
          name: 'one'
        }, {
          id: 6,
          name: 'one'
        }, {
          id: 6,
          name: 'one'
        }, {
          id: 6,
          name: 'one'
        }, {
          id: 6,
          name: 'one'
        }, {
          id: 6,
          name: 'one'
        }, {
          id: 6,
          name: 'one'
        }, {
          id: 6,
          name: 'one'
        }, {
          id: 6,
          name: 'one'
        }, {
          id: 6,
          name: 'one'
        }, {
          id: 6,
          name: 'one'
        }, {
          id: 6,
          name: 'one'
        }, {
          id: 6,
          name: 'one'
        }, {
          id: 6,
          name: 'one'
        }, {
          id: 6,
          name: 'one'
        }, {
          id: 6,
          name: 'one'
        }, {
          id: 6,
          name: 'one'
        }, {
          id: 6,
          name: 'one'
        }, {
          id: 6,
          name: 'one'
        }, {
          id: 6,
          name: 'one'
        }, {
          id: 6,
          name: 'one'
        }, {
          id: 6,
          name: 'one'
        }, {
          id: 6,
          name: 'one'
        }, {
          id: 6,
          name: 'one'
        }, {
          id: 6,
          name: 'one'
        }, {
          id: 6,
          name: 'one'
        }, {
          id: 6,
          name: 'one'
        }, {
          id: 6,
          name: 'one'
        }, {
          id: 6,
          name: 'one'
        }, {
          id: 6,
          name: 'one'
        }, {
          id: 6,
          name: 'one'
        }, {
          id: 6,
          name: 'one'
        }, {
          id: 6,
          name: 'one'
        }, {
          id: 6,
          name: 'one'
        }, {
          id: 6,
          name: 'one'
        }, {
          id: 6,
          name: 'one'
        }, {
          id: 6,
          name: 'one'
        }, {
          id: 6,
          name: 'one'
        }, {
          id: 6,
          name: 'one'
        }, {
          id: 6,
          name: 'one'
        }, {
          id: 6,
          name: 'one'
        }, {
          id: 6,
          name: 'one'
        }]
      }
    }
  }
</script>

<style lang="less" scoped>
  .chapter_title {
    margin-bottom: 20px;
  }

  .chapter_list {
    column-count: 3;
    margin: 0 10px;

    .chapter_item {
      border-bottom: 2px solid black;
      text-decoration: none;
      display: inline-block;
      height: 40px;
      width: 100%;
      font-size: 18px;
      text-align: center;
      padding-top: 10px;
      line-height: 40px;
    }
  }
</style>
