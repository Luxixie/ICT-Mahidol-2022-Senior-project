<template>
    <div style="margin-top: 5%;">
        <el-row>
            <el-col :span="12" :offset="10">
                <h1 style="color: #f5efe0;">Regist your Account</h1>
            </el-col>
        </el-row>
        <el-form id="regist-form" ref="form" :model="form">
            <el-form-item>
                <el-input id="regist-input" placeholder="Firest Name" v-model="form.name"
                    style="width: 40%;"></el-input>
                <el-input id="regist-input" placeholder="Last Name" v-model="form.name2"
                    style="width: 40%; float: right;"></el-input>
            </el-form-item>
            <el-form-item>
                <el-input id="regist-input" placeholder="Region" v-model="form.region" style="width: 40%;"></el-input>
                <!-- <el-input id="regist-input" placeholder="Birth Date" v-model="form.name" ></el-input> -->
                <el-date-picker  id="regist-input" style="width: 40%; float: right;" v-model="value1" type="date" placeholder="Birth Date">
                </el-date-picker>
            </el-form-item>
            <el-form-item>
                <el-input id="regist-input" placeholder="Email" v-model="form.email"></el-input>
            </el-form-item>
            <el-form-item>
                <el-input id="regist-input" placeholder="Password" v-model="form.password"></el-input>
            </el-form-item>

            <el-form-item>
                <el-input id="regist-input" placeholder="Confirm Password" v-model="form.password"></el-input>
            </el-form-item>
            <el-form-item>

            </el-form-item>
            <el-form-item>
                <el-popover placement="bottom" title="Opening test" width="800" trigger="click" >
                <el-button slot="reference" round type="warning" style="width: 45%; margin-left: 25%;">Create User</el-button>
                <en-row>
                    <span>Do you want to learn some stock knowledge first?</span>
                </en-row>
                <en-row>
                    <en-col>
                        <el-button @click = "Tryopentest">YES</el-button>
                    </en-col>
                    <en-col>
                        <el-button  @click = "TryLogin">NO</el-button>
                    </en-col>
                </en-row>
                
                </el-popover>
            </el-form-item>
        </el-form>
    </div>
</template>
<script>
export default {
    data() {
        return {
            form: {
                name: '',
                name2:'',
                region: '',
                date1: '',
                date2: '',
                delivery: false,
                type: [],
                resource: '',
                desc: '',
                password:''
            },
            value1: '',
            visible: false,

        }
    },
    methods: {
        TryLogin() {
            console.log('submit!');
            this.$router.push('/home2')
        },
        GoRegisterPage() {
            console.log('submit!');
        },
        Tryopentest(){
            console.log('sussce');
            this.$router.push('/opentest')
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