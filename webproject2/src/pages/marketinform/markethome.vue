<template>
    <div>
        <el-row id = "martkethome-header" >
            <el-col :span="6" offset="5" >
                <el-row>
                    <h1> SET </h1>
                </el-row>
                <el-row>
                    <span>Hight xxx</span>
                </el-row>
                <el-row>
                    <span>Low xxx</span>
                </el-row>
            </el-col>
            <el-col :span="6">
                <el-row>
                    <h1>Market Status: close </h1>
                </el-row>
                <el-row>
                    <span>1629.38</span>
                </el-row>
                <el-row>
                    <span>+6.00 (+0.37%)</span>
                </el-row>
            </el-col>
            <el-col :span="6">
                <el-row>
                    <div style="text-align: center;padding-top: 100px">
                        Time:{{ nowTime }}
                    </div>
                </el-row>
                
            </el-col>
        </el-row>
        <el-row :gutter="18">
        <el-col :span="6"><div class="grid-content bg-purple">Communication services</div></el-col>
        <el-col :span="6"><div class="grid-content bg-purple">Consumer discretionary</div></el-col>
        <el-col :span="6"><div class="grid-content bg-purple"> Consumer staples</div></el-col>
        <el-col :span="6"><div class="grid-content bg-purple">Energy</div></el-col>
        </el-row>
        <el-row :gutter="18">
        <el-col :span="6"><div class="grid-content bg-purple">Financial</div></el-col>
        <el-col :span="6"><div class="grid-content bg-purple"></div></el-col>
        <el-col :span="6"><div class="grid-content bg-purple"></div></el-col>
        <el-col :span="6"><div class="grid-content bg-purple"></div></el-col>
        </el-row>
    </div>
</template>

<script>
export default {
  data() {
    return {
      nowTime: ''
    };
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


<style>
#martkethome-header{
    background:#d9d9d9;
    height: 180px;
}
.el-row {
    margin-bottom: 20px;
    &:last-child {
      margin-bottom: 0;
    }
  }
  .el-col {
    border-radius: 4px;
  }
  .bg-purple-dark {
    background: #99a9bf;
  }
  .bg-purple {
    background: #d3dce6;
  }
  .bg-purple-light {
    background: #e5e9f2;
  }
  .grid-content {
    border-radius: 4px;
    min-height: 80px;
  }
  .row-bg {
    padding: 10px 0;
    background-color: #f9fafc;
  }
</style>
