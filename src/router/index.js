import { createRouter, createWebHistory } from "vue-router";
// import HomeView from "@/views/HomeView.vue";
import TinyMce from "@/views/TinyMce.vue";

const routes = [
  {
    path: "/",
    name: "home",
    component: TinyMce,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
