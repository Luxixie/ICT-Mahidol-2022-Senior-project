<template>
  <div>
    <el-row style="background: #F5F5F5;; margin-top:2%;  margin-left:2%; margin-right:2%; height:250px">
      <el-col :span="17" :offset="1" style="background: #1F3D70;border-radius: 25px;margin-top:2%;">
        <el-row>
          <el-col :span="10" style="margin-left:8%">
            <h3 style="float: left; margin-left:5%;color: #F5EFE0;">SET</h3>
          </el-col>
        </el-row>
          <el-row>
          <el-col :span="10" style="margin-left:8%">
            <h4 style="float: left; margin-left:5%;color: #F5EFE0;">high: {{high}}</h4>
          </el-col>
          <el-col :span="10" >
            <h4 style="float: right; margin-right:6%;color: #F5EFE0;">current: {{current}}</h4>
          </el-col>
        </el-row>
        <el-row>
          <el-col :span="10" style="margin-left:8%">
            <h4 style="float: left; margin-left:5%; color: #F5EFE0;">low: {{low}}</h4>
          </el-col>
          <el-col :span="10" >
            <h4 style="float: right; margin-right:6%; color: #F5EFE0;">+6.00  (+0.37%)</h4>
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
          <el-dropdown @command="handleCommand">
          <span class="el-dropdown-link">Communication services<i class="el-icon-arrow-down el-icon--right"></i></span>
          <el-dropdown-menu slot="dropdown">
            <el-dropdown-item command="case1">Diversified Telecommunication Service</el-dropdown-item>
            <el-dropdown-item command="case2">Entertainment</el-dropdown-item>
            <el-dropdown-item command="case3">Interactive Media & Service</el-dropdown-item>
            <el-dropdown-item command="case4">Media</el-dropdown-item>           
            <el-dropdown-item command="case5">Wireless Telecommunication Service</el-dropdown-item>
            </el-dropdown-menu>
          </el-dropdown>
          </el-col>
          <el-col :span="4" :offset="1" class="box">
            <el-dropdown  @command="handleCommand">
            <span class="el-dropdown-link">Consumer discretionary<i class="el-icon-arrow-down el-icon--right"></i></span>
            <el-dropdown-menu slot="dropdown">
              <el-dropdown-item command="case6">Auto Components</el-dropdown-item>
              <el-dropdown-item command="case7">Automobiles</el-dropdown-item>
              <el-dropdown-item command="case8">Distributors</el-dropdown-item>
              <el-dropdown-item command="case9">Diversified Consumer Service</el-dropdown-item>           
              <el-dropdown-item command="case10">Hotels, Restaurants & Leisure</el-dropdown-item>
              <el-dropdown-item command="case11">Internet & Direct Marketing Retail</el-dropdown-item>
              <el-dropdown-item command="case12">Leisure Products</el-dropdown-item>
              <el-dropdown-item command="case13">Multiline Retail</el-dropdown-item>
              <el-dropdown-item command="case14">Specialty Retail</el-dropdown-item>
              <el-dropdown-item command="case15">Textiles, Apparel & Luxury Goods</el-dropdown-item>
              </el-dropdown-menu>
            </el-dropdown>
          </el-col>

          <el-col :span="4" :offset="1" class="box">
          <el-dropdown @command="handleCommand">
            <span class="el-dropdown-link">Consumer staples<i class="el-icon-arrow-down el-icon--right"></i></span>
            <el-dropdown-menu slot="dropdown">
              <el-dropdown-item command="case16">Beverages</el-dropdown-item>
              <el-dropdown-item command="case17">Food & Staples Retailing</el-dropdown-item>
              <el-dropdown-item command="case18">Food Products</el-dropdown-item>
              <el-dropdown-item command="case19">Household Products</el-dropdown-item>           
              <el-dropdown-item command="case20">Personal Products</el-dropdown-item>
              <el-dropdown-item command="case21">Tobacco</el-dropdown-item>
              </el-dropdown-menu>
            </el-dropdown>
          </el-col>

          <el-col :span="4" :offset="1" class="box">
          <el-dropdown @command="handleCommand">
            <span class="el-dropdown-link">Energy<i class="el-icon-arrow-down el-icon--right"></i></span>
            <el-dropdown-menu slot="dropdown">
              <el-dropdown-item command="case22">Energy Equipment & Service</el-dropdown-item>
              <el-dropdown-item command="case23">Oil, Gas & Consumer Fules</el-dropdown-item>
              </el-dropdown-menu>
            </el-dropdown>
          </el-col>

          <el-col :span="4" :offset="1" class="box">
          <el-dropdown @command="handleCommand">
            <span class="el-dropdown-link">Financial<i class="el-icon-arrow-down el-icon--right"></i></span>
            <el-dropdown-menu slot="dropdown">
              <el-dropdown-item command="case24">Banks</el-dropdown-item>
              <el-dropdown-item command="case25">Consumer Finance</el-dropdown-item>
              <el-dropdown-item command="case26">Diversified Financial Service</el-dropdown-item>
              <el-dropdown-item command="case27">Insurance</el-dropdown-item>           
              <el-dropdown-item command="case28">Mortgage REITs</el-dropdown-item>
              <el-dropdown-item command="case29">Thrifts & Mortgage Finance</el-dropdown-item>
              </el-dropdown-menu>
            </el-dropdown>
          </el-col>
        </el-row>

        <el-row :gutter="20" style="margin-top:1%">
          <el-col :span="4" :offset="1" class="box">
          <el-dropdown @command="handleCommand">
          <span class="el-dropdown-link">Healthcare<i class="el-icon-arrow-down el-icon--right"></i></span>
          <el-dropdown-menu slot="dropdown">
            <el-dropdown-item command="case30">Biotechnology</el-dropdown-item>
            <el-dropdown-item command="case31">Health Care Eequipment & Supplies</el-dropdown-item>
            <el-dropdown-item  command="case32">Health Care Prividers & Services</el-dropdown-item>
            <el-dropdown-item  command="case33">Health Care technology</el-dropdown-item>           
            <el-dropdown-item  command="case34">Life Sciences Tools & Services</el-dropdown-item>
            <el-dropdown-item  command="case35">Pharmaceuticals</el-dropdown-item>
            </el-dropdown-menu>
          </el-dropdown>
          </el-col>
          <el-col :span="4" :offset="1" class="box">
          <el-dropdown  @command="handleCommand">
          <span class="el-dropdown-link">Industrials<i class="el-icon-arrow-down el-icon--right"></i></span>
          <el-dropdown-menu slot="dropdown">
            <el-dropdown-item command="case36" >Aerospace & Defense</el-dropdown-item>
            <el-dropdown-item command="case37">Freight & Logistics</el-dropdown-item>
            <el-dropdown-item command="case38">Airlines</el-dropdown-item>
            <el-dropdown-item command="case39">Building Products</el-dropdown-item>           
            <el-dropdown-item command="case40">Commercial Services & Supplies</el-dropdown-item>
            <el-dropdown-item command="case41">Construction & Engineering</el-dropdown-item>
            <el-dropdown-item command="case42">Electrical Equipment</el-dropdown-item>
            <el-dropdown-item command="case43">Industrial Conglomerates</el-dropdown-item>
            <el-dropdown-item command="case44">Machinery</el-dropdown-item>
            <el-dropdown-item command="case45">Marine</el-dropdown-item>
            <el-dropdown-item command="case46">Professional Services</el-dropdown-item>
            <el-dropdown-item command="case47">Road & Rail</el-dropdown-item>
            <el-dropdown-item command="case48">Trading Companies & Distributors</el-dropdown-item>
            <el-dropdown-item command="case49">Transportation Infrastructure</el-dropdown-item>
            <el-dropdown-item command="case50">All</el-dropdown-item>
            
            </el-dropdown-menu>
          </el-dropdown>
          </el-col>
          <el-col :span="4" :offset="1" class="box">
          <el-dropdown>
          <span class="el-dropdown-link">Information technology<i class="el-icon-arrow-down el-icon--right"></i></span>
          <el-dropdown-menu slot="dropdown">
            <el-dropdown-item command="case62">Communications Equipment</el-dropdown-item>
            <el-dropdown-item command="case63">Electronic Equipment, Instruments & Components</el-dropdown-item>
            <el-dropdown-item command="case64">IT Services</el-dropdown-item>
            <el-dropdown-item command="case65">Semiconductors & Semiconductors Equipment</el-dropdown-item>           
            <el-dropdown-item command="case66">Software</el-dropdown-item>
            <el-dropdown-item command="case67">technology Hardware, storage & Peripherals</el-dropdown-item>
            </el-dropdown-menu>
          </el-dropdown>
          </el-col>
          <el-col :span="4" :offset="1" class="box">
          <el-dropdown @command="handleCommand">
          <span class="el-dropdown-link">Materials<i class="el-icon-arrow-down el-icon--right"></i></span>
          <el-dropdown-menu slot="dropdown">
            <el-dropdown-item command="case51">Chemicals</el-dropdown-item>
            <el-dropdown-item command="case52">Construction Materials</el-dropdown-item>
            <el-dropdown-item command="case53">Containers & Packgaging</el-dropdown-item>
            <el-dropdown-item command="case53">Metals & Mining</el-dropdown-item>           
            <el-dropdown-item command="case54">Paper & Forest Products</el-dropdown-item>
            </el-dropdown-menu>
          </el-dropdown>
          </el-col>
          <el-col :span="4" :offset="1" class="box">
          <el-dropdown @command="handleCommand">
          <span class="el-dropdown-link">Real estate<i class="el-icon-arrow-down el-icon--right"></i></span>
          <el-dropdown-menu slot="dropdown">
            <el-dropdown-item command="case55">Equity Real Estate Investment Trusts</el-dropdown-item>
            <el-dropdown-item command="case56">Real Estate Management & Development</el-dropdown-item>
            </el-dropdown-menu>
          </el-dropdown>
          </el-col>
        </el-row>

        <el-row :gutter="20" style="margin-top:1%">
          <el-col :span="4" :offset="1" class="box">
          <el-dropdown @command="handleCommand">
          <span class="el-dropdown-link">Utilities<i class="el-icon-arrow-down el-icon--right"></i></span>
          <el-dropdown-menu slot="dropdown">
            <el-dropdown-item command="case57">Electic Utilities</el-dropdown-item>
            <el-dropdown-item command="case58">Gas Utilities</el-dropdown-item>
            <el-dropdown-item command="case59">Independent Power and Renewable Electricity Producers</el-dropdown-item>
            <el-dropdown-item command="case60">Multi-Utilies</el-dropdown-item>           
            <el-dropdown-item command="case61">Water Utilies</el-dropdown-item>
            </el-dropdown-menu>
          </el-dropdown>
          </el-col>
        </el-row>
    

    </el-row>
  </div>
  
