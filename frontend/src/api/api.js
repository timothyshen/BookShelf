import axios from 'axios';

let host = 'http://127.0.0.1:8000';

export const register = (params) => {
    return axios.post(`${host}/user`, params)
};

export const getUserDetail = (params) => {
  return axios.get(`${host}/user/`, params)
};

export const login = params => {
    return axios.post(`${host}/login/`, params)
};


