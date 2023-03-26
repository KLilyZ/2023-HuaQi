<template>


  <div id="title" >
    <image-vue :image-url="imageUrl" id="icon"></image-vue>
    <div :style="{'--color':color}" class="head">
      <h1 id="score">{{ shorthand }}:&nbsp;{{ score }}</h1>
    </div>
  </div>
  <!--  <h1> This is {{ species }}</h1>-->
  <br>
  <div id="flex">
    <table id="tableList" style="width:40% ;table-layout: fixed">
      <tr>
        <th style="width:20%">序号</th>
        <th style="width:50%">项目</th>
        <th style="width:30%"> 得分</th>
      </tr>
      <tr v-for="(tr,index) in details">
        <td>{{ index + 1 }}</td>
        <td v-for="td in tr">
          {{ td }}
        </td>
      </tr>
    </table>
    <div id="echart" class="center"
         style="width : 50%;height : 400px;min-height: 30px"></div>
    <br><br><br><br>
  </div>


</template>


<script>
import * as echarts from "echarts";
import axios from "axios";
import MyScroll from "@/components/scroll";
import VueScrollbar from "vue3-scrollbar";
import imageVue from "@/components/imageVue";

export default {
  name: "Environment",
  components: {
    // MyScroll
    VueScrollbar,
    imageVue
  },
  data() {
    return {
      companyName: 'ESG',
      details: [],
      score: 0.0,
      species: '',
      shorthand: '',
      color: 'red',
      color2: 'grey',
      tableTh: {//表头的描述信息
      },
      category: [],
      scorePer: [],
      imageUrl: ''
    }
  },
  created() {
    this.getInformation();
    //获取指定数据数据
  },
  mounted() {
    var myChart = echarts.init(document.getElementById('echart'));
    axios.get('/detail/' + this.companyName + '/' + this.species,
        {'name': this.companyName, 'species': this.species}).// detail是后端的url
        then(response => {
          this.details = response.data['details'];
          this.category = response.data['category'];
          this.scorePer = response.data['scorePer'];
          this.article = response.data['article'];
          console.log("category" + this.category)
          console.log("scorePer" + this.scorePer)
          var species = this.species;
          console.log(this.scorePer)
          myChart.setOption({
            title: {
              text: '各项目得分细则',
              left: 'center',
              grid: {
                left: '70%',
                containLabel: true
              },
              textStyle: {
                'fontSize': 25,
                'fontFamily': '黑体-简',
                // 'color':'#ffe'
                // 'fontWeight': '500',
                // 'color': '#fff'
              },
            },
            tooltip: {},
            xAxis: {
              type: 'value',
              name: '分数',
              nameTextStyle: {
                'fontSize': 15,
                color: 'black',
                type: 'solid'
              },
              width: 200
            },
            yAxis: {
              type: 'category',
              name: '项目名称',
              nameTextStyle: {
                'fontSize': 15,
                color: 'black',
                type: 'solid'
              },
              data: this.category,
              axisLabel: {
                interval: 0,
                rotate: "45", //表示的角度倾斜45度
              },
              width: 100
            },
            grid: {
              x: '15%',
              y2:'10%'
            },
            series: [
              {
                name: '分数',
                type: 'bar',
                // data: [5, 20, 36, 10, 10, 20]
                data: response.data['scorePer'],
                itemStyle: {
                  normal: {
                    // 这里就可以实现，配置柱状图的颜色
                    color: function (params) {
                      var colorList;
                      if (species === 'Governance') {
                        //粉红色系
                        colorList = ['#feeeed', '#f8aba6', '#f69c9f', '#f47a55', '#f3704b', '#f58f98', '#ca8687'];
                      } else if (species === 'Environment') {
                        //黄绿色系
                        colorList = ['#5c7a29', '#bed742', '#b2d235', '#fcf16e', '#decb00', '#cbc547', '#b7ba6b',];
                      } else {
                        // 蓝色系
                        colorList = ['#94d6da', '#afdfe4', '#90d7ec', '#d3d7d4', '#145b7d', '#009ad6', '#afb4db'];
                      }

                      return colorList[params.dataIndex]
                    },
                  }
                },
              }
            ],

          })

          //TODO：用于调试,记得删
          //this.details = {name:'排放',value:'污染'}
          console.log("已从后端拉取数据")
          console.log(response)
        }).catch(error => {
      console.log(error)
    })
  },
  methods: {
    getInformation() {
      this.companyName = this.$route.params.name;   // 此处非router
      this.species = this.$route.params.species;
      if (this.species === 'Environment') {
        this.shorthand = 'E';
        this.color = '#67C23A';
        this.color2 = '#cde6c7';
        this.imageUrl = '/assets/E_logo.png'
      } else if (this.species === 'Social') {
        this.shorthand = 'S';
        this.color = '#4e72b8';
        this.color2 = '#afdfe4';
        this.imageUrl = '/assets/S_logo.png'
      } else {
        this.shorthand = 'G';
        this.color = 'pink';
        this.color2 = '#feeeed'
        this.imageUrl = '/assets/G_logo.png'
      }
    },
  }
}
</script>

<style scoped>
/*#article{*/
/*  margin:20px;*/
/*  border: 3px solid #999999;*/
/*}*/

.head {
  margin: auto;
  /*background-image:linear-gradient(25deg, #4ba7a2, #8cc4c0, #c6e1df, #ffffff);*/
  width: 30%;
  height: 10%;
  border-radius: 10px; /* 设置输入框的圆角 */
  /*box-shadow: 1px 1px 1px #888888; !* 设置输入框的阴影 *!*/
}

.wrapper {
  height: 300px;
}

.content {
  height: 500px;
}

#score {
  /*color:#67C23A;*/
  font: 900 100px/100px "Times New Roman";
  color: var(--color) !important;
}

#echart {
  margin: auto;
  width: 60%;
  /*border: 3px solid #73AD21;*/
  padding: 10px;
  border-radius: 10px; /* 设置输入框的圆角 */
  box-shadow: 2px 2px 5px #888888; /* 设置输入框的阴影 */
  /*background: rgb(252,250,237);*/
}

#list {
  margin-left: 120px;
  text-align: center;
  border: 3px solid #73AD21;
}

#article {
  display: flex;
  justify-content: space-between;
  gap: 30px;
}

#flex {
  display: flex;
  /*display: inline-block;*/
  /*align-items: baseline;*/
  justify-content: space-between;
  /*gap:10px;*/
}

table {
  margin-left: 4%;
  /*border: 1px solid #000000;*/
  /*border-collapse: collapse;*/
  /*background-color: black;*/
  text-align: center;
  border-radius: 10px;
  box-shadow: 2px 2px 2px #888888;
}

table th {
  background: #ecf1f3;
  /*background-image: linear-gradient(25deg, #ecf1f3, #edf3ee, #eff4ea, #f0f6e5);*/
  font-size: 20px;
  /*border: 1px solid #000000;*/
  text-align: center;
}

table td {
  /*border: 1px solid #000000;*/
  text-align: center;
  background-color: #ffffff;
  min-height: 30px;
}

#title {
  margin-left: 60px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-top: 0;
}

#icon {
  width: 12%;
  height: 12%;
}

#icon, .head {
  margin: 0; /* 取消默认外边距 */
}

.head {
  display: flex;
  align-items: center;
}

</style>