</template>

<script>
import axios from 'axios'
export default {
    data() {
        return {
          current:'',
          high:'',
          low:'',
          nowTime: ''
        }
    },
    mounted() {
    this.getNowTime();
    this.getSETPrice();
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
          getSETPrice () {
          let speed = 1000 * 60
          let that = this
          let theNowPrice = function () {
              axios.post("http://127.0.0.1:8088/GetSETCurrentPrice").then((res) => {
              console.log(res.data)
              that.high = res.data['dayhigh']
              that.low = res.data['daylow']
              that.current = res.data['lastprice']
          });
          }
          setInterval(theNowPrice, speed)
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
    
    handleCommand(command) {
      switch (command) {
        case "case1":
           this.$router.push({
            path:"/submarket/"+'Diversified Telecommunicaton Service',
            params:{industryName:'Diversified Telecommunicaton Service'}
          })
          break;
        case "case2":
            this.$router.push({
              path:"/submarket/"+'Entertainment',
              params:{industryName:'Entertainment'}
          })
          break;
        case "case3":
          this.$router.push({
              path:"/submarket/"+'Interactive Media & Service',
              params:{industryName:'Interactive Media & Service'}
          })
          break;
        case "case4":
            this.$router.push({
              path:"/submarket/"+'Media',
              params:{industryName:'Media'}
          })
          break;
        case "case5":
            this.$router.push({
              path:"/submarket/"+'Wireless Telecommunication Service',
              params:{industryName:'Wireless Telecommunication Service'}
          })
          break;
        case "case6":
            this.$router.push({
              path:"/submarket/"+'AutoComponents',
              params:{industryName:'AutoComponents'}
          })
          break;
        case "case7":
            this.$router.push({
              path:"/submarket/"+'Automobiles',
              params:{industryName:'Automobiles'}
          })
          break;
        case "case8":
            this.$router.push({
              path:"/submarket/"+'Distributors',
              params:{industryName:'Distributors'}
          })
          break;
        case "case9":
            this.$router.push({
              path:"/submarket/"+'Diversified Consumer Service',
              params:{industryName:'Diversified Consumer Service'}
          })
          break;
        case "case10":
            this.$router.push({
              path:"/submarket/"+'Entertainment',
              params:{industryName:'Entertainment'}
          })
          break;       
        case "case11":
            this.$router.push({
              path:"/submarket/"+'Hotels, Restaurants & Leisure',
              params:{industryName:'Hotels, Restaurants & Leisure'}
          })
          break; 
        case "case12":
            this.$router.push({
              path:"/submarket/"+'Leisure Products',
              params:{industryName:'Leisure Products'}
          })
          break;   
        case "case13":
            this.$router.push({
              path:"/submarket/"+'Multiline Retail',
              params:{industryName:'Multiline Retail'}
          })
          break;   
        case "case14":
            this.$router.push({
              path:"/submarket/"+'Specialty Retail',
              params:{industryName:'Specialty Retail'}
          })
          break; 
        case "case15":
            this.$router.push({
              path:"/submarket/"+'Textiles, Apparel & Luxury Goods',
              params:{industryName:'Textiles, Apparel & Luxury Goods'}
          })
          break;        
        case "case16":
                    this.$router.push({
                      path:"/submarket/"+'Beverages',
                      params:{industryName:'Beverages'}
                  })
                  break;              
        case "case17":
                    this.$router.push({
                      path:"/submarket/"+'Food & Staples Retailing',
                      params:{industryName:'Food & Staples Retailing'}
                  })
                  break;  

        case "case18":
          this.$router.push({
            path:"/submarket/"+'Food Products',
            params:{industryName:'Food Products'}
            })
          break; 
        case "case19":
          this.$router.push({
            path:"/submarket/"+'Household Products',
            params:{industryName:'Household Products'}
            })
          break; 
        case "case20":
          this.$router.push({
            path:"/submarket/"+'Personal Products',
            params:{industryName:'Personal Products'}
            })
          break; 
        case "case21":
          this.$router.push({
            path:"/submarket/"+'Tobacco',
            params:{industryName:'Tobacco'}
            })
          break; 
        case "case22":
          this.$router.push({
            path:"/submarket/"+'Energy Equipment & Service',
            params:{industryName:'Energy Equipment & Service'}
            })
          break;
        case "case23":
          this.$router.push({
            path:"/submarket/"+'Oil, Gas & Consumer Fules',
            params:{industryName:'Oil, Gas & Consumer Fules'}
            })
          break;  
        case "case24":
          this.$router.push({
            path:"/submarket/"+'Banks',
            params:{industryName:'Banks'}
            })
          break; 
        case "case25":
          this.$router.push({
            path:"/submarket/"+'Consumer Finance',
            params:{industryName:'Consumer Finance'}
            })
          break; 
        case "case26":
          this.$router.push({
            path:"/submarket/"+'Diversified Financial Service',
            params:{industryName:'Diversified Financial Service'}
            })
          break; 
        case "case27":
          this.$router.push({
            path:"/submarket/"+'Insurance',
            params:{industryName:'Insurance'}
            })
          break; 
        case "case28":
          this.$router.push({
            path:"/submarket/"+'Mortgage REITs',
            params:{industryName:'Mortgage REITs'}
            })
          break; 
        case "case29":
          this.$router.push({
            path:"/submarket/"+'Thrifts & Mortgage Finance',
            params:{industryName:'Thrifts & Mortgage Finance'}
            })
          break; 
        case "case30":
          this.$router.push({
            path:"/submarket/"+'Biotechnology',
            params:{industryName:'Biotechnology'}
            })
          break; 
        case "case31":
          this.$router.push({
            path:"/submarket/"+'Health Care Eequipment & Supplies',
            params:{industryName:'Health Care Eequipment & Supplies'}
            })
          break; 
        case "case32":
          this.$router.push({
            path:"/submarket/"+'Health Care Prividers & Services',
            params:{industryName:'Health Care Prividers & Services'}
            })
          break; 
        case "case33":
          this.$router.push({
            path:"/submarket/"+'Health Care technology',
            params:{industryName:'Health Care technology'}
            })
          break; 
        case "case34":
          this.$router.push({
            path:"/submarket/"+'Life Sciences Tools & Services',
            params:{industryName:'Life Sciences Tools & Services'}
            })
          break; 
        case "case35":
          this.$router.push({
            path:"/submarket/"+'Pharmaceuticals',
            params:{industryName:'Pharmaceuticals'}
            })
          break; 
        case "case36":
          this.$router.push({
            path:"/submarket/"+'Aerospace & Defense',
            params:{industryName:'Aerospace & Defense'}
            })
          break; 
        case "case37":
          this.$router.push({
            path:"/submarket/"+'Freight & Logistics',
            params:{industryName:'Freight & Logistics'}
            })
          break; 
        case "case38":
          this.$router.push({
            path:"/submarket/"+'Airlines',
            params:{industryName:'Airlines'}
            })
          break; 
        case "case39":
          this.$router.push({
            path:"/submarket/"+'Building Products',
            params:{industryName:'Building Products'}
            })
          break; 
        case "case40":
          this.$router.push({
            path:"/submarket/"+'Commercial Services & Supplies',
            params:{industryName:'Commercial Services & Supplies'}
            })
          break; 
        case "case41":
          this.$router.push({
            path:"/submarket/"+'Construction & Engineering',
            params:{industryName:'Construction & Engineering'}
            })
          break; 
        case "case42":
          this.$router.push({
            path:"/submarket/"+'Electrical Equipment',
            params:{industryName:'Electrical Equipment'}
            })
          break; 
        case "case43":
          this.$router.push({
            path:"/submarket/"+'Industrial Conglomerate',
            params:{industryName:'Industrial Conglomerate'}
            })
          break; 
        case "case44":
          this.$router.push({
            path:"/submarket/"+'Machinery',
            params:{industryName:'Machinery'}
            })
          break; 
        case "case45":
          this.$router.push({
            path:"/submarket/"+'Marine',
            params:{industryName:'Marine'}
            })
          break; 
        case "case46":
          this.$router.push({
            path:"/submarket/"+'Professional Services',
            params:{industryName:'Professional Services'}
            })
          break; 
        case "case47":
          this.$router.push({
            path:"/submarket/"+'Road&Rail',
            params:{industryName:'Road & Rail'}
            })
          break; 
        case "case48":
          this.$router.push({
            path:"/submarket/"+'Trading Companies & Distributors',
            params:{industryName:'Trading Companies & Distributors'}
            })
          break; 
        case "case49":
          this.$router.push({
            path:"/submarket/"+'Transportation Infrastructure',
            params:{industryName:'Transportation Infrastructure'}
            })
          break; 
        case "case50":
          this.$router.push({
            path:"/submarket/"+'All',
            params:{industryName:'All'}
            })
          break; 
        case "case51":
          this.$router.push({
            path:"/submarket/"+'Chemicals',
            params:{industryName:'Chemicals'}
            })
          break; 
        case "case52":
          this.$router.push({
            path:"/submarket/"+'Construction Materials',
            params:{industryName:'Construction Materials'}
            })
          break; 
        case "case53":
          this.$router.push({
            path:"/submarket/"+'Containers & Packgaging',
            params:{industryName:'Containers & Packgaging'}
            })
          break; 
        case "case54":
          this.$router.push({
            path:"/submarket/"+'Paper & Forest Products',
            params:{industryName:'Paper & Forest Products'}
            })
          break; 
        case "case55":
          this.$router.push({
            path:"/submarket/"+'Equity Real Estate Investment Trusts',
            params:{industryName:'Equity Real Estate Investment Trusts'}
            })
          break; 
        case "case56":
          this.$router.push({
            path:"/submarket/"+'Real Estate Management & Development',
            params:{industryName:'Real Estate Management & Development'}
            })
          break; 
        case "case57":
          this.$router.push({
            path:"/submarket/"+'Electic Utilities',
            params:{industryName:'Electic Utilities'}
            })
          break; 
        case "case58":
          this.$router.push({
            path:"/submarket/"+'Gas Utilities',
            params:{industryName:'Gas Utilities'}
            })
          break; 
        case "case59":
          this.$router.push({
            path:"/submarket/"+'Independent Powerand Renewable Electricity Producers',
            params:{industryName:'Independent Power and Renewable Electricity Producers'}
            })
          break; 
        case "case60":
          this.$router.push({
            path:"/submarket/"+'Multi-Utilies',
            params:{industryName:'Multi-Utilies'}
            })
          break; 
        case "case61":
          this.$router.push({
            path:"/submarket/"+'Water Utilies',
            params:{industryName:'Water Utilies'}
            })
          break; 
        case "case62":
          this.$router.push({
            path:"/submarket/"+'Communications Equipmen',
            params:{industryName:'Communications Equipmen'}
            })
          break; 
        case "case63":
          this.$router.push({
            path:"/submarket/"+'Electronic Equipment, Instruments & Components',
            params:{industryName:'Electronic Equipment, Instruments & Components'}
            })
          break; 
        case "case64":
          this.$router.push({
            path:"/submarket/"+'IT Services',
            params:{industryName:'IT Services'}
            })
          break; 
        case "case65":
          this.$router.push({
            path:"/submarket/"+'Semiconductors & Semiconductors Equipment',
            params:{industryName:'Semiconductors & Semiconductors Equipment'}
            })
          break; 
        case "case66":
          this.$router.push({
            path:"/submarket/"+'Software',
            params:{industryName:'Software'}
            })
          break; 
        case "case67":
          this.$router.push({
            path:"/submarket/"+'technology Hardware, storage & Peripherals',
            params:{industryName:'technology Hardware, storage & Peripherals'}
            })
          break; 
      }
    },
  },
  created(){
        axios.post("http://127.0.0.1:8088/GetSETCurrentPrice").then((res) => {
           console.log(res.data)
           this.high = res.data['dayhigh']
           this.low = res.data['daylow']
           this.current = res.data['lastprice']
        });
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