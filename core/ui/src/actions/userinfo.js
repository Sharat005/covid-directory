import axios from 'axios';
import { createMessage, returnErrors } from './messages';
// import { tokenConfig } from './auth';

import { GET_USERINFO, DELETE_USERINFO, ADD_USERINFO } from './types';

// GET Userinfo
export const getUserinfo = () => (dispatch, getState) => {
  axios
    .get('/api/patientinfo/')
    .then((res) => {
      dispatch({
        type: GET_USERINFO,
        payload: res.data,
      });
    })
    .catch((err) => dispatch(returnErrors(err.response.data, err.response.status)));
};

// DELETE Userinfo
export const deleteUserinfo = (id) => (dispatch, getState) => {
  axios
    .delete(`/api/patientinfo/${id}/`)
    .then((res) => {
      dispatch(createMessage({ deleteUserinfo: 'UserInfo Deleted' }));
      dispatch({
        type: DELETE_USERINFO,
        payload: id,
      });
    })
    .catch((err) => console.log(err));
};

// ADD Userinfo
export const addUserinfo = (userinfo) => (dispatch, getState) => {
  axios
    .post('/api/patientinfo/', userinfo)
    .then((res) => {
      dispatch(createMessage({ addUserinfo: 'UserInfo Added' }));
      dispatch({
        type: ADD_USERINFO,
        payload: res.data,
      });
    })
    .catch((err) => dispatch(returnErrors(err.response.data, err.response.status)));
};

