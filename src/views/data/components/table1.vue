<script lang="ts" setup>
import { onMounted } from "vue";
import list from "mock/list";
import { ref } from "vue";
import { array } from "vue-types";
import { getAllEncoderData, showVoice, saveEncoderData } from "@/api/data";

const res = ref([]);

onMounted(async () => {
  // 在组件挂载后执行的异步操作

  try {
    const result = await getAllEncoderData();
    res.value = result.data;
    console.log("11",result)
  } catch (error) {
    console.error("Error fetching data:", error);
  }
});

const currentPage = ref(1);
const pagination = ref({
  current: 1,
  pageSize: 20,
  total: 0,
  pageSizes: [10, 20, 50]
});

const playAudio = rowData => {
  const videoPath = rowData.path; // 获取路径
  // 在这里处理播放 MP4 的逻辑，比如使用 video 标签等方式
  console.log("111");
  console.log(rowData);
  const audio = new Audio(videoPath);
  audio.play();
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

const onPageSizeChange = val => {
  pagination.value = val;
};

const onCurrentChange = val => {
  currentPage.value = val;
};

import WaveSurfer from "wavesurfer.js";
import { getTime } from "@pureadmin/utils";
import { Play, Pause, Forward, Rewind } from "../svg";
import { onBeforeUnmount } from "vue";

const mediaDialogVisible = ref(false);
const selectedRow = ref({ audioUrl: "", imageUrl: "" });
const videoPath = ref()
const showMediaDialog = row => {
  selectedRow.value.audioUrl = row.audioUrl;
  selectedRow.value.imageUrl = row.imageUrl;
  mediaDialogVisible.value = true;
  videoPath.value = row.path; // 获取路径
  // 在这里处理播放 MP4 的逻辑，比如使用 video 标签等方式
  console.log("111");
  console.log(videoPath.value);
};

import { reactive } from "vue";
import AudioPlayer from "../components/audioPlayer.vue";
let audio = ref(null);
function handleChangeAudioVolume() {
  // 点击页面关闭音量键显示
  if (audio.value) {
    audio.value.audioHuds = false;
  }
}
const postDataTest = async () => {
    const data = {
    number: 1,
    ip: '192.168.1.168',
    time: '2024-01-19 10:01:00',
    length: 3,
    type: 'normal',
    path: 'public/audio/output11.mp4',
  };

  const response = await saveEncoderData({ data });
  console.log(res)
   
};
</script>

<template>
  <el-table :data="res" style="width: 100%">
    <el-table-column prop="id" label="序号" width="180" />
    <el-table-column prop="number" label="编号" width="180" />
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
    <el-table-column label="音频频谱" width="180">
      <template #default="scope">
        <el-button @click="showMediaDialog(scope.row)" type="primary">
          查看
        </el-button>
        <!-- <el-button @click="postDataTest()" type="primary"> 测试存储 </el-button> -->
      </template>
    </el-table-column>
  </el-table>
  <el-dialog
    v-model="mediaDialogVisible"
    title="查看音频"
    width="1000px"
    height="1000px"
    class="video_box"
  >
    <div class="page" @click="handleChangeAudioVolume">
      <audio-player
        ref="audio"
        class="audio-box"
        :fileurl="videoPath"
      ></audio-player>
    </div>
  </el-dialog>

  <el-affix position="bottom" :offset="0" class="affix" style="height: 5vh">
    <div class="pagination-container">
      <el-pagination
        class="float-right"
        style="
          height: 40px;
          line-height: 40px;
          margin-right: 20px;
          padding-top: 10px;
        "
        v-model:currentPage="pagination.current"
        :page-size="pagination.pageSize"
        :total="pagination.total"
        :page-sizes="pagination.pageSizes"
        :background="true"
        layout="total, sizes, prev, pager, next, jumper"
        @size-change="onPageSizeChange"
        @current-change="onCurrentChange"
      />
    </div>
  </el-affix>
</template>

<!-- 是不是所有音频都要保存，保存几秒，间隔多久
  1. 保存音频  -- 服务器
  2. 隔多少秒 抽取多长时间
  3. 并发处理 -- 检测 存储
-->

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
