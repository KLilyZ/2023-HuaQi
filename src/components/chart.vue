<template>
  <div id="all">
    <h1>
    <!--    此处为图表界面&nbsp;-->
    {{ companyName }}
  </h1>
<!--  <p id="tips">Tips:可点击图表相应区域，查看该项详细情况</p>-->
  <div>
    <div id="echart" class="center"
         style="width : 80%;height : 360px">
    </div>
    <p id="tips">Tips:可点击图表相应区域，查看该项详细情况</p>
  </div>
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
        text: this.companyName + '的ESG评分',
        // subtext:"Tips:可点击图表相应区域，查看该项详细情况",
        textStyle: {
          'fontSize': 28,
          'fontFamily':" sans-serif",
          // 'color':'#ffe'
          // 'fontWeight': '500',
          'color': '#fff'
        },
      },
      tooltip: {},
      series: [{
        type: 'pie',
        data: [],
      }]
    });
    axios.get('/detail/' + this.$data.companyName + '/',
                  {'name': this.$data.companyName,
                    'code':this.$route.params.code
                  }
    ).// detail是后端的url
        then(response => {
          this.value = response.data['value'];
          console.log("responce:" + response.data['value'])
          myChart.setOption({
            // tooltip: {
            //   trigger: 'item', formatter: "{a} <br/>{b} : {c} ({d}%)"
            // },
            series: [{
              itemStyle: {
                normal: {
                  label: {
                    show: true,
                    formatter: '{b} : {c} ({d}%)'
                  },
                  labelLine: {show: true},
                  borderWidth: 1,
                  shadowBlur: 9, // 图形阴影的模糊大小。该属性配合 shadowColor,shadowOffsetX, shadowOffsetY 一起设置图形的阴影效果
                  shadowOffsetX: 4, // 阴影水平方向上的偏移距离
                  shadowOffsetY: 4,
                  shadowColor: '#888888' // 阴影颜色
                }
              },
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
              ],
              label: {
                "normal": {
                  "show": true,
                  "textStyle": {
                    "fontSize": 18,
                    color: 'white',
                  }
                },
              }
            }
            ]
          })
          myChart.setOption(option)
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
h1 {
  font-size: 64px;
  font-family: sans-serif, 黑体;
  /*color:black*/
}

#tips{
  text-align: right;
  margin-right: 30px;
  margin-top: 0;
  /*color: whitesmoke;*/
}
#echart{
  margin: auto;
  width: 60%;
  /*border: 3px solid #73AD21;*/
  padding: 10px;
  border-radius: 10px; /* 设置输入框的圆角 */
  box-shadow: 2px 2px 5px #888888; /* 设置输入框的阴影 */
  /*background: rgb(252,250,237);*/
  /*background-image: linear-gradient(25deg, #71a5be, #8fa7a8, #a6aa92, #b9ac7b);*/
 background-image: linear-gradient(25deg, #152e3c, #4e616a, #89999c, #c8d5d1)
}

.center {
  margin: auto;
  width: 60%;
  /*border: 3px solid #73AD21;*/
  padding: 10px;
}


</style>
