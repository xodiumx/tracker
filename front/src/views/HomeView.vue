<script setup>
</script>

<template>
  <div class="main-block">
    <div class="container">
      <div class="external-block">
          <div class="internal-block">
              <TrackerComponent> </TrackerComponent>
          </div>
      </div>
    </div>
  </div>
</template>

<style scoped>

.container {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
}
.external-block {
    padding: 5%;
    margin: 5%;
    height: 100vh;
    width: 100vh;
    display: flex;
    flex-direction: column;
}
.internal-block {
    flex-grow: 1;
    margin: 2%;
    background-color: #b5b5b5;
    background-image: linear-gradient(45deg, white, silver);
    border-radius: 10px;
}
.main-block {
  background: linear-gradient(45deg, gray, black);
  height: 100%;
  width: 100%;
  margin: 0;
  padding: 0;
}
</style>