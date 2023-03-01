<template>
    <div>
        <el-row class="chapterbox" >
            <h2 style="margin-left: 3%;  margin-top:4%"> 06 Alternative Assets</h2>
        </el-row>
        <el-row style="background: #F5EFE0;border-radius: 30px;margin-top:1%; margin-left: 3%; margin-right: 3%;" >
            <h2 style="margin-left: 3%;  margin-top:2%">Classifications</h2>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:1%"> For the most part, new investors should steer clear of anything other than the securities discussed in the preceding pages. Once you dip your toe into the market, you might hear about other investment options, including the following:</h4>
            <p style="margin-left: 5%; margin-right: 3%;  margin-top:1%">·  <em style="font-weight: bold;">Commodity futures.  </em> Nearly 100 commodities trade on markets worldwide. They include natural resources such as oil, metals, and lumber as well as agricultural goods such as corn, soybeans, and cattle. Investors can gain commodity exposure by purchasing stock in
                companies that deal in those commodities, or they can invest directly via a futures contract. Futures contracts allow investors to buy or sell commodities and other assets for predetermined prices in the future.</p>
            <p style="margin-left: 5%; margin-right: 3%;  margin-top:1%">·  <em style="font-weight: bold;">Options.  </em>  These derivatives allow stock or ETF investors to bet on whether shares will rise or fall without buying the shares themselves. Suppose a stock trades for $50 per share. If you believe the shares will rise, you might purchase a call option that gives you the right to purchase the shares at $55. When the stock tops $55, you can either purchase the stock at a discount or sell the call option at a profit. Put options allow similar bets to the downside.</p>
            <p style="margin-left: 5%; margin-right: 3%;  margin-top:1%">·  <em style="font-weight: bold;">Hedge funds. </em> These entities pool investor money like mutual funds do, but they tend to pursue unusual or esoteric strategies. Hedge funds, lightly regulated and often secretive, frequently take on massive risks.</p>
            <p style="margin-left: 5%; margin-right: 3%;  margin-top:1%">·  <em style="font-weight: bold;">Precious metals.</em> Investors purchase precious metals as a hedge against inflation, or as a backstop to protect wealth against a catastrophe, assuming that when disaster wracks the financial markets, metals such as gold will retain their value.</p>
                <p style="margin-left: 5%; margin-right: 3%;  margin-top:1%">·  <em style="font-weight: bold;">Collectibles.</em> While investors can make money in collectibles, most lack the market expertise to profit consistently.</p>
                    <p style="margin-left: 5%; margin-right: 3%;  margin-top:1%">·  <em style="font-weight: bold;">Real estate.</em> The only exception to this book's "avoid alternative assets" rule, real estate can diversify a portfolio of stocks, and it acts as a hedge against inflation, tending to rise in value during periods when inflation erodes the price of financial assets. However, if you already own a home, you probably have enough exposure to real estate. Of course, plenty of investors appreciate the inflation protection and total-return potential of real estate and would like to buy in. However, because pieces of real estate cost so much, few individuals have the funds to directly invest in property beyond their personal residences. You can’t buy shares of a piece of property on a public market. If you seek real estate exposure, consider real estate investment trusts (REITs). These companies buy, sell, and manage real estate, and their trust units trade on exchanges like stocks.</p>
            



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
            <span>Title: Alternative Investments Explained</span>
            </el-row>
            <el-row class="source-text">
            <span>Author: Blue Sky Alternative Investments Limited</span>
            </el-row>
            <el-row class="source-text">
                Source: https://youtu.be/d3NWBvKQEdE
            </el-row>
            <el-row class="source-text">
                <p>Why do alternative assets matter? Watch how the power of alternative investments can generate strong returns, then visit blueskyfunds.com.au.</p>
                <p>Blue Sky Alternative Investments Limited is an Australian-based diversified alternative asset manager specialising in four asset classes: Private Equity, Private Real Estate, Hedge Funds and Real Assets.</p>
                <p>Visit blueskyfunds.com.au to find out more.</p>
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
      videoEmbedCode: 'https://www.youtube.com/embed/d3NWBvKQEdE',
    };
  },
  methods:{
      GoNext(){
          this.$router.push('/chapter3.7')
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
    margin-right: 3%;
}
.bordered-row {
  border: 1px solid #ccc;
  padding: 10px;
}
</style>
