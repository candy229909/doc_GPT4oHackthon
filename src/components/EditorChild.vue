<script>
import {ref, reactive, onMounted, onBeforeUnmount, toRefs, watch, defineComponent } from "vue";

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
    editorId: {
      type: String,
      required: true,
    },
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
    const { modelValue, editorId } = toRefs(props);
    const content = ref(modelValue.value);
    const tinymceId = ref(editorId.value);
    // console.log('::', editorId)

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
      setup: (editor) => {
        editor.on('keydown', (event) => {
          if (event.key === 'Enter') {
            console.log('Key pressed:', event.key);
            // emit('onEnterPress', content.value);
          }
        })
      }
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
      tinymce.init({})
    })

    return {
      content, init, tinymceId
    }
  }
});
</script>
<template>
<div>

  <!-- {{ content }} -->

  <Editor
      :id="tinymceId"
      v-model="content"
      :init="init"
      ref="editor"
    ></Editor>
</div>
</template>
<style lang="scss" scoped>

</style>