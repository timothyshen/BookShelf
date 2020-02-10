import axios from 'axios';

let host = 'http://127.0.0.1:8000';

export const login = (params, config) => {
    return axios.post(`${host}/user`, params, config)
}


export const login_one = parmas => {
    return axios.post(`${host}/login/`, parmas)
}

export const getUserDetail = () => {
    return axios.get(`${host}/profile/1/`)
}

export const updateUserInfo = params => {
    return axios.patch(`${host}/profile/1/`, params)
}
