<script setup>
</script>

<template>
  <main>
    <div class="container">
      <div class="external-block">
          <div class="internal-block">
              <TrackerComponent> </TrackerComponent>
          </div>
      </div>
    </div>
  </main>
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
    background-color: #0a0000;
    height: 100vh;
    width: 100vh;
}
.internal-block {
    width: 100vh;
    height: 90vh;
    background-color: #d0d0d0;
}
</style>