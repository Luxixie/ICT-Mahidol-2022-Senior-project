<template>
  <div style="margin:2%;">
    <el-row style="height: 200px;">
      <el-col :span="12">
        <el-row style="height: 30%; overflow: auto;">
          <span style="font-size: xx-large; color:#f5efe1;">BKK:WICE</span>
        </el-row>
        <el-row style="height: 30%;">
          <span style="font-size: x-large; color:#f5efe1;">Wice Logistics Public Company Limited</span>
        </el-row>
        <el-row style="height: 30%;">
          <el-button style="margin-top: 3%;border-radius: 35px;" type="warning" icon="el-icon-star-off">Add to Watch
            list</el-button>
          <el-button style="margin-top: 3%;border-radius: 35px;" type="warning" @click="ShowBuyAndSell" > Buy / Sell
          </el-button>
          <el-button style="margin-top: 3%;border-radius: 35px;" type="warning" @click="ShowStockInfo"> Stock
            Infomation </el-button>
        </el-row>
      </el-col>
      <el-col :span="12">
        <el-row>
          <el-col :span="8" :offset="8">
            <span style="font-size: xx-large; color:#f5efe1;">12.00</span>
          </el-col>

        </el-row>
        <el-row style="height: 30%;">
          <el-col :span="8" :offset="6">
            <span style="font-size: xx-large; color:#f5efe1;">-0.10(-0.83%)</span>
          </el-col>
        </el-row>
        <el-row style="height: 30%;">
          <el-col :span="12" :offset="5">
            <span style="font-size:small; color:#f5efe1;">Market Status:Pre-Open2 update 14/2/2023 18:16:00{{ nowTime }}</span>
          </el-col>
        </el-row>
      </el-col>
    </el-row>
    <el-row>
      <el-col :span="14">
        <div style="background: #d9d9d9; border-radius: 30px;">
          <div id="chart" style="height:300px;padding-top: 3%;  padding-left: 3%;"></div>
        </div>
      </el-col>
      <el-col :span="6" :offset="1">
        <div style="background: #d9d9d9; border-radius: 30px;">
          <div style="height:300px;padding-top: 3%;  padding-left: 3%;">
            <el-row>
              <span style="font-size: x-large; padding-bottom: 2%;">Data Summary</span>
            </el-row>

            <el-row class="dataSummaryItem">
              <span>Currency: </span>
              <span class="dataSummaryItemValue">12.10</span>
            </el-row>
            <el-row class="dataSummaryItem">
              <span>High: </span>
              <span class="dataSummaryItemValue">10</span>
            </el-row>
            <el-row class="dataSummaryItem">
              <span>Low: </span>
              <span class="dataSummaryItemValue">9 </span>
            </el-row>
            <el-row class="dataSummaryItem">
              <span>Exchange: </span>
              <span class="dataSummaryItemValue">12.00</span>
            </el-row>
            <el-row class="dataSummaryItem">
              <span>Last price: </span>
              <span class="dataSummaryItemValue">12</span>
            </el-row>
            <el-row class="dataSummaryItem">
              <span>Last Volume: </span>
              <span class="dataSummaryItemValue">10000</span>
            </el-row>
            <el-row class="dataSummaryItem">
              <span>Open: </span>
              <span class="dataSummaryItemValue">8:00</span>
            </el-row>
            <el-row class="dataSummaryItem">
              <span>Previous Close: </span>
              <span class="dataSummaryItemValue">6,293.048</span>
            </el-row>


          </div>
        </div>
      </el-col>
    </el-row>

    <div v-if="!showInfo">

      <el-row style="margin-top: 2%;  height: 400px;">
        <el-col :span="11" style="border-radius: 15px; height: 100%; ">
          <div style="margin-left: 4%; margin-right: 4%;">
            <el-row>
              <el-button :span="11"
                style="color: black; font-size: larger; font-weight: bolder; margin-top: 3%;border-radius: 35px; width: 40%;"
                type="warning"> Sell
              </el-button>
              <el-button :span="11"
                style=" color: black; font-size: larger; font-weight: bolder;  float: right; margin-top: 3%;border-radius: 35px;  width: 40%;"
                type="warning"> Buy </el-button>
            </el-row>
            <el-row style="height: 300px; margin-top: 2%; border-radius: 12px; background: #f5efe1;">
              <el-col :span="12" style=" height: 100%;">
                <el-row style="margin-top:10%; margin-bottom: 5%; margin-left: 7%;">
                  <span :span="5" style="font-size:medium;">Price</span>
                  <button :span="3" size="mini" style="margin-left: 8%;  border: 0px;">-</button>
                  <el-input
                    style="outline: none;   width: 40%; margin-left: 5%; margin-right: 5%; border-color: transparent;"
                    placeholder="input the price"></el-input>
                  <button :span="3" size="mini" style="background: #f8bd9e; border: 0px;">+</button>
                </el-row>
                <el-row style="margin-top:10%; margin-bottom: 5%; margin-left: 7%;">
                  <span :span="5" style="font-size:medium;">Volume</span>
                  <button :span="3" size="mini" style="margin-left: 2%;  border: 0px;">-</button>
                  <el-input
                    style="outline: none; margin-left: 5%; margin-right: 5%; border-color: transparent; width: 40%; "
                    placeholder="input the price"></el-input>
                  <button :span="3" size="mini" style="background: #f8bd9e; border: 0px;">+</button>
                </el-row>

                <el-row style="margin-left: 10%;">
                  <el-button round style="background: #203f6f; color: white;">1/4</el-button>
                  <el-button round style="background: #203f6f; color: white;">1/3</el-button>
                  <el-button round style="background: #203f6f; color: white;">1/2</el-button>
                  <el-button round style="background: #203f6f; color: white;">ALL IN</el-button>
                </el-row>
                <el-row>
                  <el-col :span="8" :offset="7" style="margin-top: 4%;">
                    <el-button round type="warning" style="color: black;">Simulation of buy</el-button>
                  </el-col>
                </el-row>
              </el-col>
              <el-col :span="12" style="height: 100%; ">
                <el-row>
                  <el-col :span="12" :offset="6" style="margin-top: 10%; ">
                    <div
                      style="height: 30px; background: #dfd4dd; border-radius: 15px; padding-top: 3%; padding-left: 5%; padding-right: 5%;">
                      <span style="float:left;">new price</span>
                      <span style="float:right;">70.00</span>
                    </div>

                    <div
                      style="height: 30px;  margin-top: 10%; background: #dfd4dd; border-radius: 15px; padding-top: 3%; padding-left: 5%; padding-right: 5%;">
                      <span style="float:left;">new price</span>
                      <span style="float:right;">70.00</span>
                    </div>

                    <div
                      style="height: 30px; background: #dfd4dd; margin-top: 10%;border-radius: 15px; padding-top: 3%; padding-left: 5%; padding-right: 5%;">
                      <span style="float:left;">new price</span>
                      <span style="float:right;">70.00</span>
                    </div>



                  </el-col>
                </el-row>

                <el-row>
                  <el-col :span="14" :offset="5">
                    <div
                      style="color: white; height: 30px; background: #203f6f; margin-top: 10%;border-radius: 15px; padding-top: 3%; padding-left: 5%; padding-right: 5%;">
                      <span style="float:left;">Total</span>
                      <span style="float:right;">THB</span>
                      <span style="float:right;">70.00</span>

                    </div>
                  </el-col>

                </el-row>

              </el-col>
            </el-row>
          </div>

        </el-col>
        <el-col :span="11" :offset="2" style="border-radius: 15px; height: 100%;  ">
          <el-row style="background: #f5efe1; height: 40%; border-radius: 15px; ">
            <el-table :data="StockData" style="width: 80%;margin-top: 3%; margin-left: 10%; background-color: #f5efe1;">
              <el-table-column prop="Vol" label="Vol">
              </el-table-column>
              <el-table-column prop="Bid" label="Bid">
              </el-table-column>
              <el-table-column prop="Ask" label="Ask">
              </el-table-column>
            </el-table>
          </el-row>
          <el-row style="background: #f5efe1; height: 50%;margin-top: 4%; border-radius: 15px;">
            <el-table :data="AccountData" style="width: 80%;margin-top: 6%; margin-left: 10%; background: transparent;">
              <el-table-column prop="Balance" label="Balance">
              </el-table-column>
              <el-table-column prop="Order" label="Order">
              </el-table-column>
              <el-table-column prop="InPort" label="in Port">
              </el-table-column>
            </el-table>
          </el-row>
        </el-col>
      </el-row>

    </div>
    <div v-if="showInfo">
      <el-row style="margin-top: 2%;">

        <div style="background: #d9d9d9; border-radius: 30px;">
          <div style="height:500px;padding-top: 1%;  padding-left: 3%;">
            <el-row>
              <span style="font-size:xx-large; font-weight: bold;">Statistics</span>
            </el-row>
            <el-row>
              <el-col :span="11" style=" height: 450px; ">
                <el-row>
                  <span style="float: left; " class="statisticsItem">QuoteType</span>
                  <span style="float: right;" class="statisticsItemValue">7.63B</span>
                </el-row>
                <el-row>
                  <span style="float: left;" class="statisticsItem">Ten Day Average Volume</span>
                  <span style="float: right;" class="statisticsItemValue">7.02B</span>
                </el-row>
                <el-row>
                  <span style="float: left;" class="statisticsItem">Three Month Average Volume</span>
                  <span style="float: right;" class="statisticsItemValue">11.47</span>
                </el-row>
                <el-row>
                  <span style="float: left;" class="statisticsItem">Two Hundred Day Average</span>
                  <span style="float: right;" class="statisticsItemValue">N/A</span>
                </el-row>
                <el-row>
                  <span style="float: left;" class="statisticsItem">Year Change)</span>
                  <span style="float: right;" class="statisticsItemValue">N/A</span>
                </el-row>
                <el-row>
                  <span style="float: left;" class="statisticsItem">Year High</span>
                  <span style="float: right;" class="statisticsItemValue">0.87</span>
                </el-row>
                <el-row>
                  <span style="float: left;" class="statisticsItem">Year Low</span>
                  <span style="float: right;" class="statisticsItemValue">5.18</span>
                </el-row>
                <el-row>
                  <span style="float: left;" class="statisticsItem">Shares</span>
                  <span style="float: right;" class="statisticsItemValue">0.79</span>
                </el-row>
                <el-row>
                  <span style="float: left; font-size:20px" class="statisticsItem">holders</span>
                </el-row>
                <el-row>
                <span>                         0   1</span>
                </el-row>
                <el-row>
                      <span>0           Previous Close NaN</span>
                </el-row>
                
              </el-col>
            </el-row>


          </div>
        </div>
      </el-row>
      <el-row style="margin-top: 2%;">
        <div style="background: #d9d9d9; border-radius: 30px;">
          <span style="font-size:xx-large; font-weight: bold; margin-left:3%;margin-top:2%">Historical Data</span>
          <div ref="candleChart" style="height:400px;"></div>

          
        </div>
      </el-row>
      <el-row style="margin-top: 2%;background: #d9d9d9; border-radius: 30px;">
        <span style="font-size:xx-large; font-weight: bold; margin-left:3%;margin-top:2%">Company Profile</span>
        <h2 style="margin-left:3%">Wice Logistics Public Company Limited</h2>
        <el-row>
            <el-col :span="10">
              <span style="margin-left:8%">88/8 Nonsee Road</span>
            </el-col>
            <el-col :span="10">
              <span>Sector(s): Industrials</span>
            </el-col>
            <el-col :span="10">
              <span style="margin-left:8%">Chong-Nonsee Yannawa</span>
            </el-col>
            <el-col :span="10">
              <span>Industry: Integrated Freight & Logistics</span>
            </el-col>
            <el-col :span="10">
              <span style="margin-left:8%">Bangkok 10120</span>
            </el-col>
            <el-col :span="10">
              <span>Full Time Employees: </span>
            </el-col>
        </el-row> 
        <el-row :span="10">
          <span style="margin-left:3%">Thailand</span>
        </el-row>
        <el-row :span="10">
          <span style="margin-left:3%">66 2 681 6181</span>
        </el-row>
        <el-row :span="10">
          <el-link style="margin-left:3%">https://www.wice.co.th</el-link>
        </el-row>
        <el-row>
          <h3 style="font-weight: bold; margin-left:3%;margin-top:2%">Description</h3>
        </el-row>
        <el-row style="margin-left:3%;margin-right:4%">
          <span >Wice Logistics Public Company Limited provides air and sea freight forwarding, customs brokerage, inland transportation, cross-border and multimodal transportation, warehousing, and various freight related services for imports and exports in Thailand and internationally. It operates through Sea Freight, Air Freight, Cross Border Service, and Service Supply Chain Solutions. The company transports sea freight comprising full container load and less than container load services for various forwarders and containers; and offers air freight services. It also provides customs clearance services, including duty intensive consultation; internal transportation services using trailer and dump trucks, lorries, or minivans from pick up point to the port; and warehouse storage and management services. The company was formerly known as Wice Freight Services (Thailand) Company Limited and changed its name to Wice Logistics Public Company Limited in April 2015. Wice Logistics Public Company Limited was founded in 1993 and is headquartered in Bangkok, Thailand.</span>
        </el-row>
        <el-row style="font-weight: bold; margin-left:3%;margin-top:2%">
          <h3 >Corporate Governance</h3>
        </el-row>
        <el-row style="margin-left:3%;margin-right:4%">
          <span >Wice Logistics Public Company Limited’s ISS Governance QualityScore as of N/A is N/A. The pillar scores are Audit: N/A; Board: N/A; Shareholder Rights: N/A; Compensation: N/A. </span>
        </el-row>
        <el-row style="margin-left:3%;margin-right:4%;margin-top:1%">
          <span >Corporate governance scores courtesy of Institutional Shareholder Services (ISS). Scores indicate decile rank relative to index or region. A decile score of 1 indicates lower governance risk, while a 10 indicates higher governance risk.</span>
        </el-row>

      </el-row>
    </div>
  </div>


