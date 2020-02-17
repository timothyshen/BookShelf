<template>
  <div id="app">
    <head></head>
    <router-link to="/home">Main</router-link>
    <router-view/>
  </div>
</template>

<script>
  import head from "./components/head";
export default {
  name: 'App',
  components: {head}
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
