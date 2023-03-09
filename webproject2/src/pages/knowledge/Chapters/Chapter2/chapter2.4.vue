<template>
    <div>
        <el-row class="chapterbox" >
            <h2 style="margin-left: 3%;  margin-top:4%"> 04  Which should I buy, stocks or bonds?</h2>
        </el-row>
                
        <el-row style="background: #F5EFE0;border-radius: 30px; margin-top:1%; margin-left: 3%; margin-right: 3%;" >
            <h2 style="margin-left: 3%;  margin-top:2%">Answer</h2>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:1%">For most investors, the smart answer is both. Both stocks and bonds play an important role in a portfolio. While stocks offer superior growth potential during good years (as well as a lot more downside potential during bad years), bonds provide greater income and steadier overall returns (though they can’t match stocks for potential upside).</h4>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:1%">While not all stocks trace the same path, they do tend to move in similar directions. If the S&P 500 Index has returned 15% in a given year, for example, most stocks—even those outside of the index—have probably posted positive returns. Some tread more quickly than others, of course.</h4>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:1%">Bonds also tend to move in the same direction as other bonds, though different classes within the bond group (such as long-term corporate bonds, Treasury bills, high-yield bonds, etc.) will see their returns diverge.</h4>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:1%">While both bonds and stocks tend to run in loose packs, a fact investors should exploit to reduce volatility is that those packs don’t often run together. So, how much should you put in stocks versus bonds? There’s no single right answer that applies to everyone. But you can start with this longtime industry rule of thumb: Subtract your age from 110, and you have a good baseline for stock exposure. The equation suggests a 30-year-old should hold 80% stocks and 20% bonds, while an 80-year-old should hold 30% stocks and 70% bonds. Of course, many other factors beyond age contribute to this decision,</h4>
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
            <span>Title: Stocks or Bonds in Today's Stock Market?</span>
            </el-row>
            <el-row class="source-text">
            <span>Author: Learn to Invest - Investors Grow</span>
            </el-row>
            <el-row class="source-text">
                Source: <a v-bind:href="linkUrl">https://youtu.be/RT5Kawc5XbQ</a>
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
      videoEmbedCode: 'https://www.youtube.com/embed/RT5Kawc5XbQ',
    };
  },
  methods:{
      GoNext(){
          this.$router.push('/chapter2.5')
      },
      Goback(){
          this.$router.push('/chapter2')
      }
    },
    created(){
        
            var userid = this.$store.state.accountid;
            var chapterid = 2;
            var subchapterindex = 4;
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
      return 'https://youtu.be/RT5Kawc5XbQ';
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
