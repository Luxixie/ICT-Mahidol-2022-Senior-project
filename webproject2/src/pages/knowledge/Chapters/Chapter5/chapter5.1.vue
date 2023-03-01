<template>
    <div>
        <el-row class="chapterbox" >
            <h2 style="margin-left: 3%;  margin-top:4%"> 01 How to Read Stock Charts for Beginners (1)</h2>
            <h2 style="margin-left: 3%;  margin-top:4%; color:gray">Written by Chris Muller | Modified date: Dec. 24, 2022</h2>
        </el-row>
        <el-row style="background: #F5EFE0;border-radius: 30px;margin-top:1%; margin-left: 3%; margin-right: 3%;" >
            <h2 style="margin-left: 3%;  margin-top:2%">What exactly is a stock chart, and how does it help you analyze stocks?</h2>
            <el-card style="margin-left: 20%;margin-right: 20%;" >
                <iframe style=" height:400px;width:800px"
                    :src="videoEmbedCode"
                    frameborder="0"
                    allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture"
                    allowfullscreen
                ></iframe>
            </el-card>
            <el-row class="source-text">
            <span>Title: How to analyze stocks: The basics of reading a stock chart (Recap)</span>
            </el-row>
            <el-row class="source-text">
            <span>Author: Money Under 30</span>
            </el-row>
            <el-row class="source-text">
                Source: <a v-bind:href="linkUrl">https://youtu.be/jX75o5BOZnc</a>
            </el-row>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:1%">Simply put, a stock chart is a graph that shows you the price of a stock over a specific period of time — for example, five years. More advanced stock charts will show additional data, and by understanding the basics you can pull out a lot of information about a stock’s historic, current, and expected performance.</h4>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:1%">Now let’s take a look at a typical stock chart. For the sake of this article, let’s use Apple as an example stock, as displayed on Yahoo! Finance.</h4>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:1%">If you don’t already know, the series of letters after the name of the company is the ticker symbol. It identifies the company on the stock exchange.</h4>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:1%">In this case, I’ll search for AAPL, which is Apple’s ticker symbol. This is what we get:</h4>
            <el-row :span="2" class="container" style="margin-top:3%;margin-left:25%">
                    <img src="./images/2.png" class="image" />
            </el-row>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:1%"> Next, click the ‘Full screen’ link in the top right corner of the chart to expand it.</h4>
            <el-row :span="2" class="container" style="margin-top:3%;margin-left:25%">
                    <img src="./images/3.png" class="image" />
            </el-row>
            
            
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:1%">I’ve also taken the liberty of filtering to the last 15 years, which you can easily do by changing the date range near the top of the expanded chart.</h4>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:1%">So here we’re looking at the last 15 years of Apple’s stock. I bet you wish you would have invested in Apple in late 2008/early 2009!</h4>
            <h4 style="margin-left: 3%; margin-right: 3%;  margin-top:1%">Now let’s dive into the different pieces and parts of the stock chart so you can begin to read one like a pro.</h4>
        
        <h2 style="margin-left: 3%;  margin-top:2%">Key concepts when learning how to read a stock chart</h2>
            <p style="margin-left: 3%; margin-right: 3%;  margin-top:1%">A stock chart becomes particularly useful when you know how to read its information and decipher what it’s showing </p>
            <p style="margin-left: 3%; margin-right: 3%;  margin-top:1%">Here are the four key data points you need to understand in order to fully leverage the power of a stock chart. </p>
            <h2 style="margin-left: 3%;  margin-top:2%">1. Identify the trendline</h2>
            <el-row :span="2" class="container" style="margin-top:3%;margin-left:25%">
                    <img src="./images/4.png" class="image" />
            </el-row>
            <p style="margin-left: 3%; margin-right: 3%;  margin-top:1%">This is that blue line you see every time you hear about a stock — it’s either going up or down, right? While the trendline seems like common sense, there are a few things I want to call out so you can understand it in a little more detail.</p>
            <p style="margin-left: 3%; margin-right: 3%;  margin-top:1%">First, know that stocks will take huge dives and also make huge climbs. Don’t react to large drops or huge gains in a positive or negative way. You should be using this piece of the stock chart merely to see what’s going on.</p>
            <p style="margin-left: 3%; margin-right: 3%;  margin-top:1%">In fact, the trendline should lead you to dig further. For instance, Apple as a company really took off from 2009 to 2012.</p>
            <p style="margin-left: 3%; margin-right: 3%;  margin-top:1%">But what happened from 2012 to 2013? The stock began to sink — at one point, shares were down more than 40%!</p>
            <p style="margin-left: 3%; margin-right: 3%;  margin-top:1%">This is where your trendline comes in handy. News comes and goes, but when news coincides with a dramatic shift in the trendline, it’s something to pay attention to.</p>
            <p style="margin-left: 3%; margin-right: 3%;  margin-top:1%">If you saw something like this happen, I’d urge you to find out what’s going on with the company. Most strong companies can rebound from hits like this, but not all can.</p>

            <p style="margin-left: 3%; margin-right: 3%;  margin-top:1%">For those who don’t know, right around this time Apple experienced a few major shifts:</p>
            <p style="margin-left: 3%; margin-right: 3%;  margin-top:1%">First, its longtime CEO, Steve Jobs, resigned in 2011. Then around 2012, Apple noted that its profit margins were significantly decreasing, despite a growing smartphone market. Finally, they were trying to expand the smartphone into developing countries, where they were just too expensive to compete.</p>
            <p style="margin-left: 3%; margin-right: 3%;  margin-top:1%">These factors, combined with plenty of other variables, contributed to the stock price falling.</p>
            <p style="margin-left: 3%; margin-right: 3%;  margin-top:1%">But new CEO Tim Cook made some strategic moves with the company to turn it around, and the rest of the trendline shows that.</p>
            <p style="margin-left: 3%; margin-right: 3%;  margin-top:1%">The lesson here is to use your trendline as a first-glance, high-level indicator of something to look into.</p>
            
            <h2 style="margin-left: 3%;  margin-top:2%">2. Look for lines of support and resistance</h2>
            <p style="margin-left: 3%; margin-right: 3%;  margin-top:1%">Next, you’ll want to identify lines of support and resistance. A line of support is a price that a stock is unlikely to drop below, while a line of resistance is one that it’s unlikely to go above. That is, until some major change occurs, such as a reduced profit margin.</p>
            <p style="margin-left: 3%; margin-right: 3%;  margin-top:1%">Think of these lines as bumpers at a bowling alley. When you’re bowling, the ball bounces back and forth between these inflated barriers.</p>
            <p style="margin-left: 3%; margin-right: 3%;  margin-top:1%">A stock’s price does the same thing within these lines of support and resistance.</p>
            <p style="margin-left: 3%; margin-right: 3%;  margin-top:1%">The goal here is to know when to buy and when to sell. Let’s take a look at Apple’s stock chart again to see an example:</p>
            <el-row :span="2" class="container" style="margin-top:3%;margin-left:25%">
                    <img src="./images/5.png" class="image" />
            </el-row>
            <p style="margin-left: 3%; margin-right: 3%;  margin-top:1%">These are subjective and interpreted differently by everyone, but the process is important. Note that everyone will draw lines of resistance and support differently, depending on their investment horizon (how long they plan to hold the stock).</p>
            <p style="margin-left: 3%; margin-right: 3%;  margin-top:1%">So, if you plan on holding it for a long time, you may not draw as many lines of support and resistance, because you don’t care as much about the ups and downs. But if you’re a short-term investor, you may draw more to analyze trends during a shorter period.</p>
            <p style="margin-left: 3%; margin-right: 3%;  margin-top:1%">Let me break down the image above with each of the trendlines:</p>
            <p style="margin-left: 3%; margin-right: 3%;  margin-top:1%">· Line A is the very first line of support shown. Based on trends prior to this, you can feel comfortable that the stock price won’t go below this point.</p>
            <p style="margin-left: 3%; margin-right: 3%;  margin-top:1%">· Line B is my first line of resistance. You can see that the stock has peaked at that point for now and you shouldn’t expect it to go higher.</p>
            <p style="margin-left: 3%; margin-right: 3%;  margin-top:1%">· As you can see with Line C, the stock has peaked again, thus creating another line of resistance.</p>
            <p style="margin-left: 3%; margin-right: 3%;  margin-top:1%">· Line D shows the stock price has bottomed out again, creating a line of support.</p>
            <p style="margin-left: 3%; margin-right: 3%;  margin-top:1%">· The price peaks again with Line E, and the trend continues as time goes on.</p>
            <p style="margin-left: 3%; margin-right: 3%;  margin-top:1%">If it seems complex, don’t fret. It is. And a lot of it is guesswork.</p>
            <p style="margin-left: 3%; margin-right: 3%;  margin-top:1%">Knowing the lines of resistance can help you decide when to buy or sell a stock. Remember, though, that it’s subjective and it won’t give you a clear-cut road map on exactly what to do. You’ll have to use some of your own analysis and judgment.</p>

            

            <h2 style="margin-left: 3%;  margin-top:2%">3. Know when dividends and stock splits occur</h2>
            <p style="margin-left: 3%; margin-right: 3%;  margin-top:1%">At the bottom of the chart, you’ll see if and when the company issued a dividend, as well as if there was ever a stock split:</p>
            <el-row :span="2" class="container" style="margin-top:3%;margin-left:25%">
                    <img src="./images/6.png" class="image" />
            </el-row>
            <p style="margin-left: 3%; margin-right: 3%;  margin-top:1%">A dividend is when the company (the board of directors) decides to give a portion of its earnings back to its shareholders.  If you own the stock, you get a small chunk of the profit.</p>
            <p style="margin-left: 3%; margin-right: 3%;  margin-top:1%">Some companies issue dividends, some don’t. Just because a company does or doesn’t issue a dividend doesn’t mean it’s not worth investing in. There are plenty of other factors to consider.</p>
            <p style="margin-left: 3%; margin-right: 3%;  margin-top:1%">Some companies just prefer to focus on growth, so they’ll reinvest their earnings as opposed to giving them back to the shareholders. Other companies (like Apple) can pay dividends without sacrificing growth.</p>
            <p style="margin-left: 3%; margin-right: 3%;  margin-top:1%">As you can see by the image, Apple started issuing quarterly dividends to its shareholders midway through 2012.</p>
            <p style="margin-left: 3%; margin-right: 3%;  margin-top:1%">You can also see that there were stock splits in 2014 and 2020. A stock split is a strategic move done by the company’s board of directors to issue more shares of stock to the public.</p>
            <p style="margin-left: 3%; margin-right: 3%;  margin-top:1%">In 2014, Apple did a seven to one stock split (noted as 7:1), which means that for every share of AAPL you owned prior to the split, you’d now have seven. So if you owned 100 shares of APPL prior to the split, you’d now have 700.</p>
            <p style="margin-left: 3%; margin-right: 3%;  margin-top:1%">The value of the company doesn’t change, but the share price might. Companies will often do this if the price isn’t in line with competitors or to attract smaller investors (if the share price decreases).</p>
            <p style="margin-left: 3%; margin-right: 3%;  margin-top:1%">You can see the uptick in the trendline after the split occurred, too. Many times when a stock split happens, more people invest (since the share price is often lower) which increases demand and, in many cases, the overall share price.</p>
        


            <h2 style="margin-left: 3%;  margin-top:2%">4. Understand historic trading volumes</h2>
            <p style="margin-left: 3%; margin-right: 3%;  margin-top:1%">At the very bottom of the chart, you can see many small, vertical lines. This is a trend of the volumes at which the stock is traded.</p>
            <p style="margin-left: 3%; margin-right: 3%;  margin-top:1%">Volumes are good to know, but shouldn’t be your only determining factor when buying a stock. Usually, trading volumes increase when there is major news (good or bad) about the company.</p>
            <p style="margin-left: 3%; margin-right: 3%;  margin-top:1%">When volumes are increasing, it can also shift the price of the stock quickly. Let’s look at an example:</p>
            
            <el-row :span="2" class="container" style="margin-top:3%;margin-left:25%">
                    <img src="./images/7.png" class="image" />
            </el-row>
            <p style="margin-left: 3%; margin-right: 3%;  margin-top:1%">In Line A, you can see there was a high volume of trading activity that corresponded with a drop in the stock price. There may have been news that day that caused people to panic (aside from the entire economy crashing that year).</p>
            <p style="margin-left: 3%; margin-right: 3%;  margin-top:1%">In Line B, you can see a slight uptick in trading volume that corresponds with an upward trend in the stock price.</p>
            <p style="margin-left: 3%; margin-right: 3%;  margin-top:1%">Don’t always assume there will be a correlation between stock price and trading volume, but it’s good to know what the volumes have been in the past and what they are currently before making a decision.</p>
            <p style="margin-left: 3%; margin-right: 3%;  margin-top:1%">With high volumes comes greater ease when buying or selling. If a lot of people are trading the stock that day, you should be able to buy or sell it quickly.</p>


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
export default {
  data() {
    return {
      videoEmbedCode: 'https://www.youtube.com/embed/jX75o5BOZnc',  
    };
  },
  methods:{
      Gotest(){
          this.$router.push('/chapter5.2')
      },
      Goback(){
          this.$router.push('/chapter5')
      }
  },
    computed: {
    linkUrl() {
      // return the URL for the link
      return 'https://youtu.be/jX75o5BOZnc';
    }
    }
  
};

</script>


<style>
.chapterbox{
    background:#F5EFE0;
    border-radius: 30px; 

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
