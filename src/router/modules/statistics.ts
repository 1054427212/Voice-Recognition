const Layout = () => import("@/layout/index.vue");

export default {
  path: "/",
  name: "Statistics",
  component: Layout,
  redirect: "/statistics",
  meta: {
    icon: "homeFilled",
    title: "首页",
    rank: 90
  },
  children: [
    {
      path: "/statistics",
      name: "Statistics",
      component: () => import("@/views/statistics/index.vue"),
      meta: {
        title: "统计"
        // showLink: VITE_HIDE_HOME === "true" ? false : true
      }
    }
  ]
} as RouteConfigsTable;
