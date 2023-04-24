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
            <h4 style="float: left; margin-left:5%;color: #F5EFE0;">high: {{high | numberWithCommas }}</h4>
          </el-col>
          <el-col :span="10" >
            <h4 style="float: right; margin-right:6%;color: #F5EFE0;">current: {{current | numberWithCommas }}</h4>
          </el-col>
        </el-row>
        <el-row>
          <el-col :span="10" style="margin-left:8%">
            <h4 style="float: left; margin-left:5%; color: #F5EFE0;">low: {{low | numberWithCommas }}</h4>
          </el-col>
          <el-col :span="10" >
            <h4 style="float: right; margin-right:6%; color: #F5EFE0;">                
              <span> {{ (current - previousclose) >= 0 ? '+' : '-' }}{{ Math.abs(current - previousclose).toFixed(2) }} ({{((current / previousclose-1)*100).toFixed(2)}}%)
                </span></h4>
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
          <el-col :span="4" :offset="1" class="box1">
          <el-dropdown @command="handleCommand">
          <span class="el-dropdown-link">Communication Services<i class="el-icon-arrow-down el-icon--right"></i></span>
          <el-dropdown-menu slot="dropdown">
            <el-dropdown-item command="case1">Telecom Services</el-dropdown-item>
            <el-dropdown-item command="case2">Advertising Agencies</el-dropdown-item>
            <el-dropdown-item command="case3">Publishing</el-dropdown-item>
            <el-dropdown-item command="case4">Broadcasting</el-dropdown-item>           
            <el-dropdown-item command="case5">Entertainment</el-dropdown-item>
            <el-dropdown-item command="case7">Electronic Gaming & Multimedia</el-dropdown-item>

            </el-dropdown-menu>
          </el-dropdown>
          </el-col>
          <el-col :span="4" :offset="1" class="box1">
            <el-dropdown  @command="handleCommand">
            <span class="el-dropdown-link">Consumer Cyclical<i class="el-icon-arrow-down el-icon--right"></i></span>
            <el-dropdown-menu slot="dropdown">
              <el-dropdown-item command="case8">Auto & Truck Dealerships</el-dropdown-item>
              <el-dropdown-item command="case9">Auto Manufacturers</el-dropdown-item>
              <el-dropdown-item command="case10">Auto Parts</el-dropdown-item>
              <el-dropdown-item command="case12">Furnishings, Fixtures & Appliances</el-dropdown-item>
              <el-dropdown-item command="case14">Textile Manufacturing</el-dropdown-item>
              <el-dropdown-item command="case15">Apparel Manufacturing</el-dropdown-item>
              <el-dropdown-item command="case16">Footwear & Accessories</el-dropdown-item>
              <el-dropdown-item command="case17">Packaging & Containers</el-dropdown-item>
              <el-dropdown-item command="case19">Restaurants</el-dropdown-item>           
              <el-dropdown-item command="case20">Apparel Retail</el-dropdown-item>           
              <el-dropdown-item command="case21">Department Stores</el-dropdown-item>           
              <el-dropdown-item command="case22">Home Improvement Retail</el-dropdown-item>           
              <el-dropdown-item command="case23">Luxury Goods</el-dropdown-item>           
              <el-dropdown-item command="case25">Specialty Retail</el-dropdown-item>           
              <el-dropdown-item command="case27">Leisure</el-dropdown-item>           
              <el-dropdown-item command="case28">Lodging</el-dropdown-item>           
              <el-dropdown-item command="case29">Resorts & Casinos</el-dropdown-item>           
              </el-dropdown-menu>
            </el-dropdown>
          </el-col>

          <el-col :span="4" :offset="1" class="box1">
          <el-dropdown @command="handleCommand">
            <span class="el-dropdown-link">Consumer Defensive<i class="el-icon-arrow-down el-icon--right"></i></span>
            <el-dropdown-menu slot="dropdown">
              <el-dropdown-item command="case33">Beverages—Non-Alcoholic</el-dropdown-item>
              <el-dropdown-item command="case34">Confectioners</el-dropdown-item>           
              <el-dropdown-item command="case35">Farm Products</el-dropdown-item>
              <el-dropdown-item command="case36">Household & Personal Products</el-dropdown-item>
              <el-dropdown-item command="case37">Packaged Foods</el-dropdown-item>
              <el-dropdown-item command="case38">Education & Training Services</el-dropdown-item>
              <el-dropdown-item command="case40">Food Distribution</el-dropdown-item>
              <el-dropdown-item command="case41">Grocery Stores</el-dropdown-item>
              </el-dropdown-menu>
            </el-dropdown>
          </el-col>

          <el-col :span="4" :offset="1" class="box1">
          <el-dropdown @command="handleCommand">
            <span class="el-dropdown-link">Energy<i class="el-icon-arrow-down el-icon--right"></i></span>
            <el-dropdown-menu slot="dropdown">
              <el-dropdown-item command="case44">Oil & Gas E&P</el-dropdown-item>
              <el-dropdown-item command="case45">Oil & Gas Integrated</el-dropdown-item>
              <el-dropdown-item command="case46">Oil & Gas Midstream</el-dropdown-item>
              <el-dropdown-item command="case47">Oil & Gas Refining & Marketing</el-dropdown-item>
              <el-dropdown-item command="case50">Thermal Coal</el-dropdown-item>
              <el-dropdown-item command="case51">Uranium</el-dropdown-item>

              </el-dropdown-menu>
            </el-dropdown>
          </el-col>


        </el-row>

        <el-row :gutter="20" style="margin-top:1%">
          <el-col :span="4" :offset="1" class="box1">
          <el-dropdown @command="handleCommand">
          <span class="el-dropdown-link">Healthcare<i class="el-icon-arrow-down el-icon--right"></i></span>
          <el-dropdown-menu slot="dropdown">
            <el-dropdown-item  command="case69">Drug Manufacturers—Specialty & Generic</el-dropdown-item>
            <el-dropdown-item  command="case71">Medical Care Facilities</el-dropdown-item>
            <el-dropdown-item command="case74">Medical Devices</el-dropdown-item>
            <el-dropdown-item command="case75">Medical Instruments & Supplies</el-dropdown-item>
            </el-dropdown-menu>
          </el-dropdown>
          </el-col>
          <el-col :span="4" :offset="1" class="box1">
          <el-dropdown  @command="handleCommand">
          <span class="el-dropdown-link">Industrials<i class="el-icon-arrow-down el-icon--right"></i></span>
          <el-dropdown-menu slot="dropdown">
            <el-dropdown-item command="case78">Aerospace & Defense</el-dropdown-item>
            <el-dropdown-item command="case79">Specialty Business Services</el-dropdown-item>
            <el-dropdown-item command="case80">Consulting Services</el-dropdown-item>
            <el-dropdown-item command="case81">Rental & Leasing Services</el-dropdown-item>           
            <el-dropdown-item command="case82">Security & Protection Services</el-dropdown-item>
            <el-dropdown-item command="case84">Conglomerates</el-dropdown-item>
            <el-dropdown-item command="case85">Engineering & Construction</el-dropdown-item>
            <el-dropdown-item command="case86">Infrastructure Operations</el-dropdown-item>
            <el-dropdown-item command="case87">Building Products & Equipment</el-dropdown-item>
            <el-dropdown-item command="case88">Farm & Heavy Construction Machinery</el-dropdown-item>
            <el-dropdown-item command="case89">Industrial Distribution</el-dropdown-item>
            <el-dropdown-item command="case90">Business Equipment & Supplies</el-dropdown-item>
            <el-dropdown-item command="case91">Specialty Industrial Machinery</el-dropdown-item>
            <el-dropdown-item command="case92">Metal Fabrication</el-dropdown-item>
            <el-dropdown-item command="case93">Pollution & Treatment Controls</el-dropdown-item>
            <el-dropdown-item command="case94">Tools & Accessories</el-dropdown-item>
            <el-dropdown-item command="case95">Electrical Equipment & Parts</el-dropdown-item>
            <el-dropdown-item command="case96">Airports & Air Services</el-dropdown-item>
            <el-dropdown-item command="case97">Airlines</el-dropdown-item>
            <el-dropdown-item command="case98">Railroads</el-dropdown-item>
            <el-dropdown-item command="case99">Marine Shipping</el-dropdown-item>
            <el-dropdown-item command="case100">Trucking</el-dropdown-item>
            <el-dropdown-item command="case101">Integrated Freight & Logistics</el-dropdown-item>
            <el-dropdown-item command="case102">Waste Management</el-dropdown-item>

            </el-dropdown-menu>
          </el-dropdown>
          </el-col>
          <el-col :span="4" :offset="1" class="box1">
          <el-dropdown  @command="handleCommand">
          <span class="el-dropdown-link">Technology<i class="el-icon-arrow-down el-icon--right"></i></span>
          <el-dropdown-menu slot="dropdown">
            <el-dropdown-item command="case103">Information Technology Services</el-dropdown-item>
            <el-dropdown-item command="case104">Software—Application</el-dropdown-item>
            <el-dropdown-item command="case105">Electronic Components</el-dropdown-item>
            <el-dropdown-item command="case106">Electronics & Computer Distribution</el-dropdown-item>
            <el-dropdown-item command="case109">Semiconductors</el-dropdown-item>
            <el-dropdown-item command="case110">Solar</el-dropdown-item>
            <el-dropdown-item command="case113">Communication Equipment</el-dropdown-item>
            <el-dropdown-item command="case114">Computer Hardware</el-dropdown-item>
            <el-dropdown-item command="case115">Consumer Electronics</el-dropdown-item>
            </el-dropdown-menu>
          </el-dropdown>
          </el-col>
          <el-col :span="4" :offset="1" class="box1">
          <el-dropdown @command="handleCommand">
          <span class="el-dropdown-link">Basic Materials<i class="el-icon-arrow-down el-icon--right"></i></span>
          <el-dropdown-menu slot="dropdown">
            <el-dropdown-item command="case116">Paper & Paper Products</el-dropdown-item>
            <el-dropdown-item command="case117">Aluminum</el-dropdown-item>
            <el-dropdown-item command="case119">Other Industrial Metals & Mining</el-dropdown-item>
            <el-dropdown-item command="case124">Steel</el-dropdown-item>
            <el-dropdown-item command="case125">Agricultural Inputs</el-dropdown-item>
            <el-dropdown-item command="case126">Building Materials</el-dropdown-item>
            <el-dropdown-item command="case127">Chemicals</el-dropdown-item>
            <el-dropdown-item command="case128">Specialty Chemicals</el-dropdown-item>           
            <el-dropdown-item command="case129">Lumber & Wood Production</el-dropdown-item>
            </el-dropdown-menu>
          </el-dropdown>
          </el-col>

        </el-row>

        <el-row :gutter="20" style="margin-top:1%">
          <el-col :span="4" :offset="1" class="box1">
          <el-dropdown @command="handleCommand">
          <span class="el-dropdown-link">Utilities<i class="el-icon-arrow-down el-icon--right"></i></span>
          <el-dropdown-menu slot="dropdown">
            <el-dropdown-item command="case142">Utilities—Independent Power Producers</el-dropdown-item>
            <el-dropdown-item command="case143">Utilities—Renewable</el-dropdown-item>
            <el-dropdown-item command="case144">Utilities—Regulated Water</el-dropdown-item>
            <el-dropdown-item command="case145">Utilities—Regulated Electric</el-dropdown-item>           
            <el-dropdown-item command="case146">Utilities—Regulated Gas</el-dropdown-item>
            <el-dropdown-item command="case147">Utilities—Diversified</el-dropdown-item>
            </el-dropdown-menu>
          </el-dropdown>
          </el-col>

          <el-col :span="4" :offset="1" class="box1">
          <el-dropdown @command="handleCommand">
            <span class="el-dropdown-link">Financial Services<i class="el-icon-arrow-down el-icon--right"></i></span>
            <el-dropdown-menu slot="dropdown">
              <el-dropdown-item command="case52">Asset Management</el-dropdown-item>
              <el-dropdown-item command="case54">Banks—Regional</el-dropdown-item>
              <el-dropdown-item command="case56">Capital Markets</el-dropdown-item>
              <el-dropdown-item command="case58">Insurance—Life</el-dropdown-item>
              <el-dropdown-item command="case59">Insurance—Property & Casualty</el-dropdown-item>
              <el-dropdown-item command="case60">Insurance—Reinsurance</el-dropdown-item>
              <el-dropdown-item command="case62">Insurance Brokers</el-dropdown-item>
              <el-dropdown-item command="case63">Insurance—Diversified</el-dropdown-item>
              <el-dropdown-item command="case65">Financial Conglomerates</el-dropdown-item>
              <el-dropdown-item command="case66">Credit Services</el-dropdown-item>
              </el-dropdown-menu>
            </el-dropdown>
          </el-col>
          <el-col :span="4" :offset="1" class="box1">
          <el-dropdown @command="handleCommand">
          <span class="el-dropdown-link">Real estate<i class="el-icon-arrow-down el-icon--right"></i></span>
          <el-dropdown-menu slot="dropdown">
            <el-dropdown-item command="case130">Real Estate—Development</el-dropdown-item>
            <el-dropdown-item command="case131">Real Estate Services</el-dropdown-item>
            <el-dropdown-item command="case132">Real Estate—Diversified</el-dropdown-item>
            <el-dropdown-item command="case134">REIT—Hotel & Motel</el-dropdown-item>
            <el-dropdown-item command="case135">REIT—Industrial</el-dropdown-item>
            <el-dropdown-item command="case136">REIT—Office</el-dropdown-item>
            <el-dropdown-item command="case137">REIT—Residential</el-dropdown-item>
            <el-dropdown-item command="case138">REIT—Retail</el-dropdown-item>
            <el-dropdown-item command="case140">REIT—Specialty</el-dropdown-item>
            <el-dropdown-item command="case141">REIT—Diversified</el-dropdown-item>
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
          let speed = 1000 * 600
          let that = this
          let theNowPrice = function () {
              axios.post("http://127.0.0.1:8088/GetSETCurrentPrice").then((res) => {
              console.log(res.data)
              that.high = res.data['dayhigh']
              that.low = res.data['daylow']
              that.current = res.data['lastprice']
              that.previousclose = res.data['previousclose']
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
            path:"/submarket/"+'Telecom Services',
            params:{industryName:'Telecom Services'}
          })
          break;
        case "case2":
            this.$router.push({
              path:"/submarket/"+'Advertising Agencies',
              params:{industryName:'Advertising Agencies'}
          })
          break;
        case "case3":
          this.$router.push({
              path:"/submarket/"+'Publishing',
              params:{industryName:'Publishing'}
          })
          break;
        case "case4":
            this.$router.push({
              path:"/submarket/"+'Broadcasting',
              params:{industryName:'Broadcasting'}
          })
          break;
        case "case5":
            this.$router.push({
              path:"/submarket/"+'Entertainment',
              params:{industryName:'Entertainment'}
          })
          break;
        case "case7":
            this.$router.push({
              path:"/submarket/"+'Electronic Gaming & Multimedia',
              params:{industryName:'Electronic Gaming & Multimedia'}
          })
          break;
        case "case8":
            this.$router.push({
              path:"/submarket/"+'Auto & Truck Dealerships',
              params:{industryName:'Auto & Truck Dealerships'}
          })
          break;
        case "case9":
            this.$router.push({
              path:"/submarket/"+'Auto Manufacturers',
              params:{industryName:'Auto Manufacturers'}
          })
          break;
        case "case10":
            this.$router.push({
              path:"/submarket/"+'Auto Parts',
              params:{industryName:'Auto Parts'}
          })
          break;       
       
        case "case12":
            this.$router.push({
              path:"/submarket/"+'Furnishings, Fixtures & Appliances',
              params:{industryName:'Furnishings, Fixtures & Appliances'}
          })
          break;   
          
        case "case14":
            this.$router.push({
              path:"/submarket/"+'Textile Manufacturing',
              params:{industryName:'Textile Manufacturing'}
          })
          break; 
        case "case15":
            this.$router.push({
              path:"/submarket/"+'Apparel Manufacturing',
              params:{industryName:'Apparel Manufacturing'}
          })
          break;        
        case "case16":
                    this.$router.push({
                      path:"/submarket/"+'Footwear & Accessories',
                      params:{industryName:'Footwear & Accessories'}
                  })
                  break;              
        case "case17":
                    this.$router.push({
                      path:"/submarket/"+'Packaging & Containers',
                      params:{industryName:'Packaging & Containers'}
                  })
                  break;  

       
        case "case19":
          this.$router.push({
            path:"/submarket/"+'Restaurants',
            params:{industryName:'Restaurants'}
            })
          break; 
        case "case20":
          this.$router.push({
            path:"/submarket/"+'Apparel Retail',
            params:{industryName:'Apparel Retail'}
            })
          break; 
        case "case21":
          this.$router.push({
            path:"/submarket/"+'Department Stores',
            params:{industryName:'Department Stores'}
            })
          break; 
        case "case22":
          this.$router.push({
            path:"/submarket/"+'Home Improvement Retail',
            params:{industryName:'Home Improvement Retail'}
            })
          break;
        case "case23":
          this.$router.push({
            path:"/submarket/"+'Luxury Goods',
            params:{industryName:'Luxury Goods'}
            })
          break;  
       
        case "case25":
          this.$router.push({
            path:"/submarket/"+'Specialty Retail',
            params:{industryName:'Specialty Retail'}
            })
          break; 
       
        case "case27":
          this.$router.push({
            path:"/submarket/"+'Leisure',
            params:{industryName:'Leisure'}
            })
          break; 
        case "case28":
          this.$router.push({
            path:"/submarket/"+'Lodging',
            params:{industryName:'Lodging'}
            })
          break; 
        case "case29":
          this.$router.push({
            path:"/submarket/"+'Resorts & Casinos',
            params:{industryName:'Resorts & Casinos'}
            })
          break; 
     
        case "case33":
          this.$router.push({
            path:"/submarket/"+'Beverages—Non-Alcoholic',
            params:{industryName:'Beverages—Non-Alcoholic'}
            })
          break; 
        case "case34":
          this.$router.push({
            path:"/submarket/"+'Confectioners',
            params:{industryName:'Confectioners'}
            })
          break; 
        case "case35":
          this.$router.push({
            path:"/submarket/"+'Farm Products',
            params:{industryName:'Farm Products'}
            })
          break; 
        case "case36":
          this.$router.push({
            path:"/submarket/"+'Household & Personal Products',
            params:{industryName:'Household & Personal Products'}
            })
          break; 
        case "case37":
          this.$router.push({
            path:"/submarket/"+'Packaged Foods',
            params:{industryName:'Packaged Foods'}
            })
          break; 
        case "case38":
          this.$router.push({
            path:"/submarket/"+'Education & Training Services',
            params:{industryName:'Education & Training Services'}
            })
          break; 
      
        case "case40":
          this.$router.push({
            path:"/submarket/"+'Food Distribution',
            params:{industryName:'Food Distribution'}
            })
          break; 
        case "case41":
          this.$router.push({
            path:"/submarket/"+'Grocery Stores',
            params:{industryName:'Grocery Stores'}
            })
          break; 
     

        case "case44":
          this.$router.push({
            path:"/submarket/"+'Oil & Gas E&P',
            params:{industryName:'Oil & Gas E&P'}
            })
          break; 
        case "case45":
          this.$router.push({
            path:"/submarket/"+'Oil & Gas Integrated',
            params:{industryName:'Oil & Gas Integrated'}
            })
          break; 
        case "case46":
          this.$router.push({
            path:"/submarket/"+'Oil & Gas Midstream',
            params:{industryName:'Oil & Gas Midstream'}
            })
          break; 
            case "case47":
          this.$router.push({
            path:"/submarket/"+'Oil & Gas Refining & Marketing',
            params:{industryName:'Oil & Gas Refining & Marketing'}
            })
          break; 
   
        case "case50":
          this.$router.push({
            path:"/submarket/"+'Thermal Coal',
            params:{industryName:'Uranium'}
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
            path:"/submarket/"+'Asset Management',
            params:{industryName:'Asset Management'}
            })
          break; 
  
        case "case54":
          this.$router.push({
            path:"/submarket/"+'Banks—Regional',
            params:{industryName:'Banks—Regional'}
            })
          break; 
  
        case "case56":
          this.$router.push({
            path:"/submarket/"+'Capital Markets',
            params:{industryName:'Capital Markets'}
            })
          break; 
      
        case "case58":
          this.$router.push({
            path:"/submarket/"+'Insurance—Life',
            params:{industryName:'Insurance—Life'}
            })
          break; 
        case "case59":
          this.$router.push({
            path:"/submarket/"+'Insurance—Property & Casualty',
            params:{industryName:'Insurance—Property & Casualty'}
            })
          break; 
        case "case60":
          this.$router.push({
            path:"/submarket/"+'Insurance—Reinsurance',
            params:{industryName:'Insurance—Reinsurance'}
            })
          break; 
    
        case "case62":
          this.$router.push({
            path:"/submarket/"+'Insurance Brokers',
            params:{industryName:'Insurance Brokers'}
            })
          break; 
        case "case63":
          this.$router.push({
            path:"/submarket/"+'Insurance—Diversified',
            params:{industryName:'Insurance—Diversified'}
            })
          break; 
     
        case "case65":
          this.$router.push({
            path:"/submarket/"+'Financial Conglomerates',
            params:{industryName:'Financial Conglomerates'}
            })
          break; 
        case "case66":
          this.$router.push({
            path:"/submarket/"+'Credit Services',
            params:{industryName:'Credit Services'}
            })
          break; 
    
     
        case "case69":
          this.$router.push({
            path:"/submarket/"+'Drug Manufacturers—Specialty & Generic',
            params:{industryName:'Drug Manufacturers—Specialty & Generic'}
            })
          break;
   
        case "case71":
          this.$router.push({
            path:"/submarket/"+'Medical Care Facilities',
            params:{industryName:'Medical Care Facilities'}
            })
          break;

        case "case74":
          this.$router.push({
            path:"/submarket/"+'Medical Devices',
            params:{industryName:'Medical Devices'}
            })
          break;
        case "case75":
          this.$router.push({
            path:"/submarket/"+'Medical Instruments & Supplies',
            params:{industryName:'Medical Instruments & Supplies'}
            })
          break;
     
      
        case "case78":
          this.$router.push({
            path:"/submarket/"+'Aerospace & Defense',
            params:{industryName:'Aerospace & Defense'}
            })
          break;
        case "case79":
          this.$router.push({
            path:"/submarket/"+'Specialty Business Services',
            params:{industryName:'Specialty Business Services'}
            })
          break;
        case "case80":
          this.$router.push({
            path:"/submarket/"+'Consulting Services',
            params:{industryName:'Consulting Services'}
            })
          break;
        case "case81":
          this.$router.push({
            path:"/submarket/"+'Rental & Leasing Services',
            params:{industryName:'Rental & Leasing Services'}
            })
          break;
        case "case82":
          this.$router.push({
            path:"/submarket/"+'Security & Protection Services',
            params:{industryName:'Security & Protection Services'}
            })
          break;
      
        case "case84":
          this.$router.push({
            path:"/submarket/"+'Conglomerates',
            params:{industryName:'Conglomerates'}
            })
          break;
        case "case85":
          this.$router.push({
            path:"/submarket/"+'Engineering & Construction',
            params:{industryName:'Engineering & Construction'}
            })
          break;
        case "case86":
          this.$router.push({
            path:"/submarket/"+'Infrastructure Operations',
            params:{industryName:'Infrastructure Operations'}
            })
          break;
        case "case87":
          this.$router.push({
            path:"/submarket/"+'Building Products & Equipment',
            params:{industryName:'Building Products & Equipment'}
            })
          break;
        case "case88":
          this.$router.push({
            path:"/submarket/"+'Farm & Heavy Construction Machinery',
            params:{industryName:'Farm & Heavy Construction Machinery'}
            })
          break;
        case "case89":
          this.$router.push({
            path:"/submarket/"+'Industrial Distribution',
            params:{industryName:'Industrial Distribution'}
            })
          break;
        case "case90":
          this.$router.push({
            path:"/submarket/"+'Business Equipment & Supplies',
            params:{industryName:'Business Equipment & Supplies'}
            })
          break;
        case "case91":
          this.$router.push({
            path:"/submarket/"+'Specialty Industrial Machinery',
            params:{industryName:'Specialty Industrial Machinery'}
            })
          break;
        case "case92":
          this.$router.push({
            path:"/submarket/"+'Metal Fabrication',
            params:{industryName:'Metal Fabrication'}
            })
          break;
        case "case93":
          this.$router.push({
            path:"/submarket/"+'Pollution & Treatment Controls',
            params:{industryName:'Pollution & Treatment Controls'}
            })
          break;
            case "case94":
          this.$router.push({
            path:"/submarket/"+'Tools & Accessories',
            params:{industryName:'Tools & Accessories'}
            })
          break;
        case "case95":
          this.$router.push({
            path:"/submarket/"+'Electrical Equipment & Parts',
            params:{industryName:'Electrical Equipment & Parts'}
            })
          break;
        case "case96":
          this.$router.push({
            path:"/submarket/"+'Airports & Air Services',
            params:{industryName:'Airports & Air Services'}
            })
          break;
        case "case97":
          this.$router.push({
            path:"/submarket/"+'Airlines',
            params:{industryName:'Airlines'}
            })
          break;
        case "case98":
          this.$router.push({
            path:"/submarket/"+'Railroads',
            params:{industryName:'Railroads'}
            })
          break;
        case "case99":
          this.$router.push({
            path:"/submarket/"+'Marine Shipping',
            params:{industryName:'Marine Shipping'}
            })
          break;
        case "case100":
          this.$router.push({
            path:"/submarket/"+'Trucking',
            params:{industryName:'Trucking'}
            })
          break;
        case "case101":
          this.$router.push({
            path:"/submarket/"+'Integrated Freight & Logistics',
            params:{industryName:'Integrated Freight & Logistics'}
            })
          break;
          case "case102":
          this.$router.push({
            path:"/submarket/"+'Waste Management',
            params:{industryName:'Waste Management'}
            })
          break;
          case "case103":
          this.$router.push({
            path:"/submarket/"+'Information Technology Services',
            params:{industryName:'Information Technology Services'}
            })
          break;
          case "case104":
          this.$router.push({
            path:"/submarket/"+'Software—Application',
            params:{industryName:'Software—Application'}
            })
          break;
          case "case105":
          this.$router.push({
            path:"/submarket/"+'Electronic Components',
            params:{industryName:'Electronic Components'}
            })
          break;
          case "case106":
          this.$router.push({
            path:"/submarket/"+'Electronics & Computer Distribution',
            params:{industryName:'Electronics & Computer Distribution'}
            })
          break;
 
          case "case109":
          this.$router.push({
            path:"/submarket/"+'Semiconductors',
            params:{industryName:'Semiconductors'}
            })
          break;
          case "case110":
          this.$router.push({
            path:"/submarket/"+'Solar',
            params:{industryName:'Solar'}
            })
          break;

          case "case113":
          this.$router.push({
            path:"/submarket/"+'Communication Equipment',
            params:{industryName:'Communication Equipment'}
            })
          break;
          case "case114":
          this.$router.push({
            path:"/submarket/"+'Computer Hardware',
            params:{industryName:'Computer Hardware'}
            })
          break;
          case "case115":
          this.$router.push({
            path:"/submarket/"+'Consumer Electronics',
            params:{industryName:'Consumer Electronics'}
            })
          break;
          case "case116":
          this.$router.push({
            path:"/submarket/"+'Paper & Paper Products',
            params:{industryName:'Paper & Paper Products'}
            })
          break;
          case "case117":
          this.$router.push({
            path:"/submarket/"+'Aluminum',
            params:{industryName:'Aluminum'}
            })
          break;

          case "case119":
          this.$router.push({
            path:"/submarket/"+'Other Industrial Metals & Mining',
            params:{industryName:'Other Industrial Metals & Mining'}
            })
          break;


     
          case "case124":
          this.$router.push({
            path:"/submarket/"+'Steel',
            params:{industryName:'Steel'}
            })
          break;
          case "case125":
          this.$router.push({
            path:"/submarket/"+'Agricultural Inputs',
            params:{industryName:'Agricultural Inputs'}
            })
          break;
           case "case126":
          this.$router.push({
            path:"/submarket/"+'Building Materials',
            params:{industryName:'Building Materials'}
            })
          break;
           case "case127":
          this.$router.push({
            path:"/submarket/"+'Chemicals',
            params:{industryName:'Chemicals'}
            })
          break;
           case "case128":
          this.$router.push({
            path:"/submarket/"+'Specialty Chemicals',
            params:{industryName:'Specialty Chemicals'}
            })
          break;
           case "case129":
          this.$router.push({
            path:"/submarket/"+'Lumber & Wood Production',
            params:{industryName:'Lumber & Wood Production'}
            })
          break;
           case "case130":
          this.$router.push({
            path:"/submarket/"+'Real Estate—Development',
            params:{industryName:'Real Estate—Development'}
            })
          break;
           case "case131":
          this.$router.push({
            path:"/submarket/"+'Real Estate Services',
            params:{industryName:'Real Estate Services'}
            })
          break;
           case "case132":
          this.$router.push({
            path:"/submarket/"+'Real Estate—Diversified',
            params:{industryName:'Real Estate—Diversified'}
            })
          break;
     
           case "case134":
          this.$router.push({
            path:"/submarket/"+'REIT—Hotel & Motel',
            params:{industryName:'REIT—Hotel & Motel'}
            })
          break;
           case "case135":
          this.$router.push({
            path:"/submarket/"+'REIT—Industrial',
            params:{industryName:'REIT—Industrial'}
            })
          break;
           case "case136":
          this.$router.push({
            path:"/submarket/"+'REIT—Office',
            params:{industryName:'REIT—Office'}
            })
          break;
           case "case137":
          this.$router.push({
            path:"/submarket/"+'REIT—Residential',
            params:{industryName:'REIT—Residential'}
            })
          break;
           case "case138":
          this.$router.push({
            path:"/submarket/"+'REIT—Retail',
            params:{industryName:'REIT—Retail'}
            })
          break;
  
           case "case140":
          this.$router.push({
            path:"/submarket/"+'REIT—Specialty',
            params:{industryName:'REIT—Specialty'}
            })
          break;
          case "case141":
          this.$router.push({
            path:"/submarket/"+'REIT—Diversified',
            params:{industryName:'REIT—Diversified'}
            })
          break;
          case "case142":
          this.$router.push({
            path:"/submarket/"+'Utilities—Independent Power Producers',
            params:{industryName:'Utilities—Independent Power Producers'}
            })
          break;
          case "case143":
          this.$router.push({
            path:"/submarket/"+'Utilities—Renewable',
            params:{industryName:'Utilities—Renewable'}
            })
          break;
          case "case144":
          this.$router.push({
            path:"/submarket/"+'Utilities—Regulated Water',
            params:{industryName:'Utilities—Regulated Water'}
            })
          break;
          case "case145":
          this.$router.push({
            path:"/submarket/"+'Utilities—Regulated Electric',
            params:{industryName:'Utilities—Regulated Electric'}
            })
          break;
          case "case146":
          this.$router.push({
            path:"/submarket/"+'Utilities—Regulated Gas',
            params:{industryName:'Utilities—Regulated Gas'}
            })
          break;
          case "case147":
          this.$router.push({
            path:"/submarket/"+'Utilities—Diversified',
            params:{industryName:'Utilities—Diversified'}
            })
          break;
      
      }
    },
  },
  filters: {
    numberWithCommas: function (value) {
        if (!value) return ''
        var parts = value.toString().split('.')
        parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ',')
        if (parts.length > 1) {
        parts[1] = parts[1].substr(0, 2) // Only keep the first two decimal places
        } else {
        parts.push('00') // Add trailing zeros if the value doesn't have any decimal places
        }
        return parts.join('.')
    }
  },
  created(){
        axios.post("http://127.0.0.1:8088/GetSETCurrentPrice").then((res) => {
            console.log(res.data)
            this.high = res.data['dayhigh']
            this.low = res.data['daylow']
            this.current = res.data['lastprice']
            this.previousclose = res.data['previousclose']
        });
    },
}

</script>


<style >
.el-dropdown-link {
  align-items: center;
  color: #000000;
  font-weight: 800;
  font-size: 25px;


}
.box1{
    background: #F5EFE0;
    border-radius: 30px;
    width: 20%;
    height: 100px;
}

  .el-icon-arrow-down {
    font-size: 12px;
    margin-left: 5px;
  }
</style>