<template>
    <div>
        <el-row class="chapterbox" >
            <h2 style="margin-left: 3%;  margin-top:4%"> 03 I want to buy Apple, but the stock costs several hundred dollars per share, and I don’t have enough money to buy 100 shares. Should I stick to cheaper stocks?</h2>
        </el-row>
        <el-row style="background: #F5EFE0;border-radius: 30px; margin-top:1%; margin-left: 3%; margin-right: 3%;" >
            <h2 style="margin-left: 3%;  margin-top:2%">Answer</h2>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:1%">This question requires two answers. First, regarding the issue of purchasing 100 shares. A couple of decades ago, buying shares in round lots of 100 mattered. Brokers didn’t like dealing with smaller trades, and in many cases they charged lower commissions for round lots. Some full- service brokers still prefer to deal in round lots, but with securities trading electronically and discount brokers charging a fixed rate for most trades, today you can buy 87 shares of Stock A and 42 shares of Stock B, and nobody will give you a hard time.</h4>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:1%">The financial world has evolved, and dollar-based investing has become popular. Dollar-based investing focuses on the size of the stock position in dollars, not shares. Suppose you have $25,000 to invest and wish to purchase 10 stocks. Consider putting $2,500 in each stock, which equates to 50 shares of a $50 stock, 83 shares of a $30 stock, or 29 shares of an $80 stock. Holding equal dollar amounts of all your stocks not only reduces the risk inherent in lopsided portfolios (if your biggest holding falls, it causes a disproportionate decline in the value of your entire portfolio), but also makes it easier to assess how each of your stocks are performing. If you start out with equal-dollar positions, you can tell at a glance which stocks have risen and which have fallen.</h4>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:1%">The second answer addresses the issue of cheap stocks. Many investors, particularly those who began buying stocks during the days when everyone purchased shares in round lots, still view a $100 stock as more expensive than a $50 stock. However, professionals value stocks relative to earnings, cash flows, or sales, and so should you.</h4>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:1%">For example, a stock that trades for $100 per share and earns $10 per share has a price/earnings ratio of 10, while a $50 stock that earns $2.50 per share trades at 20 times earnings—and the $50 stock looks more expensive than the $100 stock.</h4>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:1%">Whether you purchase 50 shares of the $50 stock or 25 shares of the $100 stock, a 10% rise in the stock’s price will have the same effect— boosting your holdings in that stock to $2,750 from $2,500.</h4>
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
            <span>Title: How to Invest in Stocks for Teenagers 2023 (Step by Step)</span>
            </el-row>
            <el-row class="source-text">
            <span>Author: Charlie Chang</span>
            </el-row>
            <el-row class="source-text">
                Source: <a v-bind:href="linkUrl">https://youtu.be/uWmPzNsgDZs</a>
            </el-row>
            <el-row class="source-text">
                <p>In this video, I go over a 100% free step by step course on how to invest in stocks for teenagers. If you’re a teenager, and you’re looking to start investing in the stock market, I'll show you a full guide/tutorial on how to invest in stocks if you’re under 18, as well as ALL the basics you need to know.</p>
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
import axios from "axios";
export default {
  data() {
    return {
        videoEmbedCode: 'https://www.youtube.com/embed/uWmPzNsgDZs',
        };
    },
    methods:{
        GoNext(){
            this.$router.push('/chapter2.4')
        },
        Goback(){
            this.$router.push('/chapter2')
        }
    },
    created(){
        
            var userid = this.$store.state.accountid;
            var chapterid = 2;
            var subchapterindex = 3;
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
      return 'https://youtu.be/uWmPzNsgDZs';
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
