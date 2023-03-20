<template>
  <img alt="Vue logo" src="../assets/logo.png">
  <div class="hello">
    <h1>ESG</h1>
    <p>
      公司名称:&nbsp; <input placeholder="请输入公司名称" @keyup.enter="submit" v-model="companyName">
    </p>

  </div>
</template>

<script>
import axios from "axios";
import {
  succesMsg, warnMsg, infoMsg,
  errorMsg, alertBox, confirmBox
} from '@/utils/msgBox'
import Message from '@/components/message'

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
        this.$message({type: 'success', text: '已成功提交公司名称'})
        axios.post('/detail/' + this.$data.companyName + '/', {'name': this.$data.companyName}).// detail是后端的url
            then(response => {
              console.log("已提交到后端")
            }).catch(error => {
          console.log(error)
        })
         this.$router.push({name: 'detail', params: {name: this.companyName}});
        //alert("已成功提交公司名称")
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
  font-size: 15px;
}

</style>
