import axios from 'axios';

import store from "../store/store";

//http request blocker
axios.interceptors.request.use(
  config => {
    if (store.state.userInfo.token){
      config.headers.Authorization = `JWT ${store.state.userInfo.token}`;
    }
    return config;
  },
  err => {
    return Promise.reject(err)
  }
);


//http response blocker
axios.interceptors.response.use(
  undefined,
  error => {
    let error_res = error.response;
    switch(error_res.status){
      case 401:
        console.log('Not logged in');
      case 403:
        console.log('Not authorised');
        this.$store.dispatch('inspectToken').then(r => console.log(r));
      case 500:
        console.log('Server error');
    }
    return Promise.reject(error.response.data)
  }
)
