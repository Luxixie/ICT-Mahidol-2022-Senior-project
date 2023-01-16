<template>
    <div>
        <el-row>
            <el-col :span="24">
                <img src="./imges/backgroud.png" />
            </el-col>

        </el-row>
        <el-row>
            <el-col :span="8" :offset="10">
                <h1 id="homepageTitle">Home Page</h1>
            </el-col>
        </el-row>
        <el-row id="home-bt-row">
            <el-col class="home-bts" :span="6" :offset="0">
                <el-button class="homebt" type="warning" round>Buy and Sell</el-button>
            </el-col>
            <el-col class="home-bts" :span="6">
                <el-button class="homebt" type="warning" round>Market Information</el-button>
            </el-col>
            <el-col class="home-bts" :span="6">
                <el-button class="homebt" type="warning" round>Portfolio</el-button>
            </el-col>
            <el-col class="home-bts" :span="6">
                <el-button class="homebt" type="warning" round>Stock Knowledge</el-button>
            </el-col>
        </el-row>
    </div>

</template>

<script>
</script>

<style>
#homepageTitle {
    color: #ffffff;
}
#home-bt-row{
   margin-top: 100px;
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

</style>