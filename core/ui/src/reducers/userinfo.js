import { GET_USERINFO } from '../actions/types.js';

const initialState = {
    userinfo: [],
}

export default function(state = initialState, action) {
    switch(action.type) {
        case GET_USERINFO:
            return {
                ...state,
                userinfo: action.payload,
            }
        default: return state;
    }
}
