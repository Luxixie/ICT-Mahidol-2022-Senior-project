<template>
    <div id="forgetpassword-div">
        <el-row>
            <el-col id="forgetpassword-title-col" :span="24" :offset="10">
                <h1 id="forgetpassword-title">Password Recovery</h1>
            </el-col>
        </el-row>
        <el-row>
            <el-col id="forgetpassword-title-info" :span="24" :offset="9">
                <span >Enter your account's email address to recover your password</span>
            </el-col>
        </el-row>
        <el-form id="forgetpassword-form" ref="form" :model="form">
            <el-form-item label="Email Address" style="font-weight: bold; color: aliceblue;">
                <el-input id="forgetpassword-input" placeholder="Email Address" v-model="form.name"></el-input>
            </el-form-item>
            <el-form-item>
                <el-button round type="warning" @click="Tryforgetpassword" style="width: 45%; margin-left: 25%; float: left;">Send Email</el-button>
             
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
            }
        }
    },
    methods: {
        Tryforgetpassword() {
            console.log('submit!');
            this.$router.push('/sendemail')
        },
        GoRegisterPage() {
            console.log('submit!');
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
}




#forgetpassword-form {
    margin-left: 38%;
    margin-right:38%;
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