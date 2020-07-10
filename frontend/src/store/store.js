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
  user_id: cookie.getCookie('user_id'),
  name:cookie.getCookie('name'),
  token:cookie.getCookie('token'),
  role:cookie.getCookie('role')
};
const navItem = {
  collapsed: false,
  topNavState: 'author',
  leftNavState: 'author'
};
const token = {
  jwt: localStorage.getItem('token'),
  refreshJWT: 'http://127.0.0.1:8000/api/token/update/'
};
const bookcase = {
  book_list:[]
}


for(let item in navItem){
  localStorage.getItem(item) ? navItem[item] = JSON.parse(localStorage.getItem(item)) : false;
}


const state = {
  userInfo,
  navItem,
  token,
  bookcase
};
const store = new Vuex.Store({
  state,
  mutations,
  actions,
  getters
});

export default store;
