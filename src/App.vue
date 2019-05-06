<template>
  <div id="app">
    <img alt="Vue logo" width="20%" src="https://4.bp.blogspot.com/-NE9vfUe0tDU/XKGRh0SC-eI/AAAAAAABSIU/bRvU0G24mWgC-5XhtmW4GZSme0M8EtY1wCLcBGAs/s800/gengou_calender_reiwa.png">
    <HelloWorld msg="カレンダーシェア"/>
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld'

export default {
  name: 'app',
  components: {
    HelloWorld
  }
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
