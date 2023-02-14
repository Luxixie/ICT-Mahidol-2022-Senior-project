<template>
    <div>
        <el-row style="background:#F5EFE0;; margin-left:10%;margin-right:10%;margin-top:1%; border-radius: 20px;">
            <el-row>
                <span style="float:right;margin-right:2%">Market Status: Pre-Open2update</span>
            </el-row>
            <el-row>
                <span style="float:right;margin-right:2%">{{ nowTime }}</span>
            </el-row>
            <el-row>
                 <span style="font-size:xx-large;font-weight: bold;margin-left:40%">Today‘s profit</span>
            </el-row>
             <el-row>
                 <span style="font-size:xx-large;font-weight: bold;margin-left:47%;color: red">+0 {{ profit }}</span>
            </el-row>
            <el-row>
                <span style="font-weight: bold;margin-left:44%;">Holding profits +0 {{sumprofit}}</span>
            </el-row>
            <el-row>
                <el-col :span="11">
                    <el-row>
                        <span style="font-weight: bold;margin-left:46%;">Total money</span>
                    </el-row>
                    <el-row>
                        <span style="font-weight: bold;margin-left:50%;">20000 {{todaymoney}}</span>
                    </el-row>
                </el-col>
                <el-col :span="11">
                    <el-row>
                        <span style="font-weight: bold;margin-left:44%;">Avilable money</span>
                    </el-row>
                    <el-row>
                        <span style="font-weight: bold;margin-left:50%;">18800 {{avilablemoney}}</span>
                    </el-row>
                </el-col>
            </el-row>
        </el-row>

        <el-row style="margin-left:10%;margin-right:10%;margin-top:1%;">
            <el-col :span="11" style="background:blue; float:left; border-radius: 20px;" >
                <el-button icon="el-icon-sold-out" style="background: #F5EFE0; border-radius: 20px; width:100%;font-weight: bold;color:black;font-size:18px">  Buy and Sell

                </el-button>
            </el-col>
            <el-col :span="11" offset="1"  style="background:green;float:right; border-radius: 20px;">
                <el-button icon="el-icon-star-off" style="background: #F5EFE0; border-radius: 20px; width:100%;font-weight: bold;color:black;font-size:18px">Watch list
                </el-button>
            </el-col>

        </el-row>

        <el-row style="margin-left:10%;margin-right:10%;margin-top:1%;">
            <el-col :span="11" style="background:#D9D9D9;; float:left;border-radius: 20px;" >
                <div class="echart" id="mychart" :style="myChartStyle"></div>
            </el-col>
            <el-col :span="11" :offset="1" style="background:#D9D9D9;;float:right;border-radius: 20px;">
                <el-table
                    :data="tableData"
                    style="width: 100%">
                    <el-table-column
                        prop="no"
                        label="No."
                        width="180">
                    </el-table-column>
                    <el-table-column
                        prop="name"
                        label="Name"
                        width="180">
                    </el-table-column>
                    <el-table-column
                        prop="vol"
                        label="Vol">
                    </el-table-column>
                    <el-table-column
                        prop="price"
                        label="Price">
                    </el-table-column>
                    </el-table>
            </el-col>

        </el-row>
    </div>

        <!-- update pie chart data
            import VueApexCharts from 'vue-apexcharts'

        export default {
        name: 'Vue Chart',
        data: function () {
        return {
        chartOptions: {
            chart: {
            id: 'vuechart-example',
            },
            xaxis: {
            categories: [1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998],
            },
        },
        series: [{
            name: 'Vue Chart',
            data: [30, 40, 45, 50, 49, 60, 70, 81]
        }]
        }
        },
        methods: {
        updateChart() {
        const max = 90;
        const min = 20;
        const newData = this.series[0].data.map(() => {
            return Math.floor(Math.random() * (max - min + 1)) + min
        })
        // In the same way, update the series option
        this.series = [{
            data: newData
        }]
        }
        }
        } -->
    
</template>


<script>
import * as echarts from "echarts";



export default {
    data() {
        return {
            nowTime: '',
            profit:'',
            sumprofit:'',
            today_money:'',
            Avilable_money:'',
            myChart: {},
            pieData: [
                {
                value: 18800,
                name: "Avilable_money"
                },
                {
                value: 200,
                name: "Using_stock"
                },

                ],
            pieName: [],
                    myChartStyle: { float: "left", width: "100%", height: "400px" }, //图表样式
            tableData: [{
                no:'1',
                name: 'WICE',
                vol: '100',
                price:'1200',
            },
            {
                no:'2',
                name: '',
                vol: '',
                price:'',
            },
            {
                no:'3',
                name: '',
                vol: '',
                price:'',
            },
            {
                no:'4',
                name: '',
                vol: '',
                price:'',
            },
            {
                no:'5',
                name: '',
                vol: '',
                price:'',
            },
            {
                no:'6',
                name: '',
                vol: '',
                price:'',
            },
            {
                no:'7',
                name: '',
                vol: '',
                price:'',
            },
            ]
            }
    },

    mounted() {
    this.getNowTime();
    this.initDate(); //数据初始化
    this.initEcharts();
    },
    created() {
        this.initData();
    },
    methods: {
    getNowTime () {
      let speed = 1000
      let that = this
      let theNowTime = function () {
        that.nowTime = that.timeNumber()
      }
      setInterval(theNowTime, speed)
    },
    timeNumber () {
      let today = new Date()
      let date = today.getFullYear() + '-' + this.twoDigits(today.getMonth() + 1) + '-' + this.twoDigits(today.getDate())
      let time = this.twoDigits(today.getHours()) + ':' + this.twoDigits(today.getMinutes()) + ':' + this.twoDigits(today.getSeconds())
      return date + '  ' + time
    },
    twoDigits (val) {
      if (val < 10) return '0' + val
      return val
    },
    initDate() {
      for (let i = 0; i < this.pieData.length; i++) {
        // this.xData[i] = i;
        // this.yData =this.xData[i]*this.xData[i];
        this.pieName[i] = this.pieData[i].name;
      }
    },
    initEcharts() {
      // 饼图
      const option = {
        legend: {
          // 图例
          data: this.pieName,
          right: "10%",
          top: "30%",
          orient: "vertical"
        },
        /*title: {
          // 设置饼图标题，位置设为顶部居中
          text: "",
          top: "0%",
          left: "center"
        },*/
        series: [
          {
            type: "pie",
            label: {
              show: true,
              formatter: "{b} : {c}" // b代表名称，c代表对应值，d代表百分比
            },
            radius: "50%", //饼图半径
            data: this.pieData
          }
        ]
      };
      console.log(this.seriesData);
      const optionFree = {
        xAxis: {},
        yAxis: {},
        series: [
          {
            data: this.seriesData,
            type: "line",
            smooth: true
          }
        ]
      };
      this.myChart = echarts.init(document.getElementById("mychart"));
      this.myChart.setOption(option);
      //随着屏幕大小调节图表
      window.addEventListener("resize", () => {
        this.myChart.resize();
      });

    }
    }
}


</script>


<style>


</style>

