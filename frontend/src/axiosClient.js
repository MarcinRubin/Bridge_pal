import axios from "axios";

// const csrftoken = Cookies.get('csrftoken');
// axios.defaults.xsrfCookieName = "csrftoken";
// axios.defaults.headers.common['X-CSRFTOKEN'] = csrftoken; 
// axios.defaults.xsrfHeaderName = "X-CSRFToken";
//axios.defaults.withCredentials = false;

export const client = axios.create({
  baseURL: "http://localhost:8000/api/",
});



