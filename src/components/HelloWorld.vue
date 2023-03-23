<template>
  <div class="begin">
    <img alt="Vue logo" src="../assets/logo.png">
    <div class="hello">
      <h1>ESG</h1>
      <p>
        公司名称:&nbsp; <input id="input" placeholder="   请输入" @keyup.enter="submit" v-model="companyName">
      </p>
    </div>
  </div>

</template>

<script >
import axios from "axios";
import {
  succesMsg, warnMsg, infoMsg,
  errorMsg, alertBox, confirmBox
} from '@/utils/msgBox'
import {ElMessage, ElMessageBox} from "element-plus"
import 'element-plus/dist/index.css'


export default {
  data() {
    return {
      companyName: null
    }
  },
  methods: {
    submit() {
      console.log(this.$data.companyName)
      //postCompanyName({companyName:this.companyName});
      if (this.companyName != null) {
        //succesMsg('已成功提交公司名称')
        axios.post('/detail/' + this.$data.companyName + '/', {'name': this.$data.companyName}).// detail是后端的url
            then(response => {
              console.log(response)
              if (response.data['name'] === '已成功接受') {
                console.log("已提交到后端")
                 // this.$message({type: 'success', text: '已成功提交公司名称\n'+'股票代码为 '+response.data['code']})
                 // this.$router.push({name: 'detail', params: {name: this.companyName}});
                ElMessageBox.confirm(
                    '是否选择查询公司'+this.companyName+'\n对应股票代码为：'+response.data['code'],
                    '提示',
                    {
                      confirmButtonText: '确认',
                      cancelButtonText: '取消',
                      type: 'warning',
                    }
                )
                    .then(() => {
                      ElMessage({
                        type: 'success',
                        message: '已成功提交公司名称',
                      })
                      this.$router.push({name: 'detail', params: {name: this.companyName,code:response.data['code']}});
                    })
                    .catch(() => {
                      ElMessage({
                        type: 'info',
                        message: '已取消查询',
                      })
                    })

              } else {
                this.$message({type: 'error', text: '无该公司信息，请检查后再提交'})
              }
            }).catch(error => {
          console.log(error)
        })
      } else {
        this.$message({type: 'error', text: '请输入名称后再提交'})
      }
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1 {
  font-family: 楷体, sans-serif;
  font-size: 100px;
  margin-top: 3px;
  margin-bottom: 15px;
}

p {
  font-size: 18px;
  /*color: whitesmoke;*/
}

#input {
  background: transparent;
  padding: 10px;
  /*text-align: center;*/
  font-size: 15px;
  width: 300px;
  height: 20px;
  border: 1px solid #ccc;
  outline: none;
  border-radius: 10px; /* 设置输入框的圆角 */
  box-shadow: 2px 2px 5px #888888; /* 设置输入框的阴影 */
  color: whitesmoke;
}

/*input[type="text"], input[type="password"], textarea {*/
/*  color: whitesmoke !important;*/
/*}*/
#input:focus {
  border-color: black;
}

/*border: white;*/


/* 设置提示字颜色和大小 */
::placeholder {
  /*color: #ffffff;*/
  font-size: 14px;
  font-family: sans-serif;
  /*text-align: center;*/
}

</style>
