const initialState = {
  token: localStorage.getItem('token'),
  IsAuthenticated: null,
  isLoading: false,
  user: null
}

export default function(state = initialState, action){
  switch(action.type){
    default:
      return state;
  }
}
