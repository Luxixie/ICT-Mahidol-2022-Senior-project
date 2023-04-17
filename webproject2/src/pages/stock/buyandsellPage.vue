<template>
  <div style="margin:2%;">
    <el-row style="height: 200px;">
      <el-col :span="12">
        <el-row style="height: 30%; overflow: auto;">
          <span style="font-size: xx-large; color:#f5efe1;margin-left:2%">{{tickerName}}</span>
        </el-row>
        <el-row style="height: 30%;">
          <span style="font-size: x-large; color:#f5efe1;margin-left:2%">{{companyInfo.name}}</span>
        </el-row>
        <el-row style="height: 30%;">
          <el-button style="margin-top: 3%;border-radius: 35px;margin-left:1%" type="warning" icon="el-icon-star-off"  @click="Addwatchlist(tickerName)">Add to Watch
            list</el-button>
          <el-button style="margin-top: 3%;border-radius: 35px;" type="warning" @click="ShowBuyAndSell" > Buy / Sell
          </el-button>
          <el-button style="margin-top: 3%;border-radius: 35px;" type="warning" @click="ShowStockInfo"> Stock
            Infomation </el-button>
        </el-row>
      </el-col>
      <el-col :span="12" style="margin-top:2%">
        <el-row>
          <el-col :span="8" :offset="8">
            <span style="font-size: xx-large; color:#f5efe1;">{{lastprice | numberWithCommas }}</span>
          </el-col>

        </el-row>
        <el-row style="height: 30%;">
          <el-col :span="8" :offset="6">
            <span style="font-size: x-large; color:#f5efe1;margin-left: 10%;">
              {{ (lastprice - previousclose) >= 0 ? '+' : '-' }}{{ Math.abs(lastprice - previousclose).toFixed(2) }} ({{((lastprice / previousclose-1)*100).toFixed(2)}}%)
            </span>
            
        </el-col>
        </el-row>
        <el-row style="height: 30%;">
          <el-col :span="12" :offset="5">
            <span style="font-size:small; color:#f5efe1;">Market Status:{{ nowTime }}</span>
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
          <div style="padding-top: 8%;  padding-left: 6%;padding-bottom: 12%;padding-right: 6%;">
            <el-row>
              <span style="font-size: x-large; padding-bottom: 2%; margin-top:2%">Data Summary</span>
            </el-row>
            <el-row class="dataSummaryItem"> 
              <span>Previous close: </span>
              <span class="dataSummaryItemValue">{{previousclose}}</span>
            </el-row>

            <el-row class="dataSummaryItem">
              <span>High: </span>
              <span class="dataSummaryItemValue" >{{dayhigh | numberWithCommas}}</span>
            </el-row>
            <el-row class="dataSummaryItem">
              <span>Low: </span>
              <span class="dataSummaryItemValue" >{{daylow | numberWithCommas}}</span>
            </el-row>
            <el-row class="dataSummaryItem">
              <span>Open: </span>
              <span class="dataSummaryItemValue" >{{open | numberWithCommas}}</span>
            </el-row>
            <el-row class="dataSummaryItem">
              <span>Volume: </span>
              <span class="dataSummaryItemValue"> {{lastvolume | numberWithCommas}}</span>
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
             <el-radio-group v-model="action">
                <el-radio-button label="Buy"></el-radio-button>
                <el-radio-button label="Sell"></el-radio-button>
                
              </el-radio-group>
            </el-row>
            <el-row style="padding-bottom: 2%; margin-top: 2%; border-radius: 12px; background: #f5efe1;">
              <el-col :span="12" style=" height: 100%;">
                <el-row style="margin-top:15%; margin-bottom: 5%; margin-left: 7%;">
                  <span :span="5" style="font-size:medium;">Volume</span>
                  <button :span="3" size="mini" style="margin-left: 2%;  border: 0px;" @click="volumes -= 100">-</button>
                  <el-input
        
                    style="outline: none; margin-left: 5%; margin-right: 5%; border-color: transparent; width: 50%; "
                    placeholder="input the volume" 
                    v-model.number="volumes"></el-input> 
                  <button :span="3" size="mini" style="background: #f8bd9e; border: 0px;"  @click="volumes += 100" >+</button>
                  <span v-if="priceError" style="color: red; margin-left:2%;margin-top: 5%;">{{ priceError }}</span>
                </el-row>

                <el-row style="margin-left: 10%; margin-top: 10%;">
                  <el-button round style="background: #203f6f; color: white;"        
                              @click="Calvolume(0.25)">1/4</el-button>
                  <el-button round style="background: #203f6f; color: white;"
                              
                              @click="Calvolume(0.5)">1/2</el-button>
                  <el-button round style="background: #203f6f; color: white;"
                      
                              @click="Calvolume(1)">ALL</el-button>
                </el-row>
                <el-row>
                  <el-col :span="8" :offset="6" style="margin-top: 10%;">
                    <el-button round type="warning" style="color: black;" v-on:click="simulation()" >Simulation of {{action}}</el-button>
                  </el-col>
                </el-row>
              </el-col>
              <el-col :span="12" style="height: 100%; ">
                <el-row>
                  <el-col :span="12" :offset="6" style="margin-top: 10%; ">
                    <div
                      style="height: 30px; background: #dfd4dd; border-radius: 15px; padding-top: 4%; padding-left: 5%; padding-right: 5%;">
                      <span style="float:left;">Current</span>
                      <span style="float:right;">{{lastprice | numberWithCommas}}</span>
                    </div>

                    <div
                      style="height: 30px;  margin-top: 10%; background: #dfd4dd; border-radius: 15px; padding-top: 4%; padding-left: 5%; padding-right: 5%;">
                      <span style="float:left;">High</span>
                      <span style="float:right;">{{dayhigh | numberWithCommas}}</span>
                    </div>

                    <div
                      style="height: 30px; background: #dfd4dd; margin-top: 10%;border-radius: 15px; padding-top: 4%; padding-left: 5%; padding-right: 5%;">
                      <span style="float:left;">Low</span>
                      <span style="float:right;">{{daylow | numberWithCommas}}</span>
                    </div>



                  </el-col>
                </el-row>

                <el-row>
                  <el-col :span="18" :offset="5">
                    <div
                      style="color: white; height: 30px; background: #203f6f; margin-top: 13%;border-radius: 15px; padding-top: 3%; padding-left:2%; padding-right: 2%;">
                      <span style="float:left;">Total: </span>
                      <span style="float:right;">THB</span>
                      <span style="float:right;">{{(lastprice * volumes).toFixed(2) | numberWithCommas}}</span>

                    </div>
                  </el-col>

                </el-row>

              </el-col>
            </el-row>
          </div>

        </el-col>
        <el-col :span="11" :offset="2" style="border-radius: 15px; height: 100%;  ">
          <el-row style="background: #f5efe1;margin-top: 1%; border-radius: 15px;">
            <el-table :data="AccountData" style="width: 80%;margin-top: 6%; margin-left: 10%; background: transparent;">
              <el-table-column fixed prop="Balance" label="Balance" align="center">
              </el-table-column>
              <el-table-column prop="Order" label="Order" align="center">
              </el-table-column>
              <el-table-column prop="Inport" label="In Port" align="center">
              </el-table-column>
            </el-table>
          </el-row>
          <el-row style="background: #f5efe1;margin-top: 1%; border-radius: 15px;">
            <el-table
                    :key="isupdate"
                    :data="tableData2"
                    style="width: 100%"
                    border
                    height="150">
                    <el-table-column
                        prop="transactionid"
                        label="No."
                        >
                    </el-table-column>
                    <el-table-column
                        prop="shares"
                        label="Vol">
                    </el-table-column>
                    <el-table-column
                    prop="stockprice"
                        label="Price">
                    </el-table-column>
                    <el-table-column
                        prop="cost"
                        label="Cost">
                    </el-table-column>
                    </el-table>
          </el-row>
          <el-row style="background: #f5efe1; margin-top:1%; border-radius: 15px; ">

          </el-row>
        </el-col>
        
      </el-row>

    </div>
    <div v-if="showInfo">
      <el-row style="margin-top: 2%;">

        <div style="background: #d9d9d9; border-radius: 30px;">
          <div style=" padding-top: 1%; padding-bottom: 1%; padding-left: 3%;">
            <el-row>
              <span style="font-size:xx-large; font-weight: bold;">Statistics</span>
            </el-row>
            <el-row>
              <el-col :span="10" >
                <el-row>
                  <span style="float: left; " class="statisticsItem">QuoteType</span>
                  <span style="float: right;" class="statisticsItemValue">{{QuoteType}}</span>
                </el-row>
                <el-row>
                  <span style="float: left;" class="statisticsItem">Ten Day Average Volume</span>
                  <span style="float: right;" class="statisticsItemValue">{{TenDayAverageVolume | numberWithCommas }}</span>
                </el-row>
                <el-row>
                  <span style="float: left;" class="statisticsItem">Three Month Average Volume</span>
                  <span style="float: right;" class="statisticsItemValue">{{ThreeMonthAverageVolume | numberWithCommas }}</span>
                </el-row>
                <el-row>
                  <span style="float: left;" class="statisticsItem">Two Hundred Day Average</span>
                  <span style="float: right;" class="statisticsItemValue">{{TwoHundredDayAverage | numberWithCommas }}</span>
                </el-row>
              </el-col>
              <el-col :span="10" :offset="3">
                <el-row >
                  <span style="float: left;" class="statisticsItem">Year Change</span>
                  <span style="float: right;" class="statisticsItemValue">{{YearChange | numberWithCommas }}</span>
                </el-row>
                <el-row>
                  <span style="float: left;" class="statisticsItem">Year High</span>
                  <span style="float: right;" class="statisticsItemValue">{{YearHigh | numberWithCommas }}</span>
                </el-row>
                <el-row>
                  <span style="float: left;" class="statisticsItem">Year Low</span>
                  <span style="float: right;" class="statisticsItemValue">{{YearLow | numberWithCommas }}</span>
                </el-row>
                <el-row>
                  <span style="float: left;" class="statisticsItem">Shares</span>
                  <span style="float: right;" class="statisticsItemValue">{{Shares | numberWithCommas }}</span>
                </el-row>
              </el-col>
            </el-row>


          </div>
        </div>
      </el-row>
      <el-row style="margin-top: 2%;">
        <div style="background: #d9d9d9; border-radius: 30px;">
          <span style="font-size:xx-large; font-weight: bold; margin-left:3%;margin-top:2%">Historical Data</span>
          <!-- <div ref="candleChart" style="height:400px;"></div>
            <el-table :data="tableData" border style="width: 100%">
              <el-table-column
                  prop="Datetime"
                  label="Datetime"
                  align="center"
                  :v-model="tableData.Datetime">
              </el-table-column>
              <el-table-column
                  prop="Open"
                  label="Open"
                  align="center">
              </el-table-column> -->

              <!-- <el-table-column
                  prop="High"
                  label="High"
                  align="center">
              </el-table-column>
              <el-table-column
                  prop="Low"
                  label="Low"
                  align="center">
              </el-table-column>
              <el-table-column
                  prop="Close"
                  label="Close"
                  align="center">
              </el-table-column>
              <el-table-column
                  prop="Adj Close"
                  label="Adj Close"
                  align="center">
              </el-table-column>
              <el-table-column
                  prop="Volume"
                  label="Volume"
                  align="center">
              </el-table-column>
              </el-table> -->

          
        </div>
      </el-row>
      <el-row style="margin-top: 2%;background: #d9d9d9; border-radius: 30px;padding-bottom: 1%;">
        <h1 style="font-size:xx-large; font-weight: bold; margin-left:3%;margin-top:1%">Company Profile</h1>
        <h2 style="margin-left:3%;margin-top:1%">{{companyInfo['name']}}</h2>
        <span style="margin-left:3%">Address: {{companyInfo['address']}}</span>
        <el-row>
            <el-col :span="10">
              <span style="margin-left:7%;margin-top:1%">Industry: {{companyInfo['industry']}}</span>
            </el-col>
            <el-col :span="10">
              <span style="margin-left:7%;margin-top:1%">Sector(s): {{companyInfo['sector']}}</span>
            </el-col>
            <el-col :span="10">
              <span style="margin-left:7%;margin-top:1%">Phone: {{companyInfo['phone']}}</span>
            </el-col>
            <el-col :span="10">
              <span style="margin-left:7%;margin-top:1%">Website: {{companyInfo['website']}} </span>
            </el-col>
        </el-row> 
        <el-row>
          <h3 style="font-weight: bold; margin-left:3%;margin-top:2%">Description</h3>
        </el-row>
        <el-row style="margin-left:3%;margin-right:4%">
          <span style="margin-left:3%">{{companyInfo['description']}}</span>
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
  margin-top: 4%;
  margin-bottom: 1%;
  font-size: large;
  font-weight: bold;
}

