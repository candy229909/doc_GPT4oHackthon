<script>
import {ref, reactive, onMounted, toRefs, watch, defineComponent, defineProps, defineEmits, computed } from "vue";
import EditorChild from "@/components/EditorChild"

import { ElCascader } from 'element-plus';
export default defineComponent ({
  name: "TinyMce",
  components: {EditorChild, ElCascader},
  setup() {
    const value = ref('<h1>test</h1>');
    const selectedOptions = ref([]);
    const options = ref([
      {
        value: 'guide',
        label: 'Guide',
        children: [
          {
            value: 'disciplines',
            label: 'Disciplines',
            children: [
              {
                value: 'consistency',
                label: 'Consistency',
              },
              {
                value: 'feedback',
                label: 'Feedback',
              },
              {
                value: 'efficiency',
                label: 'Efficiency',
              },
              {
                value: 'controllability',
                label: 'Controllability',
              },
            ],
          },
          {
            value: 'navigation',
            label: 'Navigation',
            children: [
              {
                value: 'side nav',
                label: 'Side Navigation',
              },
              {
                value: 'top nav',
                label: 'Top Navigation',
              },
            ],
          },
        ],
      },
      {
        value: 'component',
        label: 'Component',
        children: [
          {
            value: 'basic',
            label: 'Basic',
            children: [
              {
                value: 'layout',
                label: 'Layout',
              },
              {
                value: 'color',
                label: 'Color',
              },
              {
                value: 'typography',
                label: 'Typography',
              },
              {
                value: 'icon',
                label: 'Icon',
              },
              {
                value: 'button',
                label: 'Button',
              },
            ],
          },
          {
            value: 'form',
            label: 'Form',
            children: [
              {
                value: 'radio',
                label: 'Radio',
              },
              {
                value: 'checkbox',
                label: 'Checkbox',
              },
              {
                value: 'input',
                label: 'Input',
              },
              {
                value: 'input-number',
                label: 'InputNumber',
              },
              {
                value: 'select',
                label: 'Select',
              },
              {
                value: 'cascader',
                label: 'Cascader',
              },
              {
                value: 'switch',
                label: 'Switch',
              },
              {
                value: 'slider',
                label: 'Slider',
              },
              {
                value: 'time-picker',
                label: 'TimePicker',
              },
              {
                value: 'date-picker',
                label: 'DatePicker',
              },
              {
                value: 'datetime-picker',
                label: 'DateTimePicker',
              },
              {
                value: 'upload',
                label: 'Upload',
              },
              {
                value: 'rate',
                label: 'Rate',
              },
              {
                value: 'form',
                label: 'Form',
              },
            ],
          },
          {
            value: 'data',
            label: 'Data',
            children: [
              {
                value: 'table',
                label: 'Table',
              },
              {
                value: 'tag',
                label: 'Tag',
              },
              {
                value: 'progress',
                label: 'Progress',
              },
              {
                value: 'tree',
                label: 'Tree',
              },
              {
                value: 'pagination',
                label: 'Pagination',
              },
              {
                value: 'badge',
                label: 'Badge',
              },
            ],
          },
          {
            value: 'notice',
            label: 'Notice',
            children: [
              {
                value: 'alert',
                label: 'Alert',
              },
              {
                value: 'loading',
                label: 'Loading',
              },
              {
                value: 'message',
                label: 'Message',
              },
              {
                value: 'message-box',
                label: 'MessageBox',
              },
              {
                value: 'notification',
                label: 'Notification',
              },
            ],
          },
          {
            value: 'navigation',
            label: 'Navigation',
            children: [
              {
                value: 'menu',
                label: 'Menu',
              },
              {
                value: 'tabs',
                label: 'Tabs',
              },
              {
                value: 'breadcrumb',
                label: 'Breadcrumb',
              },
              {
                value: 'dropdown',
                label: 'Dropdown',
              },
              {
                value: 'steps',
                label: 'Steps',
              },
            ],
          },
          {
            value: 'others',
            label: 'Others',
            children: [
              {
                value: 'dialog',
                label: 'Dialog',
              },
              {
                value: 'tooltip',
                label: 'Tooltip',
              },
              {
                value: 'popover',
                label: 'Popover',
              },
              {
                value: 'card',
                label: 'Card',
              },
              {
                value: 'carousel',
                label: 'Carousel',
              },
              {
                value: 'collapse',
                label: 'Collapse',
              },
            ],
          },
        ],
      },
      {
        value: 'resource',
        label: 'Resource',
        children: [
          {
            value: 'axure',
            label: 'Axure Components',
          },
          {
            value: 'sketch',
            label: 'Sketch Templates',
          },
          {
            value: 'docs',
            label: 'Design Documentation',
          },
        ],
      },
    ])
    const optionsData = ref([
      {
        "value": "edit or Review",
        "label": "Edit or review",
        "children": [
              {"value": "improve writing", "label": "improve writing"},
              { "value": "make shorter", "label": "make shorter" },
              { "value": "simplify language", "label": "simplify language" }
            
        ]
      },
      {
        "value": "generate form selection",
        "label": "Generate form selection",
        "children": [
              {"value": "summarize", "label": "summarize"},
              { "value": "continue", "label": "continue" }
        ]
      },
      {
        "value": "change tone",
        "label": "Change tone",
        "children": [
              {"value": "profesional", "label": "profesional"},
              { "value": "casual", "label": "casual" },
              { "value": "direct", "label": "direct" },
              {"value": "confident", "label": "confident"},
              {"value": "friendly", "label": "friendly"}
            
        ]
      },
      {
        "value": "change style",
        "label": "Change style",
        "children": [
              {"value": "busuness", "label": "busuness"},
              { "value": "legal", "label": "legal" },
              { "value": "journalism", "label": "journalism" }
            
        ]
      },
      {
        "value": "translate",
        "label": "Translate",
        "children": [
            
              { "value": "translate to English", "label": "translate to English" },
              {"value": "translate to Tradionnal Chinese", "label": "translate to Tradionnal Chinese"},
              { "value": "translate to Simplified Chinese", "label": "translate to Simplified Chinese" },
              { "value": "translate to Japanese", "label": "translate to Japanese" }
            
            
        ]
      },
      {
        "value": "change layout",
        "label": "Change layout",
        "children": [
              {"value": "papers", "label": "papers"},
              { "value": "press release", "label": "press release" },
              { "value": "blog", "label": "blog" }
            
        ]
      }
    ])

    // watch
    watch(value, (newValue) => {
      // console.log('parent2::',newValue);
    });
    
    // methods
    const handleChange = (value) => {
      // console.log('Selected options:', value[0], value[1], value[2]);
    };


    const dataFilter = (node, val) => {
      if (!!~node.text.indexof(val) || !!node.text.toUpperCase().indexof(val.toUpperCase())) {
        return true
      }
    };
    // const dataFilter = (node, query) => {
    //   // console.log('::', node.label);
    //   const label = node.label.toLowerCase();
    //   // console.log('label', label);
    //   return label.includes(query.toLowerCase());
    // };

    // Filter options recursively
    const filterOptions = (options, query) => {
      return options.filter((node) => {
        const labelMatch = dataFilter(node, query);
        const childMatch = node.children && filterOptions(node.children, query).length > 0;
        return labelMatch || childMatch;
      });
    };
    
    
    // computed
    const filteredOptions = computed(() => {
      const searchQuery = ''; // Get the search query from the input field
      const filteredNodes = filterOptions(options.value, searchQuery);
      return filteredNodes;
    });

    return {
      value, options, selectedOptions, handleChange, dataFilter, filteredOptions, optionsData
    }
  }
});

</script>

<template>
  <div class="q-pt-lg q-px-lg">
    <div class="q-mb-xl">
      <!-- {{ selectedOptions }} -->
      <ElCascader
        v-model="selectedOptions"
        :options="optionsData"
        @change="handleChange"
        placeholder="Please select"
      ></ElCascader>
    </div>
    <EditorChild v-model="value" :editorId="'gpt_editor'" />
  </div>
</template>