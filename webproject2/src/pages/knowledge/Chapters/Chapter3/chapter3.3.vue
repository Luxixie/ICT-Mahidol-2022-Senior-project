<template>
    <div>
        <el-row class="chapterbox" >
            <h2 style="margin-left: 3%;  margin-top:4%"> 03 Mutual Funds</h2>
        </el-row>
        <el-row style="background: #F5EFE0;border-radius: 30px;margin-top:1%; margin-left: 3%; margin-right: 3%;" >
            <h2 style="margin-left: 3%;  margin-top:2%">Concept</h2>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:1%">   Mutual funds pool the assets of multiple investors, providing buying power that exceeds that of all but the wealthiest individuals.</h4>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:1%">  Suppose you have $10,000 to invest. If you try to spread the money around into 50 stocks, commission costs alone might cripple you. But invest that same $10,000 in a mutual fund that owns 50 stocks, and you’ve purchased a tiny piece of each of those companies without the expense or hassle of acquiring them individually.</h4>
            <h4  style="margin-left: 3%; margin-right: 3%;  margin-top:1%"> Professional money managers decide when the fund buys and sells, and all of the investors win or lose together. If a mutual fund returns 10% in a year, every investor who owned the fund at the start of that year will see the same 10% return on his investment.</h4>
            <h4  style="margin-left: 3%; margin-right: 3%;  margin-top:1%"> At the end of 2012, investors worldwide had $26.8 trillion invested in mutual funds, with $13.0 trillion of those funds in the hands of U.S. money managers, according to the Investment Company Institute (ICI). Of that $13 trillion invested in U.S. mutual funds, 45% was in stock funds and 26% was in bond funds.</h4>

            <h2 style="margin-left: 3%;  margin-top:2%">Classifications</h2>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:1%"> Stock and bond mutual funds come in two flavors:</h4>
            <p style="margin-left: 5%; margin-right: 3%;  margin-top:1%">·  <em style="font-weight: bold;">Passively managed funds.  </em>Often called index funds, passively managed funds attempt to match the performance of an index. Indexes —such as the well-known S&P 500 Index of large-company stocks—are baskets of securities constructed to approximate the investment returns of a slice of the financial markets. Most indexes don’t change their component stocks often.</p>
            <p style="margin-left: 5%; margin-right: 3%;  margin-top:1%">·  <em style="font-weight: bold;">Actively managed funds.  </em> Unlike passively managed funds, actively managed funds buy and sell securities in an effort to exceed the return of their benchmark—usually an index or group of indexes.</p>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:1%"> It’s tough to overstate the importance of mutual funds as an investment vehicle. In the United States alone, more than 92 million people own mutual funds, often through retirement plans. Additionally, most 401(k) retirement
 plans invest workers’ assets in mutual funds, so if you participate in a company-sponsored retirement plan, you probably already own funds.</h4>

        <el-row style="background: #D9D9D9; border-radius: 61px;margin-left:8%;margin-right:8%"> 
            <el-col :span="9" :offset="1" style="margin-left:10%;margin-top:2%">
                <el-row class="bordered-row">
                    <h2 style="margin-left:2%;margin-right:1%;margin-top:2%；">Pros:</h2>
                </el-row>
                <el-row class="bordered-row">
                    <h4 style="margin-left:2%;margin-right:1%;">Professional management.  </h4>
                    <p style="margin-left:3%;margin-right:1%;margin-top:1%">Most individuals don’t know much about analyzing investments because of a lack of interest, a lack of training, or both. When you purchase a mutual fund, you’re hiring an expert to manage your money.</p>
                </el-row>
                <el-row class="bordered-row">
                    <h4 style="margin-left:2%;margin-right:1%;">Choice. </h4>
                    <p style="margin-left:3%;margin-right:1%;margin-top:1%">With nearly 9,000 traditional mutual funds on the market, just about any investor can find a fund to address her investment goals.</p>
                </el-row>
                <el-row class="bordered-row">
                    <h4 style="margin-left:2%;margin-right:1%;">Diversification. </h4>
                    <p style="margin-left:3%;margin-right:1%;margin-top:1%">Portfolios containing a variety of stocks or bonds tend to be less volatile than an individual stock or bond. Mutual- fund managers use their buying power to purchase multiple securities, which in most cases provide diversification.</p>
                </el-row>
                
            </el-col>

            <el-col :span="9" style="margin-right:10%;margin-left:5%;margin-top:2%">
                <el-row class="bordered-row">
                    <h2 style="margin-left:2%;margin-right:1%;margin-top:2%">Cons:</h2>
                </el-row>
                <el-row class="bordered-row">
                    <h4 style="margin-left:2%;margin-right:1%;">Costs.</h4>
                    <p style="margin-left:3%;margin-right:1%;margin-top:1%">Every mutual fund charges fees. If a broker tells you his fund doesn’t charge a fee, hang up the phone immediately because he’s lying. Remember that expert you hired when you purchased the mutual fund? He doesn’t work for free. In addition, some funds charge fees called loads, collecting extra money to compensate the salesperson or investment company.</p>
                </el-row>
                <el-row class="bordered-row">
                    <h4 style="margin-left:2%;margin-right:1%;">Complacency. </h4>
                    <p style="margin-left:3%;margin-right:1%;margin-top:1%">Mutual-fund investors often assume that since they have a professional managing a diversified basket of stocks, they can sit back and relax. Don’t make that mistake.</p>
                </el-row>
                <el-row class="bordered-row">
                    <h4 style="margin-left:2%;argin-right:1%;">Poor returns.</h4>
                    <p style="margin-left:3%;argin-right:1%;margin-top:1%">Last year, only about a third of actively managed mutual funds outperformed their benchmarks. Plenty of academic studies suggest this trend isn’t new and that fund fees deserve much of the blame. While the chronic underperformance shouldn’t scare you away from mutual funds, it should hammer home the importance of choosing your funds wisely.</p>
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
            <span>Title: Trading 101: What is a Mutual Fund?</span>
            </el-row>
            <el-row class="source-text">
            <span>Author: ClayTrader</span>
            </el-row>
            <el-row class="source-text">
                Source: https://www.youtube.com/embed/ihfHMI4XUDk
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
      videoEmbedCode: 'https://www.youtube.com/embed/ihfHMI4XUDk',
    };
  },
  methods:{
      GoNext(){
          this.$router.push('/chapter3.4')
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
