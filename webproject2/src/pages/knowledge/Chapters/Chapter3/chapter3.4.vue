<template>
    <div>
        <el-row class="chapterbox" >
            <h2 style="margin-left: 3%;  margin-top:4%"> 04 Exchange-Traded Funds</h2>
        </el-row>
        <el-row style="background: #F5EFE0;border-radius: 30px;margin-top:1%; margin-left: 3%; margin-right: 3%;" >
            <h2 style="margin-left: 3%;  margin-top:2%">Concept</h2>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:1%">  According to the ICI, at the end of 2012 investors had about $1.34 trillion parked in exchange-traded funds, often called ETFs. ETF assets equate to barely more than 10% of the value of traditional mutual funds, but these types of investments continue to grow in popularity. ETF assets have more than tripled since 2006, while the number of ETFs on the market rose to 1,239 in 2012, up from 359 at the end of 2006.</h4>

            <h2 style="margin-left: 3%;  margin-top:2%">Classifications</h2>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:1%"> ETFs operate much like mutual funds in that they commingle the resources of many investors to purchase a basket of stocks, bonds, or both. However, ETFs differ from traditional mutual funds in a few important ways:</h4>
            <p style="margin-left: 5%; margin-right: 3%;  margin-top:1%">·  <em style="font-weight: bold;">Trading on exchanges.  </em> As the name suggests, these funds trade on the same exchanges as stocks. ETF prices change from second to second, just like stock prices.</p>
            <p style="margin-left: 5%; margin-right: 3%;  margin-top:1%">·  <em style="font-weight: bold;">Mostly index funds.  </em> While a few ETF managers actively manage their funds in an attempt to top benchmarks, the bulk of them track indexes.</p>
            <p style="margin-left: 5%; margin-right: 3%;  margin-top:1%">·  <em style="font-weight: bold;">Greater transparency.</em> Unlike traditional mutual funds—which the SEC requires to disclose their holdings quarterly—ETFs must disclose daily. Of course, since indexes don’t change their holdings often, most ETFs don’t either.</p>

        <el-row style="background: #D9D9D9; border-radius: 61px;margin-left:8%;margin-right:8%"> 
            <el-col :span="9" :offset="1" style="margin-left:10%;margin-top:2%">
                <el-row class="bordered-row">
                    <h2 style="margin-left:2%;margin-right:1%;margin-top:2%；">Pros:</h2>
                </el-row>
                <el-row class="bordered-row">
                    <h4 style="margin-left:2%;margin-right:1%;">Convenient trading. </h4>
                    <p style="margin-left:3%;margin-right:1%;margin-top:1%">Unlike the way mutual funds reprice at the end of the day and trade only at that price during the following day, ETF prices rise and fall intraday like stocks.</p>
                </el-row>
                <el-row class="bordered-row">
                    <h4 style="margin-left:2%;margin-right:1%;">Hedging. </h4>
                    <p style="margin-left:3%;margin-right:1%;margin-top:1%">Investors can buy and sell options on ETFs, just as they can on most stocks. Beginning investors should probably avoid options, but the freedom to buy and sell options that ETFs allow has contributed to their popularity.</p>
                </el-row>
                <el-row class="bordered-row">
                    <h4 style="margin-left:2%;margin-right:1%;">Trading costs. </h4>
                    <p style="margin-left:3%;margin-right:1%;margin-top:1%">Many brokers charge more to trade mutual funds than stocks. When investors buy or sell exchange-traded mutual funds, they pay the same commissions charged for stock trades.</p>
                </el-row>
                
            </el-col>

            <el-col :span="9" style="margin-right:10%;margin-left:5%;margin-top:2%">
                <el-row class="bordered-row">
                    <h2 style="margin-left:2%;margin-right:1%;margin-top:2%">Cons:</h2>
                </el-row>
                <el-row class="bordered-row">
                    <h4 style="margin-left:2%;margin-right:1%;">Fund expenses.</h4>
                    <p style="margin-left:3%;margin-right:1%;margin-top:1%">Remember that every mutual fund charges fees. However, because ETFs trade like stocks, investors frequently treat them like stocks and forget about those fees. And ETFs rarely draw much attention to the fees they collect.</p>
                </el-row>
                <el-row class="bordered-row">
                    <h4 style="margin-left:2%;margin-right:1%;">Selection. </h4>
                    <p style="margin-left:3%;margin-right:1%;margin-top:1%">Most ETFs track indexes, meaning they’re passively managed. While some ETFs use active managers, investors seeking active management will find few options among ETFs.</p>
                </el-row>
                <el-row class="bordered-row">
                    <h4 style="margin-left:2%;argin-right:1%;">Perceived complexity. </h4>
                    <p style="margin-left:3%;argin-right:1%;margin-top:1%">While ETFs look like mutual funds in most respects, many investors shy away from them. A 2010 study by Mintel Comperemedia, a consulting firm, revealed that nearly 60% of investors chose not to purchase ETFs because they didn’t understand how they worked.</p>
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
            <span>Title: Investing Basics: ETFs</span>
            </el-row>
            <el-row class="source-text">
            <span>Author: TD Ameritrade</span>
            </el-row>
            <el-row class="source-text">
                Source: https://www.youtube.com/embed/kqr-h-pmky4
            </el-row>
            <el-row class="source-text">
                <span>Subscribe: http://bit.ly/SubscribeTDAmeritrade </span>
            </el-row>
            <el-row class="source-text">
                <p>Exchange-traded funds (ETFs) have grown in popularity among investors over the past decades. This video can  help you understand the risks and potential rewards of investing in this asset class.</p>
                <p>Check out Investor Insights for daily livestreamed webcasts with TD Ameritrade Education Coaches: http://bit.ly/SubscribeTDAmeritradeIn...</p>
                <p>TD Ameritrade is where smart investors get smarter. We post educational videos that bring investing and finance topics back down to earth weekly. Have a question or topic suggestion? Let us know. </p>
            </el-row>
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
export default {
  data() {
    return {
      videoEmbedCode: 'https://www.youtube.com/embed/kqr-h-pmky4',
    };
  },
  methods:{
      GoNext(){
          this.$router.push('/chapter3.5')
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
