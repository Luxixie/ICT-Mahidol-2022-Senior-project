<template>
    <div>
        <el-row class="chapterbox" >
            <h2 style="margin-left: 3%;  margin-top:4%"> 04 How much risk can you handle?</h2>
        </el-row>
        <el-row style="background: #F5EFE0;border-radius: 30px;margin-top:1%; margin-left: 3%; margin-right: 3%;" >
            <h2 style="margin-left: 3%;  margin-top:2%">Concept</h2>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:1%">Some investors require a 10% annual return to meet their financial objectives. That’s a high hurdle. People have managed it, but achieving 10% annual returns over a long period of time would tax both the skill and the luck of most professional investors, let alone that of beginners. What if the kind of securities needed to make a run at 10% annual returns will keep you up at night? Then you have two choices:</h4>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:1%">1) Live in fear. (This is not ideal.)</h4>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:1%">2) Alter your objectives so you can meet your goals with a less risky portfolio.</h4>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:1%">A lot of people choose option one, but option two makes the most sense, both for your portfolio and for your nerves.</h4>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:1%">In the investment business, fear of uncertainty is called risk aversion. In most cases, the term applies to fear of investment declines or volatility. Everyone fears losing all their money, but that isn’t really the issue here. Stocks are very likely to deliver excellent returns over a 20-year period, but you can’t just sit in your rocking chair and wait 20 years. Investing in the stock market involves living with the movements of your stocks day-to-day and year-to-year. And that’s where risk aversion comes in. Everyone has some level of risk aversion. The higher your level of risk aversion (the greater your fear of loss), the less risk you can tolerate.</h4>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:1%">Your level of wealth also affects your risk tolerance. If you have $1 million in the bank, earn a nice living, and won’t need your investments for 20 years, you can afford to take more risks than someone with $10,000 in the bank.</h4>

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
            <span>Title: How Much Risk Should You Take?</span>
            </el-row>
            <el-row class="source-text">
            <span>Author: Ben Felix</span>
            </el-row>
            <el-row class="source-text">
                Source: <a v-bind:href="linkUrl">https://youtu.be/t0EYr8Aex1I</a>
            </el-row>
            <el-row class="source-text">
                <p>Risk is more than an important part of investing. The whole concept of a financial market exists on the basis that taking risk can result in financial gain.</p>
                <p>While we are not able to control or predict the distribution of outcomes, we are able to choose the type and amount of risk that we take with our investments.</p>
            </el-row>


        </el-row>
        <el-row style="margin-left: 4%; margin-right: 4%;margin-top:1%">
            <el-col :span="12" >
                <el-button  @click="Goback" type="warning" style="color: black; font-size:25px; border-radius: 50px; width:150px;height:60px" >Back</el-button>
            </el-col>
            <el-col :span="12" style="text-align: right; " >
                <el-button @click="Gotest" type="warning" style="color: black; font-size:25px; border-radius: 50px; width:150px;height:60px" >Next</el-button>
            </el-col>
        </el-row>



        
    </div>
</template>


<script>
export default {
  data() {
    return {
      videoEmbedCode: 'https://www.youtube.com/embed/t0EYr8Aex1I',
    };
  },
  methods:{
      Gotest(){
          this.$router.push('/chapter4.5')
      },
      Goback(){
          this.$router.push('/chapter4')
      }
  },
    computed: {
    linkUrl() {
      // return the URL for the link
      return 'https://youtu.be/t0EYr8Aex1I';
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
.bordered-row {
  border: 1px solid #ccc;
  padding: 10px;
}
.container {
    width: 50%;
    height: 500px;
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
