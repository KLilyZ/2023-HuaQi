import axios from 'axios'
// import {config} from "shelljs";
// // var URL = ''  // 发布的url
// // var URL = 'http://10.193.0.22:8010/api/'
 var URL = 'http://localhost:8000/#/'  // localUrl

// 创建axios实例
const service = axios.create({
  baseUrl:URL,
    timeout: 6000,  // 请求超时时间
  withCredentials: true,
})
export default service