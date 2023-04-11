<template>
  <div>
    <el-col :span="10" style=" background:#F5EFE0;
                    border-radius: 30px; 
                    margin-top:3%; 
                    margin-left: 3%; 
                    margin-right: 10%;
                    padding-bottom: 1%;
                    ">
        <h3 style="margin-top:3%; margin-left: 3%; "> SP2022-39 </h3>
        <h3 style="margin-top:3%; margin-left: 3%; "> A WEB APPLICATION FOR VIRTUAL STOCK TRADING </h3>
        <h3 style="margin-top:3%; margin-left: 3%; "> B.Sc.(INFORMATION AND COMMUNICATION TECHNOLOGY) </h3>
        <h3 style="margin-top:3%; margin-left: 3%; "> PROJECT ADVISOR: ASST, PROF. DR. SONGSRI TANGSRIPAIROJ  </h3>
        <h3 style="margin-top:3%; margin-left: 3%; ">ABSTRACT </h3>
        <h4 style="margin-top:3%; margin-left: 3%;margin-right: 3%; ">Stock is one of the common investment methods which offers a high return on investment. More and more people invest in stock to earn passive income. However, numerous novice investors are lack of knowledge and practical experiences to invest in the stock market safely and sensibly. With this issue in mind, the objective of this research project is to propose the design and development of a web application for virtual stock trading, called “Stock Plenty”. The Stock Plenty application provides several useful features for novice investors to learn and understand basic stock investment knowledge, search and view market information, practice on buy and sell stock in a simulated trading environment, and evaluate user performance. The Stock Plenty application can be beneficial for novice investors to have plenty knowledge, get familiar with stock trading process, and accumulate hands-on experiences. Therefore, they feel ready and more confident to trade stocks in the real market.
        </h4><h3 style="margin-top:3%; margin-left: 3%; ">Developers</h3>
        <ul>
        <li v-for="partner in partners" :key="partner.id">
            <h4>{{ partner.name }}</h4>
            <p>{{ partner.description }}</p>
            <img  style="width:30%" :src="partner.image" :alt="partner.name + ' Image'" />
        </li>
        </ul>
    </el-col>

    <el-col :span="5" style=" background:#F5EFE0;
                    border-radius: 30px; 
                    height: 450px; 
                    width:500px;
                    margin-top:10%; 
                    margin-right: 10%;
                    ">
        <el-button style="margin-left:3%;margin-top:3%" @click="Goposter"> See Our Poster</el-button>
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
import axios from 'axios'
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
            image:require("../userprofile/image/yyq.png")
            
            },
            {
            id: 2,
            name: 'Miss. Luxi Xie',
            description: 'ID: 6288203, from Computer Network ',
            image:require("../userprofile/image/xlx.png")
            },
            {
            id: 3,
            name: 'Mr. Yuanqin Yang',
            description: 'ID:6288205, from E-Business',
            image:require("../userprofile/image/yyq.png")
            }
        ]
        }
    },
    methods: {
        submitForm() {
            console.log('Name: ', this.form.name)
            console.log('Email: ', this.form.email)
            console.log('Message: ', this.form.message)
            var message = {
                Name: this.form.name,
                Email:this.form.email,
                Message:this.form.message
            }
            axios.post("http://127.0.0.1:8088/savemessage",message).then((res) => {
                this.$confirm('Thank you for your suggestions!', 'Thank you', {
                confirmButtonText: 'Next',
                type: 'success',
                center: true
            });
            })
        },
        Goposter(){
            this.$router.push('/poster')
        }
    },
    

}
</script>
