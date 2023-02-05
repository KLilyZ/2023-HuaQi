import request from '@/utils/request'
// 封装请求的方式

// 传递公司名称
export function getCompanyName(data) {
  return request({
    url: '/companyName/',
    method: 'post',
      data
  })
}
