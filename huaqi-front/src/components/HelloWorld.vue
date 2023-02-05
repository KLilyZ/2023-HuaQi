<template>
  <div class="hello">
   <h1>ESG</h1>
    <p>
      公司名称:&nbsp; <input placeholder="请输入公司名称" @keyup.enter="submit" v-model="companyName">
    </p>

  </div>
</template>

<script>
export default {
  data(){
    return{
      companyName:null
    }
  },
  methods:{
    submit(){
      console.log(this.companyName)
      if(this.companyName!=null){
           alert("已成功提交公司名称")
      } else {
        alert("请输入名称后再提交")
      }

    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  h1{
    font-family: 楷体,sans-serif;
    font-size: 100px;
    margin-top:3px;
    margin-bottom:15px;
  }
  p{
    font-size: 15px;
  }

</style>
