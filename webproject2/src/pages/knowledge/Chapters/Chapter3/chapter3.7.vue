<template>
    <div>
        <el-row class="chapterbox" >
            <h2 style="margin-left: 3%;  margin-top:4%"> 07 Weighing the Options</h2>
        </el-row>
        <el-row style="background: #F5EFE0;border-radius: 30px;margin-top:1%; margin-left: 3%; margin-right: 3%;" >
            <h2 style="margin-left: 3%;  margin-top:2%">Summary</h2>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:1%">No matter how thoroughly you analyze the options for potential investment, no matter how much care you take in crunching the numbers, no matter how much time you put into studying the stock market and the forces that affect it, you’re going to make mistakes. A lot of them.</h4>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:1%">Don’t panic. Nobody gets it right all the time. In fact, excessive boasting about returns and success rates is among the best ways a beginner can spot the posers. Boasters become particularly aggressive during bull markets— when many stocks are hitting new highs. Legendary investor Warren Buffett once wrote, “Only when the tide goes out do you discover who’s been swimming naked.” If you listen to the wrong voice, you’ll end up high, dry, and possibly embarrassed when the market corrects. And don’t kid yourself —it always corrects.</h4>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:1%">So before you buy into some pundit’s foolproof plan, do some of your own work. </h4>


        </el-row>
        <el-row style="margin-left: 4%; margin-right: 4%;margin-top:1%">
            <el-col :span="12" >
                <el-button  @click="Goback" type="warning" style="color: black; font-size:25px; border-radius: 50px; width:150px;height:60px" >Back</el-button>
            </el-col>
            <el-col :span="12" style="text-align: right; " >
                <el-button @click="Gotest" type="warning" style="color: black; font-size:25px; border-radius: 50px; width:150px;height:60px" >Done</el-button>
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
      Gotest(){
          this.$router.push({
              path:"/test/"+3,
              params:{chapter:3}
          })
      },
      Goback(){
          this.$router.push('/chapter3')
      }
  },
    created(){
        
            var userid = this.$store.state.accountid;
            var chapterid = 3;
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
.bordered-row {
  border: 1px solid #ccc;
  padding: 10px;
}
</style>
