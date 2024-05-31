const { defineConfig } = require("@vue/cli-service");
module.exports = defineConfig({
  lintOnSave: false,

  pluginOptions: {
    quasar: {
      importStrategy: "kebab",
      rtlSupport: false,
    },
  },

  transpileDependencies: ["quasar"],
});
