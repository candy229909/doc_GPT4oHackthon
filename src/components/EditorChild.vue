<script>
import axios from 'axios';
import {ref, reactive, onMounted, onBeforeUnmount, toRefs, watch, defineComponent } from "vue";

// ==== tinymce ====

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

import imgAssistant from "@/assets/icon/assistant.svg";


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

    const gptDialog = ref(false)
    const imgAssistantRef = ref(imgAssistant)
    const inputText = ref('')

    let testData = reactive({data: null})
    let {data} = toRefs(testData)

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
            // console.log('Key pressed:', event.key);
            getNewDataFromGPT(content.value);
            // emit('onEnterPress', content.value);
          }
        })
      }
    });
    // https://vue-lessons-api.vercel.app/courses/list
    const getNewDataFromGPT = async (content) => {
      const url = `https://vue-lessons-api.vercel.app/courses/list`
      const res = await axios.get(url)
      console.log(res, 'res::');
      testData.data = res.data
      // try {
      //   const response = await axios.post(url, {
      //     data: {
      //       content,
      //     },
      //   });

      //   const responseData = response.data;
      //   console.log('API response:', responseData);

      // } catch (error) {
      //   console.error('API error:', error);
      // }
    };

    const openDialog = () => {
      gptDialog.value = true
    }



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
      content, init, tinymceId, data, gptDialog, openDialog, imgAssistant: imgAssistantRef, inputText
    }
  }
});
</script>
<template>
<div>

  <!-- {{ content }} -->

    {{ data }}

  <Editor
      :id="tinymceId"
      v-model="content"
      :init="init"
      ref="editor"
    ></Editor>

    <!-- 跳窗 -->
    <q-dialog v-model="gptDialog">
      <q-card class="q-pa-md" style="max-width: 60vw;">

        <div class="flex items-center">
          <img class="q-mr-md" :src="imgAssistant" />
          <div class="fz-larger text-weight-bold q-my-md">AI Assistant</div>
        </div>
        <div class="">
          <q-input
            outlined
            :input-style="{ width: '100vw', height: '50VH' }"
            v-model="inputText"
            type="textarea"
            maxlength="999"
          />
        </div>
        <div class="flex q-py-md">
          <q-btn class="q-mr-md" label="replace" color="primary" />
          <q-btn class="q-mr-md" flat label="insert below" color="dark" />
          <q-btn class="q-mr-md" flat label="try again" color="dark" />
          <q-btn class="q-mr-md" flat label="stop" color="grey" />
        </div>
      </q-card>
    </q-dialog>
</div>
</template>
<style lang="scss" scoped>

</style>