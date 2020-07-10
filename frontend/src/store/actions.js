import * as types from './mutation-types';
import axios from 'axios'
import * as JWT from 'jwt-decode';

function makeAction(type) {
  return ({commit}, ...args) => commit(type, ...args)
}
export const refreshToken = () => {
  const payload = {
    token: this._state.token.jwt
  };
  axios.post(this.state.token.refreshJWT, payload)
    .then((response) => {
      console.log('hi');
      this.commit('updateToken', response.data.token)
    })
    .catch((error) => {
      console.log(error)
    })
}
export const inspectToken = () => {
  const token = this.state.token.jwt;
  if (token) {
    const decoded = JWT(token);
    const {exp, orig_iat} = decoded;
    const seven_days = 604800; // 7*24*60*60
    const thirty_minutes = 1800; // 30*60

    if ((Date.now() / 1000) > exp) {
      this.$route.push('login')
    } else if ((Date.now() / 1000) > exp - thirty_minutes && (Date.now() / 1000) < orig_iat + seven_days) {
      // IF TOKEN EXPIRE IN LESS THAN 30MN BUT STILL IN REFRESH PERIOD THEN REFRESH
      this.dispatch('refreshToken');
      this.$router.go(0)
    }
  } else {
    // NO TOKEN THEN SEND TO LOGIN PAGE
    this.$route.push('login')
  }
}

export const setInfo = makeAction(types.SET_INFO);
export const setBookcase = makeAction(types.SET_BOOKCASE);


