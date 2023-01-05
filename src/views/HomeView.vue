<script>
import { RouterView } from 'vue-router';
import uniqueId from 'lodash.uniqueid';
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
    editTodo(todoId, newLabel){
      const toDoToEdit = this.TodoItems.find((item) => item.id === todoId)
      toDoToEdit.label = newLabel
    }
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
      <h2 id="list-summary" ref="listSummary" tabindex="-1" class="stack-large">{{ listSummary }}</h2>      <TodoFormVue @todo-added="addTodo"/>
      <ul>
        <li v-for="item in TodoItems" :key="item.id">
          <TodoItemVue
          :id="item.id"
          :label="item.label"
          :done="item.done"
          @checkbox-changed="updateDoneStatus(item.id)"
          @item-deleted="deleteTodo(item.id)"
          @item-edited="editTodo(item.id, $event)"
          />
        </li>
      </ul>
    </div>
    <RouterView/>
  </main>
</template>
<style>
.btn {
  padding: 0.8rem 1rem 0.7rem;
  border: 0.2rem solid #4d4d4d;
  cursor: pointer;
  text-transform: capitalize;
}

.btn__danger {
  color: #fff;
  background-color: #ca3c3c;
  border-color: #bd2130;
}

.btn__filter{
  border-color: lightgray;
}

.btn__danger:focus{
  outline-color: #c82333;
}

.btn__primary {
  color: #fff;
  background-color: #000;
}

.btn-group {
  display: flex;
  justify-content: space-between;
}

.btn-group > * {
  flex: 1 1 auto;
}

.btn-group > * + *{
  margin-left: 0.8rem;
}

.label-wrapper {
  margin: 0;
  flex: 0 0 auto;
  text-align: center;
}

[class*="__lg"]{
  display: inline-block;
  width: 100%;
  font-size: 1.9rem;
}

[class*="__lg"]:not(:last-child){
  margin-bottom: 1rem;
}

@media screen and (min-width: 620px) {
  [class*="__lg"] {
    font-size: 2.4rem;
  }
}

.visually-hidden{
  position: absolute;
  height: 1px;
  width: 1px;
  overflow: hidden;
  clip: rect(1px 1px 1px 1px);
  clip: rect(1px, 1px, 1px, 1px);
  clip-path: rect(1px, 1px, 1px, 1px);
  white-space: nowrap;
}

[class*="stack"] > * {
  margin-top: 0;
  margin-bottom: 0;
}
.stack-small > * + * {
  margin-top: 1.25rem;
}
.stack-large > * + * {
  margin-top: 2.5rem;
}
@media screen and (min-width: 550px) {
  .stack-small > * + * {
    margin-top: 1.4rem;
  }
  .stack-large > * + * {
    margin-top: 2.8rem;
  }
}

#app {
  background: #fff;
  margin: 2rem 0 4rem 0;
  padding: 1rem;
  padding-top: 0;
  position: relative;
  box-shadow: 0 2px 4px 0 rgba(0, 0, 0, 0.2), 0 2.5rem 5rem 0 rgba(0, 0, 0, 0.1);
}

@media screen and (min-width: 550px) {
  #app {
    padding: 4rem;
  }
}

#app > * {
  max-width: 50rem;
  margin-left: auto;
  margin-right: auto;
}
#app > form {
  max-width: 100%;
}
#app h1{
  display: block;
  min-width: 100%;
  width: 100%;
  text-align: center;
  margin: 0;
  margin-bottom: 1rem;
}
</style>