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
    <el-row>
      <el-col  :span=8> 
        <div  id="title" >
          <div style=" margin-left: 5%; ">
            <span>Chapter 2:</span>
          </div>
          <div style=" margin-left: 5%;margin-top:10%;font-size:30px">
            <span>Fundamentals of the Stock Market</span>
          </div>
        </div>
      </el-col>
      <el-col :span=15 > 
        <div style="height: 200px; margin-top: 2%; margin-left: 4%;margin-right:3% border-radius: 30px;">
          <div style="background:#F5EFE0;height: 50%; border-radius: 30px;">
            <div style="margin-left: 3%;font-size:20px">
              <span>Description:</span>
            </div>
            <div style="margin-left: 3%;font-size:20px">
              <span >In this chapter we'll cover 10 basics of stocks that will help you get started on your stock investing journey.</span>
            </div>
          </div>
          <div style="background:#F5EFE0; height: 50% ;border-radius: 30px;" >
            <div style="margin-left: 3%;margin-top: 1%;font-size:20px">
              <span>Objectives of Learning：</span>
            </div>
            <div style="margin-left: 3%;font-size:20px">
              <span>Learn simple things about the stock market</span>
            </div>
          </div>
        </div>
      </el-col>
    </el-row>

    <el-row style="background: #F5EFE0; margin-left:2%; margin-right:18%;border-radius: 30px; height: 570px; margin-top: 2%;">
      <div style="margin-left:3%;margin-top:2%; font-size:25px ">
        <span>Chapter 2 outline</span>
      </div>
      <el-row>
        <el-col :span="11" offset="1" style="margin-left:2%;">
          <el-row :span="4" v-for="(item, index) in items" :key="o" :offset="1" style="margin-left:1%"  >
              <el-card :body-style="{ padding: '0px' }">
                  <div style="padding: 0px;">
                      <div style="float:left; margin-left: 3%; width: 80%; margin-bottom: 3%;margin-top: 1%">
                          <div>
                              <span>{{item.QuestionID}}</span>
                          </div>
                          <div>
                              <span>{{item.QuestionrName}}</span>
                          </div>
                              </div>
                              <div style="float:right; margin-top: 2%;">
                                  <div>
                                      <el-button size="medium" type="primary" @click="GoLearn" round
                                          style="width: 90%;">LEARN</el-button>
                                  </div>
                              </div>
                          </div>
              </el-card>
          </el-row>
        </el-col>
        <el-col :span="12" style="margin-left:1%;margin-right:1%;">
          <el-row :span="4" v-for="(item, index) in items2" :key="o" :offset="1" style="margin-left:1%"  >
              <el-card :body-style="{ padding: '0px' }">
                  <div style="padding: 0px;">
                      <div style="float:left; margin-left: 3%; width: 80%; margin-bottom: 3%; margin-top: 1%">
                          <div>
                              <span>{{item.QuestionID}}</span>
                          </div>
                          <div>
                              <span>{{item.QuestionrName}}</span>
                          </div>
                              </div>
                              <div style="float:right; margin-top: 2%;">
                                  <div>
                                      <el-button size="medium" type="primary" @click="GoLearn" round
                                          style="width: 90%;">LEARN</el-button>
                                  </div>
                              </div>
                          </div>
              </el-card>
          </el-row>
        </el-col>

      </el-row>
      
    </el-row>
    <el-row>
      <h5 style="margin-left: 3%;margin-right: 3%;font-family: 'Inter';font-style: normal;font-weight: 300;font-size: 25px;line-height: 36px;color: #FFFFFF;">From book: Stock Market Investing for Beginners: Essentials to Start Investing Successfully, Tycho Tycho Press, Callisto Media Incorporated, 2013</h5>
    </el-row>

   
    
  </div>
</template>

<script>
export default {
  data() {
    return {
      items: [
        {
          id: "1",
          QuestionID: "Question #1:",
          QuestionrName: "How do I start investing in stocks?",
        },
        {
          id: "2",
          QuestionID: "Question #2:",
          QuestionrName:
            "How much money do I need to start investing in stocks?",
        },
        {
          id: "3",
          QuestionID: "Question #3:",
          QuestionrName:
            "I want to buy Apple, but the stock costs several hundred dollars per share, and I don’t have enough money to buy 100 shares. Should I stick to cheaper stocks?",
        },
        {
          id: "4",
          QuestionID: "Question #4:",
          QuestionrName: "Which should I buy, stocks or bonds?",
        },
        {
          id: "5",
          QuestionID: "Question #5:",
          QuestionrName: "How do I know which stocks to buy?",
        },
      ],
      items2: [
        {
          id: "6",
          QuestionID: "Question #6:",
          QuestionrName: "How do I know when to sell a stock?",
        },
        {
          id: "7",
          QuestionID: "Question #7:",
          QuestionrName:
            "My stock has declined, but I can’t find any news on it. What caused the dip?",
        },
        {
          id: "8",
          QuestionID: "Question #8:",
          QuestionrName: "How do I track my portfolio?",
        },
        {
          id: "9",
          QuestionID: "Question #9:",
          QuestionrName:
            "Should I subscribe to a newsletter or go to a broker for help picking stocks? Or am I better of making my own investment decisions and not paying for advice?",
        },
        {
          id: "10",
          QuestionID: "Question #10:",
          QuestionrName:
            "The stock market is falling, but I like the looks of Acme Widget. Should I buy the shares now or wait until the price dips further?",
        },

      ],
    };
  },
  methods: {
    GoLearn() {
      this.$router.push("/chapter2.1");
    },
  },
};
</script>

<style>
#title {
  background: #fbf9f6;
  font-size:20px;
  height: 200px; 
  margin-top: 4%; 
  margin-left: 5%;
  border-radius: 30px;
}

#knowledgehome-title {
  background: #fbf9f6;
}

#knowledgehome-tabs {
  background: #f6f7e4;
}

.text {
  font-size: 40px;
}

</style>