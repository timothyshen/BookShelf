<template>
  <div class="register_container">
    <el-steps :active="active" finish-status="success">
      <el-step title="Step 1"/>
      <el-step title="Step 2"/>
      <el-step title="Step 3"/>
    </el-steps>
    <div>
      <h2>Author registration</h2>
    </div>
    <div class="register_form" v-if="active === 0">
      <el-form label-width="100px" :label-position="labelPosition">
        <el-form-item label="Username" >
          <el-input type="text">username</el-input>
        </el-form-item>
        <el-form-item label="Password:" prop="password">
          <el-input
            type="password"
            show-password/>
        </el-form-item>
        <el-form-item label="Confirm password:" prop="checkPass">
          <el-input
            type="password"
            show-password/>
        </el-form-item>
      </el-form>
    </div>
    <div class="register_form" v-if="active === 1">
      <el-form>
        <el-form-item label="Gender:" prop="gender">
          <el-radio-group>
            <el-radio label="m">Male</el-radio>
            <el-radio label="f">Female</el-radio>
          </el-radio-group>
        </el-form-item>
        <el-form-item label="Email:" prop="email">
          <el-input type="email" />
        </el-form-item>
      </el-form>
    </div>
    <div class="register_form" v-if="active === 2">
      <el-form>
        <el-form-item label="Mobile number:" prop="password">
          <el-input
            type="text"
            show-password/>
        </el-form-item>
        <el-form-item label="Date of Birth" prop="birthday">
          <el-date-picker
            type="date"
            placeholder="pick a date">
          </el-date-picker>
        </el-form-item>
        <el-form-item label="Avatar" prop="avatar">
          <el-upload
            :before-upload="beforeAvatarUpload"
            :on-success="handleAvatarSuccess"
            :show-file-list="false"
            action="https://jsonplaceholder.typicode.com/posts/"
            class="avatar-uploader">
            <img v-if="imageUrl" :src="imageUrl" class="avatar">
            <i v-else class="el-icon-plus avatar-uploader-icon"></i>
          </el-upload>
        </el-form-item>
      </el-form>
    </div>
    <div>
      <el-button>Prev</el-button>
      <el-button @click="next">Next</el-button>
      <el-button>Submit</el-button>
    </div>
  </div>
</template>

<script>
  export default {
    name: "author_register",
    data() {
      return {
        active: 0,
        labelPosition:'top'
      };
    },

    methods: {
      next() {
        if (this.active++ > 2) this.active = 0;
      }
    }
  }
</script>

<style lang="less" scoped>
  .register_container{
    margin: 50px auto;
    width: 900px;
    h2{
      margin-top: 20px;
      text-align: center;
    }
    .register_form{
      margin: 50px auto;
      width: 70%;
    }
  }
</style>
