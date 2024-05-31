<script>
import {ref, reactive, onMounted, toRefs, watch, defineComponent, defineProps, defineEmits } from "vue";
import EditorChild from "@/components/EditorChild"
export default defineComponent ({
  name: "TinyMce",
  components: {EditorChild},
  setup(props, { emit }) {
    const value = ref('<p>Content of the editor.</p>');
    return {
      value
    }
  }
});

</script>

<template>
  <div>
    <EditorChild v-model="value" />
  </div>
</template>