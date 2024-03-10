<template>
    <div class="tracker">
      <div class="input-container">
        <input
          class="type-1"
          type="text" 
          v-model="taskText" 
          placeholder="Новая задача" 
        />
        <img 
        class="play-button"
        src="../assets/play-button.svg" 
        alt="Add Task" 
        @click="addTask" 
       />
      </div>
      <div class="tasks-container">
        <div v-for="(task, index) in tasks" :key="index">
          <component :is="task.component" :taskText="task.taskText" />
          <hr>
        </div>
      </div>
    </div>
</template>

<script>
import TaskComponent from '@/components/TaskComponent.vue';

export default {
  data() {
    return {
      tasks: [],
      taskText: "",
    };
  },
  methods: {
    addTask() {
      this.tasks.push({
        component: TaskComponent,
        taskText: this.taskText,
      });
      this.taskText = "";
    },
  },
};
</script>

<style scoped>

hr {
  width: 80vh;
  padding-right: 1rem;
}

.input-container {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 85vh;
  height: auto;
  padding: 1rem;
}

input {
  flex: 1;
  margin-right: 10px;
  padding: 0.5rem;
  border-radius: 10px;
  border: 1px solid #eee;
  transition: .3s border-color;
}

input:hover {
  border: 1px solid #aaa;
}

.play-button {
  width: 4%;
  height: 4%;
  cursor: pointer;
  filter: grayscale(100%);
}

.play-button:hover {
  width: 5%;
  height: 5%;
  transition: .6s;
  filter: grayscale(40%);
}

.tracker {
  padding: 2%;
  margin: 2%;
}

.tasks-container {
  overflow: auto; /* Добавлено для прокрутки, если задач становится слишком много */
}
</style>