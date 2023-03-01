<template>
    <div>
        <el-row class="chapterbox" >
            <h2 style="margin-left: 3%;  margin-top:4%"> 01 Opening</h2>
        </el-row>
        <el-row style="background: #F5EFE0;border-radius: 30px;margin-top:1%; margin-left: 3%; margin-right: 3%;" >
            <h2 style="margin-left: 3%;  margin-top:2%">Opening</h2>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:1%">Everybody invests. From the savvy stockbroker on Wall Street to the assembly line worker who skips breakfast every Friday because he runs out of money before his next paycheck, everyone invests their time, effort, and attention in what they find important.</h4>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:1%">If you spend your Saturdays training for a marathon or tackling 50-mile bike rides, you’re investing in your health. If you pack your weekends with family activities, taking the kids to swimming practice or attending Little League games or visiting museums, you’re investing in your children. And if you attend classes in hopes that a college degree will help you land a better job, you’re investing in your career.</h4>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:1%">While each of these forms of investing appears to support a different goal, all of them—and dozens more—share a common purpose: to provide for the future. Investing in good health now increases your chances of a happier, more productive retirement. Investing in your family now can build relationships that will sustain in times when you may require more from others yet have less to give in return. Investing in your career now can open professional and financial doors currently out of reach.</h4>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:1%">Most people reap the richest rewards from their investments after retirement, but the sooner you start planning, the better off you will be in the future. Making even a small commitment to a different kind of investing —the financial strategies presented in this book—can put you well on your way to a longer and stronger retirement.</h4>
        
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
            <span>Title: Why Investing is the Best Way to Get Rich | Phil Town</span>
            </el-row>
            <el-row class="source-text">
            <span>Author: Phil Town's Rule #1 Investing</span>
            </el-row>
            <el-row class="source-text">
                Source: <a v-bind:href="linkUrl">https://youtu.be/bOVamLc5Etc</a>
            </el-row>
            <el-row class="source-text">
                <span>Investing is perhaps the greatest way to have your money work for you. With the power of compounding interest, your money can grow exponentially over the years. And the earlier you start investing, the greater affect this compounding will have on your financial freedom.</span>
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
      videoEmbedCode: 'https://www.youtube.com/embed/bOVamLc5Etc',
      };
  },
  methods:{
      Gotest(){
          this.$router.push('/chapter1.2')
      },
      Goback(){
          this.$router.push('/chapter1')
      }
  },    
  computed: {
    linkUrl() {
      // return the URL for the link
      return 'https://youtu.be/bOVamLc5Etc';
    },
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
