<script setup lang="ts">
import { onMounted } from "vue";
import Table1 from "@/views/data/components/table1.vue";
import Table2 from "@/views/data/components/table2.vue";
import Table3 from "@/views/data/components/table3.vue";
import Table4 from "@/views/data/components/table4.vue";
import Table5 from "@/views/data/components/table5.vue";
import { getAllEncoderData } from "@/api/data";

// onMounted(async () => {
//   // 在组件挂载后执行的异步操作
//   try {
//     const res = await getAllEncoderData();
//     console.log(res);
//   } catch (error) {
//     console.error("Error fetching data:", error);
//   }
// });
</script>

<template>
  <div>
    <div class="scroll-bar" style="padding: 20px">
      <el-card style="width: 100%; height: 100%">
        <el-tabs>
          <el-tab-pane label="声纹数据"> <Table1 /> </el-tab-pane>
          <!-- <el-tab-pane label="异常类型1"> <Table2 /> </el-tab-pane> -->
          <!-- <el-tab-pane label="异常类型2"> <Table3 /> </el-tab-pane> -->
          <!-- <el-tab-pane label="异常类型3"> <Table4 /> </el-tab-pane> -->
          <!-- <el-tab-pane label="异常类型4"> <Table5 /> </el-tab-pane> -->
        </el-tabs>
      </el-card>
    </div>
  </div>
</template>

<style scoped></style>
