import axios from 'axios';
import store from "../store/store";

let host = 'http://127.0.0.1:8000';
let token = store.state.userInfo.token;

export const register = (params) => {
    return axios.post(`${host}/user`, params)
};

export const getUserDetail = (id) => {
  return axios.get(`${host}/user/${id}`)
};

export const login = params => {
    return axios.post(`${host}/api/token/`, params)
};

export const getBookShelves = () => {
  return axios.get(`${host}/bookcase/`,)
};

export const deleteBook = (bookid) =>{
  return axios.delete(`${host}/bookcase/`+bookid+`/`)
}
