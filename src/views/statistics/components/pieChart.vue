<script setup lang="ts">
import { ref, computed } from "vue";
import { useDark, useECharts } from "@pureadmin/utils";

const { isDark } = useDark();

const theme = computed(() => (isDark.value ? "dark" : "light"));

const pieChartRef = ref();
const { setOptions } = useECharts(pieChartRef, {
  theme
});

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
      name: "饼图",
      type: "pie",
      top: "20%",
      radius: "80%",
      center: ["50%", "50%"],
      color: ["#e6a23c", "#f56c6c", "#53a7ff", "#000000"],
      data: [
        { value: 400, name: "error1" },
        { value: 1600, name: "error2" },
        { value: 7200, name: "error3" },
        { value: 8200, name: "error4" },
      ]
    }
  ]
});
</script>

<template>
  <div ref="pieChartRef" style="width: 100%; height: 35vh" />
</template>
