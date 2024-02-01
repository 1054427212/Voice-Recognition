const Layout = () => import("@/layout/index.vue");

export default {
    path: "/",
    name: "Visual",
    component: Layout,
    redirect: "/visual",
    meta: {
        icon: "fluent:data-bar-vertical-ascending-16-filled",
        title: "综合展示",
        rank: -1
    },
    children: [
        {
            path: "/visual",
            name: "Visual",
            component: () => import("@/views/visual/index.vue"),
            meta: {
                title: "综合展示"
            }
        }
    ]
} as RouteConfigsTable;