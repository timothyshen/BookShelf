import axios from 'axios';

let host = 'http://127.0.0.1:8000';

export const register = (params) => {
    return axios.post(`${host}/all-profiles`, params)
};


export const login = params => {
    return axios.post(`${host}/login/`, params)
};

export const getUserDetail = () => {
    return axios.get(`${host}/profile/1/`)
};

export const updateUserInfo = params => {
    return axios.patch(`${host}/profile/1/`, params)
};
