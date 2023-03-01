<template>
    <div>
        <el-row class="chapterbox" >
            <h2 style="margin-left: 3%;  margin-top:4%"> 03 Attach importance to investment</h2>
        </el-row>
        <el-row style="background: #F5EFE0;border-radius: 30px;margin-top:1%; margin-left: 3%; margin-right: 3%;" >
            <h2 style="margin-left: 3%;  margin-top:2%">Concept</h2>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:1%">Look at Figure 1.1. Over the last 87 years, large-company stocks have averaged annual returns of 11.8%. Over the same period, stocks of small companies delivered a 16.5% average return. Long-term government bonds returned an average of 6.1% a year since 1926, while Treasury bills—about the lowest-risk investment available—managed just 3.6% returns. While both types of stocks handily outperformed bonds, the price of that return was overall higher risk. Small company stocks posted higher highs and lower lows than large companies and bonds, and they were also more likely than large stocks to see returns vary greatly from year to year. Investors call this type of risk volatility. Of course, bond investors didn’t suffer nearly as much volatility as stock investors.</h4>
            <el-row :span="2" class="container" style="margin-top:3%;margin-left:20%">
                    <img src="./images/2.jpg" class="image" />
            </el-row>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:1%">If you wish to become a successful investor, commit this concept to memory:</h4>
            <p style="font-weight: bold;margin-left: 3%; margin-right: 3%;  margin-top:1%;box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);font-size:30px">“High risk, high return. Low risk, low return.”</p>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:1%">Like so many important truths, the investment mantra above is simple to understand, but not always easy to implement. Still, the relationship between risk and return is the cornerstone of investing.</h4>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:1%">Every investment has ups and downs; nothing charts a straight path. However, some paths are rockier than others. The more risk you take, the greater your chance for a high return—or a big loss.</h4>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:1%">If a stockbroker or financial adviser tells you he can earn high returns with little risk, you’ve probably found the wrong guy to assist you with your investments.</h4>
        
        
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
            <span>Title: Why is investing important? | Edelweiss Wealth Management</span>
            </el-row>
            <el-row class="source-text">
            <span>Author: Nuvama Wealth</span>
            </el-row>
            <el-row class="source-text">
                Source: <a v-bind:href="linkUrl">https://youtu.be/udfEG48f8UE</a>
            </el-row>
            <el-row class="source-text">
                <span>This video will help you to understand why investing is important and how it will help you to deal with the inflation. Also, to know more on the basics of investing. </span>
                <p>
                    Why Investing is Important?
                </p>
                <p>Money is one of the most important and crucial part of human life as it plays a major role for daily livelihood and creating wealth for future. Many people have the habit to save money, however saving is different than investing. Savings is all about keeping a part of your income aside for future requirements. Whereas investing is about using the part of your income to invest in various options which will help to grow money. Most importantly, investing will not only help you to grow money but it will also help you to deal with the "Inflation". Consider the following example:</p>
                <p style="margin-top:2%"> Your Income - 100</p>
                <p>Your Expenses - 75</p>
                <p>Savings - 25</p>
                <p style="margin-top:2%">After Inflation - Expenses increase but the income is still same</p>
                <p style="margin-top:1%">Your Income - 100</p>
                <p>Your Expenses - 80</p>
                <p>Savings - 20</p>

                <p style="margin-top:2%">Instead of saving, it is better to invest money at a particular rate of interest which would help to deal with the inflation. There are many advantages of investing, you can invest based on your future financial goals.</p>
                <p>Some of the Benefits/Importance of Investing:</p>
                <p>1. Grow your money - Primary benefit of investing is to grow your money. There are various investment options available in the market that offer better rate of returns. You can choose the best investment options based on your financial goals and risk appetite.</p>
                <p>2. Tax Saving Investments - There are various investment options which will help you to save tax. Some of these options includes - tax saving mutual funds, ELSS funds, PF, PPF, tax saving fixed deposit, so on.</p>
                <p>3. Financial Goal - You can make investments for your short, mid or long-term financial goals. Some of these can be investing for your wedding, child's education or buying your dream home and so on. Start investing now to achieve your financial targets.</p>
            
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
      videoEmbedCode: 'https://www.youtube.com/embed/udfEG48f8UE',
    };
  },
  methods:{
      Gotest(){
          this.$router.push('/chapter1.4')
      },
      Goback(){
          this.$router.push('/chapter1')
      }
  },
    computed: {
    linkUrl() {
      // return the URL for the link
      return 'https://youtu.be/udfEG48f8UE';
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
