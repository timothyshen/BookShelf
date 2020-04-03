var path = require('path');
var webpack = require('webpack');

module.exports = {
  entry: './js/main.js',
  output: {
    path: path.resolve(__dirname, 'build'),
    filename: 'main.bundle.js'
  },
  module: {
    loaders: [
      {
        test: /\.js$/,
        loader: 'babel-loader',
        query: {
          presets: ['es2015']
        }
      },
      {
        test: /\\.css$/,
        loader: "style!css"
      },
      {
        test: /\\.(eot|woff|woff2|ttf)([\\?]?.*)$/,
        loader: "file"
      },
      {
        test: /\.less$/,
        loader: "style-loader!css-loader!less-loader",
      },
    ]
  },
  stats: {
    colors: true
  },
  devtool: 'source-map'
};
