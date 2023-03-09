<template>
    <div>
        <el-row class="chapterbox" >
            <h2 style="margin-left: 3%;  margin-top:4%"> 07 Equation</h2>
        </el-row>
        <el-row style="background: #F5EFE0;border-radius: 30px;margin-top:1%; margin-left: 3%; margin-right: 3%;" >
            <h2 style="margin-left: 3%;  margin-top:2%">Concept</h2>
            <p style="margin-left: 3%; margin-right: 3%;  margin-top:1%;font-weight: bold;font-size:22px;font-style: italic;">(Stock allocation X Stock returns) + (Bond allocation X Bond return) (70% X 10%) + (30% X 6%) = 7.0% + 1.8% = 8.8%.</p>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:1%">Remember, this is just an approximate portfolio return based on estimated stock and bond returns. It’s definitely a work in progress—and at best a rough estimate—but now you have enough to compare your required return (the return you need to get where you wish to go) and your target return (the return implied by your target allocation). If your requirements exceed your target, you’ll either have to take on more risk—as in choosing a higher stock allocation—or scale back on your investment targets.</h4>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:1%">Nobody likes to cut back on their goals or realize they can’t live it up during retirement. When it comes to whether or not you can keep your house or cover your medical expenses after retirement, surprises can hurt. It’s better to take the time to learn how far your resources can take you. Then you can adjust your goals to match your reality.</h4>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:1%">If your target exceeds your requirements, then life is good. You can reduce your risk to boost your chance of achieving your goals, or you can attempt to build extra wealth—potentially providing increased flexibility in the future.</h4>
        </el-row>
        <el-row style="background: #F5EFE0;border-radius: 30px;margin-top:1%; margin-left: 3%; margin-right: 3%;" >
            <h2 style="margin-left: 3%;  margin-top:2%">Summary -- Closing It Out</h2>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:1%">Whew. It took some work, but by now you should have a good idea about how to reach your financial destination without running out of money. After you master the concepts in this book, take the initiative to expand your knowledge of investing. Read books about investment analysis or delve deeper into the world of portfolio management—the list of suggested readings at the end of this book is a great place to start. It’s never too late to begin working toward your goals for the future, and no matter how much you learn, you’ll never figure everything out.</h4>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:1%">The journey never really ends. Fortunately, the strategies in this book should get you off to a good start.</h4>
        </el-row>
        
        <el-row style="margin-left: 4%; margin-right: 4%;margin-top:1%">
            <el-col :span="12" >
                <el-button  @click="Goback" type="warning" style="color: black; font-size:25px; border-radius: 50px; width:150px;height:60px" >Back</el-button>
            </el-col>
            <el-col :span="12" style="text-align: right; " >
                <el-button @click="Gotest" type="warning" style="color: black; font-size:25px; border-radius: 50px; width:150px;height:60px" >Go Test</el-button>
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
            path:"/test/"+4,
            params:{chapter:4}
          })
        },
        Goback(){
            this.$router.push('/chapter4')
        }
    },
    created(){
        
            var userid = this.$store.state.accountid;
            var chapterid = 4;
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


</style>
