/**
 * 时间：2020/11/20
 * Created by dingwangjun on
 * 说明：消息
 */
import { ElNotification, ElMessage,ElMessageBox } from 'element-plus'
/**
 * 如何调用，如下面调用案例
 * import {succesMsg,warnMsg,infoMsg,
     errorMsg,alertBox,confirmBox} from '@/utils/msgBox.ts'

  confirmBox('确认删除该标签吗？','确定',null).then(res => {
    alert("确定："+res)
  }).catch(res => {
    alert("取消关闭："+res)
  })
 * */
// 成功提示信息
export function succesMsg(msgInfo){
  ElMessage({
    type: 'success',
    showClose: true,
    dangerouslyUseHTMLString: true,
    message: msgInfo,
  })
}

// 警告提示信息
export function warnMsg(msgInfo){
  ElMessage({
    type: 'warning',
    showClose: true,
    dangerouslyUseHTMLString: true,
    message: msgInfo,
  })
}

// 错误提示信息
export function errorMsg(msgInfo){
  ElMessage({
    type: 'error',
    showClose: true,
    dangerouslyUseHTMLString: true,
    message: msgInfo,
  })
}

// 一般信息提示信息
export function infoMsg(msgInfo){
  ElMessage({
    type: 'info',
    showClose: true,
    dangerouslyUseHTMLString: true,
    message: msgInfo,
  })
}

// 确定一个确定按钮alertBox
export function alertBox(msg,btnName,type) {
  let confirmName = btnName == '确定'? '确定' : '是'
  return ElMessageBox.alert(msg, '提示',{
    type: type,
    confirmButtonText: confirmName,
    dangerouslyUseHTMLString: true
  });
}

// 确定取消;是否按钮弹出框
export function confirmBox(msg,btnName,type) {
  let confirmName = btnName == '确定'? '确定' : '是'
  let cancelsName = btnName == '确定'? '取消' : '否'
  return ElMessageBox.confirm(msg,'提示', {
    type: type,
    confirmButtonText: confirmName,
    cancelButtonText: cancelsName,
    closeOnClickModal: false,
    closeOnPressEscape: false,
    dangerouslyUseHTMLString: true
  })
}


