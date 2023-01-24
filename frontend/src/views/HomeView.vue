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
          id: this.id,
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

    async deleteTodo(taskId){
      const itemIndex = this.TodoItems.findIndex((item) => item.taskId === taskId)

      try {
      
      await this.$http.delete(`http://localhost:8000/backend/tasks/${taskId}`)
    
      }catch(error) {
      console.log(error)
    }
      this.TodoItems.splice(itemIndex, 1)
    },

    async toggleTodo(task, newLabel){
      try{

        const response = await this.$http.put(`http://localhost:8000/backend/tasks/${task.taskId}`,
          {
            done: !task.done,
            label: newLabel,
            id: this.id
          }
        );

          let taskIndex = this.TodoItems.find((t) => t.taskId == task.taskId)
          if (taskIndex == task){
            task.label = newLabel
            return response.data
          }
          return task
        
          

      }catch(error) {
        console.log(error)
      }
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
          :id="item.taskId"
          :label="item.label"
          :done="item.done"
          @checkbox-changed="updateDoneStatus(item.id)"
          @item-deleted="deleteTodo(item.taskId)"
          @item-edited="toggleTodo(item, $event)"
          />
        </li>
      </ul>
    </div>
    <RouterView/>
  </main>
</template>
<style>

</style>