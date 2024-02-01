<script lang="ts" setup>
import { onMounted, onUnmounted, ref, getCurrentInstance, reactive } from "vue";
import { formatTime } from "@/utils";
// import threeDBox from "@/views/visual/components/3dBox.vue";
import threeDBox from "@/views/visual/components/3dBox1.vue";

const decorationColor = ["#568aea", "#000000"];
// 时间日期处理部分
const date = reactive({
  dateDay: null,
  dateWeek: null,
  dateYear: null
});
let timing = ref(null);
const weekday = reactive([
  "周日",
  "周一",
  "周二",
  "周三",
  "周四",
  "周五",
  "周六"
]);
const timeFn = () => {
  timing.value = setInterval(() => {
    date.dateDay = formatTime(new Date(), "HH: mm: ss");
    date.dateYear = formatTime(new Date(), "yyyy-MM-dd");
    date.dateWeek = weekday[new Date().getDay()];
  }, 1000);
};

// 生命周期
onMounted(() => {
  // windowDraw()
  // calcRate()
  // 格式化时间函数
  timeFn();
  // getTheWidthAndHeight();
  // console.log(width.value);
  // console.log(height.value);
});
</script>

<template>
  <div style="width: 100%; height: 100%" ref="fatherRef">
    <div class="index">
      <div class="bg">
        <div class="host-body">
          <!-- 标题 -->
          <div class="d-flex jc-center">
            <dv-decoration-10 class="dv-dec-10" />
            <div class="d-flex jc-center">
              <dv-decoration-8 class="dv-dec-8" :color="decorationColor" />
              <div class="title">
                <span class="title-text">声纹检测</span>
                <dv-decoration-6
                  class="dv-dec-6"
                  :reverse="true"
                  :color="['#50e3c2', '#67a1e5']"
                />
              </div>
              <dv-decoration-8
                class="dv-dec-8"
                :reverse="true"
                :color="decorationColor"
              />
            </div>
            <dv-decoration-10 class="dv-dec-10-s" />
          </div>
          <!--时间部分-->
          <div class="date">
            <div class="text">
              {{ date.dateYear }} {{ date.dateWeek }} {{ date.dateDay }}
            </div>
          </div>
          <!--图表部分-->
          <!-- <div class="d-flex jc-sb">
            <div class="left">
              <dv-border-box-8 title="皮带3D图">
                <threeDBox></threeDBox>
              </dv-border-box-8>
            </div>
            <div class="right">
              <div class="right-top">
                <dv-border-box-8 :reverse="true"> </dv-border-box-8>
              </div>
              <div class="right-bottom">
                <dv-border-box-8 :reverse="true"> </dv-border-box-8>
              </div>
            </div>
          </div> -->
          <div class="d-flex jc-sb">
            <div class="td">
              <dv-border-box-8 title="皮带3D图">
                <threeDBox></threeDBox>
              </dv-border-box-8>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<style lang="scss">
.index {
  color: #d3d6dd;
  height: 100%;
  display: flex;
  // 背景图设置
  .bg {
    width: 100%;
    height: 100%;
    background-image: url("@/assets/pageBg.png");
    background-size: cover;
    background-position: center center;
  }
  // 主体部分
  .host-body {
    height: 100%;
    
    .d-flex {
      display: flex;
      justify-content: center;
      .td {
        display: flex;
        height: 100%;
        width: 100%;
      }
      .left {
        display: flex;
        padding: 10px;
        height: 100%;
        width: 60%;
      }
      .right {
        display: flex;
        flex-direction: column; /* 设置为列布局，即上下排列 */
        width: 40%;
      }
      .right-top,
      .right-bottom {
        padding: 10px;

        width: 100%;
        height: 50%; /* 上下两部分平分高度 */
      }
    }
    // 时间部分
    .date {
      height: 40px;
      position: relative;

      .text {
        display: inline-block;
        line-height: 40px;
        position: absolute;
        right: 20px;
        font-family: Arial, Helvetica, sans-serif;
      }
    }

    .jc-sb {
      justify-content: space-around;
      height: calc(100% - 90px);
      width: 100%;
    }

    .dv-dec-10,
    .dv-dec-10-s {
      width: 33.3%;
      height: 5px;
    }

    .dv-dec-10-s {
      transform: rotateY(180deg);
    }

    .dv-dec-8 {
      width: 200px;
      height: 50px;
    }

    .title {
      position: relative;
      width: 500px;
      text-align: center;
      background-size: cover;
      background-repeat: no-repeat;

      .title-text {
        font-size: 30px;
        position: absolute;
        bottom: 0;
        left: 50%;
        transform: translate(-50%);
      }

      .dv-dec-6 {
        position: absolute;
        bottom: -30px;
        left: 50%;
        width: 250px;
        height: 8px;
        transform: translate(-50%);
      }
    }
  }
}

// .left{
//   height: 80%;
//   widows: 80%;
// }
.left-top {
  height: 100%;
  width: 80%;
}

.left-center {
  height: 50%;
}

.left-bottom {
  height: 300px;
}

.center {
  height: 100%;
}
</style>
