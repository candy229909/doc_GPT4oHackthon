<script>
import axios from 'axios';
import {ref, reactive, onMounted, onBeforeUnmount, toRefs, watch, defineComponent } from "vue";

import {generateData, enter2Data, getData} from "@/api/editor";

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
import 'tinymce/plugins/image'; // 新增 image 插件
import 'tinymce/plugins/imagetools';
import 'tinymce/plugins/paste';

import imgAssistant from "@/assets/icon/assistant.svg";
import {editIcon} from "@/shared/svg";

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
      default: 'quickbars emoticons image table paste',
    },
    toolbar: {
    type: [String, Array],
    default:
      ' customButton | bold italic underline strikethrough | fontsizeselect | forecolor backcolor | alignleft aligncenter alignright alignjustify|bullist numlist |outdent indent blockquote | undo redo | axupimgs | removeformat | table | insertfile  | image |emoticons',
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

      // paste_data_images: true, // 启用粘贴图片功能
      // automatic_uploads: true, // 自动上传
      // images_upload_url: '', // 设置上传URL
      // file_picker_types: 'image',
      setup: (editor) => {
        editor.on('keydown', (event) => {
          if (event.key === 'Enter') {
            getNewDataFromGPT(content.value);
            // emit('onEnterPress', content.value);
          }
        });

        // 处理粘贴和拖放
        // editor.on('drop', (e) => {
        //   const items = (e.dataTransfer && e.dataTransfer.files) || [];
        //   if (items.length) {
        //     e.preventDefault();
        //     const file = items[0];
        //     const reader = new FileReader();
        //     reader.onload = (event) => {
        //       const base64 = event.target.result;
        //       // 将图片插入到编辑器
        //       editor.insertContent(`<img src="${base64}" />`);
        //     };
        //     reader.readAsDataURL(file);
        //   }
        // });


        // editor.on('paste', (e) => {
        //   const clipboardData = e.clipboardData || window.clipboardData;
        //   const items = clipboardData.items || [];
        //   for (const item of items) {
        //     if (item.type.indexOf('image') !== -1) {
        //       const file = item.getAsFile();
        //       const reader = new FileReader();
        //       reader.onload = (event) => {
        //         const base64 = event.target.result;
        //         // 将图片插入到编辑器
        //         editor.insertContent(`<img src="${base64}" />`);
        //       };
        //       reader.readAsDataURL(file);
        //       e.preventDefault();
        //     }
        //   }
        // });

        editor.ui.registry.addButton('customButton', {
          icon: 'custom-icon',
          onAction: () => {
            console.log('onAction');
          }
        });

        editor.ui.registry.addIcon('custom-icon', editIcon);
      }
    });
    // https://vue-lessons-api.vercel.app/courses/list
    const getNewDataFromGPT = async (content) => {
      const url = `https://vue-lessons-api.vercel.app/courses/list`
      // const res = await axios.get(url)
      // console.log(res, 'res::');
      // testData.data = res.data

      try {
        const data = {
          format: 'blog',
          sentence: content
        }
        console.log(data, 'data::');
        const res = await enter2Data(data);
        console.log(res, 'res::');
        // const responseData = response.data;
        // console.log('API response:', responseData);

      } catch (error) {
        console.error('API error:', error);
      }
    };

    const openDialog = () => {
      gptDialog.value = true
    }



    watch(content, (newValue) => {
      // console.log('watch1:', newValue)
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

    <!-- {{ data }} -->


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