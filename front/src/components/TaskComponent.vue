<template>
  <div class="task-container">
    <div class="task" @click="toggleTimer">
      <div class="task-content">
        <h3>{{ taskText }}</h3>
      </div>
      <div class="timer">
        <h4>{{ formattedTime }}</h4>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    taskText: {
      type: String,
      required: true,
    },
  },
  data() {
    return {
      timer: 0,
      timerInterval: null,
      isTimerRunning: true,
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
  },
  beforeDestroy() {
    this.stopTimer();
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