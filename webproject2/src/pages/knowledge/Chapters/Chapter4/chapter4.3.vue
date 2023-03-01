<template>
    <div>
        <el-row class="chapterbox" >
            <h2 style="margin-left: 3%;  margin-top:4%"> 03 How much can you invest?</h2>
        </el-row>
        <el-row style="background: #F5EFE0;border-radius: 30px;margin-top:1%; margin-left: 3%; margin-right: 3%;" >
            <h2 style="margin-left: 3%;  margin-top:2%">Concept</h2>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:1%">The answer to this question depends largely on two things: how much you make, and how much you spend to live. You have a lot more control over the second than the first. When it comes to this question, you need to really be honest. Who doesn’t believe he’s worth $100,000 per year? However, most Americans won’t sniff that annual salary.</h4>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:1%">Fortunately, you can build up a nest egg even if you never make $100,000 per year. Don’t believe it? The following table shows how quickly you can build an investment portfolio.</h4>
            <el-row :span="2" class="container" style="margin-top:3%;margin-left:25%">
                <img src="./images/3.jpg" class="image" >
            </el-row>
            <p  style="text-align: center;">Table 11.2 - Building Wealth a Month at a Time</p>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:1%">These are not bad numbers, and they assume you never get a raise—and thus never increase your monthly investment. Of course, the more you can set aside, the more you’ll have when you need it. And herein lies the most important key to building wealth: Spend less than you make.</h4>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:1%">Regardless of what your investments do from year to year—and you certainly can’t count on them delivering such steady growth—if you spend less than you make every single year, you’ll earn enough to support yourself and set some aside.</h4>
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
            <span>Title: How Much You Need To Invest By EVERY Age</span>
            </el-row>
            <el-row class="source-text">
            <span>Author: Graham Stephan</span>
            </el-row>
            <el-row class="source-text">
                Source: <a v-bind:href="linkUrl">https://youtu.be/0wzxE2Y-onA</a>
            </el-row>
            <el-row class="source-text">
                <p>AGE 20: Average Net Worth: $39,915</p>
                <p>1. GET A CREDIT CARD</p>
                <p>The point is to begin building up your credit score as soon as possible, and since 50% of your score is made up from your on-time payment history and how LONG you’ve had credit for…this is something you should do immediately.</p>
                <p>2. OPEN A ROTH IRA</p>
                <p>This will allow you to invest $6000 per year and grow your money COMPLETELY TAX FREE by the age of 59.5…meaning, by the time you’re older…everything is pure profit. </p>
                <p>3. SAVE 20% OF YOUR INCOME</p>
                <p>4. INVEST IN THE MARKETS</p>
            </el-row>
            <el-row class="source-text">
                <p>AGE 30: Average Net Worth: -$1043</p>
                <p>1. GET A CREDIT SCORE OF AT LEAST 750</p>
                <p>2. BE BAD-DEBT FREE BY 30 YEARS OLD</p>
                <p>This means you’ve paid off any loans or debt that’s above a 5% interest rate, you don’t have any credit card debt or personal loans outstanding, and besides the possibility of a low interest rate mortgage or student loan…you don’t have anything weighing you down. </p>
                <p>3. HAVE A 3-6 MONTH SAFETY FUND</p>
                <p>4. AIM FOR 1X YOUR SALARY SAVED</p>
            </el-row>

            <el-row class="source-text">
                <p>AGE 40: Median Net Worth: $80,000</p>
                <p>1. MAX OUT RETIREMENT ACCOUNTS ANNUALLY</p>
                <p>2. MAXIMIZE YOUR EARNINGS</p>
                <p>3. HAVE A BUDGET - NO MATTER WAHT</p>
                <p>4. KNOW HOW MUCH YOU NEED TO RETIRE</p>
                <p>The rule of thumb is that, for a 30-year retirement, you’ll need to have anywhere between 25 to 30x your annual spending INVESTED in order for that money to last you without running out. </p>
            </el-row>
            <el-row class="source-text">
                <p>AGE 50: Median Net Worth: $212,000</p>
                <p>1. HAVE 7-8X YOUR SALARY SAVED, OR 10-12X YOUR EXPENSES</p>
                <p>2. BE CLOSE TO PAYING OFF YOUR MORTGAGE</p>
                <p>3. HAVE A CLEAR PLAN FOR RETIREMENT</p>
            </el-row>
            <el-row class="source-text">
                <p>AGE 60: Median Net Worth: $266,000</p>
                <p>1. AIM FOR 10-12X YOUR SALARY SAVED UP</p>
                <p>2. PAY OFF YOUR PRIMARY RESIDENCE</p>
                <p>3. BEGIN WITHDRAWING FROM RETIREMENT ACCOUNTS</p>
            
            </el-row>
            <el-row class="source-text">
                <p>Obviously, this is only going to be a rough ballpark and some people may be way ahead or way behind this - but, that’s not important - it’s more important to realize that NOW is the best time to begin working towards these goals, and showing you that - the sooner you start - the easier it’s going to be…even if you’re not as far along as you would’ve liked. </p>
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
      videoEmbedCode: 'https://www.youtube.com/embed/yMq8yVqs4Zg',
    };
  },
  methods:{
      Gotest(){
          this.$router.push('/chapter4.4')
      },
      Goback(){
          this.$router.push('/chapter4')
      }
  },
    computed: {
    linkUrl() {
      // return the URL for the link
      return 'https://youtu.be/yMq8yVqs4Zg';
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
    margin-top: 1%;
}
.bordered-row {
  border: 1px solid #ccc;
  padding: 10px;
}
.container {
    width: 50%;
    height: 900px;
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
