import cookie from "../static/cookie/cookie";
import * as types from './mutation-types';
import token from './store'
import Vue from 'vue';
import Axios from "axios";
Vue.prototype.$http = Axios;

export default {
  [types.SET_INFO](state){
    state.userInfo = {
      user_id: cookie.getCookie('user_id'),
      name:cookie.getCookie('name'),
      token:cookie.getCookie('token'),
      role:cookie.getCookie('role')
    };
    console.log(state.userInfo)
  },
  updateToken(state, newToken) {
    localStorage.setItem('token', newToken);
    this.state.token.jwt = newToken;
  },
  removeToken(state) {
    localStorage.removeItem('token');
    this.state.token.jwt = null;
  }
}

