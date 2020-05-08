import axios from 'axios';

import store from "../store/store";

//http request blocker
axios.interceptors.request.use(
  config => {
    if (store.state.userInfo.token){
      console.log(store.state.userInfo.token);
      let token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyNSwidXNlcm5hbWUiOiJzaGVuMTIzIiwiZXhwIjoxNTg4MTY2Nzg0LCJlbWFpbCI6InRpbUBzaGVuLmNvbSJ9.BM_EhCM7hGEgr3n9N86bYTGMXOTp2mcGoGzku3zUnu8\n'
      config.headers.Authorization = `JWT ${token}`;
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
      case 500:
        console.log('Server error');
    }
    return Promise.reject(error.response.data)
  }
)
