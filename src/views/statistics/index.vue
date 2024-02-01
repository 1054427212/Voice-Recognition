<script setup lang="ts">
import { ref } from "vue";
import Print from "@/utils/print";
import pieChart from "./components/pieChart.vue";

defineOptions({
  name: "Print"
});

interface User {
  date: string;
  name: string;
  age: number;
  address: string;
}

const value = ref("1");

const options = [
  {
    value: "1",
    el: ".el-table",
    label: "Table"
  },
  {
    value: "2",
    el: ".echart",
    label: "Echart"
  },
  {
    value: "3",
    el: ".img",
    label: "Image"
  }
];

function onPrint() {
  const el = options.filter(v => v.value === value.value)[0]?.el;
  Print(el).toPrint;
}

const tableRowClassName = ({ rowIndex }: { row: User; rowIndex: number }) => {
  if (rowIndex === 1) {
    return "warning-row";
  } else if (rowIndex === 3) {
    return "success-row";
  }
  return "";
};

const tableData: User[] = [
  {
    date: "2016-05-03",
    name: "Tom",
    age: 18,
    address: "No. 189, Grove St, Los Angeles"
  },
  {
    date: "2016-05-02",
    name: "Tom",
    age: 18,
    address: "No. 189, Grove St, Los Angeles"
  },
  {
    date: "2016-05-04",
    name: "Tom",
    age: 18,
    address: "No. 189, Grove St, Los Angeles"
  },
  {
    date: "2016-05-01",
    name: "Tom",
    age: 18,
    address: "No. 189, Grove St, Los Angeles"
  }
];
</script>

<template>
  <el-card shadow="never">
    <pieChart class="echart mt-[10px]" />
  </el-card>
</template>

<style lang="scss" scoped>
:deep(.el-table__row.warning-row) {
  --el-table-tr-bg-color: var(--el-color-warning-light-9);
}

:deep(.el-table__row.success-row) {
  --el-table-tr-bg-color: var(--el-color-success-light-9);
}

.card-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
}
</style>