</template>
<style>
.input:focus {
  border: 0;
  /*这里你可以自己调节边框样式*/
}

.dataSummaryItem {
  margin-top: 1%;
  margin-bottom: 1%;
  font-size: large;
  font-weight: bold;
}

.statisticsItem {
  margin-top: 7px;
  margin-bottom: 7px;
  font-size: medium;
  font-weight: bold;
}

.el-table th.el-table__cell {
    overflow: hidden;
    -webkit-user-select: none;
    -moz-user-select: none;
    user-select: none;
    background-color: #f5efe1;
}

.el-table tr {
    background-color: #f5efe1;
}

.statisticsItemValue {

  font-size: medium;
  font-weight: bold;
}


.dataSummaryItemValue {
  color: #1930dc;
  font-size: large;
  font-weight: bold;
}
</style>

<script>
import * as echarts from 'echarts';

export default {
  data() {
    return {
      nowTime: '',
      chart: null,
      showInfo: false,
      StockData: [{
        Vol: 12.00,
        Bid: 11.90,
        Ask: 12.00
      }],
      AccountData: [{
        Balance: "18800",
        Order: "-",
        InPort: 100
      }],
    };
  },
  mounted() {
    this.initChart();
    this.createCandleChart();
    this.getNowTime();
  },
  methods: {
    createCandleChart() {
      let candleChart = this.$echarts.init(this.$refs.candleChart)
      let option2 = {
        xAxis: {
          type: 'category',
          data: ['2022/12/19', '2022/12/19', '2022/12/19', '2022/12/19', '2022/12/19', '2022/12/19', '2022/12/19']
        },
        yAxis: {
          type: 'value',
        
        },
        series: [{
          type: 'candlestick',
          data: [
            [2320.26, 2320.26, 2287.3, 2362.94],
            [2300, 2291.3, 2288.26, 2308.38],
            [2295.35, 2346.5, 2295.35, 2346.92],
            [2347.22, 2358.98, 2337.35, 2363.8],
            [2360.75, 2382.48, 2347.89, 2383.76],
            [2383.43, 2385.42, 2371.23, 2391.82],
            [2377.41, 2419.02, 2369.57, 2421.15],
            [2425.92, 2428.15, 2417.58, 2440.38],
            [2411, 2433.13, 2403.3, 2437.42],
            [2432.68, 2434.48, 2427.7, 2441.73],
            [2430.69, 2418.53, 2394.22, 2433.89],
            [2416.62, 2432.4, 2414.4, 2443.03],
            [2441.91, 2421.56, 2415.43, 2444.8],
            [2420.26, 2427.93, 2414.01, 2440.98],
            [2425.99, 2406.96, 2404.51, 2426.41],
            [2405.48, 2391.4, 2365.65, 2405.9],
            [2397.67, 2397.29, 2370.61, 2397.93],
            [2378.04, 2425.76, 2376.08, 2436.03],
            [2433.61, 2434.45, 2419.04, 2452.72],
            [2432.4, 2446.65, 2429.67, 2450.5],
            [2446.91, 2440.58, 2420.05, 2448.97],
            [2440.54, 2465.27, 2440.54, 2468.88],
            [2445.76, 2448.96, 2439.38, 2457.57],
            [2447.93, 2448.36, 2432.52, 2458.07],
            [2433.49, 2434.9, 2427.17, 2435.76],
            [2429.13, 2416.63, 2414.4, 2429.37],
            [2418.21, 2415.25, 2406.01, 2419.57],
            [2412.33, 2434.3, 2411.68, 2442.68],
            [2433.89, 2431.04, 2424.06, 2440.1],
            [2432.04, 2416.43, 2407.65, 2432.72],
            [2416.93, 2416.93, 2407.7, 2430.57],
            [2417.63, 2417.29, 2405.08, 2425.93]
          ],
          itemStyle: {
            normal: {
              color: '#f7a35c',
              color0: '#00a65a',
              borderColor: '#f7a35c',
              borderColor0: '#00a65a'
            }
          }
        }]
      }
      candleChart.setOption(option2)
    },
    ShowBuyAndSell(){
        this.showInfo = false;
    },
    ShowStockInfo(){
      this.showInfo = true;
    },
    initChart() {
      this.chart = echarts.init(document.getElementById("chart"));
      this.chart.setOption({
        title: {
          text: "Stock Real-Time Price"
        },
        xAxis: {
          type: "category",
          data: ["10:00", "10:05", "10:10", "10:15", "10:20", "10:25"]
        },
        yAxis: {
          type: "value",
          min: 0,
          max:500,

          
        },
        series: [
          {
            data: [120, 230, 300, 279, 166, 450],
            type: "line",
            smooth: false
          }
        ]
      });
    },
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
  }
};
</script>
