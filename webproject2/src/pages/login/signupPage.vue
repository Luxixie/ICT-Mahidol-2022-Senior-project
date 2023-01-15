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
                <el-input id="regist-input" placeholder="Last Name" v-model="form.name"
                    style="width: 40%; float: right;"></el-input>
            </el-form-item>
            <el-form-item>
                <el-input id="regist-input" placeholder="Region" v-model="form.name" style="width: 40%;"></el-input>
                <!-- <el-input id="regist-input" placeholder="Birth Date" v-model="form.name" ></el-input> -->
                <el-date-picker  id="regist-input" style="width: 40%; float: right;" v-model="value1" type="date" placeholder="Birth Date">
                </el-date-picker>
            </el-form-item>
            <el-form-item>
                <el-input id="regist-input" placeholder="Email" v-model="form.name"></el-input>
            </el-form-item>
            <el-form-item>
                <el-input id="regist-input" placeholder="Password" v-model="form.name"></el-input>
            </el-form-item>

            <el-form-item>
                <el-input id="regist-input" placeholder="Confirm Password" v-model="form.name"></el-input>
            </el-form-item>
            <el-form-item>

            </el-form-item>
            <el-form-item>
                <el-button round type="warning" @click="TryLogin" style="width: 45%; margin-left: 25%;">Create
                    User</el-button>

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
                region: '',
                date1: '',
                date2: '',
                delivery: false,
                type: [],
                resource: '',
                desc: ''
            },
            value1: ''

        }
    },
    methods: {
        TryLogin() {
            console.log('submit!');
        },
        GoRegisterPage() {
            console.log('submit!');
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