import * as types from './mutation-types';

function makeAction(type){
  return ({commit}, ...args) => commit (type, ...args)
}

export const setInfo =  makeAction(types.SET_INFO);
