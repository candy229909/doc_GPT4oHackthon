<script>
import {ref, reactive, onMounted, toRefs, watch, defineComponent, defineProps, defineEmits } from "vue";
import EditorChild from "@/components/EditorChild"
export default defineComponent ({
  name: "TinyMce",
  components: {EditorChild},
  setup() {
    const value = ref('<h1>test</h1>');

    watch(value, (newValue) => {
      // console.log('parent2::',newValue);
    });
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