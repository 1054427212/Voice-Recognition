<script setup lang="ts">
import * as THREE from "three";
import { getCurrentInstance, onMounted, ref } from "vue";
import { OrbitControls } from "three/examples/jsm/controls/OrbitControls";

const { proxy }: any = getCurrentInstance();
const threeCanvas = ref(null);
const width = ref(1920);
const height = ref(920);
const getTheWidthAndHeight = () => {
  width.value = proxy.$refs.fatherRef.offsetWidth;
  height.value = proxy.$refs.fatherRef.offsetHeight;
};
const render3D = () => {
  const scene = new THREE.Scene();
  const geometry = new THREE.BoxGeometry(1000, 10, 100);
  const material = new THREE.MeshBasicMaterial({ color: 0xdcdcdc });
  const mesh = new THREE.Mesh(geometry, material);
  scene.add(mesh);
  // 添加坐标
  const axesHelper = new THREE.AxesHelper(250);
  scene.add(axesHelper);
  // 添加相机
  const camera = new THREE.PerspectiveCamera(
    30,
    width.value / height.value,
    1,
    3000
  );
  camera.position.set(292, 223, 185);
  camera.lookAt(0, 0, 0);

  const renderer = new THREE.WebGLRenderer();
  renderer.setSize(width, height);
  // 将渲染器的 canvas 元素添加到指定的 div 中
  const targetDiv = document.getElementById("1"); // 替换成你实际的 div ID
  targetDiv.appendChild(renderer.domElement);
  // 添加轨道控制器
  const controls = new OrbitControls(camera, renderer.domElement);
  // 设置带阻尼的控制拖动惯性
  controls.enableDamping = true;
  function render() {
    controls.update();
    renderer.render(scene, camera);
    // mesh.rotateY(0.001);
    requestAnimationFrame(render);
  }

  render();

  // 监听窗口变化
  window.addEventListener("resize", () => {
    // 重置渲染器宽高比例
    renderer.setSize(width, height);
    // 重置相机宽高比例
    camera.aspect = width / height;
    // 更新相机投影矩阵
    camera.updateProjectionMatrix();
  });
};
onMounted(() => {
  getTheWidthAndHeight();
  render3D();
});
</script>

<template>
  <div class="body" id="1" ref="fatherRef">
    <!-- <canvas ref="fatherRef"></canvas> -->
  </div>
</template>

<style lang="scss" scoped>
.body {
  display: flex;
}
canvas {
  display: flex;
}
</style>
