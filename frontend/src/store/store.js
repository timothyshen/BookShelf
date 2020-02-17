//adding vue
import Vue from 'vue'
//implement vuex
import Vuex from 'vuex';
import cookie from "../static/cookie/cookie";
import mutations from "./mutations";
import * as actions from './actions';
import * as getters from './getters';

Vue.use(Vuex);

const userInfo = {
  name:cookie.getCookie('name'),
  token:cookie.getCookie('token')
};

const state = {
  userInfo
};
const store = new Vuex.Store({
  state,
  mutations,
  actions,
  getters
});

