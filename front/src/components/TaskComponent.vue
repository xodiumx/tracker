<template>
  <div class="task-container" @click="UpdateTaskInDB">
    <div class="task" @click="toggleTimer">
      <div class="task-content">
        <h3>{{ taskName }}</h3>
      </div>
      <div class="timer">
        <h4>{{ formattedTime }}</h4>
      </div>
    </div>
  </div>
</template>

<script>

import axios from 'axios';

const apiUrl = import.meta.env.VITE_TASKS_API

export default {
  props: {
    taskId: {
      type: Number,
      required: true,
    },
    taskName: {
      type: String,
      required: true,
    },
    taskTime: {
      type: Number,
      required: true,
    },
  },
  data() {
    return {
      timer: this.taskTime,
      timerInterval: null,
      isTimerRunning: false,
    };
  },
  mounted() {
    this.startTimer();
  },
  computed: {
    formattedTime() {
      const hours = Math.floor(this.timer / 3600);
      const minutes = Math.floor((this.timer % 3600) / 60);
      const seconds = this.timer % 60;

      if (hours > 0) {
        return `${hours}:${this.padZero(minutes)}:${this.padZero(seconds)} hour${hours > 1 ? 's' : ''}`;
      } else if (minutes > 0) {
        return `${minutes}:${this.padZero(seconds)} min`;
      } else {
        return `${seconds} sec`;
      }
    },
  },
  methods: {
    startTimer() {
      this.timerInterval = setInterval(() => {
        if (this.isTimerRunning) {
          this.timer++;
        }
      }, 1000);
    },
    stopTimer() {
      clearInterval(this.timerInterval);
    },
    padZero(value) {
      return value < 10 ? `0${value}` : value;
    },
    toggleTimer() {
      this.isTimerRunning = !this.isTimerRunning;
    },
    UpdateTaskInDB: async function () {
      if (this.timer < 60) {
        alert('Время работы должно быть не менее 60 секунд.');
        return;
      }
      const data = {
          name: this.taskName,
          time_in_work: this.timer,
      };
      try {
        const response = await axios.patch(`${apiUrl}/${this.taskId}`, data);
        console.log(response.data);
        this.fetchTasks();
        alert('Задача успешно обновлена.');
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
          const response = await axios.get(apiUrl, config);
          this.tasks = response.data;
          console.log(this.tasks)
        } catch (error) {
          console.error('Ошибка при получении списка задач', error);
        }
    },
  },
};
</script>


<style scoped>
h3 {
  padding-left: 3rem;
}
h4 {
  color: blue;
}
.task-container {
  margin: 0;
  padding: 0;

}
.task {
  display: flex;
  justify-content: space-between;
  margin-right: 6rem;
}
.task-content {
  flex: 1;
}
</style>