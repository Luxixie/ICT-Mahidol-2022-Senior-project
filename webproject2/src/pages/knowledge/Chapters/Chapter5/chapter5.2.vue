<template>
    <div>
        <el-row class="chapterbox" >
            <h2 style="margin-left: 3%;  margin-top:4%"> 02 How to Read Stock Charts for Beginners (2)</h2>
            <h2 style="margin-left: 3%;  margin-top:4%; color:gray">Written by Warrior Trading </h2>
        </el-row>
        <el-row style="background: #F5EFE0;border-radius: 30px;margin-top:1%; margin-left: 3%; margin-right: 3%;" >
            <h2 style="margin-left: 3%;  margin-top:2%">What is a Stock Chart</h2>
            <p style="margin-left: 3%; margin-right: 3%;  margin-top:1%">A stock chart is a set of information on the stock of a particular company that generally displays details about trading volume, price changes, historical lows and highs, dividends, current trading price, and other company-related financial details.</p>
            <p style="margin-left: 3%; margin-right: 3%;  margin-top:1%">Knowing how to read stock charts is one of the best ways to understand the performance of a particular company’s stock.</p>
            <p style="margin-left: 3%; margin-right: 3%;  margin-top:1%">Stock charts also help you to know how a stock is likely to perform and what is going on in the broader market.</p>

        </el-row>
        <el-row style="background: #F5EFE0;border-radius: 30px;margin-top:1%; margin-left: 3%; margin-right: 3%;">
            <h2 style="margin-left: 3%;  margin-top:2%">Different Types of Stock Charts</h2>
            <el-row :span="2" class="container" style="margin-top:3%;margin-left:25%">
                    <img src="./images/8.jpg" class="image" />
            </el-row>
            <p style="margin-left: 3%; margin-right: 3%;  margin-top:1%">The above image is more or less what a standard stock chart will look like when you first open your brokers trading platform. You’ll have basic quoting data, either a line or candlestick chart, volume, and most of the time price will be on the right side of the chart along the y-axis with time running along the x-axis.</p>
            <p style="margin-left: 3%; margin-right: 3%;  margin-top:1%">This is a daily candlestick chart of Apple going back a few months. Each candle represents a days worth of price action. You’ll also notice the teal-blue line running through the candles. This is a moving average that takes past pricing data and averages it over a certain period time, depending on your settings.</p>
            <p style="margin-left: 3%; margin-right: 3%;  margin-top:1%">The green vertical bars on the bottom of the chart represent volume, or the amount of shares traded during a day. You can see some days are more active than others and will have higher volume bars.</p>
            <el-row :span="2" class="container" style="margin-left:25%">
                    <img src="./images/9.jpg" class="image" />
            </el-row>
            <p style="margin-left: 3%; margin-right: 3%;  margin-top:1%">I zoomed in on the data that is located on the upper left part of this chart. This is where you will find important information like the ticker, exchange and pricing data.</p>
            <p style="margin-left: 5%; margin-right: 3%;  margin-top:1%"><em style="font-weight: bold;">·  Ticker </em> – this is the symbol that the company obtained when filing to go public and is what is used when pulling up charts on a trading platform. No two companies can have the same ticker. In this example AAPL is the ticker used for the company Apple Inc.</p>
            <p style="margin-left: 5%; margin-right: 3%;  margin-top:1%"><em style="font-weight: bold;">·  Timeframe </em> – daily means this chart is showing price action that occurred over a full day of trading. So each candle is one days worth of data. This can be customized to almost any timeframe with the 1,5 and 15 minute timeframes being the most popular for day trading and the 30, 60, daily and weekly the most popular for swing trading.</p>
            <p style="margin-left: 5%; margin-right: 3%;  margin-top:1%"><em style="font-weight: bold;">·  Exchange </em>  – Apple trades on the NASDAQ but if you were looking at a company like General Electric it would show NYSE since they trade on the New York Stock Exchange. The NASDAQ and NYSE are the most common exchanges.</p>
            <p style="margin-left: 5%; margin-right: 3%;  margin-top:1%"><em style="font-weight: bold;">·  L </em> – L stands for last price so in this example the last price traded was $179.14. B stands for Bid which was $179.14 and A stands for Ask which was $179.16 as the time of this writing. This changes often throughout the trading day. O stands for Open, which means $178.92 was the opening print for the trading day.</p>
            <p style="margin-left: 5%; margin-right: 3%;  margin-top:1%"><em style="font-weight: bold;">·  Hi </em> – this is the highest price that stock has traded throughout the day.</p>
            <p style="margin-left: 5%; margin-right: 3%;  margin-top:1%"><em style="font-weight: bold;">·  Lo </em> – this is the lowest price the stock has traded throughout the day.</p>
            <p style="margin-left: 5%; margin-right: 3%;  margin-top:1%"><em style="font-weight: bold;">·  V </em> – is the volume traded for the day or the amount of shares that have traded hands.</p>
            <p style="margin-left: 5%; margin-right: 3%;  margin-top:1%"><em style="font-weight: bold;">·  Mov Avg Exponential </em>– This is the settings for moving average that is displayed on the chart. This is a 9 period moving average which means that it will take the data from the previous nine days and average them out to create a line over time.</p>
        </el-row>
        
        <el-row style="background: #F5EFE0;border-radius: 30px;margin-top:1%; margin-left: 3%; margin-right: 3%;">
            <h2 style="margin-left: 3%;  margin-top:2%">Line Charts</h2>
            <el-row :span="2" class="container" style="margin-left:25%">
                    <img src="./images/10.jpg" class="image" />
            </el-row>
            <p style="margin-left: 5%; margin-right: 3%;  margin-top:1%">FB Line Chart</p>
            <p style="margin-left: 3%; margin-right: 3%;  margin-top:1%">The most common type of stock chart you will see on websites like Yahoo Finance and Google Finance is a line chart. Line charts are the stepping stone for beginner stock traders, and are the most basic charts. They show the price trends of a stock over a selected period of time. The y-axis shows the price of the stock while the x-axis shows the period of time.</p>
            <p style="margin-left: 3%; margin-right: 3%;  margin-top:1%">Generally, you will be asked what period of time you would like to have a look at when you are reading a stock chart. You can use a chart to see how a stock has performed in the past 5 minutes or 30 years.</p>
            <p style="margin-left: 3%; margin-right: 3%;  margin-top:1%">For price, the lowest price is near the x-axis, with the highest near the upper right-hand corner. Line charts also contain the name of the stock as well as its ticker symbol.</p>
            <p style="margin-left: 3%; margin-right: 3%;  margin-top:1%">Line charts are great for spotting trends but they lack in some other major areas like showing the range for the day which is important for day traders who are looking for stocks that have wide ranges.</p>
            
            <h2 style="margin-left: 3%;  margin-top:2%">Candlestick Charts</h2>
            <el-row :span="2" class="container" style="margin-left:25%">
                    <img src="./images/11.jpg" class="image" />
            </el-row>
            <p style="margin-left: 3%; margin-right: 3%;  margin-top:1%">FB Candlestick Chart</p>
            <p style="margin-left: 3%; margin-right: 3%;  margin-top:1%">The other popular charting technique for plotting price data in the stock market is candlestick.</p>
            <p style="margin-left: 3%; margin-right: 3%;  margin-top:1%">Traders use candlestick charts to see the open, high, low, and close of a stock over a time frame. The body of a candlestick chart further allows you to know how a stock closed relative to its open. It is typically colored red for down days and green for up days.</p>
            <p style="margin-left: 3%; margin-right: 3%;  margin-top:1%">The first price traded during the candlestick is the open, and is indicated by either the bottom or top of the body. The top of the wick that occurs above the body of a candlestick indicates the highest price traded during the time frame.</p>
            <p style="margin-left: 3%; margin-right: 3%;  margin-top:1%">There will be no upper wick in the candlestick if the open was the highest price during the time frame.</p>
            <p style="margin-left: 3%; margin-right: 3%;  margin-top:1%">The bottom of the wick that occurs below the body of a candlestick indicates the lowest price traded during the time frame. A candlestick will not have a lower wick if the open was the lowest price during the time period.</p>
            <p style="margin-left: 3%; margin-right: 3%;  margin-top:1%">The last price traded during the time frame is the close, and is indicated by either the bottom or top of the body.</p>
            <p style="margin-left: 3%; margin-right: 3%;  margin-top:1%;font-weight: bold;;font-size:19px">Candlesticks are by far the most popular charts because of the amount of information they display.</p>
            <p style="margin-left: 3%; margin-right: 3%;  margin-top:1%">They show the intraday range, different types of candlesticks like hammers and shooting start which can help traders understand market sentiment quicker, and they work effectively on any time frame.</p>
        

        </el-row>
        <el-row style="background: #F5EFE0;border-radius: 30px;margin-top:1%; margin-left: 3%; margin-right: 3%;">
            <h2 style="margin-left: 3%;  margin-top:2%">Identifying Trends</h2>
            <p style="margin-left: 3%; margin-right: 3%;  margin-top:1%">Trends are one of the easier things to spot on a chart. When stocks are trading in a set direction, whether up or down, they are said to be trending.</p>
            <el-row :span="2" class="container" style="margin-left:25%">
                    <img src="./images/12.jpeg" class="image" />
            </el-row>
            <p style="margin-left: 3%; margin-right: 3%;  margin-top:1%">Above you can clearly see that Apple is trending higher for a few months. The trick with trending stocks is to trade with the trend. Trying to fight it can be costly.</p>
            <p style="margin-left: 3%; margin-right: 3%;  margin-top:1%">Look for pullbacks to important support levels or moving averages for entries to join the trend higher, in this case.</p>
            <p style="margin-left: 3%; margin-right: 3%;  margin-top:1%">We don’t know when a trend will end so a good rule of thumb is to stay in the trade until we get consecutive closes below a support level or a moving average.</p>


        </el-row>
        
        <el-row style="background: #F5EFE0;border-radius: 30px;margin-top:1%; margin-left: 3%; margin-right: 3%;">
            <h2 style="margin-left: 3%;  margin-top:2%">Identifying Support and Resistance</h2>
            <p style="margin-left: 3%; margin-right: 3%;  margin-top:1%">Identifying support and resistance is one of the first things we teach new traders. These levels are where you want to be trading.</p>
            <el-row :span="2" class="container" style="margin-left:25%">
                    <img src="./images/13.png" class="image" />
            </el-row>
            <p style="margin-left: 3%; margin-right: 3%;  margin-top:1%">Above you can clearly see there is a defined level of support at the $26.75 price and clear resistance at $29.50. These levels mean there are buyers at the support prices and sellers at the resistance prices.</p>
            <p style="margin-left: 3%; margin-right: 3%;  margin-top:1%">Why this is important is because if we know we can expect buyers or sellers to show up at a certain price, then we can expect a bounce to profit from.</p>
            
            <p style="margin-left: 3%; margin-right: 3%;  margin-top:1%">Now obviously this doesn’t work every time, but it puts probabilities in our favor which is our main goal as traders. It also provides you with a favorable risk/reward ratio with a defined stopping point.</p>
            <p style="margin-left: 3%; margin-right: 3%;  margin-top:1%">If we buy at support then we know we are wrong if it breaks below that price and can exit the position. The same goes if we sell short off resistance.</p>
            <p style="margin-left: 3%; margin-right: 3%;  margin-top:1%">A good set up for trading support and resistance levels is a breakout trade. This happens when a defined level of support or resistance forms and prices break through it.</p>
            <p style="margin-left: 3%; margin-right: 3%;  margin-top:1%">There are a couple things you want to look for on a breakout trade:</p>
            <p style="margin-left: 5%; margin-right: 3%;  margin-top:1%"><em style="font-weight: bold;">·  High relative volume </em>(volume picks up compared to previous trading periods)</p>
            <p style="margin-left: 5%; margin-right: 3%;  margin-top:1%"><em style="font-weight: bold;">·  Prices hold above/below the level </em>(ideally it breaks out and comes back and tests that level and holds, that’s a good entry point)</p>
            <p style="margin-left: 3%; margin-right: 3%;  margin-top:1%">Breakout trades are very popular because you can catch bigger moves and make more money, which is what we want!</p>
        </el-row>

        <el-row style="margin-left: 4%; margin-right: 4%;margin-top:1%">
            <el-col :span="12" >
                <el-button  @click="Goback" type="warning" style="color: black; font-size:25px; border-radius: 50px; width:150px;height:60px" >Back</el-button>
            </el-col>
            <el-col :span="12" style="text-align: right; " >
                <el-button @click="GoNext" type="warning" style="color: black; font-size:25px; border-radius: 50px; width:150px;height:60px" >Next</el-button>
            </el-col>
        </el-row>



        
    </div>
