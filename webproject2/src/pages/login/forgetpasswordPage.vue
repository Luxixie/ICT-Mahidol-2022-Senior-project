<template>
    <div id="forgetpassword-div">
        <el-row>
            <el-col id="forgetpassword-title-col" :span="24" :offset="9">
                <h1 id="forgetpassword-title">Password Recovery</h1>
            </el-col>
        </el-row>
        <el-row>
            <el-col id="forgetpassword-title-info" :span="24" :offset="8">
                <span >Enter your account's email address to recover your password</span>
            </el-col>
        </el-row>
        <el-row>
             <el-input id="forgetpassword-input" placeholder="Email Address" v-model="email" type="email"></el-input>
        </el-row>
        <el-row :span="8">
            <el-button round type="warning" style="width: 15%; margin-left: 40%;margin-top:2%" @click="Useremail">Send Email</el-button>
        </el-row>

    </div>
</template>

<script>
import axios from 'axios'
export default {
    data() {
        return {
            email: '',

        }
    },
    methods: {
        Useremail() {
            const email = this.email
            
            axios.post('http://127.0.0.1:8088/forgetpassword/'+email).then(res => {
                        console.log('Email data sent successfully');
                        this.$router.replace('/new'); 
                    })
                    .catch(error => {
                    console.error('Error sending email data:', error);
                    });

    }
    }
}
</script>

<style>
.forgetpassword-bt{
 margin-left: 30px;
}
#forgetpassword-input {
    background: #1f3d70;
    border-color: #1f3d70;
    border-radius: 100px;
    color: #f5efe0;
    width: 30%;
    margin-left:33% ;
    margin-top: 1%;
}




#forgetpassword-div {
    margin-top: 8%;
}

#forgetpassword-title {
    color: #f5efe0;
    font-size: 30px;
}

#forgetpassword-title-info {
  margin-bottom: 3%;
  color: #f5efe0;
}
</style>