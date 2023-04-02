<template>
  <div>
    <el-row>
      <el-col :span="24" class="container">
                <img src="./imges/backgroud.png" class="image" />
           
        </el-col>
    </el-row>
    <el-row>
      <el-col :span="8" :offset="10">
        <h1 id="homepageTitle">Home Page</h1>
      </el-col>
    </el-row>
    <el-row id="home-bt-row">
      <el-col class="home-bts" :span="6" :offset="1">
        <el-button class="homebt" type="warning" @click="GoMarket" round >Market Infomation</el-button>
      </el-col>
      <el-col class="home-bts" :span="6">
        <el-button class="homebt" type="warning" @click="Goknowledgehome" round>Stock knowledge</el-button>
      </el-col>
      <el-col class="home-bts"  :span="5" v-if="username">
        <el-button class="homebt" type="warning" @click="Gobuyandsell" round>Buy and Sell</el-button>
      </el-col>
      <el-col class="home-bts"  :span="5" v-if="username">
        <el-button class="homebt" type="warning" @click="GoPortfolio" round>Portfolio</el-button>
      </el-col>
    </el-row>
  </div>
</template>

<script>
export default {
  name: "Home",
  methods: {
    GoMarket(){
            this.$router.push('/markethome')
    },
    Goknowledgehome(){
        this.$router.push('/knowledgeHome')
        },
        Gobuyandsell(){
          this.$router.push('/buyandsell')
        },
        GoPortfolio(){
          this.$router.push('/portfolio')
        }

        
  },
  computed: {
    username() {
      return this.$store.state.username;
    },

  },
};
</script>

<style>
#homepageTitle {
  color: #ffffff;
}



.homebt {
  color: black;
  font-size: 30px;
  width: 80%;
  height: 60%;
}

.home-bts {
  height: 150px;
  border-radius: 100px;
}
.container {
    width: 100%;
    height: 350px;
}
.image {
    max-width: 100%;
    max-height: 100%;
}
</style>