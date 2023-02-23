<template>
    <div>
        <el-row class="chapterbox" >
            <h2 style="margin-left: 3%;  margin-top:4%"> 01 Stocks</h2>
        </el-row>
        <el-row style="background: #F5EFE0;border-radius: 30px;margin-top:1%; margin-left: 3%; margin-right: 3%;" >
            <h2 style="margin-left: 3%;  margin-top:2%">Concept</h2>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:2%">       Common stocks provide investors with an ownership interest in a company. Shares of stock represent company equity and are often called just that, equities. Investors can buy and sell stocks on exchanges—entities that exist mostly to create a marketplace for the shares. Stocks trade constantly during business hours—9:30 a.m. to 4.00 p.m. Eastern time most weekdays—with prices changing from second to second. As the value of a company rises and falls, so does the value of an investor’s stock. Over the long haul, stock prices tend to rise when companies increase their sales and profits. But in the short term, stocks can gyrate, moved by things like overall economic trends, news from rival companies, government action, and a host of other factors.</h4>
            
            <h2 style="margin-left: 3%;  margin-top:2%">Classifications</h2>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:2%">        Not all stocks behave the same way, which means they can play different roles in your portfolio. Here are some classifications every stock investor should understand:</h4>
            <p style="margin-left: 5%; margin-right: 3%;  margin-top:2%">·  <em style="font-weight: bold;">Value stocks.</em> Investors tend to set values for stocks relative to their earnings (or sales, or cash flows, etc). If a stock that earned $100 million over the last year trades at 10 times earnings, its market cap is 10 times $100 million, or $1 billion. In most cases, investors focus on per-share numbers. For example, if the company earning $100 million has 100 million shares outstanding, it earns $1 per share. A price/earnings ratio of 10 prices the stock at $10 per share. Many academic studies have shown that stocks with low price/earningsratios relative to the rest of the market tend to outperform. Valueoriented investors gravitate toward value stocks—companies that trade at a discount relative to their earnings or some other operating statistic.</p>
            <p style="margin-left: 5%; margin-right: 3%;  margin-top:2%">· <em style="font-weight: bold;">Growth stocks. </em>Stocks with above-market growth of sales or profits tend to outperform their peers. These stocks tend to cost more (higher price/earnings ratios, etc.) than other stocks, as many investors will pay a premium for growth.</p>
            <p style="margin-left: 5%; margin-right: 3%;  margin-top:2%">· <em style="font-weight: bold;">Large-capitalization (large-cap) stocks. </em> Large-capitalization (large-cap) stocks. The name tells the story. Since investors tend to set values for stocks relative to earnings, companies with massive profits can sport enormous market capitalizations. Stocks of large companies tend to be less volatile, and investors often consider them safer than smaller stocks.</p>
            <p style="margin-left: 5%; margin-right: 3%;  margin-top:2%">· <em style="font-weight: bold;">Small-cap stocks. </em>Stocks of smaller companies have historically delivered higher returns than stocks of large companies—again, at the cost of higher risk. What constitutes a small-cap stock? It depends onwho you ask, as there is no market consensus on where lies the cutoffpoint between small and large. A commonly cited dividing line is $3 billion, with anything smaller classified as a small-cap. </p>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:2%">Because of their different risk-return profiles, investors should treat large-cap and small-cap stocks as separate asset classes. In general, you should own a blend of large-cap and small-cap stocks in the equity portion of your portfolio. Sure, you could stuff the portfolio with only large-caps or stick to just small-caps, but you might end up with a lower rate of return (the large-cap option) or higher risk (the small-cap option) than you desire.</h4>
        
            <p style="margin-left: 5%; margin-right: 3%;  margin-top:2%"> · <em style="font-weight: bold;">U.S. stocks. </em>   Because economic trends vary from country to country, at times U.S. stocks will thrive while the rest of the world limps along, and vice versa.   As a rule, investors consider U.S. stocks safer than foreign stocks. This belief stems, at least in part, from the size and liquidity of the stock market and that U.S. accounting rules require greater disclosure of financial data than most other countries.</p>
            <p style="margin-left: 5%; margin-right: 3%;  margin-top:2%"> · <em style="font-weight: bold;">Foreign stocks.  </em>     Many investors purchase foreign stocks to diversify their portfolios.  For now, just realize that you can reduce portfolio volatility and thus reduce risk by blending assets that don’t move in the same direction all the time.   In addition, you can sometimes boost returns by purchasing stocks of companies in emerging markets like China and India, where the economies grow far faster than in the United States.   Of course, those emerging-market stocks come with—you guessed it—more risk</p>
        
        <el-row style="background: #D9D9D9; border-radius: 61px;margin-left:8%;margin-right:8%"> 
            <el-col :span="9" :offset="1" style="margin-left:10%;margin-top:2%">
                <el-row class="bordered-row">
                    <h2 style="margin-left:2%;margin-right:1%;margin-top:2%；">Pros:</h2>
                </el-row>
                <el-row class="bordered-row">
                    <h4 style="margin-left:2%;margin-right:1%;">Variety </h4>
                    <p style="margin-left:3%;margin-right:1%;margin-top:1%">With the stocks of more than 5,000 companies trading on U.S. exchanges, investors can buy into almost any business they choose.</p>
                </el-row>
                <el-row class="bordered-row">
                    <h4 style="margin-left:2%;margin-right:1%;">Flexibility</h4>
                    <p style="margin-left:3%;margin-right:1%;margin-top:1%">Stocks trade all day long, which allows investors to buy and sell at specific levels and attempt to play short-term price moves.   (The risky strategy of timing intraday fluctuations is called day trading.   Even professionals make plenty of mistakes day trading, and beginners shouldn’t mess with it.)</p>
                </el-row>
                <el-row class="bordered-row">
                    <h4 style="margin-left:2%;margin-right:1%;">High returns</h4>
                    <p style="margin-left:3%;margin-right:1%;margin-top:1%">Stocks tend to outperform bonds and other income-oriented investments.</p>
                </el-row>
                
            </el-col>

            <el-col :span="9" style="margin-right:10%;margin-left:5%;margin-top:2%">
                <el-row class="bordered-row">
                    <h2 style="margin-left:2%;margin-right:1%;margin-top:2%">Cons:</h2>
                </el-row>
                <el-row class="bordered-row">
                    <h4 style="margin-left:2%;margin-right:1%;">Volatility</h4>
                    <p style="margin-left:3%;margin-right:1%;margin-top:1%">Stock prices fluctuate more than bond prices. However,investors must accept that risk if they wish to tap into stocks’ potentially excellent returns.</p>
                </el-row>
                <el-row class="bordered-row">
                    <h4 style="margin-left:2%;margin-right:1%;">Complex analysis</h4>
                    <p style="margin-left:3%;margin-right:1%;margin-top:1%">Stock analysis involves looking at a number of statistics, gauging trends, and estimating future growth rates. It takes time and effort, which might explain, at least in part, the popularity of mutual funds.</p>
                </el-row>
                <el-row class="bordered-row">
                    <h4 style="margin-left:2%;argin-right:1%;">Vigilance required</h4>
                    <p style="margin-left:3%;argin-right:1%;margin-top:1%">Because stock prices can change so quickly,and because they often respond sharply to news about the company or the market, investors must pay close attention to them.</p>
                </el-row>
            </el-col>

        </el-row>
            



        </el-row>
        <el-row style="background: #F5EFE0;border-radius: 30px; margin-top:1%; margin-left: 3%; margin-right: 3%;"> 
            <h2 style="margin-left: 3%;  margin-top:2%">Video part</h2>
            <el-card style="margin-left: 20%;margin-right: 20%;" >
            <iframe style=" height:400px;width:800px"
                :src="videoEmbedCode"
                frameborder="0"
                allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture"
                allowfullscreen
            ></iframe>
            </el-card>
            
            <el-row class="source-text">
            <span>Title: Stocks Definition | Learn About Common and Preferred Stock | Your Online Finance Dictionary</span>
            </el-row>
            <el-row class="source-text">
            <span>Author: Finance Strategists</span>
            </el-row>
            <el-row class="source-text">
                Source: https://youtu.be/YUgso6IQmco
            </el-row>
        </el-row>
        
        <el-row style="margin-left: 4%; margin-right: 4%;margin-top:1%">
            <el-col :span="12" >
                <el-button  @click="Goback" type="warning" style="color: black; font-size:25px; border-radius: 50px; width:150px;height:60px" >Back</el-button>
            </el-col>
            <el-col :span="12" style="text-align: right; " >
                <el-button @click="Gotest" type="warning" style="color: black; font-size:25px; border-radius: 50px; width:150px;height:60px" >Go test</el-button>
            </el-col>
        </el-row>


        
    </div>
</template>


<script>
export default {
  data() {
    return {
      videoEmbedCode: 'https://www.youtube.com/embed/YUgso6IQmco',
    
    };
  },
  methods:{
      Gotest(){
          this.$router.push('/test')
      },
      Goback(){
          this.$router.push('/chapter3')
      }
  },
  
};

</script>


<style>
.chapterbox{
    background:#F5EFE0;
    border-radius: 30px; 
    height: 150px; 
    margin-top:1%; 
    margin-left: 3%; 
    margin-right: 3%;

}
.source-text{
    margin-left: 3%;
}
.bordered-row {
  border: 1px solid #ccc;
  padding: 10px;
}
</style>
