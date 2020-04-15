import cookie from "../static/cookie/cookie";
import * as types from './mutation-types';
import Vue from 'vue';
import Axios from "axios";
Vue.prototype.$http = Axios;

export default {
  [types.SET_INFO](state){
    state.userInfo = {
      name: cookie.getCookie('name'),
      token: cookie.getCookie('token'),
      ole:cookie.getCookie('role')
    };
    console.log(state.userInfo)
  }
}
