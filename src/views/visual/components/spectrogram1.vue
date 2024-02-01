<script setup lang="ts" name="Histogram">
</script>
<template>
  <div class="histogram">
    <div class="histogram-title">
      <div>频谱展示1</div>
    </div>
    <div class="histogram-content" ref="pieChartRef">
      <!-- <img src="./test.png" alt=""> -->
    </div>
  </div>
</template>

<style scoped>
.histogram {
  display: flex;
  padding: 15px;
  width: 100%;
  height: 100%;
  flex-direction: column;
  .histogram-title {
    display: flex;
    /* text-align: center; */
    height: 10%;
    width: 100%;
    /* justify-content: center; */
    padding-left: 10px;
    align-items: center;
    font-size: 25px;
  }
  .histogram-content {
    display: flex;
    width: 100%;
    height: 90%;
    /* background-color: #031a67; */
  }
}
</style>
