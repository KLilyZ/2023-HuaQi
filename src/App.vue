<template>

<!--  <HelloWorld msg="Welcome to Your Vue.js App"/>-->
  <router-view></router-view>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'

export default {
  name: 'App',
  components: {
    HelloWorld
  }
}
</script>

<style>
img{
  width:412px;
  height: 309px;
  margin-bottom: 1px;
  margin-top:5px;
}
html {
  height: 100%;
  background-repeat: no-repeat;
  background-size: cover;
  background-position: center;
  /*background-image: linear-gradient(25deg, #d17c46, #e6a781, #f6d2bf, #ffffff);*/
  background-image: linear-gradient(25deg, #387590, #7b95a0, #b3b7b0, #ebdabf);
  background-attachment:fixed;
}

#app {

  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

</style>
