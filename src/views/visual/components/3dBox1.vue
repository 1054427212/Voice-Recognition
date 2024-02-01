<script setup lang="ts">
import * as THREE from "three";
import Histogram from "./histogram.vue";
import Pie from "./pie.vue";
import Spectrogram1 from "./spectrogram1.vue";
import Spectrogram2 from "./spectrogram2.vue";
import { getEncoderErrorData } from "@/api/visual";
import { getCurrentInstance, nextTick, onMounted, ref } from "vue";
import { OrbitControls } from "three/examples/jsm/controls/OrbitControls";
import { GLTFLoader } from "three/addons/loaders/GLTFLoader.js";

const { proxy }: any = getCurrentInstance();
const threeCanvas = ref(null);
const width = ref(900);
const height = ref(900);
const fatherRef = ref(null);
const getTheWidthAndHeight = () => {
  // width.value = proxy.$refs.fatherRef.offsetWidth;
  // height.value = proxy.$refs.fatherRef.offsetHeight;

  width.value = fatherRef.value.clientWidth;
  height.value = fatherRef.value.clientHeight;
  console.log(width.value);
  console.log(height.value);
};
const render3D = () => {
  const parentDiv = proxy.$el.parentElement;
  // width.value = parentDiv.clientWidth + 150;
  width.value = parentDiv.clientWidth;
  height.value = parentDiv.clientHeight;
  console.log("Parent Div Width:", width.value);
  console.log("Parent Div Height:", height.value);
  // 创建场景
  const scene = new THREE.Scene();
  // 添加坐标系
  // const axesHelper = new THREE.AxesHelper(250);
  // scene.add(axesHelper);

  // 添加相机、相机位置、角度
  const camera = new THREE.PerspectiveCamera(
    30,
    width.value / height.value,
    1,
    3000
  );
  camera.position.set(0, 400, 900);
  camera.lookAt(0, 0, 0);
  // 创建立方体
  const geometry = new THREE.BoxGeometry(1000, 10, 100); // x y z z是朝向我们的，y是向上的
  // 3D模型的加载
  // const loader = new GLTFLoader(); // 创建一个gltf文件加载器

  // loader.load('./3d/scene.gltf', function (gltf) {
  //   const sofa = gltf.scene
  //   // gltf的.scene就是我们最终可以添加到 场景当中的模型j
  //   gltf.scene.scale.x = 2;
  //   gltf.scene.scale.y = 2;
  //   gltf.scene.scale.z = 2;
  //   sofa.position.x = 2
  //   scene.add(gltf.scene)
  // })
  // 贴图方式的加载
  const texLoader = new THREE.TextureLoader();
  // .load()方法加载图像，返回一个纹理对象Texture   .setCrossOrigin("anonymous") 设置跨域
  const texture = texLoader.load("public/3d/chuansongdai2.jpg"); // 这里的load路径很奇怪，我写@的方式就不行，只能直接写，可能图片的加载路径不同吧
  // 做滚动动画
  texture.wrapS = THREE.RepeatWrapping;
  texture.wrapT = THREE.RepeatWrapping;
  // 定义纹理的滚动速度
  const scrollSpeed = 0.002;
  // 初始化纹理坐标的偏移值
  let textureOffset = 0;
  const material = new THREE.MeshBasicMaterial({
    // 设置纹理贴图：Texture对象作为材质map属性的属性值
    map: texture // map表示材质的颜色贴图属性
    // color: 0x808080, // 颜色
    // transparent: true
    // side: THREE.DoubleSide
    // wireframe:true,
  });
  // 创建立方体网格
  const cubeMesh = new THREE.Mesh(geometry, material);

  const gap = 50; // 间隔

  for (let i = -500, num = 1; i <= 500; i += gap, num++) {
    const geo = new THREE.BoxGeometry(10, 10, 10);
    const mat = new THREE.MeshBasicMaterial({ color: 0xffffe0 });
    const cube = new THREE.Mesh(geo, mat);
    cube.position.set(i, 0, 55); // 或者 geo.translate(i,0,50);;
    cube.name = String(num);
    cubeMesh.add(cube);
  }

  scene.add(cubeMesh);

  // 创建立方体的边框
  const edges = new THREE.EdgesGeometry(geometry);
  const lineMaterial = new THREE.LineBasicMaterial({ color: 0x000000 });
  const edgesMesh = new THREE.LineSegments(edges, lineMaterial);
  cubeMesh.add(edgesMesh);
  // 创建星星的材质和几何体
  const starGeometry = new THREE.BufferGeometry();
  const starMaterial = new THREE.PointsMaterial({ color: 0xffffff, size: 0.1 });

  // 生成随机位置的星星
  const positions = new Float32Array(300 * 3);
  for (let i = 0; i < 300; i++) {
    const i3 = i * 3;
    positions[i3] = (Math.random() - 0.5) * 2000;
    positions[i3 + 1] = (Math.random() - 0.5) * 2000;
    positions[i3 + 2] = (Math.random() - 0.5) * 2000;
  }
  starGeometry.setAttribute(
    "position",
    new THREE.BufferAttribute(positions, 3)
  );
  // 创建星星的点云
  const starField = new THREE.Points(starGeometry, starMaterial);
  scene.add(starField);

  // 渲染器
  const renderer = new THREE.WebGLRenderer();
  renderer.setSize(width.value, height.value);
  // 设置背景颜色
  renderer.setClearColor(0x060711, 1);
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
    // 使星星点云旋转
    starField.rotation.x += 0.001;
    starField.rotation.y += 0.001;
    // 传送带滚动
    textureOffset += scrollSpeed;

    // 将更新后的偏移值应用于纹理坐标
    texture.offset.set(textureOffset, 0);
  }
  render();

  // 监听窗口变化 让3d图随着窗口的放大缩小自适应变化
  window.addEventListener("resize", () => {
    // console.log(":!111");
    width.value = parentDiv.clientWidth;
    height.value = parentDiv.clientHeight;
    // 重置渲染器宽高比例
    renderer.setSize(width.value, height.value);
    // 重置相机宽高比例
    camera.aspect = width.value / height.value;
    // 更新相机投影矩阵
    camera.updateProjectionMatrix();
  });

  const raycaster = new THREE.Raycaster();
  const mouse = new THREE.Vector2();

  async function onMouseClick(event) {
    // 计算鼠标点击位置
    const rect = renderer.domElement.getBoundingClientRect();
    mouse.x = ((event.clientX - rect.left) / rect.width) * 2 - 1;
    mouse.y = -((event.clientY - rect.top) / rect.height) * 2 + 1;

    // 更新射线的起点
    raycaster.setFromCamera(mouse, camera);

    // 计算射线和物体的交点
    const intersects = raycaster.intersectObjects(cubeMesh.children, true);

    if (intersects.length > 0) {
      const clickedCube = intersects[0].object;
      console.log("Clicked on cube:", clickedCube.name);
      const data = {
        number: clickedCube.name
      };
      encoderRes.value = await getEncoderErrorData({ data });
      console.log(encoderRes.value);
      console.log(encoderRes.value.data);
      console.log(encoderRes.value.data.length);
      // 初始化一个对象用于统计 type 数量，用于pieData
      const typeCount = {
        error1: 0,
        error2: 0,
        error3: 0,
        error4: 0
      };
      for (let i = 0; i < encoderRes.value.data.length; i++) {
        // 2. 统计近一个月内所有错误类型，一共4钟错误
        const errorType = encoderRes.value.data[i].type;
        typeCount[errorType]++;
      }
      pieData.value = Object.entries(typeCount).map(([type, count]) => ({
        value: count,
        name: type
      }));
    }
  }

  // 添加点击事件监听器
  window.addEventListener("click", onMouseClick, false);
};
// 初始化饼图和柱状图部分
let allEncoderRes = ref();
let encoderRes = ref();

