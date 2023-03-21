<template>
  <div :style="{'--color':color}">
    <h1 id="score">{{ shorthand }}:&nbsp;{{ score }}</h1>
  </div>

  <h1> This is {{ species }}</h1>
  <br><br>
  <div id="flex">
    <table id="tableList" style="width:40% ;table-layout: fixed">
      <tr>
        <th style="width:20% ">序号</th>
        <th style="width:50% ">项目</th>
        <th style="width:30% "> 得分</th>
      </tr>
      <tr v-for="(tr,index) in details">
        <td>{{ index + 1 }}</td>
        <td v-for="td in tr">
          {{ td }}
        </td>
      </tr>
    </table>
    <div id="echart" class="center"
         style="width : 50%;height : 300px"></div>
  </div>
  <br><br><br><br><br><br>
  <div id="article">
    <div id="left" style="width: 50%">
      <div id="part1" style="height: 50%">
        <p>
          hhhhhhhhhhhhhhhhhhhhhhhhhhh<br>
          hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh<br>
          hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh<br>
          文がいくつか集まり、かつ、まとまった内容を表すもの。内容のうえで前の文と密接な関係をもつと考えられる文は、そのまま続いて書き継がれ、前の文と隔たりが意識されたとき、次の文は行を改めて書かれる。すなわち、段落がつけられるということであり、これは、書き手がまとまった内容を段落ごとにまとめようとするからである。この、一つの段落にまとめられる、いくつかの文の集まりを一文章というが、よりあいまいに、いくつかの文をまとめて取り上げるときにそれを文章と称したり、文と同意義としたりすることもあるなど文章はことばの単位として厳密なものでないことが多い。これに対して、時枝誠記(ときえだもとき)は、文章を語・文と並ぶ文法上の単位として考えるべきことを主張し、表現者が一つの統一体ととらえた、完結した言語表現を文章と定義した。これによれば、一編の小説は一つの文章であり、のちに続編が書き継がれた場合には、この続編をもあわせたものが一つの文章ということになる。俳句、和歌の一句・一首は、いずれも一つの文章であり、これをまとめた句集・歌集は、編纂(へんさん)者の完結した思想があることにおいて、それぞれ一つの文章ということになる。

          ［山口明穂］

          『時枝誠記著『日本文法　口語篇』（1950・岩波書店）』
        </p>
        <!--    <v-scroll native-->
      </div>
      <br>
      <div id="part2" style="height: 50%">
        <p>
          hhhhhhhhhhhhhhhhhhhhhhhhhhh<br>
          hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh<br>
          hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh<br>
          文がいくつか集まり、かつ、まとまった内容を表すもの。内容のうえで前の文と密接な関係をもつと考えられる文は、そのまま続いて書き継がれ、前の文と隔たりが意識されたとき、次の文は行を改めて書かれる。すなわち、段落がつけられるということであり、これは、書き手がまとまった内容を段落ごとにまとめようとするからである。この、一つの段落にまとめられる、いくつかの文の集まりを一文章というが、よりあいまいに、いくつかの文をまとめて取り上げるときにそれを文章と称したり、文と同意義としたりすることもあるなど文章はことばの単位として厳密なものでないことが多い。これに対して、時枝誠記(ときえだもとき)は、文章を語・文と並ぶ文法上の単位として考えるべきことを主張し、表現者が一つの統一体ととらえた、完結した言語表現を文章と定義した。これによれば、一編の小説は一つの文章であり、のちに続編が書き継がれた場合には、この続編をもあわせたものが一つの文章ということになる。俳句、和歌の一句・一首は、いずれも一つの文章であり、これをまとめた句集・歌集は、編纂(へんさん)者の完結した思想があることにおいて、それぞれ一つの文章ということになる。

          ［山口明穂］

          『時枝誠記著『日本文法　口語篇』（1950・岩波書店）』
        </p>
      </div>
    </div>
    <div id="right" style="width: 50%">
      <div id="part3">
        hhhhhhhhhhhhhhhhhhhhhhhhhhh<br>
        hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh<br>
        hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh<br>
        文がいくつか集まり、かつ、まとまった内容を表すもの。内容のうえで前の文と密接な関係をもつと考えられる文は、そのまま続いて書き継がれ、前の文と隔たりが意識されたとき、次の文は行を改めて書かれる。すなわち、段落がつけられるということであり、これは、書き手がまとまった内容を段落ごとにまとめようとするからである。この、一つの段落にまとめられる、いくつかの文の集まりを一文章というが、よりあいまいに、いくつかの文をまとめて取り上げるときにそれを文章と称したり、文と同意義としたりすることもあるなど文章はことばの単位として厳密なものでないことが多い。これに対して、時枝誠記(ときえだもとき)は、文章を語・文と並ぶ文法上の単位として考えるべきことを主張し、表現者が一つの統一体ととらえた、完結した言語表現を文章と定義した。これによれば、一編の小説は一つの文章であり、のちに続編が書き継がれた場合には、この続編をもあわせたものが一つの文章ということになる。俳句、和歌の一句・一首は、いずれも一つの文章であり、これをまとめた句集・歌集は、編纂(へんさん)者の完結した思想があることにおいて、それぞれ一つの文章ということになる。

        ［山口明穂］

        『時枝誠記著『日本文法　口語篇』（1950・岩波書店）』
        hhhhhhhhhhhhhhhhhhhhhhhhhhh<br>
        hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh<br>
        hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh<br>
        文がいくつか集まり、かつ、まとまった内容を表すもの。内容のうえで前の文と密接な関係をもつと考えられる文は、そのまま続いて書き継がれ、前の文と隔たりが意識されたとき、次の文は行を改めて書かれる。すなわち、段落がつけられるということであり、これは、書き手がまとまった内容を段落ごとにまとめようとするからである。この、一つの段落にまとめられる、いくつかの文の集まりを一文章というが、よりあいまいに、いくつかの文をまとめて取り上げるときにそれを文章と称したり、文と同意義としたりすることもあるなど文章はことばの単位として厳密なものでないことが多い。これに対して、時枝誠記(ときえだもとき)は、文章を語・文と並ぶ文法上の単位として考えるべきことを主張し、表現者が一つの統一体ととらえた、完結した言語表現を文章と定義した。これによれば、一編の小説は一つの文章であり、のちに続編が書き継がれた場合には、この続編をもあわせたものが一つの文章ということになる。俳句、和歌の一句・一首は、いずれも一つの文章であり、これをまとめた句集・歌集は、編纂(へんさん)者の完結した思想があることにおいて、それぞれ一つの文章ということになる。

        ［山口明穂］

        『時枝誠記著『日本文法　口語篇』（1950・岩波書店）』
        『時枝誠記著『日本文法　口語篇』（1950・岩波書店）』
        hhhhhhhhhhhhhhhhhhhhhhhhhhh<br>
        hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh<br>
        hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh<br>
        文がいくつか集まり、かつ、まとまった内容を表すもの。内容のうえで前の文と密接な関係をもつと考えられる文は、そのまま続いて書き継がれ、前の文と隔たりが意識されたとき、次の文は行を改めて書かれる。すなわち、段落がつけられるということであり、これは、書き手がまとまった内容を段落ごとにまとめようとするからである。この、一つの段落にまとめられる、いくつかの文の集まりを一文章というが、よりあいまいに、いくつかの文をまとめて取り上げるときにそれを文章と称したり、文と同意義としたりすることもあるなど文章はことばの単位として厳密なものでないことが多い。これに対して、時枝誠記(ときえだもとき)は、文章を語・文と並ぶ文法上の単位として考えるべきことを主張し、表現者が一つの統一体ととらえた、完結した言語表現を文章と定義した。これによれば、一編の小説は一つの文章であり、のちに続編が書き継がれた場合には、この続編をもあわせたものが一つの文章ということになる。俳句、和歌の一句・一首は、いずれも一つの文章であり、これをまとめた句集・歌集は、編纂(へんさん)者の完結した思想があることにおいて、それぞれ一つの文章ということになる。

        ［山口明穂］

        『時枝誠記著『日本文法　口語篇』（1950・岩波書店）』
      </div>
    </div>

  </div>

