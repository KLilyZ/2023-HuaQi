import request from "@/utils/request";

export function getCompanyScore(companyName) {
  return request({
    url: '/detail/'+companyName+'/',
    method: 'get',
  })
}

export function postCompanyName(data) {
    return request({
    url:'/#/',
    method: 'post',
    data
})
}