<template>
  <div id="app">
    <router-view name = "head"></router-view>
    <router-view name ='content'></router-view>
    <router-view name = 'footer'></router-view>
  </div>
</template>

<script>
    export default {
        name: "app"
    }
</script>

<style scoped>

</style>