</template>


<script>
import * as echarts from "echarts";
import axios from "axios";
import MyScroll from "@/components/scroll";
import VueScrollbar from "vue3-scrollbar";

export default {
  name: "Environment",
  components: {
    // MyScroll
    VueScrollbar
  },
  data() {
    return {
      companyName: 'ESG',
      score: 0.0,
      species: '',
      shorthand: '',
      color: 'red',
      tableTh: {//表头的描述信息
        c1: {
          title: "项目", //还可以增加其他描述，比如width等
          align: "center"
        },
        c2: {
          title: "得分",
          align: "center"
        }
      },
      details: [ //字典的列表
        {
          //数据包，字段名作为关键字，便于列的调整先后顺序
          c1: "度娘2",
          c2: "123123123"
        },
        {
          c1: "企鹅2",
          c2: "7897899787"
        },
        {
          c1: "阿里爸爸2",
          c2: "456456456"
        }
      ],
      category:
          ["度娘2", "企鹅2", "阿里爸爸2"],
      scorePer:
          [123123123, 7897899787, 456456456],
      article:
          ["『時枝誠記著『日本文法　口語篇』（1950・岩波書店）』\n" +
          "        hhhhhhhhhhhhhhhhhhhhhhhhhhh<br>\n" +
          "          hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh<br>\n" +
          "          hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh<br>\n" +
          "          文がいくつか集まり、かつ、まとまった内容を表すもの。内容のうえで前の文と密接な関係をもつと考えられる文は、そのまま続いて書き継がれ、前の文と隔たりが意識されたとき、次の文は行を改めて書かれる。すなわち、段落がつけられるということであり、これは、書き手がまとまった内容を段落ごとにまとめようとするからである。この、一つの段落にまとめられる、いくつかの文の集まりを一文章というが、よりあいまいに、いくつかの文をまとめて取り上げるときにそれを文章と称したり、文と同意義としたりすることもあるなど文章はことばの単位として厳密なものでないことが多い。これに対して、時枝誠記(ときえだもとき)は、文章を語・文と並ぶ文法上の単位として考えるべきことを主張し、表現者が一つの統一体ととらえた、完結した言語表現を文章と定義した。これによれば、一編の小説は一つの文章であり、のちに続編が書き継がれた場合には、この続編をもあわせたものが一つの文章ということになる。俳句、和歌の一句・一首は、いずれも一つの文章であり、これをまとめた句集・歌集は、編纂(へんさん)者の完結した思想があることにおいて、それぞれ一つの文章ということになる。\n" +
          "\n" +
          "          ［山口明穂］\n" +
          "\n" +
          "          『時枝誠記著『日本文法　口語篇』（1950・岩波書店）』", "", ""]
    }
  },
  created() {
    this.getInformation();
    //获取指定数据数据
  },
  mounted() {
    var myChart = echarts.init(document.getElementById('echart'));
    // 绘制图表
    // var option = {
    //   title: {
    //     text: '各项目得分细则'
    //   },
    //   tooltip: {},
    //   legend: {
    //     data: ['销量']
    //   },
    //   xAxis: {
    //     type:'value'
    //   },
    //   yAxis: {
    //     type:'category',
    //     // data: ['衬衫', '羊毛衫', '雪纺衫', '裤子', '高跟鞋', '袜子']
    //     data:this.category,
    //   },
    //   series: [
    //     {
    //       name: '分数',
    //       type: 'bar',
    //       // data: [5, 20, 36, 10, 10, 20]
    //       data:this.scorePer,
    //     }
    //   ]
    // };
    // // 使用刚指定的配置项和数据显示图表。
    // myChart.setOption(option);
    axios.get('/detail/' + this.companyName + '/' + this.species,
        {'name': this.companyName, 'species': this.species}).// detail是后端的url
        then(response => {
          this.details = response.data['details'];
          this.category = response.data['category'];
          this.scorePer = response.data['scorePer'];
          this.article = response.data['article'];
          console.log(this.scorePer)
          myChart.setOption({
            title: {
              text: '各项目得分细则'
            },
            tooltip: {},
            legend: {
              data: ['销量']
            },
            xAxis: {
              type: 'value'
            },
            yAxis: {
              type: 'category',
              // data: ['衬衫', '羊毛衫', '雪纺衫', '裤子', '高跟鞋', '袜子']
              // data: this.category,
              data: this.category,
              axisLabel: {
                interval: 0,
                rotate: "45", //表示的角度倾斜45度
              }
            },
            series: [
              {
                name: '分数',
                type: 'bar',
                // data: [5, 20, 36, 10, 10, 20]
                data: this.scorePer,
                 itemStyle: {
                    normal: {
                        // 这里就可以实现，配置柱状图的颜色
                        color: function (params) {
                            var colorList = [ '#ccc', '#c101c1', '#FCCE10', '#E87C25', '#27727B', '#D7504B'];
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
      } else if (this.species === 'Social') {
        this.shorthand = 'S';
        this.color = 'blue';
      } else {
        this.shorthand = 'G';
        this.color = 'pink';
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
#part1, #part2 {
  margin-left: 30px;
  overflow: auto;
  max-height: 400px; /* 设置最大高度以启用纵向滚动条 */
  border: 3px solid #2c3e50;
}

#part1::-webkit-scrollbar, #part2::-webkit-scrollbar, #part3::-webkit-scrollbar {
  display: none;
}

#part3 {
  margin-right: 30px;
  overflow: auto;
  max-height: 825px; /* 设置最大高度以启用纵向滚动条 */
  border: 3px solid #2c3e50;
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
  border: 3px solid #73AD21;
  padding: 10px;
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
  border: 1px solid #000000;
  border-collapse: collapse;
  background-color: black;
  text-align: center;
}

table th {
  /*background: #e3e3e3;*/
  font-size: 20px;
  border: 1px solid #000000;
  text-align: center;
  background-color: #e3e3e3; /*e3e3e3*/
}

table td {
  border: 1px solid #000000;
  text-align: center;
  background-color: #ffffff;
}
</style>