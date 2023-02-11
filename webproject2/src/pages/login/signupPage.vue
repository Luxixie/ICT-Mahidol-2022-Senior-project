<template>
    <div style="margin-top: 5%;">
        <el-row>
            <el-col :span="12" :offset="10">
                <h1 style="color: #f5efe0;">Register your Account</h1>
            </el-col>
        </el-row>
        <el-form id="regist-form" ref="form" :model="form">
            <el-form-item >
                <el-input id="regist-input" placeholder="First Name" v-model="form.firstname"
                    style="width: 40%;"></el-input>
                <el-input id="regist-input" placeholder="Last Name" v-model="form.lastname"
                    style="width: 40%; float: right;"></el-input>
            </el-form-item>
            <el-form-item>
                <el-input id="regist-input" placeholder="Region" v-model="form.region" style="width: 40%;"></el-input>
                <!-- <el-input id="regist-input" placeholder="Birth Date" v-model="form.name" ></el-input> -->
                <el-date-picker  id="regist-input" style="width: 40%; float: right;" v-model="form.bod" type="date" placeholder="Birth Date">
                </el-date-picker>
            </el-form-item>
            <el-form-item>
                <el-input id="regist-input" placeholder="Email" v-model="form.email"></el-input>
            </el-form-item>
            <el-form-item>
                <el-input id="regist-input" placeholder="Password" v-model="form.password"></el-input>
            </el-form-item>

            <el-form-item>
                <el-input id="regist-input" placeholder="Confirm Password" v-model="form.confirmpassword"></el-input>
            </el-form-item>
            <el-form-item>

            </el-form-item>
            <el-form-item>
                <el-button round type="warning" @click="CreateUser" style="width: 45%; margin-left: 25%;">Create User</el-button>

            </el-form-item>
        </el-form>
    </div>
</template>
<script>
import axios from 'axios'
export default {
    data() {
        return {
            form: {
                firstname: '',
                lastname: '',
                region: '',
                bod: '',
                email: '',
                password: '',
                confirmpassword: ''
            },
           
        }
    },
    methods: {
        CreateUser() {
            axios.post('http://127.0.0.1:8088/signup', this.form).then(res => {
                        console.log(res.data)
                        if (res.data.state == 1) {
                            alert('success');
                            //跳转到主页
                            this.$router.replace('/login');
                        } else {
                            alert('Incorrect user name or password!');
                            return false;
                        }
                    });
        }
    }
}
</script>

<style>
.login-bt {
    margin-left: 30px;
}

#regist-input {
    background: #1f3d70;
    border-color: #1f3d70;
    border-radius: 100px;
    color: #f5efe0;
}

#regist-form {
    margin-left: 30%;
    margin-right: 30%;
}

#login-div {
    margin-top: 8%;
}

#login-title {
    color: wheat;
    font-size: 40px;
}

#login-title-col {
    margin-bottom: 60px;
}
</style>