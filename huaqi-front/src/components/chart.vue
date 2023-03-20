<template>
  <h1>
    此处为图表界面&nbsp;
    公司名称:{{ companyName }}
  </h1>
  <div>
    <div id="echart" class="center"
         style="width : 80%;height : 300px"></div>
  </div>
</template>

<script>
import * as echarts from 'echarts';
import axios from "axios";

export default {
  name: "chart",
  data() {
    return {
      value: [],
      companyName: null
    }
  },
  created() {
    this.getid();
  },
  mounted() {
    console.log("in mount" + this.value);
    var myChart = echarts.init(document.getElementById('echart'));
    // 绘制图表
    myChart.setOption({
      title: {
        text: this.companyName + '的ESG评分'
      },
      tooltip: {},
      series: [{
        type: 'pie',
        data: [],
      }]
    });
    axios.get('/detail/' + this.$data.companyName + '/', {'name': this.$data.companyName}).// detail是后端的url
        then(response => {
          this.value = response.data['value'];
          console.log("responce:" + response.data['value'])
          myChart.setOption({
            series: [{
              type: 'pie',
              data: [{
                value: this.$data.value[0],
                name: 'E-环境'
              },
                {
                  name: 'S-社会',
                  value: this.value[1]
                },
                {
                  name: 'G-公司治理',
                  value: this.value[2]
                },
              ]
            }
            ]
          })
          console.log(this.value)
        }).catch(error => {
      console.log(error)
    })

    //匿名函数
    myChart.on("click", (params) => {
      //要变成箭头函数，才读得到this里的内容，否则this读到的是echart
      console.log(params);
      if (params.name === "E-环境") {
        this.$router.push({name: 'species', params: {name: this.companyName, species: 'Environment'}});
        //window.location.href = "#/detail/"+this.companyName+"/Environment";
      } else if (params.name === "S-社会") {
        this.$router.push({name: 'species', params: {name: this.companyName, species: 'Social'}});
        //window.location.href = "#/detail/"+this.companyName+"/Environment";
      } else if (params.name === "G-公司治理") {
        this.$router.push({name: 'species', params: {name: this.companyName, species: 'Governance'}});
        //window.location.href = "#/detail/"+this.companyName+"/Environment";
      }
    });

  },
  methods: {
    getid() {
      this.companyName = this.$route.params.name   // 此处非router
    },
  }
}

</script>

<style scoped>
.center {
  margin: auto;
  width: 60%;
  border: 3px solid #73AD21;
  padding: 10px;
}

</style>
