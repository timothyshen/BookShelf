<template>
  <el-main>
    <el-form>
      <el-form-item label="Username" prop="username">
        <el-input type="text" >username</el-input>
      </el-form-item>
      <el-form-item label="Password:" prop="password">
        <el-input
          type="password"
          show-password>password</el-input>
      </el-form-item>
      <el-form-item label="Confirm password:" prop="checkPass">
        <el-input
          type="password"
          show-password>password</el-input>
      </el-form-item>
      <el-form-item label="Gender:" prop="gender">
        <el-radio-group >
          <el-radio label="m">Male</el-radio>
          <el-radio label="f">Female</el-radio>
        </el-radio-group>
      </el-form-item>
      <el-form-item label="Email:" prop="email">
        <el-input type="email"/>
      </el-form-item>
      <el-form-item label="Date of Birth" prop="birthday">
        <el-date-picker

          type="date"
          placeholder="pick a date">
        </el-date-picker>
      </el-form-item>

      <el-button type="primary">Register</el-button>
      <el-button>Reset</el-button>
    </el-form>
  </el-main>
</template>

<script>
    export default {
        name: "user_setting"
    }
</script>

<style scoped>

</style>