</template>


<script>
import axios from "axios";
export default {
    data() {
        return {
            videoEmbedCode: 'https://www.youtube.com/embed/jX75o5BOZnc',  
            };
        },
    methods:{
        GoNext(){
            this.$router.push('/chapter5.3')
        },
        Goback(){
            this.$router.push('/chapter5')
        }
        },
    created(){
        
            var userid = this.$store.state.accountid;
            var chapterid = 5;
            var subchapterindex = 2;
            console.log(userid);
            console.log(chapterid);
            console.log(subchapterindex);
            var record = {};
            record.userid = userid;
            record.chapterid = chapterid;
            record.subchapterindex = subchapterindex;

            axios.post("http://127.0.0.1:8088/knowledge/recordcheck", record).then(res => {
                                console.log(res.data)}).finally(()=>{

                                });
        }, 
    computed: {
    linkUrl() {
      // return the URL for the link
      return 'https://youtu.be/jX75o5BOZnc';
    }
    }
  
};

</script>


<style>
.chapterbox{
    background:#F5EFE0;
    border-radius: 30px; 

    margin-top:1%; 
    margin-left: 3%; 
    margin-right: 3%;
    

}
.source-text{
    margin-left: 3%;
    margin-right: 3%;
}
.bordered-row {
  border: 1px solid #ccc;
  padding: 10px;
}
.container {
    width: 50%;
    height: 500px;
    display: flex;
    justify-content: center;
    align-items: center;
}
.image {
    max-width: 100%;
    max-height: 100%;
    background-color: transparent;
}
</style>
