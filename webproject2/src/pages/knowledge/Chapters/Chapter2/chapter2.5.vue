<template>
    <div>
        <el-row class="chapterbox" >
            <h2 style="margin-left: 3%;  margin-top:4%"> 05 How do I know which stocks to buy?</h2>
        </el-row>
                
        <el-row style="background: #F5EFE0;border-radius: 30px; margin-top:1%; margin-left: 3%; margin-right: 3%;" >
            <h2 style="margin-left: 3%;  margin-top:2%">Answer</h2>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:1%">Entire books have been written on this topic, but most stock analysis boils down to a few key themes:</h4>
            <p style="margin-left: 5%; margin-right: 3%;  margin-top:1%"><em style="font-weight: bold;">· Value.</em> Even the fastest-growing stock isn’t worth buying if you must overpay. Beginners in particular shouldn’t mess around with pricey hypergrowth stocks. Before you buy, consider the stock’s key valuation ratios (price/earnings, price/sales, price/book, and price/operating cash flow).</p>
            <p style="margin-left: 5%; margin-right: 3%;  margin-top:1%"><em style="font-weight: bold;">· Growth.</em>Even the cheapest stock isn’t worth buying if the company can’t increase its profits. Rising sales, profits, and cash flow suggest the company’s products sell well enough to increase its penetration of the market.</p>
            <p style="margin-left: 5%; margin-right: 3%;  margin-top:1%"><em style="font-weight: bold;">· Profitability.</em>Any company can grow if it spends enough money. Well- run companies can maintain their profit margins while still growing. Investors should target stocks with stable or rising profitability.</p>
            <p style="margin-left: 5%; margin-right: 3%;  margin-top:1%"><em style="font-weight: bold;">· News.</em>What kind of headlines does the stock generate? Both good news and bad news can affect a stock’s price before any changes trickle down to the income statement or balance sheet.</p>
            <p style="margin-left: 5%; margin-right: 3%;  margin-top:1%"><em style="font-weight: bold;">· Comfort level.</em> If a stock will keep you up at night for any reason, don’t buy it. This rule applies even if the stock skyrockets or if all of your friends load up on the hot name. No investment, even a profitable one, makes sense for an investor who can’t buy into the idea as well as the stock.</p>
        
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
            <span>Title: How I Pick Stocks: Investing for Beginners | 6 STEPS</span>
            </el-row>
            <el-row class="source-text">
            <span>Author: Humphrey Yang</span>
            </el-row>
            <el-row class="source-text">
                Source: <a v-bind:href="linkUrl">https://youtu.be/ea6qNsLbxNA</a>
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
      videoEmbedCode: 'https://www.youtube.com/embed/ea6qNsLbxNA',
      };
  },
  methods:{
      GoNext(){
          this.$router.push('/chapter2.6')
      },
      Goback(){
          this.$router.push('/chapter2')
      }
  },
    computed: {
    linkUrl() {
      // return the URL for the link
      return 'https://youtu.be/ea6qNsLbxNA';
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
    margin-right: 3%;
}


.container {
    width: 80%;
    height: 300px;
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
