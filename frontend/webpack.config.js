const AssetConfigWebpackPlugin = require('asset-config-webpack-plugin');
const JsConfigWebpackPlugin = require('js-config-webpack-plugin');
const ScssConfigWebpackPlugin = require('scss-config-webpack-plugin');

module.exports = {
  plugins: [
    // File loader configuration for .woff and .woff2 files
    // File loader configuration for .gif .jpg .jpeg .png and .svg files
    // https://github.com/namics/webpack-config-plugins/tree/master/packages/asset-config-webpack-plugin
    new AssetConfigWebpackPlugin(),
    // Multi threading babel loader configuration with caching for .js and .jsx files
    // see https://github.com/namics/webpack-config-plugins/tree/master/packages/js-config-webpack-plugin/config
    new JsConfigWebpackPlugin(),
    // SCSS Configuration for .css .module.css and .scss .module.scss files
    // see https://github.com/namics/webpack-config-plugins/tree/master/packages/scss-config-webpack-plugin/config
    new ScssConfigWebpackPlugin(),
  ],
};
