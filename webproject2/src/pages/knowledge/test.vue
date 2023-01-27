<template>
    <div id="test-div">
        <el-row>
            <el-col id="test-title-col" :span = "10"  offset="8">
                <h1 id="test-title">Opening test 1 of 6</h1>
            </el-col>
        </el-row>

        <el-row id="test-box">
            <el-col :span="8" offset="8" >
                <el-card :body-style="{ padding: '0px' }" id="card-color">
                <div style="padding: 50px;" class="size">
                    <span>Which one of the following is computed by divided by the current stock price?</span>
                </div>
                </el-card>
            </el-col>
        </el-row>
    
        <el-row id ="test-bt" >
            <el-col :span="6" offset="7" >
            <el-radio-group v-model="radio1">
            <el-radio-button label="A. Yield to maturity"></el-radio-button>
            </el-radio-group>
            </el-col>
            <el-col :span="6">
            <el-radio-group v-model="radio1" >
            <el-radio-button label="B. Capital gains yiel"></el-radio-button>
            </el-radio-group>
            </el-col>
        </el-row>
        <el-row>
            <el-col :span="6"  offset="7">
            <el-radio-group v-model="radio1">
            <el-radio-button label="C. Dividend yield"></el-radio-button>
            </el-radio-group>
            </el-col>
            <el-col :span="6">
            <el-radio-group v-model="radio1">
            <el-radio-button label="D. I don’t know"></el-radio-button>
            </el-radio-group>           
            </el-col> 
        </el-row>
    </div>
</template>

<script>
export default {
    data(){
        return {
            radio1:'',
            currentDate: new Date()
        }
    }
}
</script>

<style>
#test-div {
    margin-top: 2%;
}

#test-title {
    color: white;
    font-size: 40px;
}

#test-title-col {
    margin-bottom: 30px;
}
#test-box {
    margin-bottom: 30px;
}
#test-bt {
    margin-bottom: 30px;
}

#card-color {
    background: #A68FD7;
    border-radius: 30px;
}
.size{
    font-weight: bold;
    font-size: 20px;
}

.clearfix:before,
.clearfix:after {
      display: table;
      content: "";
  }
  
.clearfix:after {
      clear: both
  }
</style>



  
