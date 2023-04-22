<template>
    <div>
        <el-row style="background:#F5EFE0;; margin-left:10%;margin-right:10%;margin-top:1%; border-radius: 20px;">
            <el-row>
                <span style="float:right;margin-right:8%">Market time:</span>
            </el-row>
            <el-row>
                <span style="float:right;margin-right:2%">{{ nowTime }}</span>
            </el-row>
            <el-row>
                 <span style="font-size:xx-large;font-weight: bold;margin-left:40%">Holding profits</span>
            </el-row>
            <el-row>
              <span :style="{ fontSize: 'xx-large', fontWeight: 'bold', marginLeft: '40%', color: profits > 0 ? 'red' : 'green' }">{{profits.toFixed(2) | numberWithCommas}} THB</span>
            </el-row>


            <el-row>
                <el-col :span="11">
                    <el-row>
                        <span style="font-weight: bold;margin-left:46%;">Total money</span>
                    </el-row>
                    <el-row>
                        <span style="font-weight: bold;margin-left:45%;">100,000.00 THB</span>
                    </el-row>
                </el-col>
                <el-col :span="11">
                    <el-row>
                        <span style="font-weight: bold;margin-left:44%;">Avilable money</span>
                    </el-row>
                    <el-row>
                        <span style="font-weight: bold;margin-left:45%;">{{avilablemoney | numberWithCommas }} THB</span>
                    </el-row>
                </el-col>
            </el-row>
        </el-row>

        <el-row style="margin-left:10%;margin-right:10%;margin-top:1%;">
            <el-col :span="11" style="background:blue; float:left; border-radius: 20px;" >
                <el-button icon="el-icon-sold-out" style="background: #F5EFE0; border-radius: 20px; width:100%;font-weight: bold;color:black;font-size:18px" @click="Gobuyandsell">  Buy and Sell

                </el-button>
            </el-col>
            <el-col :span="11" :offset="1"  style="background:green;float:right; border-radius: 20px;">
                <el-button icon="el-icon-star-off" style="background: #F5EFE0; border-radius: 20px; width:100%;font-weight: bold;color:black;font-size:18px" @click="Gowatchlist">Watch list
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
                    style="width: 100%"
                    border
                    height="400">
                    <el-table-column
                        type="index"
                        label="No."
                        >
                    </el-table-column>
                    <el-table-column
                        prop="ticker"
                        label="TickerName"
                       >
                    </el-table-column>
                    <el-table-column
                        prop="shares"
                        label="Vol">
                    </el-table-column>
                    <el-table-column
                        prop="average_stock_price"
                        label="Avg.Price">
                    </el-table-column>

                    </el-table>
            </el-col>


        </el-row>
    </div>
</template>


<script>
import * as echarts from "echarts";
import axios from 'axios'


export default {
    data() {
        return {
            usingstock:0,
            nowTime: '',
            avilablemoney:'',
            Avilable_money:'',
            myChart: {},
            pieData: [
                {
                value: 100000 ,
                name: "Avilable_money"
                },
                {
                value: '',
                name: "Using_stock"
                },

                ],
            pieName: [],
            myChartStyle: { float: "left", width: "100%", height: "400px" }, //图表样式
            tableData: [],
            profits:'',
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
          top: "90%",
          orient: "vertical"
        },
        title: {
          // 设置饼图标题，位置设为顶部居中
          text: "Balance Proportion",
          top: "8%",
          left: "center"
        },
        series: [
          {
            type: "pie",
            label: {
              show: true,
              formatter: " {c}" // b代表名称，c代表对应值，d代表百分比
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

    },
    Gobuyandsell(){
          this.$router.push('/markethome')
    },
    Gowatchlist(){
          this.$router.push('/watchlist')
    },
    },
    filters: {
        numberWithCommas: function (value) {
            if (!value) return ''
            var parts = value.toString().split('.')
            parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ',')
            if (parts.length > 1) {
            parts[1] = parts[1].substr(0, 2) // Only keep the first two decimal places
            } else {
            parts.push('00') // Add trailing zeros if the value doesn't have any decimal places
            }
            return parts.join('.')
        }
    },
    created(){
        var id = this.$store.state.accountid
        console.log(id)
        var req = {
            accountid:id
        }
        axios.post("http://127.0.0.1:8088/GetBalance",req).then((res) => {
            console.log(res)
            this.profits = parseFloat(res.data['profit'])
            this.avilablemoney = parseFloat(res.data['Balance'])
            console.log('test')
            console.log(this.avilablemoney)
            console.log(this.profits)
            
            axios.post("http://127.0.0.1:8088/GetBuyHistory",req).then((res) => {
            console.log(res)
            this.tableData = res.data.data

            })

            axios.post("http://127.0.0.1:8088/Gettotal",req).then((res) => {
            //Calculate the total value of all shares currently held
            var responseData = res.data;

            var totalstockcost = 0
            responseData.forEach(data => {
                totalstockcost += data['cost']
            });
            console.log(totalstockcost)
            this.usingstock = totalstockcost

            console.log(this.avilablemoney)
            console.log(this.usingstock)        
              this.pieData= [
                {
                value: this.avilablemoney,
                name: "Avilable_money"
                },
                {
                value:this.usingstock,
                name: "Using_stock"
                },

                ]
            console.log(this.pieData)
            this.initEcharts()
            })
        })
        
          
    }
}


</script>


<style>


</style>

