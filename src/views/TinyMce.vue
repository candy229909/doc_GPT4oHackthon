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


    const dataFilter = (node, query) => {
      // console.log('::', node.label);
      const label = node.label.toLowerCase();
      // console.log('label', label);
      return label.includes(query.toLowerCase());
    };

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
      value, selectedOptions, handleChange, dataFilter, filteredOptions, optionsData
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