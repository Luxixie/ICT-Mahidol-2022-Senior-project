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

    <el-row style="background: #f6f7e4; height: 50px">
      <div :span="8" :offset="5" style="margin-left: 2%; margin-top: 1%">
        <el-link style="font-size: 20px">Basic Knowledge</el-link>
      </div>
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
// import axios from "axios";
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
  methods: {
    GoLearn(path, id) {
      this.$router.push(path)
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