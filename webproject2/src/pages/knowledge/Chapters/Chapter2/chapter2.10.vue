<template>
    <div>
        <el-row class="chapterbox" >
            <h2 style="margin-left: 3%;  margin-top:4%"> 10 The stock market is falling, but I like the looks of Acme Widget. Should I buy the shares now or wait until the price dips further?</h2>
        </el-row>
                
        <el-row style="background: #F5EFE0;border-radius: 30px; margin-top:1%; margin-left: 3%; margin-right: 3%;" >
            <h2 style="margin-left: 3%;  margin-top:2%">Answer</h2>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:1%">Plenty of investors make buy and sell decisions based solely on a stock’s price action—a process called technical analysis. Technical analysts look at a stock’s price chart and draw conclusions about where it will go based on where it has been. Some people make money this way, and some lose it. However, even experts will agree that predicting and timing short-term stock or market movements is extremely difficult.</h4>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:1%">This book provides you with the tools to analyze stocks from a fundamental standpoint: by looking at their operating statistics or valuation ratios. Once you identify a stock with strong investment potential at its current price, you take a risk by not purchasing it immediately. Sure, the stock could dip, offering you a chance to snap it up at a bargain. However, the price could also rise, eating away some of your potential profit. As a practical matter, investors who loved a stock at $50 per share tend to find it far more difficult to pull the trigger on the buy after it jumps to $60, even if it rises on good news and the future still looks bright.</h4>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:1%">Markets often shift direction erratically, and just because stocks have declined over the last week doesn’t mean they’ll keep declining any more than it means they’ll reverse course completely. In most cases, you just can’t tell. Unless you have some personal insight about the direction of the stock or the market in the coming days, don’t hold off on your purchase in the hopes of buying at a better price.</h4>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:1%">Keep in mind that after you buy, the market could always go up or go down. Don’t kick yourself for acting too soon if the market declines, and don’t pat yourself on the back because you bought right before an upturn. If you purchased the right stock, you’ll reap your reward in time, regardless of what the market does immediately after you make your buy.</h4>
        </el-row>
        

        <el-row style="margin-left: 4%; margin-right: 4%;margin-top:1%">
            <el-col :span="12" >
                <el-button  @click="Goback" type="warning" style="color: black; font-size:25px; border-radius: 50px; width:150px;height:60px" >Back</el-button>
            </el-col>
            <el-col :span="12" style="text-align: right; " >
                <el-button @click="Gotest" type="warning" style="color: black; font-size:25px; border-radius: 50px; width:150px;height:60px" >Go Test</el-button>
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
      Gotest(){
        this.$router.push({
            path:"/test/"+2,
            params:{chapter:2}
          })
      },
      Goback(){
          this.$router.push('/chapter2')
      }
    },
    created(){
        
            var userid = this.$store.state.accountid;
            var chapterid = 2;
            var subchapterindex = 10;
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
