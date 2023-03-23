<template>
<div>
    <el-row id="knowledgehome-title">
      <el-col :span="8" :offset="9" class="text">
        <span>Stock knowledge</span>
      </el-col>
      <el-col :span="18" :offset="7">
        <h3>The hard part isn’t making the decision. It’s living with it.</h3>
      </el-col>
    </el-row>

    <el-row style="background: #f6f7e4; height: 50px; ">
      <el-tabs v-model="activeName" @tab-click="handleClick" style="margin-left:3%;font-size:32px">
        <el-tab-pane label="Basic Knowledge" name="first"></el-tab-pane>
        <el-tab-pane label="Starter Guide" name="second"></el-tab-pane>

      </el-tabs>
    </el-row>
    <el-row :span="8" :offset="3" style="background:gray;margin-top:2%">
        <span style="font-size:35px;color: #f6f7e4;margin-left:5%">Starter Guide</span>
    </el-row>
    <el-row style="font-size:20px;color: #f6f7e4;margin-left:5%;margin-right:5%">
        <p>Dear User:</p>
        <p>Thank you for choosing to use our website to learn about and simulate stock trading.</p>
        <p>First of all, you can use our website to view information about stocks and learn about stocks without registering. Then,when you have finished registering your account, you will have <span style="color:red" >20,000 baht</span> in virtual funds. If you need to increase your virtual funds, you can change your expected funds in your "user profile".</p>
    </el-row>
    <el-row :span="8" class="container" style=";margin-left:15%">
        <img src="./images/8.png" class="image" >
    </el-row>
    <el-row style="font-size:20px;color: #f6f7e4;margin-left:5%;margin-right:5%">
        <p>1.Market Information: </p>
        <p>On this page, you can get the stock price change chart, a data summary, and a company profile. You can also use the filter to filter the stock price for a year.</p>
        <p style="color:yellow">(In order for you to buy and sell in a more professional way, we suggest you learn Chapters 1–3.)</p>
        <p>2. Stock Knowledge:</p>
        <p>1) The Knowledge section covers six basics about stocks, from introducing them to how to buy and sell them.</p>
        <p>2) The website will record your learning progress at the same time. You can check the knowledge homepage or check the specific learning time in the Personal Information section.</p>
        <p>With the exception of chapters 1 and 5, which do not have a quiz, the other chapters include a quiz, and you have the option to complete the exercises or move on to the next chapter when you are done studying. You can check quiz history in the Personal Information section.</p>
        <p>3. Buy and Sell:</p>
        <p>Virtual funds will be used to trade stocks on the "buy and sell" page. Our trading hours are synchronized with the stock trading hours in Thailand.</p>
        <p style="color:yellow">(In order for you to buy and sell in a more professional way, we suggest you learn Chapters 4-6.)</p>
        <p>4. Portfolio: </p>
        <p>You can check your purchase and sale records and see how much you have left on the "portfolio" page.</p>
        <p style="color:yellow">(In order for you to buy and sell in a more professional way, we suggest you learn Chapter 4.)</p>
        <p></p>
        <p>How do you have any ideas that you would like us to improve, you can leave us a message through the setting "contact us".</p>
        <p>Thank you for using our service.</p>
        <p>Best Regards,</p>
        <p>Stock Plenty Team</p>



    </el-row>

</div>
    
</template>


<script>

</script>


<style>
.container {
    width: 70%;
    height: 600px;
    display: flex;
    justify-content: center;
    align-items: center;
}
.image {
    max-width: 100%;
    max-height: 100%;
    background-color: transparent;
}
#title {
  background: #fbf9f6;
}

#knowledgehome-title {
  background: #fbf9f6;
}

#knowledgehome-tabs {
  background: #f6f7e4;
}

.text {
  font-size: 60px;
}

</style>