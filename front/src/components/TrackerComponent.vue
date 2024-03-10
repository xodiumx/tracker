<template>
    <div class="tracker">
      <textarea v-model="taskText"></textarea>
      <img 
        class="play-button"
        src="../assets/play-button.png" 
        alt="Add Task" 
        @click="addTask" 
      />
      <div v-for="(task, index) in tasks" :key="index">
        <component :is="task.component" :taskText="task.taskText" />
      </div>
    </div>
</template>

<style scoped>
.tracker {
    padding: 2%;
    margin: 2%;
    width: 100vh;
    height: 20vh;
}
.play-button {
    padding: 1%;
}
</style>

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