.statisticsItem {
  margin-top: 3%;
  margin-bottom: 1%;
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
  margin-top: 3%;
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
import axios from 'axios'

export default {
  data() {
    return {
      isupdate:true,
      tickerName:'',
      balance:0,
      companyInfo:{},
      lastprice:'',
      previousclose:'',
        dayhigh:'',
        daylow:'',
        exchange:'',
        lastvolume:'',
        open:'',
        QuoteType:'',
        TenDayAverageVolume:'',
        ThreeMonthAverageVolume:'',
        TwoHundredDayAverage:'',
        YearChange:'',
        YearHigh:'',
        YearLow:'',
        Shares:'',  
      totalprice:'',
      volume: 0.25,
      volumes:0,
      statistics:[],      
      action:"Buy",
      nowTime: '',
      chart: null,
      showInfo: false,
      AccountData:[],
      tableData2:[],
      inport:0
    };
  },
  computed: {
    priceError() {
      if (!this.volumes || isNaN(this.volumes) || this.volumes <= 0) {
        return "Please enter a valid volume";
      }
      return null;
    },

  },
  watch: {
  volumes(newVal) {
    this.totalprice = (newVal * this.lastprice).toFixed(2)
     
  }
  },
  mounted() {
    this.getNowTime();
    this.initChart();
    this.createCandleChart();
  },
  methods: {
    Calvolume(percentage){
       console.log(percentage)
      if(this.action === "Buy"){
         var balance = parseFloat(this.balance)
       console.log(balance)
       var currentprice = parseFloat(this.lastprice)
       console.log(currentprice)
       if(balance < currentprice){
         this.volumes = 0
         alert("you dont have  enough balance")
       }
       else{
          var enablevolumes = balance / currentprice
          console.log(enablevolumes)
          this.volumes  = parseInt(enablevolumes * percentage)
       }
      }
      else{
          var inport = this.inport
          var volumes = this.volumes
          if(volumes > inport){
              this.volumes = 0
              alert("you dont have enough volumes for sell")
          }
          else{
             this.volumes = parseInt(inport * percentage)
          }
        
       }
       
    },
    Addwatchlist(tickerName){
      console.log(tickerName)

      console.log(this.$store.state.accountid)
      var id = this.$store.state.accountid
      var result = {
        tickerName: tickerName,
        accountid: id
      }
      axios.post('http://127.0.0.1:8088/AddToWatchlist', result).then((res)=>{
                console.log(res.data)
            })


         
    },
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
    
    buyStock(){
      console.log("buyStock called");
      var id = this.$store.state.accountid
      console.log(id)
      var stockprice = this.lastprice
      console.log(stockprice)
      var tickerName = this.$route.params.tickerName
      console.log(tickerName)
      var shares = this.volumes
      console.log(shares)
      var action = this.action
      console.log(action)
      var cost = this.totalprice
      console.log(cost)
      var buydata = {
        AccountId: id , 
        ticker: tickerName,
        stockprice: stockprice , 
        shares: shares, 
        action: action, 
        cost:cost,
      }
      if(parseFloat(cost) >parseFloat(this.balance)){
        alert("you dont have enough balance")
        return
      }
      console.log(buydata)
      var id = this.$store.state.accountid
      console.log(id)
      var tickerName = this.$route.params.tickerName
      var req = {
          accountid:id,
          ticker: tickerName
      }
      axios.post("http://127.0.0.1:8088/BuyStock",buydata).then((res) => {
        console.log(res)
        //this.AccountData = res.data
        this.AccountData = []
        var balance = res.data.Balance.toFixed(2);
        this.balance = balance;
        this.inport = parseInt(res.data['Inport'])
        var data = {
          "Balance": balance,
          "Order": res.data['Order'],
          "Inport": res.data['Inport']
        }
        this.AccountData.push(data)
        });
      axios.post("http://127.0.0.1:8088/GetonelHistory",req).then((res) => {
            console.log(res)
            this.tableData2 = []
            res.data.forEach(data => {
              this.tableData2.push(data)
            });
            this.isupdate = !this.isupdate

        })
      
    },
    SellStock(){
      console.log("SellStock called");
      var id = this.$store.state.accountid
      console.log(id)
      var currentprice = this.lastprice
      console.log(currentprice)
      var tickerName = this.$route.params.tickerName
      console.log(tickerName)
      var volume = this.volumes
      console.log(volume)
      var action = this.action
      console.log(action)
      var cost = this.totalprice
      console.log(cost)
      var selldata = {
        accountid: id , 
        ticker: tickerName,
        currentprice: currentprice , 
        volume: volume, 
        action: action, 
        cost:cost,
      }
      if(volume > this.inport){
        alert("you dont have enough volume for sell")
        return
      }
      console.log(selldata)
      axios.post("http://127.0.0.1:8088/SellStock",selldata).then((res) => {
            console.log(res)
            //this.AccountData = res.data
            this.AccountData = []
            var balance = res.data.Balance.toFixed(2);
            this.balance = balance
            this.inport = parseInt(res.data['Inport'])
            var data = {
              "Balance": balance,
              "Order": res.data['Order'],
              "Inport": res.data['Inport']
            }
            this.AccountData.push(data)
      });
      var id = this.$store.state.accountid
      console.log(id)
      var tickerName = this.$route.params.tickerName
      var req = {
          accountid:id,
          ticker: tickerName
      }
      axios.post("http://127.0.0.1:8088/GetonelHistory",req).then((res) => {
            console.log(res)
            this.tableData2 = res.data
             this.isupdate = !this.isupdate
        })
      
    },

    simulation(){
      console.log('simulation() called');
      
      var action = this.action;
      console.log(action)
       if(action === "Buy"){
         this.buyStock()
       }
       else{
         this.SellStock()
       }
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
      console.log(this.$route.params.tickerName) 
       var tickerName = this.$route.params.tickerName
       this.tickerName = tickerName
       axios.post("http://127.0.0.1:8088/marketinform/"+tickerName).then((res) => {
          console.log(res.data)
          this.dayhigh = res.data['dayhigh']
          this.daylow = res.data['daylow']
          this.lastprice = res.data['lastprice']
          this.previousclose = res.data['previousclose']
          this.lastvolume = res.data['lastvolume']
          this.open = res.data['open']
          this.QuoteType = res.data['QuoteType']
          this.TenDayAverageVolume = res.data['TenDayAverageVolume']
          this.ThreeMonthAverageVolume = res.data['ThreeMonthAverageVolume']
          this.TwoHundredDayAverage  =res.data['TwoHundredDayAverage']
          this.YearChange = res.data['YearChange']
          this.YearHigh = res.data['YearHigh']
          this.YearLow = res.data['YearLow']
          this.Shares = res.data['Shares']
          this.companyInfo = res.data['Company']
          console.log(this.companyInfo)


        });     
      var id = this.$store.state.accountid
      console.log(id)
      var tickerName = this.$route.params.tickerName
      var req = {
          accountid:id,
          ticker: tickerName
      }
      axios.post("http://127.0.0.1:8088/GetPurchaseinfor",req).then((res) => {
          var balance = res.data.Balance.toFixed(2);
          console.log(res)
          this.balance = balance
          this.inport = parseInt(res.data['Inport'])
          console.log(this.inport)
          var data = {
              "Balance": balance,
              "Order": res.data['Order'],
              "Inport": res.data['Inport']
            }
          console.log(data)
          this.AccountData.push(data)
      })
      var tickerName = this.$route.params.tickerName
      var res = {
          ticker: tickerName
      }
      // axios.post("http://127.0.0.1:8088/Getstockprice",res).then((res) => {
      //       console.log(res.data)
      //       this.high = res.data['dayhigh']
      //       this.low = res.data['daylow']
      //       this.current = res.data['lastprice']
      //       this.previousclose = res.data['previousclose']
      //   });

      axios.post("http://127.0.0.1:8088/GetonelHistory",req).then((res) => {
            console.log(res)
            this.tableData2 = res.data
             this.isupdate = !this.isupdate
        })

      

    }


};
</script>
