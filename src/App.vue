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

<style scoped>

</style>
