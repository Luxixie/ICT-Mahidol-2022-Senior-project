<template>
    <div id="newpassword-div">
        <el-row>
            <el-col id="newpassword-title-col" :span="24" :offset="10">
                <h1 id="newpassword-title">Reset Password</h1>
            </el-col>
        </el-row>
        <el-row>
            <el-col id="newpassword-title-info" :span="24" :offset="9">
                <span >Choose a new password for your account.</span>
            </el-col>
        </el-row>
        <el-form id="newpassword-form" ref="form" :model="form">
            <el-form-item>
                <el-input id="newpassword-input" placeholder="Password" v-model="form.password"></el-input>
            </el-form-item>
            <el-form-item>   
                <el-input id="newpassword-input" placeholder="Confirm Password" v-model="form.password2"/>
            </el-form-item>
            <el-form-item>
                <el-button round type="warning" @click="completepassword" style="width: 45%; margin-left: 25%; float: left;">submit</el-button>
             
            </el-form-item>
        </el-form>
    </div>
</template>
<script>
export default {
    data() {
        return {
            form: {
                password:'',
                password1:''
            }
        }
    },
    methods: {
        completepassword() {
            console.log('submit!');
            this.$router.push('/completeresetpassword')
        }
    }
}
</script>

<style>
.newpassword-bt{
 margin-left: 30px;
}
#newpassword-input {
    background: #1f3d70;
    border-color: #1f3d70;
    border-radius: 100px;
    color: #f5efe0;
}

#newpassword-form {
    margin-left: 38%;
    margin-right:38%;
}

#newpassword-div {
    margin-top: 8%;
}

#newpassword-title {
    color: #f5efe0;
    font-size: 30px;
}

#newpassword-title-info {
  margin-bottom: 3%;
  color: #f5efe0;
}
</style>