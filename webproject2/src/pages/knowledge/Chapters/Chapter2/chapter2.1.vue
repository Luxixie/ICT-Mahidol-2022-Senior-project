<template>
    <div>
        <el-row class="chapterbox" >
            <h2 style="margin-left: 3%;  margin-top:4%"> 01 How do i start invest in stock?</h2>
        </el-row>
        <el-row style="background: #F5EFE0;border-radius: 30px; height: 450px; margin-top:1%; margin-left: 3%; margin-right: 3%;" >
            <h2 style="margin-left: 3%;  margin-top:2%">Concept</h2>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:2%">Most large companies and many small ones trade on exchanges to make it easier for investors to buy their shares. Exchanges require companies to meet certain criteria, such as the number of shares available for issue, market value, share price and financial benchmarks, before they can go public. However, thousands of companies do not list on the exchange, either because they cannot meet listing requirements or simply choose not to pay the exchange's fees. These stocks are traded through a network of securities dealers who negotiate deals with each other. These stocks are known as over-the-counter (OTC) transactions. Over-the-counter stocks have a reputation for risk because they tend to be smaller and less well-known than their exchange-traded counterparts. Of course, plenty of over-the-counter stocks are good investments, and many large foreign companies trade over the counter. However, newbies may want to avoid over-the-counter stocks, especially penny stocks - stocks that are priced very low. Both exchanges and over-the-counter markets welcome foreign companies. Companies outside the United States can register American Depositary Receipts (ADRs) or other specialized securities that allow their shares to trade on U.S. exchanges. Many American companies use similar systems to trade on markets in Canada, Europe or Asia. Never before have investors enjoyed so much flexibility in buying and selling securities.</h4>
       <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:2%"> Open an investment account with a broker. While there are several hundred companies that allow you to buy your first stock directly from them, most can only trade their shares on the stock exchange or through a dealer network. A brokerage account gives you access to thousands of stocks, as well as thousands of mutual funds and other investments. Most brokers make the account setup process easy, especially if you use the Internet. Visit your broker's website and fill out an account application. After you set up an account and send money in, you can start trading.
        </h4>
         
        </el-row>
        <el-row style="background: #F5EFE0;border-radius: 30px; height: 600px; margin-top:1%; margin-left: 3%; margin-right: 3%;"> 
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
            <span>Title: How to Invest in Stocks - Stock Market For Beginners</span>
            </el-row>
            <el-row class="source-text">
            <span>Author: ClearValue Tax</span>
            </el-row>
            <el-row class="source-text">
                Source: https://youtu.be/dbDijzEgo7E
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
      videoEmbedCode: 'https://www.youtube.com/embed/dbDijzEgo7E'
    };
  },
  methods:{
      Gotest(){
          this.$router.push('/test')
      },
      Goback(){
          this.$router.push('/chapter2')
      }
  }
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

</style>
