<template>
  <div id="app">
    <Header></Header>
    <div class="container">
      <br>
      <router-view></router-view>
    </div>

  </div>
</template>

<script>
// import Table from './components/Table.vue'
import Header from './components/Header.vue'


export default {
  name: 'App',
  components: {
    // Table,
    Header,
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}
</style>
