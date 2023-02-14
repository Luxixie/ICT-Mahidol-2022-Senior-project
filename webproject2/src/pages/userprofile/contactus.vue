<template>
  <div>
    <el-col :span="10" style=" background:#F5EFE0;
                    border-radius: 30px; 
                    height: 1200px; 
                    margin-top:3%; 
                    margin-left: 3%; 
                    margin-right: 10%;
                    ">
        <h3 style="margin-top:3%; margin-left: 3%; "> SP2022-39 </h3>
        <h3 style="margin-top:3%; margin-left: 3%; "> A WEB APPLICATION FOR VIRTUAL STOCK TRADING </h3>
        <h3 style="margin-top:3%; margin-left: 3%; "> B.Sc.(INFORMATION AND COMMUNICATION TECHNOLOGY) </h3>
        <h3 style="margin-top:3%; margin-left: 3%; "> PROJECT ADVISOR: ASST, PROF. DR. SONGSRI TANGSRIPAIROJ  </h3>
        <h3 style="margin-top:3%; margin-left: 3%; ">ABSTRACT </h3>
        <h4 style="margin-top:3%; margin-left: 3%;margin-right: 3%; ">As the concept of stock investment becomes more popular, it has become a common way to earn passive income through stock trading. However, many novice investors need more practical experience and knowledge to invest in the stock market safely and sensibly. With this issue in mind, the objective of this project is to provide a tool to support novice investors by creating a realistic trading environment, imparting stock knowledge, and accumulating practical experiences. Therefore, a web application for a virtual stock trading simulation platform titled “Stock Plenty” has been designed and developed. The application encompasses four significant modules, including stock market information, buy and sell, stock knowledge, and user performance evaluation. </h4>
        <h3 style="margin-top:3%; margin-left: 3%; ">Partner</h3>
        <ul>
        <li v-for="partner in partners" :key="partner.id">
            <h4>{{ partner.name }}</h4>
            <p>{{ partner.description }}</p>
            <img  style="width:70px" :src="partner.logo" :alt="partner.name + ' logo'" />
        </li>
        </ul>
    </el-col>

    <el-col :span="5" style=" background:#F5EFE0;
                    border-radius: 30px; 
                    height: 400px; 
                    width:500px;
                    margin-top:10%; 
                    margin-right: 10%;
                    ">
        <h3 style="margin-top:3%;margin-left:3%">Contact Us</h3>
        <h3 style="margin-top:3%;margin-left:3%">We can help. Our team will give you the beat sugesstion! Leave you idea and problem.</h3>

        <el-form  :label-position="labelPosition" label-width="80px" :model="form">
            <el-form-item label="Name:">
                <el-input v-model="form.name"></el-input>
            </el-form-item>
            <el-form-item label="Email:">
                <el-input v-model="form.email"></el-input>
            </el-form-item>
            <el-form-item label="Message:">
                <el-input type="textarea" v-model="form.message"></el-input>
            </el-form-item>
            <el-form-item>
                <el-button type="primary" @click="submitForm">Submit</el-button>
            </el-form-item>
        </el-form>
    </el-col>

  </div>
</template>

<script>
export default {
  data() {
    return {
        labelPosition: 'right',
        form: {
          name: '',
          email:'',
          message:'',
        },
        partners: [
            {
            id: 1,
            name: 'Mr. Viphob Lertkulthum',
            description: 'ID: 6288186, from Computer Network',
            logo:'https://www.disneyclips.com/images5/images/duffy-the-bear.png'
            },
            {
            id: 2,
            name: 'Miss. Luxi Xie',
            description: 'ID: 6288203, from Computer Network ',
            logo: 'https://www.disneyclips.com/images6/images/bunny2.gif'
            },
            {
            id: 3,
            name: 'Mr. Yuanqin Yang',
            description: 'ID:6288205, from E-Business',
            logo: 'https://www.disneyclips.com/images2/images/june2014.gif'
            }
        ]
        }
    },
    methods: {
        submitForm() {
            console.log('Name: ', this.name)
            console.log('Email: ', this.email)
            console.log('Message: ', this.message)
        }
    }
}
</script>
