<template>
    <div>
        <el-row class="chapterbox" >
            <h2 style="margin-left: 3%;  margin-top:4%"> 06 Making the Decision</h2>
        </el-row>
        <el-row style="background: #F5EFE0;border-radius: 30px;margin-top:1%; margin-left: 3%; margin-right: 3%;" >
            <h2 style="margin-left: 3%;  margin-top:2%">Concept</h2>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:1%">Now you have an idea of what you want and the kind of returns that are required to get you there. That leaves just one question: What goes into the portfolio?</h4>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:1%">· Are you already wealthy? If so, add 5% to 10% to the stock allocation,depending on how comfortable you are with your level of wealth.</h4>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:1%">· How’s your risk tolerance? Add or subtract up to 10% from the stock allocation depending on your tolerance for risk. Risk takers add to the allocation, risk avoiders subtract.</h4>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:1%">· When do you need the money? If your time horizon is more than 15 years, add up to 10% to the stock allocation. If you plan to use the money in less than 10 years, subtract up to 10%.</h4>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:1%"> Now, armed with your revised stock and bond allocations, you must make one last leap—the leap from theory to practice. Projecting investment returns befuddles even the smartest, most detail-conscious analysts. Except in rare circumstances, you just can’t predict the movements of the market. Going forward, our best estimate for long-term investment returns lies in the past.</h4>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:1%">While previous examples have used average returns for clarity, here you must rely on annualized returns. And over the long haul, large-company stocks have managed annualized returns of about 10%, long-term government bonds just over 6%, and Treasury bills about 3.5%.</h4>
            <div style="margin-left: 10%; margin-right: 10%;  ">
                <el-row class="bordered-row">
                    <h4 style="margin-left: 1%; margin-right: 1%;  margin-top:1%">Why Use Annualized Returns?</h4>
                    <p style="margin-left:1%; margin-right: 1%;  margin-top:1%">Annualized returns assume steady growth with no variations, and they will always lag the average annual return. In real life, investment returns vary from year to year, and the greater the variance, the greater the difference between average and annualized returns. For example:</p>
                    <p  style="margin-left:1%; margin-right: 1%;  margin-top:1%"><em style="font-weight: bold;">·  The perfect world. </em> Invest $100 at exactly 10% this year and next year, and you’ll have $121 at the end of two years. That’s a two-year annualized return of 10%, and an average return of 10%.</p>
                    <p  style="margin-left:1%; margin-right: 1%;  margin-top:1%"><em style="font-weight: bold;">·  Messy reality.  </em> Invest $100 at a negative 20% this year and a positive 51% next year, and you’ll have $121. That’s a two-year annualized return of 10%, but an average return of more than 15%. A return of negative 35% for the first year and a positive 86% for the second year also gets you to $121, but with an average annual return of more than 25%.
                        Annualized returns tell a truer story. Since estimating the variance in annual returns over long periods is simply impossible, most long-term forecasts assume annualized returns.</p>                 
                </el-row>
            </div>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:1%"> While it takes a lot of work to calculate annualized portfolio returns, those three historical returns allow you to approximate the annual returns you can earn using large-company stocks, long-term government bonds, and short-term government bonds. Suppose your target allocation is 70% stocks and 30% bonds. The target annualized return of your portfolio is then 8.8%. Here’s how to get there: See next part.</h4>
        </el-row>
        
        <el-row style="background: #F5EFE0;border-radius: 30px; margin-top:1%; margin-left: 3%; margin-right: 3%;"> 
            <h2 style="margin-left: 3%;  margin-top:2%">Video part</h2>
            <el-card style="margin-left: 20%;margin-right: 20%;" >
            <iframe style=" height:400px;width:800px"
                :src="videoEmbedCode"
                frameborder="0"
                allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture"
                allowfullscreen
            ></iframe>
            </el-card>
            
                        
            <el-row class="source-text">
            <span>Title: How to Build a Rock-Solid Investment Portfolio</span>
            </el-row>
            <el-row class="source-text">
            <span>Author: Humphrey Yang</span>
            </el-row>
            <el-row class="source-text">
                Source: <a v-bind:href="linkUrl">https://youtu.be/4o46u3Bs3-4</a>
            </el-row>

        </el-row>
        <el-row style="margin-left: 4%; margin-right: 4%;margin-top:1%">
            <el-col :span="12" >
                <el-button  @click="Goback" type="warning" style="color: black; font-size:25px; border-radius: 50px; width:150px;height:60px" >Back</el-button>
            </el-col>
            <el-col :span="12" style="text-align: right; " >
                <el-button @click="Gotest" type="warning" style="color: black; font-size:25px; border-radius: 50px; width:150px;height:60px" >Next</el-button>
            </el-col>
        </el-row>



        
    </div>
</template>


<script>
import axios from "axios";
export default {
  data() {
    return {
      videoEmbedCode: 'https://www.youtube.com/embed/4o46u3Bs3-4',  
    };
  },
  methods:{
      Gotest(){
          this.$router.push('/chapter4.7')
      },
      Goback(){
          this.$router.push('/chapter4')
      }
  },
    created(){
        
            var userid = this.$store.state.accountid;
            var chapterid = 4;
            var subchapterindex = 6;
            console.log(userid);
            console.log(chapterid);
            console.log(subchapterindex);
            var record = {};
            record.userid = userid;
            record.chapterid = chapterid;
            record.subchapterindex = subchapterindex;

            axios.post("http://127.0.0.1:8088/knowledge/recordcheck", record).then(res => {
                                console.log(res.data)}).finally(()=>{

                                });
        }, 
    computed: {
    linkUrl() {
      // return the URL for the link
      return 'https://youtu.be/4o46u3Bs3-4';
    }
    }
  
};

</script>


<style>
.chapterbox{
    background:#F5EFE0;
    border-radius: 30px; 
    height: 150px; 
    margin-top:1%; 
    margin-left: 3%; 
    margin-right: 3%;
    

}
.source-text{
    margin-left: 3%;
    margin-right: 3%;
}
.bordered-row {
  border: 1px solid #ccc;
  padding: 10px;
}
.container {
    width: 50%;
    height: 500px;
    display: flex;
    justify-content: center;
    align-items: center;
}
.image {
    max-width: 100%;
    max-height: 100%;
    background-color: transparent;
}
</style>
