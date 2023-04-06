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
            <el-row style="padding-right: 3%;margin-top:2%">
                <el-table
                    :data="tableData"
                    border
                    style="width: 100%">
                    <el-table-column
                    fixed
                    prop="timestamp"
                    label="Time Stamp"
                    align="center">
                    </el-table-column>
                    <el-table-column
                    fixed
                    prop="watchlistid"
                    label="Watchlist Id"
                    align="center">
                    </el-table-column>
                    <el-table-column
                    prop="ticker"
                    label="Ticker"
                    align="center">
                    </el-table-column>
                    <el-table-column
                    fixed="right"
                    label="Action"
                    align="center">
                    <template slot-scope="scope">
                        <el-button @click="Goinfor(scope.row.ticker)" type="text" size="small">Buy and Sell</el-button>
                        <el-button  @click.native.prevent="deleteRow(scope.$index, tableData,scope.row.watchlistid)"  type="text" size="small">Delete</el-button>
                    </template>
                    </el-table-column>
                </el-table>
            
            
            </el-row>
            <el-row :span="8" :offset="3">
                <el-button icon="el-icon-plus" style="background: #1F3D70;width:200px; margin-top:5%;margin-left:35%;color:white" @click="Gomarkethome"></el-button>
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
            tableData: [],
            
            
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
            this.tableData = res.data
        });
    },
    methods:{
    
        Editwatchlist(watchlistid){
            var watchlistid = watchlistid
            var req = {
                watchlistid: watchlistid
            }
            console.log(req)

            axios.post("http://127.0.0.1:8088/RemoveFromWatchlist",req ).then((res) => {
                console.log(res.data)
            });

           

        },
        deleteRow(index, rows,watchlistid) {
          this.Editwatchlist(watchlistid)
          rows.splice(index, 1);
           
        },
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