<template>
  <div style="margin: 2%">
    <el-row style="height: 200px">
      <el-col :span="12">
        <el-row style="height: 30%; overflow: auto">
          <span style="font-size: xx-large; color: #f5efe1; margin-left: 2%">{{
            tickerName
          }}</span>
        </el-row>
        <el-row style="height: 30%">
          <span style="font-size: x-large; color: #f5efe1; margin-left: 2%">{{
            companyInfo.name
          }}</span>
        </el-row>
        <el-row style="height: 30%">
          <el-button
            style="margin-top: 3%; border-radius: 35px; margin-left: 1%"
            type="warning"
            icon="el-icon-star-off"
            @click="Addwatchlist(tickerName)"
            >Add to Watch list</el-button
          >
          <el-button
            style="margin-top: 3%; border-radius: 35px"
            type="warning"
            @click="ShowBuyAndSell"
          >
            Buy / Sell
          </el-button>
          <el-button
            style="margin-top: 3%; border-radius: 35px"
            type="warning"
            @click="ShowStockInfo"
          >
            Stock Infomation
          </el-button>
        </el-row>
      </el-col>
      <el-col :span="12" style="margin-top: 2%">
        <el-row>
          <el-col :span="8" :offset="8">
            <span style="font-size: xx-large; color: #f5efe1">{{
              lastprice | numberWithCommas
            }}</span>
          </el-col>
        </el-row>
        <el-row style="height: 30%">
          <el-col :span="8" :offset="6">
            <span style="font-size: x-large; color: #f5efe1; margin-left: 10%">
              {{ lastprice - previousclose >= 0 ? "+" : "-"
              }}{{ Math.abs(lastprice - previousclose).toFixed(2) }} ({{
                ((lastprice / previousclose - 1) * 100).toFixed(2)
              }}%)
            </span>
          </el-col>
        </el-row>
        <el-row style="height: 30%">
          <el-col :span="12" :offset="5">
            <span style="font-size: small; color: #f5efe1"
              >Market Status:{{ nowTime }}</span
            >
          </el-col>
        </el-row>
      </el-col>
    </el-row>
    <el-row>
      <el-col :span="14">
        <div style="background: #d9d9d9; border-radius: 30px">
          <div
            id="chart"
            style="height: 300px; padding-top: 3%; padding-left: 3%"
          ></div>
        </div>
      </el-col>
      <el-col :span="6" :offset="1">
        <div style="background: #d9d9d9; border-radius: 30px">
          <div
            style="
              padding-top: 8%;
              padding-left: 6%;
              padding-bottom: 12%;
              padding-right: 6%;
            "
          >
            <el-row>
              <span
                style="font-size: x-large; padding-bottom: 2%; margin-top: 2%"
                >Data Summary</span
              >
            </el-row>
            <el-row class="dataSummaryItem">
              <span>Previous close: </span>
              <span class="dataSummaryItemValue">{{ previousclose }}</span>
            </el-row>

            <el-row class="dataSummaryItem">
              <span>High: </span>
              <span class="dataSummaryItemValue">{{
                dayhigh | numberWithCommas
              }}</span>
            </el-row>
            <el-row class="dataSummaryItem">
              <span>Low: </span>
              <span class="dataSummaryItemValue">{{
                daylow | numberWithCommas
              }}</span>
            </el-row>
            <el-row class="dataSummaryItem">
              <span>Open: </span>
              <span class="dataSummaryItemValue">{{
                open | numberWithCommas
              }}</span>
            </el-row>
            <el-row class="dataSummaryItem">
              <span>Volume: </span>
              <span class="dataSummaryItemValue">
                {{ lastvolume | numberWithCommas }}</span
              >
            </el-row>
          </div>
        </div>
      </el-col>
    </el-row>

    <div v-if="!showInfo">
      <el-row style="margin-top: 2%; height: 400px">
        <el-col :span="11" style="border-radius: 15px; height: 100%">
          <div style="margin-left: 4%; margin-right: 4%">
            <el-row>
              <el-radio-group v-model="action">
                <el-radio-button label="Buy"></el-radio-button>
                <el-radio-button label="Sell"></el-radio-button>
              </el-radio-group>
            </el-row>
            <el-row
              style="
                padding-bottom: 2%;
                margin-top: 2%;
                border-radius: 12px;
                background: #f5efe1;
              "
            >
              <el-col :span="12" style="height: 100%">
                <el-row
                  style="margin-top: 15%; margin-bottom: 5%; margin-left: 7%"
                >
                  <span :span="5" style="font-size: medium">Volume</span>
                  <button
                    :span="3"
                    size="mini"
                    style="margin-left: 2%; border: 0px"
                    @click="volumes -= 100"
                  >
                    -
                  </button>
                  <el-input
                    style="
                      outline: none;
                      margin-left: 5%;
                      margin-right: 5%;
                      border-color: transparent;
                      width: 50%;
                    "
                    placeholder="input the volume"
                    v-model.number="volumes"
                  ></el-input>
                  <button
                    :span="3"
                    size="mini"
                    style="background: #f8bd9e; border: 0px"
                    @click="volumes += 100"
                  >
                    +
                  </button>
                  <span
                    v-if="priceError"
                    style="color: red; margin-left: 2%; margin-top: 5%"
                    >{{ priceError }}</span
                  >
                </el-row>

                <el-row style="margin-left: 10%; margin-top: 10%">
                  <el-button
                    round
                    style="background: #203f6f; color: white"
                    @click="Calvolume(0.25)"
                    >1/4</el-button
                  >
                  <el-button
                    round
                    style="background: #203f6f; color: white"
                    @click="Calvolume(0.5)"
                    >1/2</el-button
                  >
                  <el-button
                    round
                    style="background: #203f6f; color: white"
                    @click="Calvolume(1)"
                    >ALL</el-button
                  >
                </el-row>
                <el-row>
                  <el-col :span="8" :offset="6" style="margin-top: 10%">
                    <el-button
                      round
                      type="warning"
                      style="color: black"
                      v-on:click="simulation()"
                      >Simulation of {{ action }}</el-button
                    >
                  </el-col>
                </el-row>
              </el-col>
              <el-col :span="12" style="height: 100%">
                <el-row>
                  <el-col :span="12" :offset="6" style="margin-top: 10%">
                    <div
                      style="
                        height: 30px;
                        background: #dfd4dd;
                        border-radius: 15px;
                        padding-top: 4%;
                        padding-left: 5%;
                        padding-right: 5%;
                      "
                    >
                      <span style="float: left">Current</span>
                      <span style="float: right">{{
                        lastprice | numberWithCommas
                      }}</span>
                    </div>

                    <div
                      style="
                        height: 30px;
                        margin-top: 10%;
                        background: #dfd4dd;
                        border-radius: 15px;
                        padding-top: 4%;
                        padding-left: 5%;
                        padding-right: 5%;
                      "
                    >
                      <span style="float: left">High</span>
                      <span style="float: right">{{
                        dayhigh | numberWithCommas
                      }}</span>
                    </div>

                    <div
                      style="
                        height: 30px;
                        background: #dfd4dd;
                        margin-top: 10%;
                        border-radius: 15px;
                        padding-top: 4%;
                        padding-left: 5%;
                        padding-right: 5%;
                      "
                    >
                      <span style="float: left">Low</span>
                      <span style="float: right">{{
                        daylow | numberWithCommas
                      }}</span>
                    </div>
                  </el-col>
                </el-row>

                <el-row>
                  <el-col :span="18" :offset="5">
                    <div
                      style="
                        color: white;
                        height: 30px;
                        background: #203f6f;
                        margin-top: 13%;
                        border-radius: 15px;
                        padding-top: 3%;
                        padding-left: 2%;
                        padding-right: 2%;
                      "
                    >
                      <span style="float: left">Total: </span>
                      <span style="float: right">THB</span>
                      <span style="float: right">{{
                        (lastprice * volumes).toFixed(2) | numberWithCommas
                      }}</span>
                    </div>
                  </el-col>
                </el-row>
              </el-col>
            </el-row>
          </div>
        </el-col>
        <el-col
          :span="11"
          :offset="2"
          style="border-radius: 15px; height: 100%"
        >
          <el-row
            style="background: #f5efe1; margin-top: 1%; border-radius: 15px"
          >
            <el-table
              :data="AccountData"
              style="
                width: 80%;
                margin-top: 6%;
                margin-left: 10%;
                background: transparent;
              "
            >
              <el-table-column
                fixed
                prop="Balance"
                label="Balance"
                align="center"
              >
              </el-table-column>
              <el-table-column prop="Order" label="Order" align="center">
              </el-table-column>
              <el-table-column prop="Inport" label="In Port" align="center">
              </el-table-column>
            </el-table>
          </el-row>
          <el-row
            style="background: #f5efe1; margin-top: 1%; border-radius: 15px"
          >
            <el-table
              :key="isupdate"
              :data="tableData2"
              style="width: 100%"
              border
              height="150"
            >
              <el-table-column type="index" label="No." width="180">
              </el-table-column>
              <el-table-column prop="shares" label="Vol"> </el-table-column>
              <el-table-column prop="stockprice" label="Price">
              </el-table-column>
              <el-table-column prop="cost" label="Cost"> </el-table-column>
            </el-table>
          </el-row>
          <el-row
            style="background: #f5efe1; margin-top: 1%; border-radius: 15px"
          >
          </el-row>
        </el-col>
      </el-row>
    </div>
    <div v-if="showInfo">
      <el-row style="margin-top: 2%">
        <div style="background: #d9d9d9; border-radius: 30px">
          <div style="padding-top: 1%; padding-bottom: 1%; padding-left: 3%">
            <el-row>
              <span style="font-size: xx-large; font-weight: bold"
                >Statistics</span
              >
            </el-row>
            <el-row>
              <el-col :span="10">
                <el-row>
                  <span style="float: left" class="statisticsItem"
                    >QuoteType</span
                  >
                  <span style="float: right" class="statisticsItemValue">{{
                    QuoteType
                  }}</span>
                </el-row>
                <el-row>
                  <span style="float: left" class="statisticsItem"
                    >Ten Day Average Volume</span
                  >
                  <span style="float: right" class="statisticsItemValue">{{
                    TenDayAverageVolume | numberWithCommas
                  }}</span>
                </el-row>
                <el-row>
                  <span style="float: left" class="statisticsItem"
                    >Three Month Average Volume</span
                  >
                  <span style="float: right" class="statisticsItemValue">{{
                    ThreeMonthAverageVolume | numberWithCommas
                  }}</span>
                </el-row>
                <el-row>
                  <span style="float: left" class="statisticsItem"
                    >Two Hundred Day Average</span
                  >
                  <span style="float: right" class="statisticsItemValue">{{
                    TwoHundredDayAverage | numberWithCommas
                  }}</span>
                </el-row>
              </el-col>
              <el-col :span="10" :offset="3">
                <el-row>
                  <span style="float: left" class="statisticsItem"
                    >Year Change</span
                  >
                  <span style="float: right" class="statisticsItemValue">{{
                    YearChange | numberWithCommas
                  }}</span>
                </el-row>
                <el-row>
                  <span style="float: left" class="statisticsItem"
                    >Year High</span
                  >
                  <span style="float: right" class="statisticsItemValue">{{
                    YearHigh | numberWithCommas
                  }}</span>
                </el-row>
                <el-row>
                  <span style="float: left" class="statisticsItem"
                    >Year Low</span
                  >
                  <span style="float: right" class="statisticsItemValue">{{
                    YearLow | numberWithCommas
                  }}</span>
                </el-row>
                <el-row>
                  <span style="float: left" class="statisticsItem">Shares</span>
                  <span style="float: right" class="statisticsItemValue">{{
                    Shares | numberWithCommas
                  }}</span>
                </el-row>
              </el-col>
            </el-row>
          </div>
        </div>
      </el-row>
      <el-row style="margin-top: 2%">
        <div style="background: #d9d9d9; border-radius: 30px">
          <span
            style="
              font-size: xx-large;
              font-weight: bold;
              margin-left: 3%;
              margin-top: 2%;
            "
            >Historical Data</span
          >
          <div ref="candleChart" style="height:400px;"></div>
          <el-row style="margin-left:5%">
            <el-col :span="3" style="font-size:20px;"> Time Period:</el-col>
            <el-col :span="1" >
              <el-button type="primary" icon="el-icon-search" v-model="period" @click="handleButtonClick('1wk')">1 Week</el-button>
            </el-col>
            <el-col :span="1" :offset="1">
              <el-button type="primary" icon="el-icon-search" v-model="period" @click="handleButtonClick('1mo')">1 Month</el-button>
            </el-col>
            <el-col :span="1" :offset="1" >
              <el-button type="primary" icon="el-icon-search" v-model="period" @click="handleButtonClick('3mo')">3 Month</el-button>
            </el-col>
            <el-col :span="1" :offset="1">
              <el-button type="primary" icon="el-icon-search" v-model="period" @click="handleButtonClick('1y')">1 Year</el-button>
            </el-col>
            <el-col :span="1" :offset="1">
              <el-button type="primary" icon="el-icon-search" v-model="period" @click="handleButtonClick('5y')">5 Year</el-button>
            </el-col>
          </el-row>
            <el-table :data="historytabledata" height="500" border style="width: 90%; margin-left:5%;">
              <el-table-column
                  prop="time"
                  label="Datetime"
                  align="center"
                  :v-model="historytabledata.Datetime">
              </el-table-column>
              <el-table-column
                  prop="open"
                  label="Open"
                  align="center">
              </el-table-column>

              <el-table-column
                  prop="high"
                  label="High"
                  align="center">
              </el-table-column>
              <el-table-column
                  prop="low"
                  label="Low"
                  align="center">
              </el-table-column>
              <el-table-column
                  prop="close"
                  label="Close"
                  align="center">
              </el-table-column>
              <el-table-column
                  prop="volume"
                  label="Volume"
                  align="center"
                  :formatter="numberWithCommas"> 
              </el-table-column>
              </el-table>
        </div>
      </el-row>
      <el-row
        style="
          margin-top: 2%;
          background: #d9d9d9;
          border-radius: 30px;
          padding-bottom: 1%;
        "
      >
        <h1
          style="
            font-size: xx-large;
            font-weight: bold;
            margin-left: 3%;
            margin-top: 1%;
          "
        >
          Company Profile
        </h1>
        <h2 style="margin-left: 3%; margin-top: 1%">
          {{ companyInfo["name"] }}
        </h2>
        <span style="margin-left: 3%"
          >Address: {{ companyInfo["address"] }}</span
        >
        <el-row>
          <el-col :span="10">
            <span style="margin-left: 7%; margin-top: 1%"
              >Industry: {{ companyInfo["industry"] }}</span
            >
          </el-col>
          <el-col :span="10">
            <span style="margin-left: 7%; margin-top: 1%"
              >Sector(s): {{ companyInfo["sector"] }}</span
            >
          </el-col>
          <el-col :span="10">
            <span style="margin-left: 7%; margin-top: 1%"
              >Phone: {{ companyInfo["phone"] }}</span
            >
          </el-col>
          <el-col :span="10">
            <span style="margin-left: 7%; margin-top: 1%"
              >Website: {{ companyInfo["website"] }}
            </span>
          </el-col>
        </el-row>
        <el-row>
          <h3 style="font-weight: bold; margin-left: 3%; margin-top: 2%">
            Description
          </h3>
        </el-row>
        <el-row style="margin-left: 3%; margin-right: 4%">
          <span style="margin-left: 3%">{{ companyInfo["description"] }}</span>
        </el-row>
      </el-row>
    </div>
  </div>
