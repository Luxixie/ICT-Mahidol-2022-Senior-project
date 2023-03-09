<template>
    <div>
        <el-row class="chapterbox" >
            <h2 style="margin-left: 3%;  margin-top:4%"> 07 My stock has declined, but I can’t find any news on it. What caused the dip?</h2>
        </el-row>
                
        <el-row style="background: #F5EFE0;border-radius: 30px; margin-top:1%; margin-left: 3%; margin-right: 3%;" >
            <h2 style="margin-left: 3%;  margin-top:2%">Answer</h2>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:1%"> You may never know. First, you must realize that the stock market reflects the collective will and opinions of millions of investors. If enough of them decide to sell Acme Widget—regardless of their individual reasons—the shares will decline in value.</h4>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:1%">Sometimes people sell a stock because it has performed well and they wish to book some profits. Stockholders may also sell because shares have begun to fall and they fear additional declines. Sometimes bad news from another company in the industry will cause a stock to decline because the factors driving the weakness in the other stock may affect the first stock. And sometimes stocks sell off in sympathy—perhaps when a close competitor has taken a heavy loss—even when the news doesn’t affect them directly; in such cases, they often rebound quickly.</h4>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:1%">Often a company’s stock will move up or down not because of any company-specific news, but because the market itself has taken a turn. Remember that stocks tend to move in a pack. As with any pack, you’ll see bold names that bolt to the front while plenty of stragglers hang back. If you own stocks, you should expect them to decline when the larger market declines.</h4>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:1%">Suppose the broad stock market dips 10% over the course of a couple of months. History suggests that it could still decline further, but eventually most stocks will recover. They always do. If your stock falls 10% in the midst of a widespread market decline of 10% without generating any negative news of its own, you can probably blame the broad market for the decline.</h4>
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
     
    };
  },
  methods:{
      GoNext(){
          this.$router.push('/chapter2.8')
      },
      Goback(){
          this.$router.push('/chapter2')
      }
  },
    created(){
        
            var userid = this.$store.state.accountid;
            var chapterid = 2;
            var subchapterindex = 7;
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
