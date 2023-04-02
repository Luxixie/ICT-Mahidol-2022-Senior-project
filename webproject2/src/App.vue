<template>
  <div id="app">
    <app-header></app-header>
    <router-view :key="$route.fullPath"> </router-view>

  </div>
</template>

<script>

import Header from "../src/components/header/header.vue"

export default {
  name: 'App',
  components: {

    "app-header": Header
  }
}
</script>

<style>
body{
  margin: 0px;
  background: #11223d;
}
</style>