</template>
<style>
.input:focus {
  border: 0;

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
import * as echarts from "echarts";
import axios from "axios";

export default {
  data() {
    return {
      isupdate: true,
      tickerName: "",
      balance: 0,
      companyInfo: {},
      lastprice: "",
      realtimechardata: [],
      previousclose: "",
      dayhigh: "",
      daylow: "",
      exchange: "",
      lastvolume: "",
      open: "",
      QuoteType: "",
      TenDayAverageVolume: "",
      ThreeMonthAverageVolume: "",
      TwoHundredDayAverage: "",
      YearChange: "",
      YearHigh: "",
      YearLow: "",
      Shares: "",
      totalprice: "",
      volume: 0.25,
      volumes: 0,
      chartmax:0,
      chartmin:0,
      statistics: [],
      action: "Buy",
      nowTime: "",
      chart: null,
      showInfo: true,
      AccountData: [],
      tableData2: [],
      inport: 0,
      historytabledata:[],
      period:"5d"
      
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
      this.totalprice = (newVal * this.lastprice).toFixed(2);
    },
  },
  mounted() {
    console.log("init chart");
    this.getNowTime();
  },
  methods: {
    Calvolume(percentage) {
      console.log(percentage);
      if (this.action === "Buy") {
        var balance = parseFloat(this.balance);
        console.log(balance);
        var currentprice = parseFloat(this.lastprice);
        console.log(currentprice);
        if (balance < currentprice) {
          this.volumes = 0;
          alert("you dont have  enough balance");
        } else {
          var enablevolumes = balance / currentprice;
          console.log(enablevolumes);
          this.volumes = parseInt(enablevolumes * percentage);
        }
      } else {
        var inport = this.inport;
        var volumes = this.volumes;
        if (volumes > inport) {
          this.volumes = 0;
          alert("you dont have enough volumes for sell");
        } else {
          this.volumes = parseInt(inport * percentage);
        }
      }
    },
    Addwatchlist(tickerName) {
      console.log(tickerName);

      console.log(this.$store.state.accountid);
      var id = this.$store.state.accountid;
      var result = {
        tickerName: tickerName,
        accountid: id,
      };
      axios.post("http://127.0.0.1:8088/AddToWatchlist", result).then((res) => {
        console.log(res.data);
      });
    },
    createCandleChart() {
      let candleChart = this.$echarts.init(this.$refs.candleChart);
      let option2 = {
        xAxis: {
          type: "category",
          data: [
            "2022/12/16",
            "2022/12/17",
            "2022/12/18",
            "2022/12/19",
            "2022/12/20",
          ],
        },
        yAxis: {
          type: "value",
        },
        series: [
          {
            type: "candlestick",
            data: [
              [2412.33, 2434.3, 2411.68, 2442.68],
              [2433.89, 2431.04, 2424.06, 2440.1],
              [2432.04, 2416.43, 2407.65, 2432.72],
              [2416.93, 2416.93, 2407.7, 2430.57],
              [2417.63, 2417.29, 2405.08, 2425.93],
            ],
            itemStyle: {
              normal: {
                color: "#f7a35c",
                color0: "#00a65a",
                borderColor: "#f7a35c",
                borderColor0: "#00a65a",
              },
            },
          },
        ],
      };
      candleChart.setOption(option2);
    },
    ShowBuyAndSell() {
      this.showInfo = false;
    },
    ShowStockInfo() {
    
      this.showInfo = true;
    },
    initChart() {
      this.chart = echarts.init(document.getElementById("chart"));
      this.chart.setOption({
        title: {
          text: "Stock Real-Time Price",
        },
        xAxis: {
          name:"Time",
          type: "category",
          data: [
            "10:00",
            "10:30",
            "11:00",
            "11:30",
            "12:00",
            "14:00",
            "14:30",
            "15:00",
            "15:30",
            "16:30",
          ],
        },
        yAxis: {
          name:"Price (THB)",
          type: "value",
          min: this.chartmin,
          max: this.chartmax,
        },
        series: [
          {
            data: this.realtimechardata,
            type: "line",
            smooth: false,
          },
        ],
      });
    },
    getNowTime() {
      let speed = 1000;
      let that = this;
      let theNowTime = function () {
        that.nowTime = that.timeNumber();
      };
      setInterval(theNowTime, speed);
    },
    timeNumber() {
      let today = new Date();
      let date =
        today.getFullYear() +
        "-" +
        this.twoDigits(today.getMonth() + 1) +
        "-" +
        this.twoDigits(today.getDate());
      let time =
        this.twoDigits(today.getHours()) +
        ":" +
        this.twoDigits(today.getMinutes()) +
        ":" +
        this.twoDigits(today.getSeconds());
      return date + "  " + time;
    },
    twoDigits(val) {
      if (val < 10) return "0" + val;
      return val;
    },

    buyStock() {
      console.log("buyStock called");
      var id = this.$store.state.accountid;
      console.log(id);
      var stockprice = this.lastprice;
      console.log(stockprice);
      var tickerName = this.$route.params.tickerName;
      console.log(tickerName);
      var shares = this.volumes;
      console.log(shares);
      var action = this.action;
      console.log(action);
      var cost = this.totalprice;
      console.log(cost);
      var buydata = {
        AccountId: id,
        ticker: tickerName,
        stockprice: stockprice,
        shares: shares,
        action: action,
        cost: cost,
      };
      if (parseFloat(cost) > parseFloat(this.balance)) {
        alert("you dont have enough balance");
        return;
      }
      console.log(buydata);
      var id = this.$store.state.accountid;
      console.log(id);
      var tickerName = this.$route.params.tickerName;
      var req = {
        accountid: id,
        ticker: tickerName,
      };
      axios.post("http://127.0.0.1:8088/BuyStock", buydata).then((res) => {
        console.log(res);
        //this.AccountData = res.data
        this.AccountData = [];
        var balance = res.data.Balance.toFixed(2);
        this.balance = balance;
        this.inport = parseInt(res.data["Inport"]);
        var data = {
          Balance: balance,
          Order: res.data["Order"],
          Inport: res.data["Inport"],
        };
        this.AccountData.push(data);
      });
      axios.post("http://127.0.0.1:8088/GetonelHistory", req).then((res) => {
        console.log(res);
        this.tableData2 = [];
        res.data.forEach((data) => {
          this.tableData2.push(data);
        });
        this.isupdate = !this.isupdate;
      });
    },
    SellStock() {
      console.log("SellStock called");
      var id = this.$store.state.accountid;
      console.log(id);
      var currentprice = this.lastprice;
      console.log(currentprice);
      var tickerName = this.$route.params.tickerName;
      console.log(tickerName);
      var volume = this.volumes;
      console.log(volume);
      var action = this.action;
      console.log(action);
      var cost = this.totalprice;
      console.log(cost);
      var selldata = {
        accountid: id,
        ticker: tickerName,
        currentprice: currentprice,
        volume: volume,
        action: action,
        cost: cost,
      };
      if (volume > this.inport) {
        alert("you dont have enough volume for sell");
        return;
      }
      console.log(selldata);
      axios.post("http://127.0.0.1:8088/SellStock", selldata).then((res) => {
        console.log(res);
        //this.AccountData = res.data
        this.AccountData = [];
        var balance = res.data.Balance.toFixed(2);
        this.balance = balance;
        this.inport = parseInt(res.data["Inport"]);
        var data = {
          Balance: balance,
          Order: res.data["Order"],
          Inport: res.data["Inport"],
        };
        this.AccountData.push(data);
      });
      var id = this.$store.state.accountid;
      console.log(id);
      var tickerName = this.$route.params.tickerName;
      var req = {
        accountid: id,
        ticker: tickerName,
      };
      axios.post("http://127.0.0.1:8088/GetonelHistory", req).then((res) => {
        console.log(res);
        this.tableData2 = res.data;
        this.isupdate = !this.isupdate;
      });
    },

    simulation() {
      console.log("simulation() called");

      var action = this.action;
      console.log(action);
      if (action === "Buy") {
        this.buyStock();
      } else {
        this.SellStock();
      }
    },
    handleButtonClick(period) {
      this.period = period;
      // make axios post request with this.period as data parameter
      console.log(`Button with period ${period} was clicked`);
      var tickerName = this.$route.params.tickerName;
      var req2 = {
          period : this.period,
          ticker: tickerName,
        }
      console.log(period)
        axios.post("http://127.0.0.1:8088/gethistorydata", req2).then((res) => {
          console.log(res);
          this.historytabledata = res.data;      
        });
    },
  },

  filters: {
    numberWithCommas: function (value) {
      if (!value) return "";
      var parts = value.toString().split(".");
      parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ",");
      if (parts.length > 1) {
        parts[1] = parts[1].substr(0, 2); // Only keep the first two decimal places
      } else {
        parts.push("00"); // Add trailing zeros if the value doesn't have any decimal places
      }
      return parts.join(".");
    },
  },
  created() {
    console.log(this.$route.params.tickerName);
    var tickerName = this.$route.params.tickerName;
    this.tickerName = tickerName;
    axios
      .post("http://127.0.0.1:8088/marketinform/" + tickerName)
      .then((res) => {
        console.log(res.data);
        this.dayhigh = res.data["dayhigh"];
        this.daylow = res.data["daylow"];
        this.lastprice = res.data["lastprice"];
        this.previousclose = res.data["previousclose"];
        this.lastvolume = res.data["lastvolume"];
        this.open = res.data["open"];
        this.QuoteType = res.data["QuoteType"];
        this.TenDayAverageVolume = res.data["TenDayAverageVolume"];
        this.ThreeMonthAverageVolume = res.data["ThreeMonthAverageVolume"];
        this.TwoHundredDayAverage = res.data["TwoHundredDayAverage"];
        this.YearChange = res.data["YearChange"];
        this.YearHigh = res.data["YearHigh"];
        this.YearLow = res.data["YearLow"];
        this.Shares = res.data["Shares"];
        this.companyInfo = res.data["Company"];
        this.realtimechardata = res.data["realtimechartdata"];
        this.chartmax = res.data["chartmaxmin"]["max"];
        this.chartmin = res.data["chartmaxmin"]["min"];

        console.log(this.chartmax);
        console.log(this.chartmin);
        this.initChart();
        this.createCandleChart();
        var id = this.$store.state.accountid;
        console.log(id);
        var tickerName = this.$route.params.tickerName;
        var req = {
          accountid: id,
          ticker: tickerName,
        };
        axios
          .post("http://127.0.0.1:8088/GetPurchaseinfor", req)
          .then((res) => {
            var balance = res.data.Balance.toFixed(2);
            console.log(res);
            this.balance = balance;
            this.inport = parseInt(res.data["Inport"]);
            console.log(this.inport);
            var data = {
              Balance: balance,
              Order: res.data["Order"],
              Inport: res.data["Inport"],
            };
            console.log(data);
            this.AccountData.push(data);
          });
        var tickerName = this.$route.params.tickerName;
        var res = {
          ticker: tickerName,
        };
        axios.post("http://127.0.0.1:8088/GetonelHistory", req).then((res) => {
          console.log(res);
          this.tableData2 = res.data;
          this.isupdate = !this.isupdate;
        });

        var req2 = {
          period : this.period,
          ticker: tickerName,
        }
        axios.post("http://127.0.0.1:8088/gethistorydata", req2).then((res) => {
          console.log(res);
          this.historytabledata = res.data;      
        });
      });

    // axios.post("http://127.0.0.1:8088/Getstockprice",res).then((res) => {
    //       console.log(res.data)
    //       this.high = res.data['dayhigh']
    //       this.low = res.data['daylow']
    //       this.current = res.data['lastprice']
    //       this.previousclose = res.data['previousclose']
    //   });
  },
};
</script>
