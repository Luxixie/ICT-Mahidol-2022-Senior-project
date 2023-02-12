<template>
    <div>
        <el-row id="knowledgehome-title">
            <el-col :span="8" :offset="9" class="text">
                <span>Stock knowledge</span>
            </el-col>
            <el-col :span="18" :offset="7">
                <h3>The hard part isn’t making the decision. It’s living with it.</h3>
            </el-col>
        </el-row>

        <el-row style="background:#F6F7E4; height: 50px;">
            <div  :span = "8" :offset="5" style="margin-left: 2%; margin-top:1%">
                <el-link style="font-size:20px">Basic Knowledge</el-link>
            </div>
        </el-row>
        <el-row style="padding-right: 3%;">
        <el-col :span="7" v-for="item in items" :key="item.id" :offset="1" style="margin-top: 1%;">
            <el-card :body-style="{ padding: '0px' }" style="margin-top: 3%; background: #F5EFE0;">
                <div style="padding: 14px;">
                    <img width="60px" height="60px" style="float: ; margin-top: 5%; " src="./images/2.png"/>
                    <div style="float:left; margin-left: 5%; width: 78%">
                            <el-link :class="topFont" @click="GoLearn">{{item.ChapterName}}</el-link>
                    </div>
                </div>
            </el-card>
        </el-col>


    </el-row>
        
    </div>
</template>

<script>
export default {
    data() {
        return {
            items: [
                { id: '1', image:"./images/1.jpeg" ,ChapterName: 'Chapter 1 Reasons to Invest',path: '/chapter1' },
                { id: '2', image:"./images/2.png",ChapterName: 'Chapter 2 Fundamentals of the Stock Market',path: '/chapter2'},
                { id: '3', image:"./images/3.png" ,ChapterName: 'Chapter 3 Types of Investments', path: '/chapter3'},
                { id: '4', image:"./images/4.png" ,ChapterName: 'Chapter 4 How to Pick Winners, Step 1: Valuation', path: '/chapter4'},
                { id: '5',  image:"./images/4.png" ,ChapterName: 'Chapter 5 How to Pick Winners, Step 2: Growth',path: '/chapter5'},
                { id: '6',  image:"./images/4.png" ,ChapterName: 'Chapter 6 How to Pick Winners, Step 3: Profitability',path: '/chapter6'},
                { id: '7',  image:"./images/4.png" ,ChapterName: 'Chapter 7 How to Pick Winners, Step 4: Putting It All Together',},
                { id: '8',  image:"./images/4.png" ,ChapterName: 'Chapter 8 How to Pick Winners, Step 5: Getting the News',},
                { id: '9',  image:"./images/4.png" ,ChapterName: 'Chapter 9 The Mechanics of Buying, Selling, and Owning Stocks',},
                { id: '10',  image:"./images/4.png" ,ChapterName: 'Chapter 10 The Power of Diversification',},
                { id: '11',  image:"./images/4.png" ,ChapterName: 'Chapter 11 Building Your Perfect Portfolio',},
            ],
                    
        };
    },
    methods:{
        Gotest(){
            this.$router.push('/chapter2')
        },
        GoLearn(){
            this.$router.push('/chapter2')
        }
    }
}
</script>

<style>
#title {
  background: #fbf9f6;
}

#knowledgehome-title {
  background: #fbf9f6;
}

#knowledgehome-tabs {
  background: #f6f7e4;
}

.text{
    font-size: 60px;
}




</style>