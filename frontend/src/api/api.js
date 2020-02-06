import axios from 'axios';

let host = 'http://127.0.0.1:8000';

export const login = params => {
    return axios.post(`${host}/profile/`, params)
}


// export const register = parmas => {
//     return axios.post(`${host}/register/`, parmas)
// }

export const getUserDetail = () => {
    return axios.get(`${host}/profile/1/`)
}

export const updateUserInfo = params => {
    return axios.patch(`${host}/profile/1/`, params)
}
