<template>
    <div id="sendemail-div">
        <el-row>
            <el-col id="sendemail-title-col" :span="24" :offset="10">
                <h1 id="sendemail-title">Password Recovery</h1>
            </el-col>
        </el-row>
        <el-row>
            <el-col id="sendemail-title-info" :span="24" :offset="9">
                <span >We just sent you an email containing further instructions.</span>
            </el-col>
        </el-row>
        <el-row>
            <el-button round type="warning" @click="Tryforgetpassword" style="width: 20%; margin-left: 40%; float: left;">Next</el-button>
        </el-row>
        
    </div>
</template>
<script>
export default {
    methods: {
        Tryforgetpassword() {
            console.log('submit!');
            this.$router.push('/newpassword')
        }
    }
}
</script>

<style>
.sendemail-bt{
 margin-left: 30px;
}

#sendemail-div {
    margin-top: 8%;
}

#sendemail-title {
    color: #f5efe0;
    font-size: 30px;
}

#sendemail-title-info {
    margin-left: 40%;
    margin-bottom: 3%;
    color: #f5efe0;

}
</style>