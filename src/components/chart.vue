<template>
  <div id="all">
    <h1>
      <!--    此处为图表界面&nbsp;-->
      {{ companyName }}
    </h1>
    <p id="tips">Tips:可点击图表相应区域，查看该项详细情况&nbsp;&nbsp;&nbsp;</p>
    <div id="chart-container">
      <div id="echart" class="center"
           style="width : 80%;height : 360px">
      </div>
      <br>
      <!--    <p id="tips">Tips:可点击图表相应区域，查看该项详细情况</p>-->
    </div>

    <div id="article">
      <div id="part1 with head" style="width: 33%">
        <h2>
          E建议
        </h2>
        <div id="part1">
          <p>
            {{ part[0] }}
          </p>
          <!--    <v-scroll native-->
        </div>
      </div>
      <div id="part2 with head" style="width: 33%">
        <h2>
          S建议
        </h2>
        <div id="part2">
          <p>
            {{ part[1] }}
          </p>
        </div>
      </div>
      <div id="part3 with head" style="width: 33%">
        <h2>
          G建议
        </h2>
        <div id="part3">
          <p>
            {{ part[3] }}
          </p>
        </div>
      </div>
    </div>
    <div>
      <h2>
        综合建议
      </h2>
      <div id="comprehensive_advice">

        <p v-html="conclude">
        </p>
      </div>
      <br><br><br><br>
    </div>
    <div id="button">
      <el-button type="success" native onclick="window.location.href='http://127.0.0.1:8000/downloadpdf/CH'">下载中文报告</el-button>
      <el-button type="warning" native onclick="window.location.href='http://127.0.0.1:8000/downloadpdf/EN'">Download English Version</el-button>
    </div>
    <br><br>

  </div>


</template>

<script>
import * as echarts from 'echarts';
import axios from "axios";
import {ElLoading} from 'element-plus'

export default {
  name: "chart",
  data() {
    return {
      value: [],
      companyName: null,
      part: [],
      conclude: "",
    }
  },
  created() {
    this.getid();
  },
  mounted() {
    console.log("in mount" + this.value);
    var myChart = echarts.init(document.getElementById('echart'));
    // 绘制图表
    const loadingInstance1 = ElLoading.service({
      fullscreen: true,
      text: "正在加载\n预计需要3~5分钟，请耐心等待",
      customClass:'el-loading-text',
    })
    axios.get('/detail/' + this.$data.companyName + '/',
        {
          'name': this.$data.companyName,
          'code': this.$route.params.code
        }
    ).// detail是后端的url
        then(response => {
          this.conclude = this.preText(response.data['conclude'])

          this.part = response.data['part'];
          this.value = response.data['value'];
          console.log("responce:" + response.data['value'])
          myChart.setOption({
            title: {
              text: 'ESG评分',
              // subtext:"Tips:可点击图表相应区域，查看该项详细情况",
              textStyle: {
                'fontSize': 28,
                'fontFamily': " sans-serif",
                // 'color':'#ffe'
                // 'fontWeight': '500',
                'color': '#fff'
              },
            },
            grid:{
              y:'30%'
            },
            series: [{
              itemStyle: {
                normal: {
                  label: {
                    show: true,
                    formatter: '{b} : {c} ({d}%)'
                  },
                   color: function (params) {
                      var colorList = ['#bed742','#feeeed','#90d7ec']
                      return colorList[params.dataIndex]
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
          console.log(this.value)
          loadingInstance1.close()
        }).catch(error => {
      console.log(error)
      loadingInstance1.close()
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
    preText (pretext) {
    return pretext.replace(/\r\n/g, '<br/>').replace(/\n/g, '<br/>').replace(/\s/g, '&nbsp;')
},
  }
}

</script>

<style scoped>
h1 {
  margin-top: 0;
  font-size: 64px;
  font-family: sans-serif, 黑体;
  /*color:black*/
}

#tips {
  text-align: right;
  margin-right: 30px;
  margin-top: 0;
  /*color: whitesmoke;*/
}


#echart {
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

p {
  line-height: 1.5em
}

h2 {
  font-size: 38px;
}

#part1 {
  background-image: linear-gradient(25deg, #ecf1f3, #edf3ee, #eff4ea, #f0f6e5)
}

#part2 {
  background-image: linear-gradient(25deg, #bed2e7, #d4e1ef, #e9f0f7, #e9f0f7)
}

#part3 {
  background-image: linear-gradient(25deg, #d2bec9, #e1d3db, #f0e9ed, #ffffff)
}

#part1, #part2, #part3 {
  margin-left: 10px;
  overflow: auto;
  max-height: 500px; /* 设置最大高度以启用纵向滚动条 */
  /*border: 0.5px solid #2c3e50;*/
  border-radius: 10px; /* 设置输入框的圆角 */
  box-shadow: 2px 2px 5px #888888; /* 设置输入框的阴影 */
  margin-bottom: 50px;
  padding: 2px;
  min-height: 500px;
}

#comprehensive_advice {
  margin: auto;
  padding: 5px 10px 10px 20px;
  border-radius: 10px; /* 设置输入框的圆角 */
  box-shadow: 1px 1px 2px #888888; /* 设置输入框的阴影 */
  overflow: auto;
  max-height: 400px;
  min-height: 400px;
  width: 90%;
  text-align: left;
  background-image: linear-gradient(25deg, #fbfcfd, #f9fbfa, #f8f9f6, #f6f8f3)
}

#part1::-webkit-scrollbar, #part2::-webkit-scrollbar, #part3::-webkit-scrollbar, #comprehensive_advice::-webkit-scrollbar {
  display: none;
}

#article {
  display: flex;
  justify-content: space-between;
  gap: 30px;
}

#tips {
  margin-right: 100px;
}
.el-loading-text {
  white-space: pre-wrap;
}
#button{
  display: flex;
  justify-content: right;
  margin-right: 8%;
}
</style>
