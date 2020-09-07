import {CREATE_MESSAGE} from './types' ;

//CREATE_MASSAGE
export const createMessage = msg => {
  return {
    type: CREATE_MESSAGE,
    payload: msg
  };
};
