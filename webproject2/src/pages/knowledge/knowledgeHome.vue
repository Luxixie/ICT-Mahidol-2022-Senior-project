<template>
  <div>
    <el-row id="knowledgehome-title">
      <el-col :span="10" :offset="7" class="text">
        <span>Stock knowledge</span>
      </el-col>
      <el-col :span="18" :offset="7">
        <h3>The hard part isn’t making the decision. It’s living with it.</h3>
      </el-col>
    </el-row>

    <el-row style="background: #f6f7e4; height: 50px; ">
      <el-tabs v-model="activeName" @tab-click="handleClick" style="margin-left:3%;font-size:32px">
        <el-tab-pane label="Basic Knowledge" name="first" ></el-tab-pane>
        <el-tab-pane label="Starter Guide" name="second" ></el-tab-pane>

      </el-tabs>
    </el-row>
    <el-row style="padding-right: 3%">
      <el-col
        :span="7"
        v-for="item in items"
        :key="item.id"
        :offset="1"
        style="margin-top: 1%"
      >
        <el-card
          :body-style="{ padding: '0px' }"
          style="margin-top: 3%; background: #f5efe0"
        >
          <div style="padding: 14px">
            <img
              width="60px"
              height="60px"
              :src="item.image"
              style="float: ; margin-top: 5%"
            />
            <div style="float: left; margin-left: 5%; width: 78%">
              <el-link :class="topFont" @click="GoLearn(item.path, item.id)">{{
                item.ChapterName
              }}</el-link>
            </div>
            <div>
              <el-progress :text-inside="true" :stroke-width="18" :percentage="item.learningProcess"></el-progress>
            </div>
          </div>
        </el-card>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import axios from "axios";
// import e from 'express';


export default {
  data() {
    return {
      items: [
        {
          id: "1",
          image: require("../knowledge/images/2.png"),
          ChapterName: "Chapter 1 Reasons to Invest",
          path: "/chapter1",
          learningProcess:30
        },
        {
          id: "2",
          image: require("../knowledge/images/3.png"),
          ChapterName: "Chapter 2 Fundamentals of the Stock Market",
          path: "/chapter2",
          learningProcess:20
        },
        {
          id: "3",
          image: require("../knowledge/images/4.png"),
          ChapterName: "Chapter 3 Types of Investments",
          path: "/chapter3",
          learningProcess:10
        },
        {
          id: "4",
          image: require("../knowledge/images/5.png"),
          ChapterName: "Chapter 4 Building Perfect Portfolio",
          path: "/chapter4",
          learningProcess:50
        },
        {
          id: "5",
          image: require("../knowledge/images/6.jpeg"),
          ChapterName: "Chapter 5 Charts and Analysis",
          path: "/chapter5",
          learningProcess:40
        },
        {
          id: "6",
          image: require("../knowledge/images/7.png"),
          ChapterName: "Chapter 6 Stock term",
          path: "/chapter6",
          learningProcess:20
        },
      ],
    };
  },
  created(){
    var userid = this.$store.state.accountid
    var items = [
        {
          id: "1",
          image: require("../knowledge/images/2.png"),
          ChapterName: "Chapter 1 Reasons to Invest",
          path: "/chapter1",
          learningProcess:0
        },
        {
          id: "2",
          image: require("../knowledge/images/3.png"),
          ChapterName: "Chapter 2 Fundamentals of the Stock Market",
          path: "/chapter2",
          learningProcess:0
        },
        {
          id: "3",
          image: require("../knowledge/images/4.png"),
          ChapterName: "Chapter 3 Types of Investments",
          path: "/chapter3",
          learningProcess:0
        },
        {
          id: "4",
          image: require("../knowledge/images/5.png"),
          ChapterName: "Chapter 4 Building Perfect Portfolio",
          path: "/chapter4",
          learningProcess:0
        },
        {
          id: "5",
          image: require("../knowledge/images/6.jpeg"),
          ChapterName: "Chapter 5 Charts and Analysis",
          path: "/chapter5",
          learningProcess:0
        },
        {
          id: "6",
          image: require("../knowledge/images/7.png"),
          ChapterName: "Chapter 6 Stock term",
          path: "/chapter6",
          learningProcess:0
        },
      ]
    console.log(items)
    if(typeof(userid) != "undefined"){
      //axios
      console.log(userid)
      var url = "http://127.0.0.1:8088/knowledge/getlearningprocess/"+userid
      axios.post(url)
      .then(res => {
             
              res.data.forEach(cheapter => {
                    var id = cheapter["chapterid"]
                     console.log(id)
                     var learningprocess = cheapter["learningprocess"]
                     console.log(learningprocess)
                 
                     items.forEach(item => {
                        if(item.id == id){
                          item.learningProcess = learningprocess
                        }
                     });
              }); 
             
    })}
    console.log(items)
    this.items = items
  
  },
  methods: {
    GoLearn(path, id) {
      this.$router.push(path)
    },
    handleClick() {
      this.$router.push('/starterguide')
    },
  }
};
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

.text {
  font-size: 60px;
}
</style>