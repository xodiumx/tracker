<template>
    <div class="tracker">
      <div class="input-container">
        <input
          type="text" 
          v-model="taskText" 
          placeholder="Новая задача" 
        />
        <img 
        class="play-button"
        src="../assets/play-button.svg" 
        alt="Add Task"
        @click="addNewTaskToDB"
       />
      </div>
      <div class="tasks-container">
        <div v-for="(task, index) in tasks" :key="index">
          <TaskComponent
            :taskId="task.id"
            :taskName="task.name" 
            :taskTime="task.time_in_work"/>
          <hr>
        </div>
      </div>
    </div>
</template>

<script>
import axios from 'axios';
import TaskComponent from '@/components/TaskComponent.vue';

export default {
  data() {
    return {
      tasks: [],
      taskText: "",
    };
  },
  created() {
    this.fetchTasks();
  },
  methods: {
    addNewTaskToDB: async function () {
      try {
        const response = await axios.post('http://178.154.207.253:8000/tasks', {
          name: this.taskText,
          time_in_work: 0
        });
        console.log(response.data);
        this.fetchTasks();
        alert('Задача успешно создана.');
        window.location.reload();
      } catch (error) {
        console.error('Ошибка при отправке запроса', error);
      }
    },
    fetchTasks: async function () {
        const config = {
          headers: {
            "Access-Control-Allow-Origin": "*",
          }
        };
        try {
          const response = await axios.get('http://178.154.207.253:8000/tasks', config);
          this.tasks = response.data;
          console.log(this.tasks)
        } catch (error) {
          console.error('Ошибка при получении списка задач', error);
        }
    },
  }
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