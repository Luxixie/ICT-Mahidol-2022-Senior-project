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
      <el-col  :span="5"> 
        <div  id="title" >
          <div style=" margin-left: 5%; ">
            <span>Chapter 5:</span>
          </div>
          <div style=" margin-left: 5%;margin-top:50%;font-size:30px">
            <span>Charts and Analysis</span>
          </div>
        </div>
      </el-col>
      <el-col :span="19" > 
        <div style="margin-top: 2%; margin-left: 2%;margin-right:2%; border-radius: 30px;">
          <div style="background:#F5EFE0; border-radius: 30px;">
            <div style="margin-left: 3%;font-size:20px">
              <span>Description:</span>
            </div>
            <div style="margin-left: 3%;margin-right: 3%;font-size:15px">
              <span>This chapter explains in detail how to understand the chart and how to analyze the data.And advanced course is part two of our day trading courses. In our Basic Day Trading Course (Part 1), we teach the most popular indicators, strategies, and how to get started as a day trader. This course goes in-depth on how penny stocks work, scanning for momentum trades, and shows you how to trade the most popular strategies. Our Next Level Training Library takes what you’ll Learn in our penny stocks trade room and courses, and teaches how to Apply day trading in the real world.</span>
            </div>
          </div>
          <div style="background:#F5EFE0; ;border-radius: 30px;" >
            <div style="margin-left: 3%;margin-top: 1%;font-size:20px">
              <span>Objectives of Learning：</span>
            </div>
            <div style="margin-left: 3%;font-size:15px">
                <el-row>
                    <p>· Know what each chart means.</p>
                    <p>· Find out how to read penny stock charts and scan for momentum trades.</p>
                    <p>· Learn about the opening range and how breakouts work.</p>
                    <p>· Understanding the gap and go and why it’s the most popular strategy.</p>
                    <p>· How the float of a stock affects price action.</p>
                    <p>· See how real-world price action comes together when trading.</p>

                </el-row>
                

            </div>
          </div>
        </div>
      </el-col>
    </el-row>


    <el-row style="background: #F5EFE0; margin-left:2%; margin-right:18%;border-radius: 30px; height: 430px; margin-top: 2%;">
      <div style="margin-left:3%;margin-top:2%; font-size:25px ">
        <span>Chapter 5 outline</span>
      </div>
      <el-row>
        <el-col :span="11" offset="1" style="margin-left:2%;">
          <el-row :span="4" v-for="(item, index) in items" :key="o" :offset="1" style="margin-left:1%"  >
              <el-card :body-style="{ padding: '0px' }">
                  <div style="padding: 0px;">
                      <div style="float:left; margin-left: 3%; width: 80%; margin-bottom: 3%;margin-top: 1%">
                          <div>
                              <span>{{item.titleID}}</span>
                          </div>
                          <div>
                              <span>{{item.title}}</span>
                          </div>
                              </div>
                              <div style="float:right; margin-top: 2%;">
                                  <div>
                                      <el-button size="medium" type="primary" @click="GoLearn(item.path)" round
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
                              <span>{{item.titleID}}</span>
                          </div>
                          <div>
                              <span>{{item.title}}</span>
                          </div>
                              </div>
                              <div style="float:right; margin-top: 2%;">
                                  <div>
                                      <el-button size="medium" type="primary" @click="GoLearn(item.path)" round
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
        <h5 style="margin-left: 3%;margin-right: 3%;font-family: 'Inter';font-style: normal;font-weight: 300;font-size: 25px;line-height: 36px;color: #FFFFFF;">Course resource: </h5> 
        <h5 style="margin-left: 3%;margin-right: 3%;font-family: 'Inter';font-style: normal;font-weight: 300;font-size: 25px;line-height: 36px;color: #FFFFFF;">1. Website: Investing for beginners: How to read stock charts<a v-bind:href="linkUrl">https://www.moneyunder30.com/how-to-read-a-stock-chart</a>. Written byChris Muller|Modified date: Dec. 24, 2022</h5>
        <h5 style="margin-left: 3%;margin-right: 3%;font-family: 'Inter';font-style: normal;font-weight: 300;font-size: 25px;line-height: 36px;color: #FFFFFF;">2. How to Read Stock Charts for Beginners <a v-bind:href="linkUrl2">https://www.warriortrading.com/how-to-read-stock-charts-for-beginners/</a>.</h5>
        <h5 style="margin-left: 3%;margin-right: 3%;font-family: 'Inter';font-style: normal;font-weight: 300;font-size: 25px;line-height: 36px;color: #FFFFFF;">3. The Bullish Bears Trading Community, <a v-bind:href="linkUrl3">https://bullishbears.com/</a>. Advanced Day Trading course</h5>
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
          titleID: "01",
          title: "How to Read Stock Charts for Beginners(1)",
          path:'/chapter5.1'
        },
        {
          id: "2",
          titleID: "02",
          title: "How to Read Stock Charts for Beginners(2)",
          path:'/chapter5.2'
        },
        {
          id: "3",
          titleID: "03",
          title:"How To Read Penny Stock Charts",
          path:'/chapter5.3'
        },
        {
          id: "4",
          titleID: "04",
          title:"Scanning For Penny Stocks To Day Trade",
          path:'/chapter5.4'
        },
        {
          id: "5",
          titleID: "05",
          title: "Mapping Out Support And Resistance",
          path:'/chapter5.5'
        },
      ],
      items2:[
        {
          id: "6",
          titleID: "06",
          title: "Low Float Penny Stocks",
          path:'/chapter5.6'
        },
        {
          id: "7",
          titleID: "07",
          title: "Swing Trading Penny Stocks",
          path:'/chapter5.7'
        },
        {
          id: "8",
          titleID: "08",
          title:"Building A Swing Trade Penny Stocks Watch List",
          path:'/chapter5.8'
        },
        {
          id: "9",
          titleID: "09",
          title:"Shorting Penny Stocks",
          path:'/chapter5.9'
        }

      ],
    };
  },
  methods: {
    GoLearn(path){
      this.$router.push(path)
        }
  },
    computed: {
    linkUrl() {
      // return the URL for the link
      return 'https://www.moneyunder30.com/how-to-read-a-stock-chart';
    },
    linkUrl2() {
      // return the URL for the link
      return 'https://www.warriortrading.com/how-to-read-stock-charts-for-beginners/';
    },
    linkUrl3() {
      // return the URL for the link
      return 'https://bullishbears.com/';
    },

    }
};
</script>

<style>
#title {
  background: #fbf9f6;
  font-size:20px;
  height: 380px; 
  margin-top: 8%; 
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
.container {
    width: 50%;
    height: 400px;
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
