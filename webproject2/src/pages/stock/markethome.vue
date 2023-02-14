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
        <el-row :gutter="20" >
          <el-col :span="4" :offset="1" class="box">
          <el-dropdown>
          <span class="el-dropdown-link">Communication services<i class="el-icon-arrow-down el-icon--right"></i></span>
          <el-dropdown-menu slot="dropdown">
            <el-dropdown-item>Diversified Telecommunication Service</el-dropdown-item>
            <el-dropdown-item>Entertainment</el-dropdown-item>
            <el-dropdown-item>Interactive Media & Service</el-dropdown-item>
            <el-dropdown-item>Media</el-dropdown-item>           
            <el-dropdown-item>Wireless Telecommunication Service</el-dropdown-item>
            </el-dropdown-menu>
          </el-dropdown>
          </el-col>
          <el-col :span="4" :offset="1" class="box">
            <el-dropdown>
            <span class="el-dropdown-link">Consumer discretionary<i class="el-icon-arrow-down el-icon--right"></i></span>
            <el-dropdown-menu slot="dropdown">
              <el-dropdown-item>Auto Components</el-dropdown-item>
              <el-dropdown-item>Automobiles</el-dropdown-item>
              <el-dropdown-item>Distributors</el-dropdown-item>
              <el-dropdown-item>Diversified Consumer Service</el-dropdown-item>           
              <el-dropdown-item>Hotels, Restaurants & Leisure</el-dropdown-item>
              <el-dropdown-item>Internet & Direct Marketing Retail</el-dropdown-item>
              <el-dropdown-item>Leisure Products</el-dropdown-item>
              <el-dropdown-item>Multiline Retail</el-dropdown-item>
              <el-dropdown-item>Specialty Retail</el-dropdown-item>
              <el-dropdown-item>Textiles, Apparel & Luxury Goods</el-dropdown-item>
              </el-dropdown-menu>
            </el-dropdown>
          </el-col>

          <el-col :span="4" :offset="1" class="box">
          <el-dropdown>
            <span class="el-dropdown-link">Consumer staples<i class="el-icon-arrow-down el-icon--right"></i></span>
            <el-dropdown-menu slot="dropdown">
              <el-dropdown-item>Beverages</el-dropdown-item>
              <el-dropdown-item>Food & Staples Retailing</el-dropdown-item>
              <el-dropdown-item>Food Products</el-dropdown-item>
              <el-dropdown-item>Household Products</el-dropdown-item>           
              <el-dropdown-item>Personal Products</el-dropdown-item>
              <el-dropdown-item>Tobacco</el-dropdown-item>
              </el-dropdown-menu>
            </el-dropdown>
          </el-col>

          <el-col :span="4" :offset="1" class="box">
          <el-dropdown>
            <span class="el-dropdown-link">Energy<i class="el-icon-arrow-down el-icon--right"></i></span>
            <el-dropdown-menu slot="dropdown">
              <el-dropdown-item>Energy Equipment & Service</el-dropdown-item>
              <el-dropdown-item>Oil, Gas & Consumer Fules</el-dropdown-item>
              </el-dropdown-menu>
            </el-dropdown>
          </el-col>

          <el-col :span="4" :offset="1" class="box">
          <el-dropdown>
            <span class="el-dropdown-link">Financial<i class="el-icon-arrow-down el-icon--right"></i></span>
            <el-dropdown-menu slot="dropdown">
              <el-dropdown-item>Banks</el-dropdown-item>
              <el-dropdown-item>Consumer Finance</el-dropdown-item>
              <el-dropdown-item>Diversified Financial Service</el-dropdown-item>
              <el-dropdown-item>Insurance</el-dropdown-item>           
              <el-dropdown-item>Mortgage REITs</el-dropdown-item>
              <el-dropdown-item>Thrifts & Mortgage Finance</el-dropdown-item>
              </el-dropdown-menu>
            </el-dropdown>
          </el-col>
        </el-row>

        <el-row :gutter="20" style="margin-top:1%">
          <el-col :span="4" :offset="1" class="box">
          <el-dropdown>
          <span class="el-dropdown-link">Healthcare<i class="el-icon-arrow-down el-icon--right"></i></span>
          <el-dropdown-menu slot="dropdown">
            <el-dropdown-item>Biotechnology</el-dropdown-item>
            <el-dropdown-item>Health Care Eequipment & Supplies</el-dropdown-item>
            <el-dropdown-item>Health Care Prividers & Services</el-dropdown-item>
            <el-dropdown-item>Health Care technology</el-dropdown-item>           
            <el-dropdown-item>Life Sciences Tools & Services</el-dropdown-item>
            <el-dropdown-item>Pharmaceuticals</el-dropdown-item>
            </el-dropdown-menu>
          </el-dropdown>
          </el-col>
          <el-col :span="4" :offset="1" class="box">
          <el-dropdown  @command="handleCommand">
          <span class="el-dropdown-link">Industrials<i class="el-icon-arrow-down el-icon--right"></i></span>
          <el-dropdown-menu slot="dropdown">
            <el-dropdown-item command="case1">Aerospace & Defense</el-dropdown-item>
            <el-dropdown-item command="case2">Freight & Logistics</el-dropdown-item>
            <el-dropdown-item command="case3">Airlines</el-dropdown-item>
            <el-dropdown-item command="case4">Building Products</el-dropdown-item>           
            <el-dropdown-item command="case5">Commercial Services & Supplies</el-dropdown-item>
            <el-dropdown-item command="case6">Construction & Engineering</el-dropdown-item>
            <el-dropdown-item>Electrical Equipment</el-dropdown-item>
            <el-dropdown-item>Industrial Conglomerates</el-dropdown-item>
            <el-dropdown-item>Machinery</el-dropdown-item>
            <el-dropdown-item>Marine</el-dropdown-item>
            <el-dropdown-item>Professional Services</el-dropdown-item>
            <el-dropdown-item>Road & Rail</el-dropdown-item>
            <el-dropdown-item>Trading Companies & Distributors</el-dropdown-item>
            <el-dropdown-item>Transportation Infrastructure</el-dropdown-item>
            <el-dropdown-item>All</el-dropdown-item>
            
            </el-dropdown-menu>
          </el-dropdown>
          </el-col>
          <el-col :span="4" :offset="1" class="box">
          <el-dropdown>
          <span class="el-dropdown-link">Information technology<i class="el-icon-arrow-down el-icon--right"></i></span>
          <el-dropdown-menu slot="dropdown">
            <el-dropdown-item>Communications Equipment</el-dropdown-item>
            <el-dropdown-item>Electronic Equipment, Instruments & Components</el-dropdown-item>
            <el-dropdown-item>IT Services</el-dropdown-item>
            <el-dropdown-item>Semiconductors & Semiconductors Equipment</el-dropdown-item>           
            <el-dropdown-item>Software</el-dropdown-item>
            <el-dropdown-item>technology Hardware, storage & Peripherals</el-dropdown-item>
            </el-dropdown-menu>
          </el-dropdown>
          </el-col>
          <el-col :span="4" :offset="1" class="box">
          <el-dropdown>
          <span class="el-dropdown-link">Materials<i class="el-icon-arrow-down el-icon--right"></i></span>
          <el-dropdown-menu slot="dropdown">
            <el-dropdown-item>Chemicals</el-dropdown-item>
            <el-dropdown-item>Construction Materials</el-dropdown-item>
            <el-dropdown-item>Containers & Packgaging</el-dropdown-item>
            <el-dropdown-item>Metals & Mining</el-dropdown-item>           
            <el-dropdown-item>Paper & Forest Products</el-dropdown-item>
            </el-dropdown-menu>
          </el-dropdown>
          </el-col>
          <el-col :span="4" :offset="1" class="box">
          <el-dropdown>
          <span class="el-dropdown-link">Real estate<i class="el-icon-arrow-down el-icon--right"></i></span>
          <el-dropdown-menu slot="dropdown">
            <el-dropdown-item>Equity Real Estate Investment Trusts</el-dropdown-item>
            <el-dropdown-item>Real Estate Management & Development</el-dropdown-item>
            <el-dropdown-item></el-dropdown-item>
            <el-dropdown-item></el-dropdown-item>           
            <el-dropdown-item></el-dropdown-item>
            </el-dropdown-menu>
          </el-dropdown>
          </el-col>
        </el-row>

        <el-row :gutter="20" style="margin-top:1%">
          <el-col :span="4" :offset="1" class="box">
          <el-dropdown>
          <span class="el-dropdown-link">Utilities<i class="el-icon-arrow-down el-icon--right"></i></span>
          <el-dropdown-menu slot="dropdown">
            <el-dropdown-item>Electic Utilities</el-dropdown-item>
            <el-dropdown-item>Gas Utilities</el-dropdown-item>
            <el-dropdown-item>Independent Power and Renewable Electricity Producers</el-dropdown-item>
            <el-dropdown-item>Multi-Utilies</el-dropdown-item>           
            <el-dropdown-item>Water Utilies</el-dropdown-item>
            </el-dropdown-menu>
          </el-dropdown>
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
    //10:30 - 
    handleCommand(command) {
      switch (command) {
        case "case1":
          this.$router.push("/submarket");
          break;
        case "case2":
          this.$router.push("/submarket");
          break;
        case "case3":
          this.$router.push("/submarket");
          break;
        case "case4":
          this.$router.push("/submarket");
          break;
      }
    },
  },
}

</script>


<style >
.el-dropdown-link {
    cursor: pointer;
    color: #000000;
    font-weight: 800;
    font-size: 20px;
    line-height: 30px;


}
.box{
    background: #F5EFE0;
    border-radius: 30px;
    width: 220px;
    height: 100px;



}

  .el-icon-arrow-down {
    font-size: 12px;
  }
</style>