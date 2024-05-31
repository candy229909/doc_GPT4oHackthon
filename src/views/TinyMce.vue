<script>
import {ref, reactive, onMounted, toRefs, watch, defineComponent, defineProps, defineEmits } from "vue";
import EditorChild from "@/components/EditorChild"
export default defineComponent ({
  name: "TinyMce",
  components: {EditorChild}
});

</script>

<template>
  <div class="">
    <EditorChild />
  </div>
</template>