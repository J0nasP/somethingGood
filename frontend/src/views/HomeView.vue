<script>
import { RouterView } from 'vue-router';
import TodoItemVue from '@/components/TodoItem.vue';
import TodoFormVue from '@/components/TodoForm.vue';


export default {
  
  components: {
    TodoFormVue,
    TodoItemVue
  },

  data(){
    return {
      TodoItems: [
        
      ]
    }
  },

  methods: {

    async addTodo(todoLabel){
      try {

        const response = await this.$http.post('http://localhost:8000/backend/tasks/', {
          label: todoLabel,
          done: false
        });
        this.TodoItems.push(response.data);

      }catch (error) {
        console.log(error)
      }
    },

    updateDoneStatus(todoId){
      const toDoToUpdate = this.TodoItems.find((item) => item.todoId == todoId)
      toDoToUpdate.done = !toDoToUpdate.done
    },
    deleteTodo(todoId){
      const itemIndex = this.TodoItems.findIndex((item) => item.todoId === todoId)
      this.TodoItems.splice(itemIndex, 1)
      this.$refs.listSammary.focus()
    },
    editTodo(todoId, newLabel){
      const toDoToEdit = this.TodoItems.find((item) => item.todoId === todoId)
      toDoToEdit.label = newLabel
    },
    async getData(){
      try {
        const response = await this.$http.get('http://localhost:8000/backend/tasks/');
        this.TodoItems = response.data;
      } catch (error) {
        console.log(error)
      }
    }
  },

  created() {
    this.getData();
  },

  computed:{
    listSummary(){
      const numberFinishedItems = this.TodoItems.filter((item) => item.done).length
      return `${numberFinishedItems} out of ${this.TodoItems.length} items completed`
    }
  
  }
};


</script>

<template>
  <main>
    <div id="app">
      <h1>My To-do List</h1>
      <h2 id="list-summary" ref="listSummary" tabindex="-1" class="stack-large">{{ listSummary }}</h2>      
      <TodoFormVue @todo-added="addTodo"/>
      <ul>
        <li v-for="item in TodoItems" :key="item.id">
          <TodoItemVue
          :id="item.id"
          :label="item.label"
          :done="item.done"
          @checkbox-changed="updateDoneStatus(item.id)"
          @item-deleted="deleteTodo(item.taskId)"
          @item-edited="editTodo(item.id, $event)"
          />
        </li>
      </ul>
    </div>
    <RouterView/>
  </main>
</template>
<style>

</style>