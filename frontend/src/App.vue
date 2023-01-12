<script setup>
import { RouterLink, RouterView } from 'vue-router'

</script>

<template>
  <header>
    <div class="header-wrapper">
      <nav>
        <RouterLink to="/">Home</RouterLink>
        <RouterLink to="/edit">Edit</RouterLink>
      </nav>
    </div>
  </header>
  <RouterView/>
</template>

<!--
<template>
  <div id="app">
    <TasksVue/>
  </div>
</template>
-->
<script>
/*
import TasksVue from './components/Tasks.vue'

export default {
  components: {
    TasksVue
  } 
}
*/
</script>
<style scoped>

</style>
