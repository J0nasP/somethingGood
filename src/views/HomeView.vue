<script>
import { RouterView } from 'vue-router';

export default {
  
  data(){
    return {
      TodoItems: [
        "hello"
      ]
    }
  },

  methods: {
    addTodo(todoLabel) {
      this.TodoItems.push({id:uniqueId(todoLabel), label:todoLabel, done:false })
    },
    updateDoneStatus(todoId){
      const toDoToUpdate = this.TodoItems.find((item) => item.id == todoId)
      toDoToUpdate.done = !toDoToUpdate.done
    },
    deleteTodo(todoId){
      const itemIndex = this.TodoItems.findIndex((item) => item.id === todoId)
      this.TodoItems.splice(itemIndex, 1)
      this.$refs.listSammary.focus()
    },
    editTodo(todoId, newLabel) {
      const toDoToEdit = this.TodoItems.findIndex((item) => item.id === todoId)
      toDoToEdit.label = newLabel
    }
  },

  computed:{
    listSammary(){
      const numberFinishedItems = this.TodoItems.filter((item) => item.done).length
      return `${numberFinishedItems} out of ${this.TodoItems.length} Tasks completed`
    }
  }
}


</script>

<template>
  <main>
    <div id="app">
      
      {{TodoItems}}
    </div>
  </main>
</template>
