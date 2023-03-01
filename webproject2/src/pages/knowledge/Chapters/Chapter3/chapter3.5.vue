<template>
    <div>
        <el-row class="chapterbox" >
            <h2 style="margin-left: 3%;  margin-top:4%"> 05 Certificates of Deposit</h2>
        </el-row>
        <el-row style="background: #F5EFE0;border-radius: 30px;margin-top:1%; margin-left: 3%; margin-right: 3%;" >
            <h2 style="margin-left: 3%;  margin-top:2%">Concept</h2>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:1%">  Traditional certificates of deposit (CDs) act as enhanced savings accounts. Investors give money to a bank, which then agrees to pay a fixed interest rate—generally for a period of five years or less. While investors can withdraw cash from a savings account at any time, CDs require them to keep the funds at the bank until the maturity date. Because of this limitation, they tend to pay more interest than typical savings accounts.</h4>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:1%">CDs can’t replace any of the other investments mentioned in this chapter. They simply provide you with a means to generate more interest on your cash holdings than you’d get from a bank savings account or a brokerage account.</h4>

        <el-row style="background: #D9D9D9; border-radius: 61px;margin-left:8%;margin-right:8%"> 
            <el-col :span="9" :offset="1" style="margin-left:10%;margin-top:2%">
                <el-row class="bordered-row">
                    <h2 style="margin-left:2%;margin-right:1%;margin-top:2%；">Pros:</h2>
                </el-row>
                <el-row class="bordered-row">
                    <h4 style="margin-left:2%;margin-right:1%;">Safety. </h4>
                    <p style="margin-left:3%;margin-right:1%;margin-top:1%">Like other bank accounts, CDs are insured for up to $250,000 by the Federal Deposit Insurance Corporation (FDIC) in the event the bank fails. Brokerage accounts do not receive FDIC coverage, though the Securities Investor Protection Corporation (SIPC) does provide similar, if less comprehensive, protection.</p>
                </el-row>
                <el-row class="bordered-row">
                    <h4 style="margin-left:2%;margin-right:1%;">No fluctuation. </h4>
                    <p style="margin-left:3%;margin-right:1%;margin-top:1%"> Because your funds remain in cash, they won’t decline in value.</p>
                </el-row>
                <el-row class="bordered-row">
                    <h4 style="margin-left:2%;margin-right:1%;">Simplicity. </h4>
                    <p style="margin-left:3%;margin-right:1%;margin-top:1%">If you understand savings accounts, you already know a lot about how CDs work.</p>
                </el-row>
                
            </el-col>

            <el-col :span="9" style="margin-right:10%;margin-left:5%;margin-top:2%">
                <el-row class="bordered-row">
                    <h2 style="margin-left:2%;margin-right:1%;margin-top:2%">Cons:</h2>
                </el-row>
                <el-row class="bordered-row">
                    <h4 style="margin-left:2%;margin-right:1%;">Low returns.</h4>
                    <p style="margin-left:3%;margin-right:1%;margin-top:1%">While CDs generally offer more interest than bank savings accounts, they’ll lag behind all of the other investment classes discussed in this chapter over the long haul.</p>
                </el-row>
                <el-row class="bordered-row">
                    <h4 style="margin-left:2%;margin-right:1%;">No liquidity. </h4>
                    <p style="margin-left:3%;margin-right:1%;margin-top:1%">CDs tie up your cash for a period of time. You can access the money if you need it, but you’ll pay an early withdrawal penalty or forfeit some of the interest.</p>
                </el-row>
                <el-row class="bordered-row">
                    <h4 style="margin-left:2%;argin-right:1%;">Separate accounts. </h4>
                    <p style="margin-left:3%;argin-right:1%;margin-top:1%">Most investors purchase stocks, bonds, and mutual funds from institutions other than banks. If you keep your cash in a bank CD, you must keep it at the bank, which means you can’t redeploy it to purchase stocks or bonds until you transfer the money to a brokerage account.</p>
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
            <span>Title: What are Certificates of Deposit? (CDs)</span>
            </el-row>
            <el-row class="source-text">
            <span>Author: Concerning Reality</span>
            </el-row>
            <el-row class="source-text">
                Source: https://youtu.be/_3cgMofw-rc
            </el-row>
            <el-row class="source-text">
                <p>What’s the best way to save and grow your money? Is it to dump it all into Bitcoin and hope it hits 100k? Or maybe you should put it all into gold and silver. Or… you could do neither of those things and put it something called a certificate of deposit. </p>
                <p>Get a free stock with WeBull: https://bit.ly/2tBxZYv</p>
                <p>Get a free stock with Robinhood: https://bit.ly/3eCJhi8</p>
                <p>Most people are familiar with savings accounts, or bank accounts where you can park your cash and get paid interest by a bank, usually about half a percent per year. That’s not much, but savings accounts do allow you to draw money out of them every month. However, if you’re looking for a higher rate of return, and don’t want to invest your cash in the stock market, a certificate of deposit or CD might be the right choice. </p>
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
      videoEmbedCode: 'https://www.youtube.com/embed/_3cgMofw-rc',
    };
  },
  methods:{
      GoNext(){
          this.$router.push('/chapter3.6')
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
