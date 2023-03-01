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
            <span>Chapter 1:</span>
          </div>
          <div style=" margin-left: 5%;margin-top:10%;font-size:30px">
            <span>Reasons to Invest</span>
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
              <span >In this section you will learn why you should choose to invest in stocks and how to set investment goals.</span>
            </div>
          </div>
          <div style="background:#F5EFE0; height: 50% ;border-radius: 30px;" >
            <div style="margin-left: 3%;margin-top: 1%;font-size:20px">
              <span>Objectives of Learning：</span>
            </div>
            <div style="margin-left: 3%;font-size:20px">
              <span>Understand the value of investing in stocks and set investment goals.</span>
            </div>
          </div>
        </div>
      </el-col>
    </el-row>

    <el-row>
        <el-col :span="10" :offset="1" style="background: #F5EFE0; margin-left:2%;border-radius: 30px;width:600px; height: 330px; margin-top: 2%;">
        <div style="margin-left:3%;margin-top:2%; font-size:25px ">
            <span>Chapter 1 outline</span>
        </div>
        <el-col :span="18" offset="1" style="margin-left:10%">
          <el-row :span="4" v-for="(item, index) in items" :key="o" :offset="1" style="margin-left:4%;"  >
              <el-card :body-style="{ padding: '0px' }">
                  <div style="padding: 0px;">
                      <div style="float:left; margin-left: 3%; margin-bottom: 3%;margin-top: 1%">
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
        </el-col>
        <el-col :span="2" class="container" style="margin-top:3%;margin-left:5%">
        
                <img src="./images/1.jpg" class="image" />
           
        </el-col>

      
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
          id: "1",titleID: "01",title: "Opening",path:'/chapter1.1'
        },
        {
          id: "2", titleID: "02",title: "Common Motivations",path:'/chapter1.2'
        },
        {
          id: "3",titleID: "03",title: "Attach importance to investment",path:'/chapter1.3'
        },
        {
          id: "4",titleID: "04:",title: "Set Attainable Goals",path:'/chapter1.4'
        },

      ],
    };
  },
  methods: {
    GoLearn(path){
      this.$router.push(path)
    }

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
