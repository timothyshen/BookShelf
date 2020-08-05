import axios from 'axios';

let host = 'http://127.0.0.1:8000';


//user related api
export const register = (params) => {
  return axios.post(`${host}/user`, params, {
    headers: {
      'Content-type': 'multipart/form-data',
    }
  })
};

export const getUserDetail = (id) => {
  return axios.get(`${host}/user/${id}`)
};
export const updateUserDetail = (id, params) => {
  return axios.patch(`${host}/user/${id}`, params)
};


export const login = params => {
  return axios.post(`${host}/api/token/`, params)
};


//bookshelves related api
export const getBookShelves = () => {
  return axios.get(`${host}/bookcase/`,)
};
export const getBookItemShelves = (bookId) => {
  return axios.get(`${host}/bookcase/${bookId}`)
};
export const addBookToShelve = (params) => {
  return axios.post(`${host}/bookcase/`, params)
}

export const deleteBook = (bookId) => {
  return axios.delete(`${host}/bookcase/${bookId}/`)
};
export const addBookMark = (params) => {
  return axios.post(`${host}/bookmark/`, params)
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

export const getBookCategory = () => {
  return axios.get(`${host}/book/all-category`)
};


export const listChapterForBook = (id) => {
  return axios.get(`${host}/create/${id}/chapter/`)
};
export const createChapterForBook = (id, params) => {
  return axios.post(`${host}/create/${id}/chapter/`, params)
};
export const getChapterItemForBook = (book_id, id) => {
  return axios.get(`${host}/create/${book_id}/chapter/${id}/`)
};

export const updateChapterItemForBook = (id, chapter_id, params) => {
  return axios.patch(`${host}/create/${id}/chapter/${chapter_id}/`, params)
};
export const deleteChapterItemForBook = (id, chapter_id) => {
  return axios.delete(`${host}/create/${id}/chapter/${chapter_id}/`)
};

//Home page render

export const rankingBoardBooks = (variableName) => {
  return axios.get(`${host}/book/${variableName}`)
};
export const CateRankingBoardBooks = (variableName, variableTwo) => {
  return axios.get(`${host}/book/${variableName}/${variableTwo}`)
};
export const indexLinkRender = () => {
  return axios.get(`${host}/index_link`)
};
export const indexImageRender = () => {
  return axios.get(`${host}/index_image`)
};

export const categoryBookRender = (typeName) =>{
  return axios.get(`${host}/category_page/${typeName}`)
};

export const categoryImageRender = (typeName) => {
  return axios.get(`${host}/category_image/${typeName}`)
};

//book detail page
export const getChapterList = (book_id) =>{
  return axios.get(`${host}/book/chapter/${book_id}`)
}
export const getChapterItem = (book_id, chapter_id) =>{
  return axios.get(`${host}/book/chapter/${book_id}/${chapter_id}`)
}
export const getBookItemView = (book_id) => {
  return axios.get(`${host}/book/detail/${book_id}`)
};

//user comment related

export const getUserCommentForBook = (book_id) =>{
  return axios.get(`${host}/comment/${book_id}`)
};

export const postUserCommentForBook = (book_id, params) =>{
  return axios.post(`${host}/comment/${book_id}`, params)
};

export const getUserCommentForUser = () =>{
  return axios.get(`${host}/comment/user/`)
};

export const updateUserCommentForBook = (comment_id) =>{
  return axios.put(`${host}/comment/user/${comment_id}/`)
};

export const getUserCommentForAuthor = (book_id) =>{
  return axios.get(`${host}/comment/book/${book_id}`)
};

