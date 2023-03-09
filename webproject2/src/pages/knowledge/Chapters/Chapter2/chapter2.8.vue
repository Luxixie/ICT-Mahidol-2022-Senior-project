<template>
    <div>
        <el-row class="chapterbox" >
            <h2 style="margin-left: 3%;  margin-top:4%"> 08 How do I track my portfolio?</h2>
        </el-row>
                
        <el-row style="background: #F5EFE0;border-radius: 30px; margin-top:1%; margin-left: 3%; margin-right: 3%;" >
            <h2 style="margin-left: 3%;  margin-top:2%">Answer</h2>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:1%">Twenty years ago, most large newspapers printed daily stock prices, and investors followed their investments in the paper. With the proliferation of websites offering the same information in a more timely fashion, often at no cost, many papers have eschewed the stock pages. These days, the Internet simply offers more information, and a host of financial websites do a fine job of providing pricing and trading data.</h4>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:1%">You can check out the performance of your stocks on your discount broker’s website. While each broker does the job a little differently, they should all show you the value of your stock positions and allow you to view the stocks’ history—how they have moved since you purchased them.</h4>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:1%">If you don’t buy all of your investments through the same broker, use a free third-party site to track all of your investments together. Popular financial websites include Yahoo! Finance (www.finance.yahoo.com), Google Finance (www.google.com/finance), and MSN Money (www.money.msn.com). All three of those sites and plenty of others provide free portfolio trackers. Just input your stocks’ ticker symbols, and you can create a portfolio of the stocks you own as well as stocks you wish to watch.</h4>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:1%">Interested in more detail than today’s share price? You can also enter the date you purchased the stock as well as the purchase price and the number of shares. If you input your transaction data, the website you selected will show you the returns of each stock since you purchased it— crucial information for assessing your portfolio.</h4>
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
            <span>Title: How I Track My Dividend Income | Portfolio Update #17</span>
            </el-row>
            <el-row class="source-text">
            <span>Author: Dividend Data</span>
            </el-row>
            <el-row class="source-text">
                Source: <a v-bind:href="linkUrl">https://youtu.be/g0AlDlRB4SI</a>
            </el-row>
            <el-row class="source-text">
                <p>Dividend Income is the best form of passive income. You simply invest in highly profitable companies and then they pay out a portion of their cash flows to you the shareholder. You can reinvest these dividends, which creates a powerful compounding effect, or you could take them as pure cash. Over time, dividend investing can help you reach financial independence with the ability to live entirely off this income. Because of this, many investors create countless spreadsheets to try and track their income. I should know, with me being one. Previously, I had a complex spreadsheet and I would generate graphs to share with you in my monthly portfolio updates. Well, I’m throwing all that out. It’s time to level up!</p>
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
        videoEmbedCode: 'https://www.youtube.com/embed/g0AlDlRB4SI',
        };
  },
  methods:{
      GoNext(){
          this.$router.push('/chapter2.9')
      },
      Goback(){
          this.$router.push('/chapter2')
      }
  },
    created(){
        
            var userid = this.$store.state.accountid;
            var chapterid = 2;
            var subchapterindex = 8;
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
      return 'https://youtu.be/g0AlDlRB4SI';
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
