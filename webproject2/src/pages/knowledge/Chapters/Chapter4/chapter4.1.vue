<template>
    <div>
        <el-row class="chapterbox" >
            <h2 style="margin-left: 3%;  margin-top:4%"> 01 How much do you need?</h2>
        </el-row>
        <el-row style="background: #F5EFE0;border-radius: 30px;margin-top:1%; margin-left: 3%; margin-right: 3%;" >
            <h2 style="margin-left: 3%;  margin-top:2%">Concept</h2>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:1%">Investors can make many types of mistakes as they plan for the future. But perhaps the most common—and the most dangerous—is not knowing how much you need.</h4>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:1%">Is $1 million enough? That depends on when you retire, how long you live, and how much you plan to spend. Check out the following table, which assumes you manage to sock away $1 million by the time you retire, and then invest well enough to earn 5% per year after inflation. The numbers might surprise you.</h4>
            <el-row :span="2" class="container" style="margin-top:3%;margin-left:25%">
                <img src="./images/2.jpg" class="image" >
            </el-row>
            <p  style="text-align: center;">Table 11.1 - Living off $1 Million</p>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:1%">Somehow $1 million doesn’t look like quite as much money after you crunch the numbers. If you plan to amass a $1 million fortune by retirement, and then live on $120,000 a year each year after you retire, you’d better plan to work until you’re 75—or die fairly young. Neither choice would appeal to most investors. (For the record, the retiree who can live on $60,000 a year and sustain a 5% investment return after inflation could stretch his $1 million for 36 years.)</h4>
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
            <span>Title: How Much Money Should I Invest - Stock Market Dividends</span>
            </el-row>
            <el-row class="source-text">
            <span>Author: Andrei Jikh</span>
            </el-row>
            <el-row class="source-text">
                Source: <a v-bind:href="linkUrl">https://youtu.be/yMq8yVqs4Zg</a>
            </el-row>
            <el-row class="source-text">
                <span>ABOUT: If you've ever wondered how much money you should save and invest, you have to watch this video. The stock market is an amazing wealth building tool that requires nothing more than a little bit of time and dedication. Building passive income with a stock portfolio takes a little bit knowledge and some simple money management. </span>
                <span>Legal Disclosure: I’m not a financial advisor. The information contained in this video is for entertainment purposes only. Before investing, please consult a licensed professional. Any stock purchases I show on video should not be considered “investment recommendations”.  I shall not be held liable for any losses you may incur for investing and trading in the stock market in attempt to mirror what I do. Unless investments are FDIC insured, they may decline in value and/or disappear entirely. Please be careful!</span>
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
      videoEmbedCode: 'https://www.youtube.com/embed/yMq8yVqs4Zg',
    };
  },
  methods:{
      Gotest(){
          this.$router.push('/chapter4.2')
      },
      Goback(){
          this.$router.push('/chapter4')
      }
  },
    created(){
        
            var userid = this.$store.state.accountid;
            var chapterid = 4;
            var subchapterindex = 1;
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
