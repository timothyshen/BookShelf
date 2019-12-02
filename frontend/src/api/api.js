import axios from 'axios';

let host = 'http://127.0.0.1:8000';

export const login = params => {
    return axios.post(`${host}/login/`, params)
}


export const register = parmas => {
    return axios.post(`${host}/users/`, parmas)
}

export const getUserDetail = () => {
    return axios.get(`${host}/users/1/`)
}

export const updateUserInfo = params => {
    return axios.patch(`${host}/users/1/`, params)
}