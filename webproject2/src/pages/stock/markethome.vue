<template>
  <div>
    <el-row style="background: #F5F5F5;; margin-top:2%;  margin-left:2%; margin-right:2%; height:250px">
      <el-col :span="17" :offset="1" style="background: #1F3D70;border-radius: 25px;margin-top:2%;">
        <el-row>
          <el-col :span="10" style="margin-left:8%">
            <h3 style="float: left; margin-left:5%;color: #F5EFE0;">SET</h3>
          </el-col>
          <el-col :span="10" >
            <h3 style="float: right;margin-right:6%;color: #F5EFE0;">SET:xxxx{{state}}</h3>
          </el-col>
        </el-row>
          <el-row>
          <el-col :span="10" style="margin-left:8%">
            <h4 style="float: left; margin-left:5%;color: #F5EFE0;">high xxx{{high}}</h4>
          </el-col>
          <el-col :span="10" >
            <h4 style="float: right; margin-right:6%;color: #F5EFE0;">1629.38{{data1}}</h4>
          </el-col>
        </el-row>
        <el-row>
          <el-col :span="10" style="margin-left:8%">
            <h4 style="float: left; margin-left:5%; color: #F5EFE0;">low xxx{{low}}</h4>
          </el-col>
          <el-col :span="10" >
            <h4 style="float: right; margin-right:6%; color: #F5EFE0;">+6.00  (+0.37%){{data2}}</h4>
          </el-col>
        </el-row>

      </el-col>
      <el-col :span="5" >
        <el-row style="margin-top:30%;margin-left:20%;">
            <div style="text-align: center;padding-top: 100px">
                Time: {{ nowTime }}
            </div>
        </el-row>
      </el-col>
    </el-row>
    <el-row style="margin-top:1%;margin-left:2%; margin-right:2%">
        <el-row :gutter="20">
          <el-col :span="4"
          ><el-button class="box">Communication services</el-button>
          </el-col>
          <el-col :span="4" :offset="1" >
            <el-button class="box">Consumer discretionary</el-button> 
            </el-col>
          <el-col :span="4" :offset="1" >
            <el-button class="box">Consumer staples</el-button>
            </el-col>
          <el-col :span="4" :offset="1" >
            <el-button class="box">Energy</el-button>
            </el-col>
                    <el-col :span="4" :offset="1" >
            <el-button class="box">Financial</el-button>
            </el-col>

        </el-row>
        <el-row :gutter="20" style="margin-top:1%;">
          <el-col :span="4" 
          ><el-button class="box">Healthcare</el-button>
          </el-col>
          <el-col :span="4" :offset="1">
            <el-button class="box">Industrials</el-button> 
            </el-col>
          <el-col :span="4" :offset="1" >
            <el-button class="box">Information technology</el-button>
            </el-col>
          <el-col :span="4" :offset="1" >
            <el-button class="box">Materials</el-button>
            </el-col>
          <el-col :span="4" :offset="1" >
            <el-button class="box">Real estate</el-button>
            </el-col>

        </el-row>

         <el-row :gutter="20" style="margin-top:1%;">
          <el-col :span="4"
          ><el-button class="box">Utilities</el-button>
          </el-col>
         </el-row>
    </el-row>
  </div>
  
</template>

<script>
export default {
    data() {
        return {
          state:'',
          high:'',
          low:'',
          data1:'',
          data2:'',
          nowTime: ''
        }
    },
    mounted() {
    this.getNowTime();
    },
    methods: {
    getNowTime () {
      let speed = 1000
      let that = this
      let theNowTime = function () {
        that.nowTime = that.timeNumber()
      }
      setInterval(theNowTime, speed)
    },
    timeNumber () {
      let today = new Date()
      let date = today.getFullYear() + '-' + this.twoDigits(today.getMonth() + 1) + '-' + this.twoDigits(today.getDate())
      let time = this.twoDigits(today.getHours()) + ':' + this.twoDigits(today.getMinutes()) + ':' + this.twoDigits(today.getSeconds())
      return date + '  ' + time
    },
    twoDigits (val) {
      if (val < 10) return '0' + val
      return val
    },
  },
}

</script>


<style >
.box{
    background: #F5EFE0;
    border-radius: 30px;
    width: 220px;
    height: 100px;
    margin-top:15%;
    font-weight: 800;
    font-size: 15px;
    line-height: 30px;

    color: #000000;
}


</style>