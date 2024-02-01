const Layout = () => import("@/layout/index.vue");

export default {
  path: "/",
  name: "Data",
  component: Layout,
  redirect: "/data",
  meta: {
    icon: "homeFilled",
    title: "首页",
    rank: 90
  },
  children: [
    {
      path: "/data",
      name: "Data",
      component: () => import("@/views/data/index.vue"),
      meta: {
        title: "声纹数据"
        // showLink: VITE_HIDE_HOME === "true" ? false : true
      }
    }
  ]
} as RouteConfigsTable;
