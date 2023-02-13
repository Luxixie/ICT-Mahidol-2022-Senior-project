<template>
    <div>
        <el-col :span="5" :offset="2" style=" margin-top:2%;">
            <el-row>
                <div style="margin-left:20%">
                    <el-avatar :size="200" :src="avatar"   />
                </div>
            </el-row> 

            
        </el-col>

        <el-col :span="10" :offset="1" style=" margin-top:2%">
            <el-row  :span="5" :offset="2" style="background: #1F3D70; border-radius: 50px;width: 200px;">
                <span style="margin-left:27%;font-family: 'Inter'; font-style: normal; font-weight: 400; font-size: 30px; line-height: 61px; color: #F5EFE0;">Profile</span>
            </el-row>
            <el-row :span="5" :offset="2" style="background: #1F3D70; border-radius: 50px;width: 200px; margin-top:5%">
                <span style="margin-left:25%;font-size: 25px;color: #F5EFE0;">Account</span>
            </el-row>
            <el-row  class="line">
                    <span class="line-text" >Account Id:</span> <span style="color: yellow; font-size:20px">{{ accountid }}</span>
            </el-row>
            <el-row  class="line">
                    <span class="line-text" >Username: </span><span style="color: yellow; font-size:20px">{{username }} </span>
            </el-row>
            <el-row  class="line">
                    <span class="line-text" >Region:  </span><span style="color: yellow; font-size:20px">{{ region}}</span>
            </el-row>
            <el-row  class="line">
                    <span class="line-text" >Birthdate: </span><span style="color: yellow; font-size:20px">{{ birthdate}}  </span>
            </el-row>
            <el-row  class="line">
                    <span class="line-text" >Email:  </span><span style="color: yellow; font-size:20px">{{email }}</span>
            </el-row>

            <el-row :span="5" :offset="2" style="background: #1F3D70; border-radius: 50px;width: 200px; margin-top:5%">
                <span style="margin-left:25%;font-size: 25px;color: #F5EFE0;">Balance</span>
            </el-row>
            <el-row  class="line">
                    <span class="line-text" >20000 </span>
            </el-row>

            <el-row :span="5" :offset="2" style="background: #1F3D70; border-radius: 50px;width: 200px; margin-top:5%">
                <span style="margin-left:25%;font-size: 25px;color: #F5EFE0;">Setting</span>
            </el-row>

            <el-button style="    background: #1F3D70; 
                            border-radius: 50px;
                            width: 500px; 
                            margin-top:2%;
                            margin-left:10%;
                            text-align: left;
                            font-size: 18px;" 
                        icon = "el-icon-chat-dot-square" type="primary">Contact us</el-button>
            <el-button style="    background: #1F3D70; 
                            border-radius: 50px;
                            width: 500px; 
                            margin-top:2%;
                            margin-left:10%;
                            text-align: left;
                            font-size: 18px;" 
                        icon = "el-icon-edit" type="primary">Edit profile information</el-button>
            <el-button style=" background: #1F3D70; 
                            border-radius: 50px;
                            width: 500px; 
                            margin-top:2%;
                            margin-left:10%;
                            text-align: left;
                            font-size: 18px;" 
                        icon = "el-icon-lock" type="primary">Reset password</el-button>


        </el-col>

    </div>
</template>

<script>
export default {
    data() {
        return {
            avatar:'https://avatars0.githubusercontent.com/u/8186664?s=460&v=4',
        };

  },
    computed: {
        accountid() {
            return this.$store.state.accountid;
        },
        username() {
            return this.$store.state.username;
        },
        region() {
            return this.$store.state.region;
        },
        birthdate() {
            return this.$store.state.birthdate;
        },
        email() {
            return this.$store.state.email;
        },
    },
};
</script>

<style >
.line{
    background: #1F3D70; 
    border-radius: 50px;
    width: 500px; 
    margin-top:2%;
    margin-left:10%
}
.line-text{
    margin-left:5%;
    font-size: 20px;
    color: bisque;


}

</style>
