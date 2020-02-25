<template>
  <el-row type="flex" justify="center" class="container_footer" align="middle">
    <el-col :span="4" :offset="2" class="site">
      <h2>About Us</h2>
      <p class="text_define">Contact Us</p>
      <p>Site Map</p>
      <p>Terms Of Use</p>
    </el-col>
    <el-col :span="6" class="social_media">
      <div>
        <h2>Follow Us</h2>
        <div class="logo_container">
          <div class="logo_icon">
            <font-awesome-icon :icon="['fab', 'twitter-square']" size="4x" style="color: #3a8ee6"/>
          </div>
          <div class="logo_icon">
            <font-awesome-icon :icon="['fab', 'facebook']" size="4x" style="color: #3a8ee6"/>
          </div>
          <div class="logo_icon">
            <font-awesome-icon :icon="['fab', 'instagram']" size="4x" style="color: #3a8ee6"/>
          </div>
        </div>
      </div>
    </el-col>
    <el-col :span="4" class="news_letter">
      <p class="text_define">Sign up for the news letter</p>
      <el-button type="alert">Sign Up</el-button>
    </el-col>
  </el-row>
</template>

<script>
  export default {
    name: "footerbar"
  }
</script>

<style lang="less">

  @bg: rgb(205, 123, 0);
  .container_footer {
    height: 300px;
    width: 100%;
    background-color: #f9fbff;
    margin-top: 20px;

    .site {
      font-size: 20px;
      color: @bg;

      h2 {
        margin: 0 100px 20px 20px;
        padding-left: 20px;
        border-bottom: 2px solid;
      }

      p {
        height: 40px;
      }
    }
  }

  .social_media {
    h2 {
      color: @bg;
    }

    .logo_container {
      display: inline-block;

      .logo_icon {
        display: inline-block;
        padding: 20px;
      }
    }
  }

  .news_letter {
    .text_define {
      font-size: 20px;
      color: @bg;
      margin-bottom: 30px;
    }
  }

</style>
