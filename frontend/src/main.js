// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import locale from 'element-ui/lib/locale/lang/en';
import Vuex from 'vuex'
import {library} from '@fortawesome/fontawesome-svg-core'
import {FontAwesomeIcon, FontAwesomeLayers, FontAwesomeLayersText} from '@fortawesome/vue-fontawesome'
import {faSpinner} from '@fortawesome/free-solid-svg-icons'
import {faFacebook, faInstagram, faTwitterSquare} from '@fortawesome/free-brands-svg-icons'
import store from "./store/store";
import '@/assets/css/style.css'
import './axios/';
import axios from 'axios';
import Component from 'vue-class-component';

Vue.prototype.$http = axios;
Vue.config.productionTip = false;
Vue.use(ElementUI, {locale});
Vue.use(Vuex);
Vue.component('font-awesome-icon', FontAwesomeIcon);
Vue.component('font-awesome-layers', FontAwesomeLayers);
Vue.component('font-awesome-layers-text', FontAwesomeLayersText);

library.add(faTwitterSquare, faFacebook, faInstagram);
library.add(faSpinner);

Component.registerHooks([
  'beforeRouteEnter',
  'beforeRouteLeave',
  'beforeRouteUpdate'
]);
/* eslint-disable no-new */



new Vue({
  el: '#app',
  router,
  store,
  components: {App, FontAwesomeIcon},
  template: '<App/>'
});
