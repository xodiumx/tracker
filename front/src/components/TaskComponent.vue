<template>
  <div class="task">
    <div class="task-content">
      <h3>{{ taskText }}</h3>
    </div>
    <div class="timer">
      <p>{{ formattedTime }}</p>
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
        this.timer++;
      }, 1000);
    },
    stopTimer() {
      clearInterval(this.timerInterval);
    },
    padZero(value) {
      return value < 10 ? `0${value}` : value;
    },
  },
  beforeDestroy() {
    this.stopTimer();
  },
};
</script>


<style scoped>
.task {
  display: flex;
  justify-content: space-between;
}
.task-content {
  flex: 1;
}
.timer {
  margin-right: 10%;
}
</style>