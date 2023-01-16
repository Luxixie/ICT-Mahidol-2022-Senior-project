<template>
    <div id="completeresetpassword-div">
        <el-row>
            <el-col id="completeresetpassword-title-col" :span="24" :offset="10">
                <h1 id="completeresetpassword-title">Password Recovery</h1>
            </el-col>
        </el-row>
        <el-row>
            <el-col id="completeresetpassword-title-info" :span="24" :offset="9">
                <span >Your password already changed! You can log into your account again </span>
            </el-col>
        </el-row>
        <el-row>
            <el-button round type="warning" @click="Backlogin" style="width: 20%; margin-left: 40%; float: left;">Log in</el-button>
        </el-row>
        
    </div>
</template>
<script>
export default {
    methods: {
        Backlogin() {
            console.log('submit!');
            this.$router.push('/login')
        }
    }
}
</script>

<style>
.completeresetpassword-bt{
 margin-left: 30px;
}

#completeresetpassword-div {
    margin-top: 8%;
}

#completeresetpassword-title {
    color: #f5efe0;
    font-size: 30px;
}

#completeresetpassword-title-info {
    margin-left: 40%;
    margin-bottom: 3%;
    color: #f5efe0;

}
</style>