<template>
    <div>
        <el-row class="chapterbox" >
            <h2 style="margin-left: 3%;  margin-top:4%"> 06 How do I know when to sell a stock?</h2>
        </el-row>
                
        <el-row style="background: #F5EFE0;border-radius: 30px; margin-top:1%; margin-left: 3%; margin-right: 3%;" >
            <h2 style="margin-left: 3%;  margin-top:2%">Answer</h2>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:1%">Entire books have been written on this topic, but most stock analysis boils down to a few key themes:</h4>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:1%">That said, there is no such thing as a permanent buy. Eventually, every stock outlives its utility in your portfolio. All stocks move up and down over time, but the ugly plunge of bank stocks in late 2008 and 2009—far worse than the decline in the broad market—illustrates the dangers of sticking with stocks when their environment changes substantially (see Figure 2.1).</h4>
            <el-row :span="2" class="container" style="margin-top:3%;margin-left:10%">
                    <img src="./images/2.png" class="image" />
            </el-row>
            <p  style="text-align: center;">Figure 2.1 - Don’t Bank on It</p>
            
            
            <h4 style="margin-left: 5%; margin-right: 3%;  margin-top:1%">1) The reason you bought the stock no longer applies. In other words, if you purchased the stock because of its valuation, does the valuation still look attractive? If growth drew you in, has that growth continued? If the answer is no, consider selling.</h4>
            <h4 style="margin-left: 5%; margin-right: 3%;  margin-top:1%">2) The company has fundamentally changed. Sometimes that drug company you purchased because of its pipeline of asthma drugs changes its direction and starts to focus on mental-health treatments. If you like the first approach but not the second, don’t be afraid to sell.</h4>
            <h4 style="margin-left: 5%; margin-right: 3%;  margin-top:1%">3) The business has fundamentally changed. Bank stocks illustrate this concept well. Back in late 2007 and early 2008, when a few critics began grousing about banks overextending themselves, many investors bailed out on their stocks. Before that, the rise of the Internet presaged the decline of newspapers. Investors who heard the train coming and sold their newspaper stocks in 2004 and their bank stocks in 2007 profited from their ability to see and from their willingness to accept the new reality.</h4>
            <h4 style="margin-left: 5%; margin-right: 3%;  margin-top:1%">4) You need the money. This one may sound silly or obvious. But didn’t you start investing to build wealth to cover expenses, either now or in the future? If you bought stocks to cope with your daughter’s college costs, sell some of them when the first tuition bill comes due, even if you still think all of your stocks make good investments. This does not mean you should sell a few shares just because the car needs new tires. You should have an emergency fund to cover that kind of expense. Even if you purchase stocks with the intention of selling them fairly soon, your stock portfolio as a whole serves a purpose with a longer time horizon.</h4>
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
            <span>Title: Warren Buffett: The 3 Times When You Should Sell a Stock</span>
            </el-row>
            <el-row class="source-text">
            <span>Author: The Swedish Investor</span>
            </el-row>
            <el-row class="source-text">
                Source: <a v-bind:href="linkUrl">https://youtu.be/uh5MgS9_roA</a>
            </el-row>
            <el-row class="source-text">
                <p>The decision to sell a stock can be rather confusing. Do you sell it because it has gone up, to secure a profit? Do you sell it because it has gone down, you know, cut your losses short? Or perhaps you should sell it because it has been flatlining while all your friends are getting rich on bitcoin?</p>
                <p>Luckily, Warren Buffett, the oracle of Omaha and the sage of securities, has got us covered on this subject. The world’s greatest investor has discussed the art of selling during quite a few different occasions. In this video, you’ll learn three practical situations in which it is time to sell you stock market holdings – Warren Buffett style. By the way, if you’ve only heard what Warren Buffett has had to say on this topic more recently, you are probably doing it wrong.</p>
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
      videoEmbedCode: 'https://www.youtube.com/embed/uh5MgS9_roA',
    };
  },
  methods:{
      GoNext(){
          this.$router.push('/chapter2.7')
      },
      Goback(){
          this.$router.push('/chapter2')
      }
  },
    created(){
        
            var userid = this.$store.state.accountid;
            var chapterid = 2;
            var subchapterindex = 6;
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
      return 'https://youtu.be/uh5MgS9_roA';
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
