<script setup lang="ts" name="Histogram">
import { ref, computed, toRefs, defineProps,watch } from "vue";
import { useDark, useECharts } from "@pureadmin/utils";
const props = defineProps(["pieData"]);
const { pieData } = toRefs(props);

const { isDark } = useDark();

const theme = computed(() => (isDark.value ? "dark" : "light"));

const pieChartRef = ref();
const { setOptions } = useECharts(pieChartRef, {
  theme
});

// setOptions({
//   tooltip: {
//     trigger: "item"
//   },
//   legend: {
//     icon: "circle",
//     //@ts-expect-error
//     right: true
//   },
//   series: [
//     {
//       name: "",
//       type: "pie",
//       top: "20%",
//       radius: "80%",
//       center: ["50%", "50%"],
//       color: ["#e6a23c", "#f56c6c", "#53a7ff", "#ffffff"],
//       data: [
//         { value: 400, name: "error1" },
//         { value: 1600, name: "error2" },
//         { value: 7200, name: "error3" },
//         { value: 8200, name: "error4" }
//       ]
//     }
//   ]
// });
watch(pieData, (newPieData) => {
  setOptions({
  tooltip: {
    trigger: "item"
  },
  legend: {
    icon: "circle",
    //@ts-expect-error
    right: true
  },
  series: [
    {
      name: "",
      type: "pie",
      top: "10%",
      radius: "90%",
      center: ["50%", "50%"],
      color: ["#e6a23c", "#f56c6c", "#53a7ff", "#ffffff"],
      data: newPieData
    }
  ]
});
}, { immediate: true });
</script>
<template>
  <div class="histogram">
    <div class="histogram-title">
      <div>声纹错误统计</div>
    </div>
    <div class="histogram-content" ref="pieChartRef"></div>
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
