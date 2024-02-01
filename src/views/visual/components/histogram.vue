<script setup lang="ts" name="Histogram">
import { ref, onMounted } from "vue";
import * as echarts from "echarts";
import { toRefs, watch, onBeforeMount, defineProps, watchEffect } from "vue";
const props = defineProps(["barData"]);
const { barData } = toRefs(props);
// 监听 barData 变化
let histogramDom = ref(null); //注意变量名 和 ref名字要对应

const initChart = () => {
  if (!histogramDom.value) return; // 防止初始化时为 null 报错
  var myChart = echarts.init(histogramDom.value);
  var option = {
    tooltip: {
      // 鼠标悬浮提示数据
      trigger: "axis",
      backgroundColor: "rgba(32, 33, 36,.7)",
      borderColor: "rgba(32, 33, 36,0.20)",
      borderWidth: 15,
      textStyle: {
        // 文字提示样式
        color: "#fff",
        fontSize: "12"
      },
      axisPointer: {
        // 坐标轴虚线
        type: "cross",
        label: {
          backgroundColor: "#6a7985"
        }
      }
    },

    // },
    grid: {
      // 控制图表的位置
      left: "5%",
      right: "5%",
      top: "18%",
      bottom: "5%",
      containLabel: true
    },
    xAxis: {
      axisLabel: {
        // X轴线 标签修改
        color: "white", //坐标值得具体的颜色
        fontSize: "15"
      },
      data: [
        // "0",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "11",
        "12",
        "13",
        "14",
        "15",
        "16",
        "17",
        "18",
        "19",
        "20",
        "21"
      ]
    },
    yAxis: {
      axisLabel: {
        // y轴线 标签修改
        color: "white" //坐标值得具体的颜色
      }
    },
    series: [
      {
        // data: [
        //   2549, 12421, 2637, 3146, 2549, 12421, 2637, 3146, 2549, 12421, 2637,
        //   3146, 2549, 12421, 2637, 3146, 2549, 12421, 2637, 3146
        // ], // 改成我们传进来的数据就ok了
        data: barData.value,
        type: "bar",
        barWidth: "48%", //调整柱状图宽度

        itemStyle: {
          borderRadius: [12, 12, 0, 0],
          color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            {
              offset: 0,
              color: "rgba(0,244,255,1)"
            },
            {
              offset: 1,
              color: "rgba(0,77,167,1)"
            }
          ])
        }
      }
    ]
  };
  option && myChart.setOption(option);
};

// 使用 onBeforeMount 替代 onMounted
onBeforeMount(() => {
  // 初始化时执行一次
  initChart();

  // 监听 barData 的变化
  watchEffect(() => {
    initChart();
  });
});

console.log("父组件传过来的值", barData.value);
</script>
<template>
  <div class="histogram">
    <div class="histogram-title">
      <div>编码器出错统计</div>
    </div>  
    <!-- <div class="histogram-content"></div> -->
    <div class="histogram-content" ref="histogramDom">
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
    padding-left: 10px;
    /* justify-content: center; */
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
