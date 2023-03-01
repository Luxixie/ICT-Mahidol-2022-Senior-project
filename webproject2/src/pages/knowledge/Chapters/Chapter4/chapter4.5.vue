<template>
    <div>
        <el-row class="chapterbox" >
            <h2 style="margin-left: 3%;  margin-top:4%"> 05 Runing the number</h2>
        </el-row>
        <el-row style="background: #F5EFE0;border-radius: 30px;margin-top:1%; margin-left: 3%; margin-right: 3%;" >
            <h2 style="margin-left: 3%;  margin-top:2%">Concept</h2>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:1%">Once you answer the four key questions, you’ll better understand what you need from your portfolio. And with that knowledge comes power.</h4>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:1%">Questions one and two—how much money do you need, and when do you need it—will help you determine your required rate of return. The following equation will give you a rate of return for any starting and ending point, assuming you wish to grow a basket of money and do not plan to add any new funds:</h4>
            <p style="margin-left: 3%; margin-right: 3%;  margin-top:2%; font-weight: bold;font-size:22px;font-style: italic;">(What you need What you have) ^ (1 Years until you need it) – 1</p>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:2%">For example, if you need $1 million, and you have $100,000, and you plan to retire in 25 years, it looks like this:</h4>
            <p style="margin-left: 3%; margin-right: 3%;  margin-top:1%;font-weight: bold;font-size:22px;font-style: italic;">($1,000,000 $100,000) ^ (1 25) – 1 = 0.096 = 9.6%</p>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:2%">But what if you have nothing, yet you can commit funds to invest over time? You can easily create a table like the wealth-building one earlier to plot different scenarios. Here’s the equation:</h4>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:1%;font-weight: bold;font-size:22px;font-style: italic;">[Portfolio value X (1 + Rate of return)] + Annual investment = Portfolio value a year later</h4>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:1%">The following is an example of the beginning of a wealth-building table, starting with the following assumptions:</h4>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:1%">* Begin at the end of the first year, assuming a year of investment contributions in your brokerage account.</h4>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:1%">* You contribute $500 per month.</h4>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:1%">* Your investments grow at 8% a year.</h4>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:2%">Year 1 : $6,000</h4>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:2%">Year 2 : $6,000 X (1.08) + $6,000 = $12,480</h4>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:2%">Year 3 : $12,480 X (1.08) + $6,000 = $19,478</h4>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:1%">Build that formula into a spreadsheet and you can see how long it will take to reach your goal. Alternatively, if you know when you need to reach that goal, try different rates of return to determine the kind of returns needed to get you there at the proper time.</h4>
            
            <h2 style="margin-left: 3%;  margin-top:2%">Classifications</h2>
            <h4  style="margin-left: 3%; margin-right: 3%;  margin-top:1%">Before you move on to the last step, make sure you’ve avoided these four pitfalls:</h4>
            <p style="margin-left: 5%; margin-right: 3%;  margin-top:1%"><em style="font-weight: bold;">·  Unreasonable expectations.</em> If your required rate of return is more than 10%, change your assumptions. Even 10% returns will be very, very difficult, and any plan based on the chance that you can earn more than 10% will fail more often than it succeeds. Don’t kid yourself. Remember the 50-year-old from Chapter 1 with a $40,000 salary, no savings, lots of college expenses, and plans to retire a millionaire at 65? He failed before he started. Don’t join him.</p>
            <p style="margin-left: 5%; margin-right: 3%;  margin-top:1%"><em style="font-weight: bold;">·  Forgetting inflation. </em>Over the last 80-plus years, inflation has averaged 3% annually. Make sure your spending estimates reflect inflation.</p>
            <p style="margin-left: 5%; margin-right: 3%;  margin-top:1%"><em style="font-weight: bold;">·  Forgetting expenses.</em> Try to add a few extra costs into your plan. You might get sick. Your house might burn down. Your brother-inlaw might guilt-trip you into backing his restaurant, even though you know most restaurants fail. Life happens, and things that cost money are a part of life.</p>
            <p style="margin-left: 5%; margin-right: 3%;  margin-top:1%"><em style="font-weight: bold;">·  Underestimating your needs and life span.</em> If you think you’ll need $60,000 a year, plan for $70,000. If you think you’ll live 20 years past retirement, plan for 25. The more conservative your estimates, the more likely your investment plan will achieve its goals.</p>

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
            <span>Title: 9 Most Popular Investment Portfolio Strategies</span>
            </el-row>
            <el-row class="source-text">
            <span>Author: Tae Kim - Financial Tortoise</span>
            </el-row>
            <el-row class="source-text">
                Source: <a v-bind:href="linkUrl">https://youtu.be/eJmt9sqDFNc</a>
            </el-row>
            <el-row class="source-text">
                <p>When it comes to investing portfolio strategies, there are countless options available. So which one is right for you? In this video, we'll take a look at nine of the most popular investment portfolio strategies and explore what each one entails.  Which strategy will you choose?</p>
                <p>DISCLAIMER:(from author) </p>
                <p>I am not a financial adviser. These videos are for educational and entertainment purposes only. I am merely sharing my personal opinion.  Please seek professional help when needed.</p>
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
      videoEmbedCode: 'https://www.youtube.com/embed/eJmt9sqDFNc',
      };
  },
  methods:{
      Gotest(){
          this.$router.push('/chapter4.6')
      },
      Goback(){
          this.$router.push('/chapter4')
      }
  },
    computed: {
    linkUrl() {
      // return the URL for the link
      return 'https://youtu.be/eJmt9sqDFNc';
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
