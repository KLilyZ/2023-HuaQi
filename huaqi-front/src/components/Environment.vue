<template>
  <div :style="{'--color':color}">
    <h1 id="score">{{shorthand}}:&nbsp;{{score}}</h1>
  </div>

  <h1> This is {{species}}</h1>
  <div id="flex">
    <ul id="list">
    <li v-for="(value,name,index) in details" :key="value">
      {{index}} {{name}} {{value}}
    </li>
  </ul>
    <div id="echart" class="center"
           style="width : 50%;height : 300px"></div>
  </div>


</template>

<script>
import * as echarts from "echarts";
import axios from "axios";

export default {
  name: "Environment",
   data(){
    return{
      companyName:'kl超聪明',
      score:0.0,
      species:'',
      shorthand:'',
      color:'red',
      details:{name:'排放',value:'污染'}
    }
    },
  created() {
    this.getInformation();
    //获取指定数据数据
      axios.get('/detail/'+this.companyName+'/'+this.species,
          {'name':this.companyName,'species':this.species}).// detail是后端的url
      then(response=>{
        this.details = response['details'];
        console.log("已从后端拉取数据")
      }).catch(error=>{
        console.log(error)
      })
  },
  mounted(){
      var myChart = echarts.init(document.getElementById('echart'));
        // 绘制图表
      var option = {
        title: {
          text: 'ECharts 入门示例'
        },
        tooltip: {},
        legend: {
          data: ['销量']
        },
        xAxis: {
          data: ['衬衫', '羊毛衫', '雪纺衫', '裤子', '高跟鞋', '袜子']
        },
        yAxis: {},
        series: [
          {
            name: '销量',
            type: 'bar',
            data: [5, 20, 36, 10, 10, 20]
          }
        ]
      };

      // 使用刚指定的配置项和数据显示图表。
      myChart.setOption(option);

    },
  methods:{
    getInformation(){
       this.companyName = this.$route.params.name;   // 此处非router
       this.species = this.$route.params.species;
       if(this.species==='Environment')
       {
         this.shorthand='E';
         this.color='#67C23A';
       }     else if(this.species==='Social') {
         this.shorthand='S';
         this.color='blue';
       } else {
         this.shorthand='G';
         this.color='pink';
       }
    },
  }
}
</script>

<style scoped>
  #score{
    /*color:#67C23A;*/
    font:900 100px/100px "Times New Roman";
    color:var(--color) !important;
  }
  /*#echart{*/
  /*  margin-left: 600px;*/
  /*  margin-right: 20px;*/
  /*}*/
  #list{
     margin-left: 20px;
  }
  #flex{
    display: flex;
    /*display: inline-block;*/
    align-items: baseline;
  }
</style>