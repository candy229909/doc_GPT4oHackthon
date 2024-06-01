<script>
import {ref, reactive, onMounted, toRefs, watch, defineComponent } from "vue";

import Editor from "@tinymce/tinymce-vue"; 
import tinymce from 'tinymce/tinymce.js'


import 'tinymce/skins/ui/oxide/skin.css'
import 'tinymce/themes/silver'

// Icon
import 'tinymce/icons/default'

// 用到的外掛
import 'tinymce/plugins/emoticons';
import 'tinymce/plugins/emoticons/js/emojis.js';
import 'tinymce/plugins/table';
import 'tinymce/plugins/quickbars';


export default defineComponent ({
  name: "EditorChild",
  props: {
    modelValue: {
      type: String,
      required: true,
    },
    plugins: {
      type: [String, Array],
      default: 'quickbars emoticons table',
    },
    toolbar: {
    type: [String, Array],
    default:
      ' bold italic underline strikethrough | fontsizeselect | forecolor backcolor | alignleft aligncenter alignright alignjustify|bullist numlist |outdent indent blockquote | undo redo | axupimgs | removeformat | table | emoticons',
  },
  },
  emits: ['update:modelValue'],
  components: {Editor},
  setup(props, { emit }) {
    const { modelValue } = toRefs(props);
    const content = ref(modelValue.value);
    // console.log(props, modelValue)

    const init = reactive({
      // language: 'zh_TW',
      height: 500,
      menubar: true,
      content_css: false, //若true 會出現引入路徑錯誤
      skin: false, //若true 會出現引入路徑錯誤
      plugins: props.plugins,
      toolbar: props.toolbar,
      quickbars_insert_toolbar: false,
      branding: false,
    });

    watch(content, (newValue) => {
      console.log('watch1:', newValue)
      emit('update:modelValue', newValue);
    });
    
    watch(modelValue, (newValue) => {
      // console.log('watch3:', newValue)
      content.value = newValue;
    });

    onMounted(() => {
      tinymce.init({});
    })
    return {
      content, init
    }
  }
});
</script>
<template>
<div>

  <!-- {{ content }} -->

  <Editor
      v-model="content"
      :init="init"
    ></Editor>
</div>
</template>
<style lang="scss" scoped>

</style>