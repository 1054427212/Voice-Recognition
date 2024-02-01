<template>
  <el-table :data="res" style="width: 100%">
    <el-table-column prop="num" label="序号" width="180" />
    <el-table-column prop="id" label="编号" width="180" />
    <el-table-column prop="ip" label="IP" width="180" />
    <el-table-column prop="time" label="捕获时间" width="180" sortable />
    <el-table-column prop="length" label="捕获长度" width="180" />
    <el-table-column
      prop="type"
      label="声纹类型"
      width="180"
      :filters="typeFilters"
      :filter-method="filterType"
    />
    <!-- <el-table-column prop="type" label="文件类型" width="180" /> -->
    <el-table-column label="音频频谱" width="180">
      <template #default="scope">
        <el-button @click="playAudio(scope.row.path)" type="primary">
          播放
        </el-button>
      </template>
    </el-table-column>
  </el-table>
</template>

<script lang="ts" setup>
import { onMounted } from "vue";
import list from "mock/list";
import { ref } from "vue";
import { array } from "vue-types";
import { getAllEncoderData } from "@/api/data";
import { showVoice } from "@/api/data";


const res = ref([]);

onMounted(async () => {
  // 在组件挂载后执行的异步操作

  try {
    const result = await getAllEncoderData();
    // res.value = result;

    console.log(result);
  } catch (error) {
    console.error("Error fetching data:", error);
  }
});


const playAudio = async (audioPath: string) => {
  try {
    const response = await showVoice({ path: audioPath });
    console.log(response)
      const audio = new Audio();
      audio.src = URL.createObjectURL(new Blob([response], { type: 'audio/mp4' }));
      audio.load();
      audio.play();

      audio.addEventListener('ended', () => {
        console.log('音频播放结束');
      });
  } catch (error) {
    console.error('请求失败：', error);
  }
};
// 声纹类型的筛选项
const typeFilters = [
  { text: "正常数据", value: "normal" },
  { text: "异常类型1", value: "error1" },
  { text: "异常类型2", value: "error2" },
  { text: "异常类型3", value: "error3" },
  { text: "异常类型4", value: "error4" }
];
// 筛选方法
const filterType = (value, row) => {
  return row.type === value;
};
const emits = defineEmits(["distribution_evt"]);

const showDistribution = () => {
  emits("distribution_evt");
};

</script>
<style scoped lang="scss">
.video_box {
  width: 100%;
  height: 100%;
}

.plugin {
  width: 100%;
  height: 100%;
}

.playWnd {
  width: 800px;
  height: 600px;
  margin: 0;
}

.video_box {
  ::v-deep .el-dialog__body {
    padding: 0 !important;
  }
}
</style>
