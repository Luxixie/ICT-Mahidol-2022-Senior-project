<template>
    <div>
        <el-row class="chapterbox" >
            <h2 style="margin-left: 3%;  margin-top:4%"> 02 How much money do I need to start investing in stocks?</h2>
        </el-row>
        <el-row style="background: #F5EFE0;border-radius: 30px; margin-top:1%; margin-left: 3%; margin-right: 3%;" >
            <h2 style="margin-left: 3%;  margin-top:2%">Answer</h2>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:1%">Not as much as many investors think. In a perfect world, you would enter the market with $100,000 - enough to buy a diversified stock portfolio all at once. But if you don't live in that perfect world, you have to set your sights a little lower. Even if you can only save $5,000 or $1,000, you can still invest in stocks. Just don't buy so many.</h4>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:1%">Of course, investing in just one company's stock or a handful of stocks carries risks. But while you take on some risk when you buy only one or two stocks, choosing not to invest exposes you to another type of risk - poverty. Chapter 10 explains in more detail the risks associated with choosing an investment.</h4>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:1%">If you open an account with a discount brokerage that charges $10 per trade, buying $1,000 of stock will cost you 1% of your investment commission. That means your stock has to return about 1% before it recoups its investment costs. In general, investors should try to limit their commission costs, preferably to less than 0.5% of the portfolio's value that year. As your portfolio grows, your trading commissions as a percentage of assets should </h4>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:1%">If you’ve set up an account at a discount broker charging $10 per trade, purchasing $1,000 in stock will cost you 1% of your investment in commissions. That means your stock must return about 1% before you recoup the cost of the investment. As a rule, investors should try to limit their commission costs, preferably keeping them below 0.5% of the portfolio value for the year. As the portfolio grows, your trading commissions should decline as a percentage of the assets (See Table 2.1).</h4>
            <el-row :span="2" class="container" style="margin-top:3%;margin-left:10%">
                    <img src="./images/1.jpg" class="image" />
            </el-row>
            <p  style="text-align: center;">Table 2.1 – Errors of Commission</p>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:1%">But if you have only $1,000 to invest, take the leap and pay the commission. After all, you’ve got to start somewhere. If you commit to investing, you’ll be adding new money to the account over time. Spend a few years watching your stocks increase in value, and after a while the commissions won’t take such a big bite out of the whole.</h4>

        </el-row>
        <el-row style="background: #F5EFE0;border-radius: 30px; height: 600px; margin-top:1%; margin-left: 3%; margin-right: 3%;"> 
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
        videoEmbedCode: 'https://www.youtube.com/embed/yMq8yVqs4Zg'
        };
    },
    methods:{
        GoNext(){
            this.$router.push('/chapter2.3')
        },
        Goback(){
            this.$router.push('/chapter2')
        }
    },
    created(){
        
            var userid = this.$store.state.accountid;
            var chapterid = 2;
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
