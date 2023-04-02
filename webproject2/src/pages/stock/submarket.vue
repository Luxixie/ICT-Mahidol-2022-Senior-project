<template>
    <div>
    <el-row style="background: #F5F5F5;; margin-top:2%;  margin-left:2%; margin-right:2%; height:250px">
      <el-col :span="17" :offset="1" style="background: #1F3D70;border-radius: 25px;margin-top:2%;">
        <el-row>
          <el-col :span="10" style="margin-left:8%">
            <h3 style="float: left; margin-left:5%;color: #F5EFE0;">SET</h3>
          </el-col>
        </el-row>
          <el-row>
          <el-col :span="10" style="margin-left:8%">
            <h4 style="float: left; margin-left:5%;color: #F5EFE0;">high: {{high}}</h4>
          </el-col>
          <el-col :span="10" >
            <h4 style="float: right; margin-right:6%;color: #F5EFE0;">current: {{current}}</h4>
          </el-col>
        </el-row>
        <el-row>
          <el-col :span="10" style="margin-left:8%">
            <h4 style="float: left; margin-left:5%; color: #F5EFE0;">low:  {{low}}</h4>
          </el-col>
          <el-col :span="10" >
            <h4 style="float: right; margin-right:6%; color: #F5EFE0;">+6.00  (+0.37%)</h4>
          </el-col>
        </el-row>
      </el-col>
      <el-col :span="5" >
        <el-row style="margin-top:30%;margin-left:20%;">
            <div style="text-align: center;padding-top: 100px">
                Time: {{ nowTime }}
            </div>
        </el-row>
      </el-col>
    </el-row>

    <el-row style="padding-right: 3%;">
        <el-row class="box">
            <span style="margin-left:2%;margin-top:1%">{{this.$route.params.industryName}}</span>
        </el-row>
        <el-col :span="7" v-for="(item, index) in items"  :offset="1" style="margin-top: 2%;">
            <el-card :body-style="{ padding: '0px' }" style="margin-top: 5%; margin-bottom: 5%; background: #1f3d70;">
                <div style="padding: 14px;">
                    <!-- <img width="60px" height="60px" style="float: left; margin-top: 5%; " /> -->
                    <div style="float:left; margin-left: 5%; width: 78%; margin-bottom: 3%;">
                        <div>
                            <span class="topFont">{{item.stockName}}</span>
                        </div>
                        <div>
                            <span class="topFont">{{item.companyName}}</span>
                        </div>
                        <div style="margin-top: 4%;">
                            <!-- <div style="float: left;width: 50%; ">
                                <div>
                                    <span class="priceFont">High:{{item.high}}</span>
                                </div>
                                <div>
                                    <span class="priceFont">Low:{{item.low}}</span>
                                </div>
                            </div> -->
                            <div style="float:right; margin-top: 2%;">
                                <div>
                                    <el-button size="medium" type="warning" @click="Goinfor(item.stockName)" round
                                        style="width: 100%;">Buy/Sell</el-button>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </el-card>
        </el-col>
    </el-row>
    <el-row>
        <el-button style="
                background: #F5EFE0;
                border-radius: 50px;
                margin-top:1%;
                margin-left:4%;
                width:200px;
                font-weight: 800;
                font-size: 25px;
                ">Back</el-button>
    </el-row>
    </div>
</template>


<style>
.topFont {
    font-size: 12px;
    font-weight: bold;
    color: #f5efe0;
}

.priceFont {
    font-size: 12px;
    color: #f5efe0;
}


.time {
    font-size: 13px;
    color: #999;
}

.bottom {
    margin-top: 13px;
    line-height: 12px;
}

.button {
    padding: 0;
    float: right;
}

.image {
    width: 100%;
    display: block;
}

.clearfix:before,
.clearfix:after {
    display: table;
    content: "";
}

.clearfix:after {
    clear: both
}
.box{
    background: #F5EFE0;
    border-radius: 30px;
    margin-top: 1%;
    margin-left: 3%;
    width:20%;
    height: 40px;
}
.el-dropdown-link {
    cursor: pointer;
    color: #000000;
    font-weight: 700;
    font-size: 20px;
    margin-left: 10%;
}
</style>

<script>
import axios from 'axios'
export default { 
    data() {
        return {
            items: [],
            high:'',
            low:'',
            current:'',
            nowTime: ''
            
        };
    },
    mounted() {
    this.getNowTime();
    this.getSETPrice();
    },
    methods:{
        Goinfor(ticker){
            console.log(ticker)
            //this.$router.push('/buyandsell')
             this.$router.push({
            path:"/buyandsell/"+ticker,
            params:{tickerName:ticker}
            })
        },
        getNowTime () {
        let speed = 1000
        let that = this
        let theNowTime = function () {
            that.nowTime = that.timeNumber()
        }
        setInterval(theNowTime, speed)
        }, 
        getSETPrice () {
        let speed = 1000 * 60
        let that = this
        let theNowPrice = function () {
            axios.post("http://127.0.0.1:8088/GetSETCurrentPrice").then((res) => {
            console.log(res.data)
            that.high = res.data['dayhigh']
            that.low = res.data['daylow']
            that.current = res.data['lastprice']
        });
        }
        setInterval(theNowPrice, speed)
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
    },
    created(){
       console.log(this.$route.params.industryName) 
       var industryName = this.$route.params.industryName
        axios.post("http://127.0.0.1:8088/GetStockByIndustry/" + industryName ).then((res) => {
           console.log(res.data)
           this.items =  res.data
        });
        axios.post("http://127.0.0.1:8088/GetSETCurrentPrice").then((res) => {
           console.log(res.data)
           this.high = res.data['dayhigh']
           this.low = res.data['daylow']
           this.current = res.data['lastprice']
        });
    }
}
</script>