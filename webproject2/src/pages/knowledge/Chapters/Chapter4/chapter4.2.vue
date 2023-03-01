<template>
    <div>
        <el-row class="chapterbox" >
            <h2 style="margin-left: 3%;  margin-top:4%"> 02 When will you need the money?</h2>
        </el-row>
        <el-row style="background: #F5EFE0;border-radius: 30px;margin-top:1%; margin-left: 3%; margin-right: 3%;" >
            <h2 style="margin-left: 3%;  margin-top:2%">Concept</h2>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:1%">If you don’t intend to touch your investments until retirement, this question has an easy answer. On the other hand, if you need $100,000 for college costs in 10 years, or if you plan to buy a vacation home years before you retire, now is the time to account for it. As a general rule, the shorter the investment period, the less you can depend on stocks, which tend to be volatile.</h4>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:1%">Between 1926 and 2012, there have been 66 periods of 20 years—1926 through 1946, 1927 through 1947, etc. Neither stocks nor bonds have ever posted a decline during a 20-year period. Large-company stocks lost value in only 4 of the 78 periods of 10 years, while neither corporate nor government bonds ever had a negative return. When it comes to five-year periods, the picture changes drastically. Large-company stocks declined in 12 of the 83 five-year periods, or roughly 14% of the time. Long-term corporate bonds declined in only 3 of the five-year periods, and it hasn’t happened in more than 40 years.</h4>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:1%">If you’re looking 20 years out, keeping mostly stocks in the portfolio makes sense. If you’re going to need the money in five years or less, you probably need some extra bond exposure.</h4>
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
            <span>Title: When Do I Buy a Stock Exactly - the Way Warren Buffet Knows When to Buy a Stock</span>
            </el-row>
            <el-row class="source-text">
            <span>Author: Learn to Invest - Investors Grow</span>
            </el-row>
            <el-row class="source-text">
                Source: <a v-bind:href="linkUrl">https://youtu.be/6Lu71eyaLoo</a>
            </el-row>
            <el-row class="source-text">
                <pn>In this video we are going to look at when to buy a stock. The goal of the video is to present a reliable strategy for identifying when to buy a stock exactly. We walk through 3 examples based on previous videos I’ve done before and when would have been the best time to buy it. </pn>
                <p>DISCLAIMER: (From author)</p>
                <p>I am not a financial advisor. These videos are for educational purposes only. Investing of any kind involves risk. Your investments are solely your responsibility and we do not provide personalized investment advice. It is crucial that you conduct your own research. I am merely sharing my opinion with no guarantee of gains or losses on investments. Please consult your financial or tax professional prior to making an investment.</p>
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
      videoEmbedCode: 'https://www.youtube.com/embed/6Lu71eyaLoo',
    };
  },
  methods:{
      Gotest(){
          this.$router.push('/chapter4.3')
      },
      Goback(){
          this.$router.push('/chapter4')
      }
  },
    computed: {
    linkUrl() {
      // return the URL for the link
      return 'https://youtu.be/6Lu71eyaLoo';
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
