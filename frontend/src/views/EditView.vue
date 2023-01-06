<script>
import TodoItemVue from '../components/TodoItem.vue';

export default{
  components: {
    TodoItemVue
  },

  data(){
    return {
      TodoItems:[
        
      ]
    }
  }
}


</script>

<template>
  <div class="edit" id="app">
    <h1>Edit the todo List</h1>
    <ul>
      <li v-for="item in TodoItems" key="item.id">
        <TodoItemVue
        :id="item.id"
        :label="item.label"
        :done="item.done"
        />
      </li>
    </ul>
  </div>

</template>

<style>
@media (min-width: 1024px) {
  .edit {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
}
</style>
