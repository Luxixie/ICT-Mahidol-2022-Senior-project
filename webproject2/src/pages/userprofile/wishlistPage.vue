<template>
    <div>
        <el-col :span="7" style="margin-top:4%">
            <el-row >
                <div style="margin-left:30%">
                    <el-avatar :size="200" :src="avatar"   />
                </div>
            </el-row> 

        </el-col>
        <el-col :span="15" style="margin-top:1%">
            <el-row :span="5" :offset="2" style="background: #1F3D70; border-radius: 50px;width: 300px; margin-top:5%">
                <span style="margin-left:20%;font-size: 40px;color: #F5EFE0;">Watch list</span>
            </el-row>
            <el-row style="padding-right: 3%;">
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
                <el-col :span="4" :offset="3">
                    <el-button icon="el-icon-plus" style="background: #1F3D70;width:200px; margin-top:5%;color:white" @click="Gomarkethome"></el-button>
                </el-col>
                <el-col :span="4" :offset="5">
                    <el-button icon="el-icon-minus" style="background: #1F3D70; width:200px;  margin-top:5%;color:white" @click="Editwatchlist"></el-button>
                </el-col>

            </el-row>
            

        </el-col>
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
</style>

<script>
import axios from 'axios'

export default { 
    data() {
        return {
            avatar:'https://avatars0.githubusercontent.com/u/8186664?s=460&v=4',
            items: [],
            
            
        };
    },
    created(){
        console.log(this.$store.state.accountid)
        var id = this.$store.state.accountid
        var req = {
                accountid:id
        }
           
        console.log(req)
        
        axios.post("http://127.0.0.1:8088/GetWatchlist",req ).then((res) => {
            console.log(res.data)
            this.items = res.data
        });
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
        Gomarkethome(){
            this.$router.push('/markethome')
        }
      
    },
    
}
</script>