let barData = ref([]);
let pieData = ref([]);
const getAllEncoderErrorData = async () => {
  // 初始化barData数组
  for (let i = 0; i < 21; i++) {
    barData.value.push(0);
  }
  // 初始化一个对象用于统计 type 数量，用于pieData
  const typeCount = {
    error1: 0,
    error2: 0,
    error3: 0,
    error4: 0
  };

  // 传入0代表着要所有的错误信息
  const data = {
    number: "0"
  };
  allEncoderRes.value = await getEncoderErrorData({ data });
  // console.log("res", allEncoderRes.value. data.length);
  for (let i = 0; i < allEncoderRes.value.data.length; i++) {
    // 1. 统计每个编码器的出错数量，一共21个编码器，barData为0-20
    const number = allEncoderRes.value.data[i].number - 1;
    barData.value[number]++;

    // 2. 统计近一个月内所有错误类型，一共4钟错误
    const errorType = allEncoderRes.value.data[i].type;
    typeCount[errorType]++;
  }
  pieData.value = Object.entries(typeCount).map(([type, count]) => ({
    value: count,
    name: type
  }));

  console.log(barData.value);
  console.log(pieData.value);
};

onMounted(() => {
  // getTheWidthAndHeight();
  // 初始化的时候要获取所有的错误，来给pie和bar进行初始化
  getAllEncoderErrorData();

  const { proxy }: any = getCurrentInstance();
  // 加nextTrck的原因是，在刚开始onMounted获取不到高度，因为在加载，所以用nextTick来解决
  nextTick(() => {
    render3D();
  });
});
</script>

<template>
  <div class="tdbody" id="1" ref="fatherRef">
    <!-- <canvas ref="fatherRef"></canvas> -->
    <!-- <img src="./dark-wood.png" alt=""> -->
    <div class="leftTop">
      <dv-border-box-8 title="编码器出错统计">
        <Histogram :barData="barData"></Histogram>
      </dv-border-box-8>
    </div>
    <div class="leftBottom">
      <dv-border-box-8 title="声纹错误统计">
        <Pie :pieData="pieData"></Pie>
      </dv-border-box-8>
    </div>
    <div class="rightTop">
      <dv-border-box-12 title="频谱展示1">
        <Spectrogram1></Spectrogram1>
      </dv-border-box-12>
    </div>
    <div class="rightBottom">
      <dv-border-box-12 title="频谱展示2">
        <Spectrogram2></Spectrogram2>
      </dv-border-box-12>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.tdbody {
  display: flex;
}

canvas {
  // overflow: hidden;
}
.leftTop {
  position: absolute;
  left: 20px;
  top: 10px;
  width: 30vw;
  height: 15vw;
}
.leftBottom {
  position: absolute;
  left: 20px;
  bottom: 10px;
  width: 30vw;
  height: 15vw;
}
.rightTop {
  position: absolute;
  right: 20px;
  top: 10px;
  width: 30vw;
  height: 15vw;
}
.rightBottom {
  position: absolute;
  right: 20px;
  bottom: 10px;
  width: 30vw;
  height: 15vw;
}
</style>
