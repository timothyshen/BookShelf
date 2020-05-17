import axios from 'axios';
import store from "../store/store";
import id from "element-ui/src/locale/lang/id";

let host = 'http://127.0.0.1:8000';


//user related api
export const register = (params) => {
    return axios.post(`${host}/user`, params)
};

export const getUserDetail = (id) => {
  return axios.get(`${host}/user/${id}`)
};

export const login = params => {
    return axios.post(`${host}/api/token/`, params)
};


//bookshelves related api
export const getBookShelves = () => {
  return axios.get(`${host}/bookcase/`,)
};

export const deleteBook = (bookId) =>{
  return axios.delete(`${host}/bookcase/`+bookId+`/`)
};


//book related api
export const getAuthorBook = () => {
  return axios.get(`${host}/create/`,)
}

export const registerAuthorBook = (params) => {
  return axios.post(`${host}/create/`, params)
};
export const getChapterForBook = (id) => {
  return axios.get(`${host}/create/${id}/chapter`)
};
export const createChapterForBook = (id, params) => {
  return axios.post(`${host}/create/${id}/chapter`, params)
};
