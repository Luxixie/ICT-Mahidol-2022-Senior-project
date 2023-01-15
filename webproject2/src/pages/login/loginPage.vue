<template>
    <div id="login-div">
        <el-row>
            <el-col id="login-title-col" :span="12" :offset="11">
                <h1 id="login-title">Log in</h1>
            </el-col>
        </el-row>
        <el-form id="login-form" ref="form" :model="form">
            <el-form-item>
                <el-input id="login-input" placeholder="User Name or User ID" v-model="form.username"></el-input>
            </el-form-item>
            <el-form-item style="margin-bottom: 0px;">
                <el-input id="login-input" placeholder="Password" show-password v-model="form.password" ></el-input>
            </el-form-item>
            <el-form-item style="margin: 0px; padding: 0px;">
                <router-link  to='./signup' style="float: right; color: white;">Forget Password?</router-link>
            </el-form-item>
            <el-form-item>
                <el-button round type="warning" @click="TryLogin" style="width: 45%; float: left;">Login</el-button>
                <el-button class="login-bt" round @click="GoRegisterPage" style="width: 45%; float:right;">Register</el-button>
            </el-form-item>
        </el-form>
    </div>
</template>
<script>
export default {
    data() {
        return {
            form: {
                username: '',
                password: '',
    
            }
        }
    },
    methods: {
        TryLogin() {
            this.$router.push("/")
        },
        GoRegisterPage() {
            console.log('submit!');
        }
    }
}
</script>

<style>
.login-bt{
 margin-left: 30px;
}
#login-input {
    background: #1f3d70;
    border-color: #1f3d70;
    border-radius: 100px;
    color: #f5efe0;
}




#login-form {
    margin-left: 38%;
    margin-right:38%;
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