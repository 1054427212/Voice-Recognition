<template>
  <el-table :data="tableData" style="width: 100%">
    <el-table-column prop="num" label="序号" width="180" />
    <el-table-column prop="id" label="编号" width="180" />
    <el-table-column prop="ip" label="IP" width="180" />
    <el-table-column prop="time" label="捕获时间" width="180" />
    <el-table-column prop="length" label="捕获长度" width="180" />
    <el-table-column prop="type" label="声纹类型" width="180" />
    <!-- <el-table-column prop="type" label="文件类型" width="180" /> -->
    <el-table-column label="音频播放" width="180">
      <template #default="scope">
        <el-button @click="playAudio(scope.row)" type="primary">
          播放
        </el-button>
      </template>
    </el-table-column>
    <el-table-column prop="type1" label="频谱预览">
      <template #default="scope">
        <el-button @click="viewSpectrum(scope.row)" type="primary">
          查看
        </el-button>
      </template>
    </el-table-column>
  </el-table>
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

<script lang="ts" setup>
import { ref } from "vue";
const tableData = [
  {
    num: 1,
    id: 2,
    ip: "192.168.1.168",
    time: "2022-01-12-21:45",
    length: "3s",
    type: "异常类型1"
  },
  {
    num: 2,
    id: 2,
    ip: "192.168.1.168",
    time: "2022-01-13-19:35",
    length: "3s",
    type: "异常类型1"
    // img_url: "/public/集成数据/气象2022-01.png"
  }
];
const currentPage = ref(1);
const pagination = ref({
  current: 1,
  pageSize: 20,
  total: 0,
  pageSizes: [10, 20, 50]
});

const playAudio = rowData => {
  // 处理音频播放的逻辑
  console.log("为:", rowData, "播放音频");
};

const viewSpectrum = rowData => {
  // 处理频谱查看的逻辑
  console.log("为:", rowData, "查看频谱");
};

const onPageSizeChange = val => {
  pagination.value = val;
};

const onCurrentChange = val => {
  currentPage.value = val;
};
</script>
