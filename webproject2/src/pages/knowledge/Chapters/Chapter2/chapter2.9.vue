<template>
    <div>
        <el-row class="chapterbox" >
            <h2 style="margin-left: 3%;  margin-top:4%"> 09  Should I subscribe to a newsletter or go to a broker for help picking stocks? Or am I better off making my own investment decisions and not paying for advice?</h2>
        </el-row>
                
        <el-row style="background: #F5EFE0;border-radius: 30px; margin-top:1%; margin-left: 3%; margin-right: 3%;" >
            <h2 style="margin-left: 3%;  margin-top:2%">Answer</h2>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:1%">The answer to this question depends on the answer to two other questions. How much time will you commit to working on your investments? And how comfortable do you feel analyzing numbers?</h4>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:1%">People who claim to have found the single trick to making money in the stock market shoot e-mails everywhere. “I made 932%, and so can you!” Sometimes they’re lying about the return, and sometimes they’re telling the truth. Even if an investor did manage to make a 932% return on a stock once, you can’t assume he’ll do it again. Markets simply don’t work that way.</h4>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:1%">Real stock analysis—the type of research performed by experts who manage other people’s money and can get fired if they mess up—takes time. You don’t need to commit 40 hours a week, but unless you know you’ll spend at least 3 hours a week reading about your companies, following market news, and comparing one stock with another, don’t try to go it alone. Find someone you trust—a newsletter editor, a financial planner, or an online guru who actually offers advice without spitting through the computer screen—and pay attention. You don’t have to follow anyone’s advice exactly, but you’ll make better decisions when you can start your own analysis by looking at stocks other people like, or when you can use someone else’s strategy to double-check your own selections.</h4>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:1%">Now, regarding the numbers. More and more, math geeks rule the world. Stock analysis isn’t rocket science, and you don’t need a PhD in mathematics or statistics to analyze stocks. The job merely requires a flexible mind, a willingness to learn a few new ideas, and a calculator. </h4>
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
          this.$router.push('/chapter2.10')
      },
      Goback(){
          this.$router.push('/chapter2')
      }
  },
    created(){
        
            var userid = this.$store.state.accountid;
            var chapterid = 2;
            var subchapterindex =9;
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
