<template>
    <div>
        <el-row class="chapterbox" >
            <h2 style="margin-left: 3%;  margin-top:4%"> 04 Set Attainable Goals</h2>
        </el-row>
        <el-row style="background: #F5EFE0;border-radius: 30px;margin-top:1%; margin-left: 3%; margin-right: 3%;" >
            <h2 style="margin-left: 3%;  margin-top:2%">Concept</h2>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:1%">Now that you understand the importance of investing and the different types of returns a few of the most common investments generate, it’s time to move on to your personal situation. Every individual has different investment requirements and strictures. No investment plan, no matter how shrewd or well considered, applies to everyone. To customize your own financial plan, ask yourself the following questions:</h4>
            <p style="margin-left: 5%; margin-right: 3%;  margin-top:1%"><em style="font-weight: bold;">·  What are my goals?</em> Be specific. “Get rich” won’t cut it. Your goals should set specific targets, such as, “Retire with $1 million in assets.”</p>
            <p style="margin-left: 5%; margin-right: 3%;  margin-top:1%"><em style="font-weight: bold;">·  How long can I take to reach those goals?</em> A 40-year-old mother with a daughter who will start college in 10 years must approach investing differently than a 40-year-old with no children who won’t touch her investments until she retires at 65.</p>
            <p style="margin-left: 5%; margin-right: 3%;  margin-top:1%"><em style="font-weight: bold;">·  How much risk should I accept?</em>  Some investors can tolerate more risk than others. Some people go cliff diving for relaxation, while others chew their nails at the thought of rain. Neither approach is right or wrong, but you’ll sleep better if you tailor your investment approach to your personal feelings about risk.</p>
            <p style="margin-left: 5%; margin-right: 3%;  margin-top:1%"><em style="font-weight: bold;">·  What must I do to meet those goals? </em> Now you’ve reached, quite literally, the million-dollar question. Even if you set modest goals, you won’t reach them overnight. As Table 1.1 illustrates, the time it takes to feather your nest depends on how quickly your investments grow. Divide 72 by an investment’s rate of return, and you know approximately how long it will take to double your money. Earn 4% a year, and your money doubles in 18 years. An 8% return doubles the money in nine years, while earning 12% shortens the doubling time to six years.</p>
            <el-table :data="tableData" border style="width: 40%; margin-left:30%;margin-right:40%">
                <el-table-column
                prop="data1"
                label="Investment growth rate"
                align="center">
                </el-table-column>
                <el-table-column
                prop="data2"
                label="Number of years to double in value"
                align="center">
                </el-table-column>
            </el-table>
            <p  style="text-align: center;">Table 1.1</p>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:1%"> Not sure how to proceed? Don’t panic. By the end of this book, you’ll have a clear understanding of your financial goals as well as a number of the tools necessary to reach them. The first step is to avoid making a foolish— but frighteningly common—mistake.</h4>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:1%">Suppose you have $100,000 in your 401(k) plan and hope to retire in 40 years with $1 million in assets. According to the Rule of 72, if you create a portfolio that returns 6% a year, your account would double to $200,000 by year 12, redouble to $400,000 by year 24, redouble again to $800,000 by year 36, and top $1 million at the end of year 40. Just in time to meet your goal.</h4>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:1%">Of course, investments never work that neatly. You can’t guarantee yourself a 6% return. And sometimes, even if you do manage a 6% annual return, you’ll endure a lot of twists and turns along the way—a 30% gain this year, a 15% loss next year, and then a flat year followed by an 8% gain. You get the picture.</h4>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:1%">Taking the innate uncertainty of investing into account, you should overengineer your investment portfolio. In other words, if you hope to accumulate a certain amount by a certain time, plan as if you need, say, 20% more than your target. Most of all, keep those targets reasonable.</h4>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:1%">For example, a 30-year-old with no savings and a job paying $40,000 per year who wants to retire a millionaire at age 65 shouldn’t require too much risk to reach that goal. A 40-year-old with no savings and a job paying $40,000 per year who wants to retire a millionaire at age 65 will only be able to attain that goal if she is willing to take on some risk. A 50-year-old with two children, no savings, and a job paying $40,000 per year who also wants to pay for his kids’ college educations without borrowing and then retire a millionaire at 65, simply does not have a reasonable goal.</h4>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:1%">At this point you may be asking, “How can I know whether my goal is reasonable?” Figure 1.2 should help.</h4>
            <el-row :span="2" class="container" style="margin-top:3%;margin-left:25%">
                    <img src="./images/3.jpg" class="image" />
            </el-row>
            <p  style="text-align: center;">Figure 1.2 - The Power of Time</p>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:1%">Too often, investors focus on the gulf between what they have and what they want and become discouraged. Don’t fall into that trap, because you haven’t embarked on this investment journey alone. You have a powerful ally: time.</h4>

            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:1%">Figure 1.2 demonstrates the power of time when it comes to investment. If you can invest at a 7.5% annual rate, $10,000 will grow to more than $20,000 in 10 years, and then to $42,000 in 20 years. After 40 years, that $10,000 will have grown into a $180,000 nest egg.</h4>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:1%">Investments seem to grow faster in later years because of the effects of compounding. The investment illustrated in Figure 1.2 never actually speeds up its growth on a percentage basis, but as the numbers get larger, the nest egg appears to grow more quickly. For example, suppose you invest $10,000 and earn a 10% return. At the end of the year, you have $11,000. If you duplicate the 10% return in the second year, you’ll gain not only another $1,000, but an extra $100—the 10% return on the $1,000 you gained last year. Over time, the excess return earned on past gains will boost your portfolio’s value exponentially.</h4>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:1%">So don’t panic. People with 40 years to invest enjoy lots of choices. And while investors with shorter time horizons may have fewer choices, this book can help you make the best choices possible.</h4>
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
            <span>Title: 5 Steps to Setting Achievable Financial Goals | Brian Tracy</span>
            </el-row>
            <el-row class="source-text">
            <span>Author: Brian Tracy</span>
            </el-row>
            <el-row class="source-text">
                Source: <a v-bind:href="linkUrl">https://youtu.be/aXDuLxEJqBo</a>
            </el-row>
            <el-row class="source-text">
                <span>Self-made millionaires all started with a dream that lead them to achieve the money goals they had set for themselves. Discover the 5 proven steps used by the most successful people in order to achieve wealth. </span>
            </el-row>
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
        videoEmbedCode: 'https://www.youtube.com/embed/aXDuLxEJqBo',
        tableData: [{
            data1: '4%',
            data2: '18'
        },{
            data1: '6%',
            data2: '12'
        },
        {
            data1: '8%',
            data2: '9'
        },
        {
            data1: '10%',
            data2: '7'
        },
        {
            data1: '12%',
            data2: '6'
        }],
    };
  },
    methods:{
        Gotest(){
            this.$router.push('/knowledgehome')
        },
        Goback(){
            this.$router.push('/chapter1')
        }
    },
    created(){
    
        var userid = this.$store.state.accountid;
        var chapterid = 1;
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
      return 'https://youtu.be/aXDuLxEJqBo';
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

.el-table td {
  text-align: center;
}

.container {
    width: 50%;
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
