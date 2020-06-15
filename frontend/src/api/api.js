import axios from 'axios';
import store from "../store/store";
import id from "element-ui/src/locale/lang/id";

let host = 'http://127.0.0.1:8000';


//user related api
export const register = (params) => {
    return axios.post(`${host}/user`, params, {headers:{
    'Content-type':'multipart/form-data',
  }})
};

export const getUserDetail = (id) => {
  return axios.get(`${host}/user/${id}`)
};
export const updateUserDetail = (id, params) => {
  return axios.patch(`${host}/user/${id}`, params, {headers:{
      'Content-type':'multipart/form-data',
    }})
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
};
export const registerAuthorBook = (params) => {
  return axios.post(`${host}/create/`, params)
};
export const getAuthorBookItem = (id) => {
  return axios.get(`${host}/create/${id}/`)
};
export const updateAuthorBookItem = (id, params) => {
  return axios.patch(`${host}/create/${id}/`, params)
};
export const deleteAuthorBookItem = (id) => {
  return axios.delete(`${host}/create/${id}/`)
};

export const getBookCategory = () =>{
  return axios.get(`${host}/book/all-category`)
}


export const listChapterForBook = (id) => {
  return axios.get(`${host}/create/${id}/chapter/`)
};
export const createChapterForBook = (id, params) => {
  return axios.post(`${host}/create/${id}/chapter/`, params)
};
export const getChapterItemForBook = (book_id,id) => {
  return axios.get(`${host}/create/${book_id}/chapter/${id}/`)
};

export const updateChapterItemForBook = (id, chapter_id,params) => {
  return axios.patch(`${host}/create/${id}/chapter/${chapter_id}/`, params)
};
export const deleteChapterItemForBook = (id, chapter_id) => {
  return axios.delete(`${host}/create/${id}/chapter/${chapter_id}/`)
};

//Home page render

export const rankingBoardBooks = (variableName) =>{
  return axios.get(`${host}/book/${variableName}`)
};
export const indexLinkRender = () =>{
  return axios.get(`${host}/index_link`)
};
export const indexImageRender = () => {
  return axios.get(`${host}/index_image`)
};

//book detail page

export const getBookItemView = (book_id) => {
  return axios.get(`${host}/book/detail/${book_id}`)
};
