<template>
    <div>
        <el-row class="chapterbox" >
            <h2 style="margin-left: 3%;  margin-top:4%"> 02 Common Motivations</h2>
        </el-row>
        <el-row style="background: #F5EFE0;border-radius: 30px;margin-top:1%; margin-left: 3%; margin-right: 3%;" >
            <h2 style="margin-left: 3%;  margin-top:2%">Concept</h2>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:1%">Motivations behind financial investing are nearly as numerous as investors themselves. Of course, your priorities may differ from your neighbor’s, but for the most part, motivations for investing tend to fall into three categories:</h4>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:1%">· Investing to build wealth.</h4>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:1%">· Investing to support a family.</h4>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:1%">· Investing to prepare for retirement.</h4>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:1%">Investors focused on building wealth tend to concentrate more on the near future than do other investors. Wealth allows you to establish and maintain a comfortable lifestyle. For some, that comfort might mean a nice- sized house, a couple of reliable cars, and a trip to somewhere warm for a week every January. Many investors are happy with such a lifestyle, while others set loftier goals. By building wealth slowly over time—the safest and surest way to do it—you can improve your lifestyle along with your net worth.</h4>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:1%">Investors who prioritize supporting a family often seek to accumulate enough wealth now to afford a home in a neighborhood with good schools, the occasional vacation, and things like ballet slippers, algebra tutoring, and summer camp. At the same time, these investors must look ahead to college, which never seems to get any cheaper. All of this is to say that family- oriented investors must be flexible.</h4>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:1%">Retirement-oriented investors take a longer view than both the wealth builders and the family oriented. You know the type—the type that work hard for 40 years, climbing the corporate ladder. Like most of us, they earn a respectable living without quite reaching the top rungs. Yet they live below their means and always keep one eye on the horizon. The ultimate goal for these investors is a smooth transition to retirement, where even without a paycheck they can maintain the standard of living they spent all those years earning.</h4>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:1%">Whether you seek to support a robust lifestyle, provide a happy home for your children, or just store enough away so you won’t have to work until you turn 80, you can improve the odds of reaching your goals by putting your money to work. Whether you’re 20, 40, or 60, you’ll enjoy more choices decades from now if you invest wisely—starting today.</h4>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:1%"> And it needs to be today. Not tomorrow, not next week, and certainly not on that mythical day when you suddenly start bringing in more than you spend and can conveniently spare a few hundred a month. People who put off investing until it’s convenient spend their golden years eating ramen noodles. You’ve got to start today.</h4>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:1%"> Not sure how to proceed? Don’t panic. By the end of this book, you’ll have a clear understanding of your financial goals as well as a number of the tools necessary to reach them. The first step is to avoid making a foolish— but frighteningly common—mistake.</h4>
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
            <span>Title: Invest In Yourself - Warren Buffett Motivational Video | Warren Buffett Speech | Simplilearn</span>
            </el-row>
            <el-row class="source-text">
            <span>Author: Simplilearn</span>
            </el-row>
            <el-row class="source-text">
                Source: <a v-bind:href="linkUrl">https://youtu.be/EqUEAk7R9FA</a>
            </el-row>
            <el-row class="source-text">
                <span>In this motivational video, Warren Buffett is an American investor, business tycoon, philanthropist, and the chairman and CEO of Berkshire Hathaway shares his incredible journey and advice for success in life. He is considered one of the most successful investors in the world and has a net worth of over US$85.6 billion as of December 2020, making him the world's fourth-wealthiest person. Warren Buffett is an investment guru and one of the celebrated philanthropist and most respected businessmen in the world.</span>
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
import axios from "axios";
export default {
  data() {
    return {
      videoEmbedCode: 'https://www.youtube.com/embed/EqUEAk7R9FA',
    };
  },
  methods:{
      Gotest(){
          this.$router.push('/chapter1.3')
      },
      Goback(){
          this.$router.push('/chapter1')
      }
  },
    created(){
        
        var userid = this.$store.state.accountid;
        var chapterid = 1;
        var subchapterindex = 2;
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
      return 'https://youtu.be/EqUEAk7R9FA';
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
</style>
