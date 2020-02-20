<template>
  <el-row :gutter="24" class="container_footer">
    <el-col :span="2" :offset="6">
      <p>Contact Us</p>
      <p>Site Map</p>
      <p>Terms Of Use</p>
    </el-col>
    <el-col :span="6" class="social_media">
      <div>
        <h2>Social Media</h2>

      </div>
    </el-col>
    <el-col :span="4" class="news_letter">
      <p>Sign up for the news letter</p>
    </el-col>
  </el-row>
</template>

<script>
  export default {
    name: "footer"
  }
</script>

<style>
  .container_footer {
    height: 300px;
    background-color: #545454;
    margin-top: 20px;
  }

  .social_media {
    top: 50%;
  }

</style>
