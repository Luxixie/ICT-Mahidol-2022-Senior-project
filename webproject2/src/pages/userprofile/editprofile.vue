<template>
    <div>
        <el-col :span="5" :offset="2" style=" margin-top:2%;">
            <el-row>
                <div style="margin-left:20%">
                    <el-avatar :size="200" :src="avatar"   />
                </div>
            </el-row> 
        </el-col>
        <el-col :span="10" :offset="1" style=" margin-top:3%">
            <el-row  style="background: #1F3D70; border-radius: 50px;width: 200px;">
                <span style="margin-left:13%; font-style: normal; font-size: 30px;color: #F5EFE0;">Edit Profile</span>
            </el-row>
            <el-row  style="background: #1F3D70; border-radius: 50px;width: 150px; margin-top:5%">
                <span style="margin-left:15%;font-size: 25px;color: #F5EFE0;">Account</span>
            </el-row>
            <el-row label="First Name" style="font-weight: bold; color: aliceblue;" prop="firstname" >
                <span id="regist-input"   @blur="firstnameLengthValidation"
                    style="width: 100%;">{{accountid}}</span>
            </el-row>
        <el-form id="regist-form" ref="form" :model="form" :rules="rules" >
            <el-form-item label="First Name" style="font-weight: bold; color: aliceblue;" prop="firstname" >
                <el-input id="regist-input" placeholder="First Name" v-model="form.firstname" @blur="firstnameLengthValidation"
                    style="width: 100%;"></el-input>
            </el-form-item>
            <el-form-item label="Last Name" style="font-weight: bold; color: aliceblue;" prop="lastname" >
                <el-input id="regist-input" placeholder="Last Name" v-model="form.lastname" @blur="lastnameLengthValidation" 
                    prop="lastname" style="width: 100%;"></el-input>
            </el-form-item>
            <el-form-item label="Country" style="font-weight: bold; color: aliceblue;">
                <el-select id="regist-input" v-model="form.region" placeholder="Please select a country" style="width: 100%;">
                    <el-option
                        v-for="country in countries"
                        :key="country.code"
                        :label="country.name"
                        :value="country.code"/>
                </el-select>
            </el-form-item>
            <el-form-item label="Birth Date" style="font-weight: bold; color: aliceblue;">
                <!-- <el-input id="regist-input" placeholder="Birth Date" v-model="form.name" ></el-input> -->
                <el-date-picker  id="regist-input" style="width: 100%;" v-model="form.bod" format="yyyy-MM-dd" value-format="yyyy-MM-dd" type="date" placeholder="Birth Date">
                </el-date-picker>
            </el-form-item>
            <el-form-item prop="email" label="Email" style="font-weight: bold; color: aliceblue;">
                <el-input id="regist-input" placeholder="Email" v-model="form.email" type="email"></el-input>
            </el-form-item>
            <el-form-item>
                <el-button round type="warning" @click="submitForm" style="width: 45%; margin-left: 25%;">Confirm</el-button>

            </el-form-item>
        </el-form>
        </el-col>

    </div>
</template>

<script>
import axios from 'axios'
export default {
    data() {
        return {
            avatar:'https://avatars0.githubusercontent.com/u/8186664?s=460&v=4',
            selectedCountry: '',
            countries: [
                { name: 'Afghanistan', code: 'AF' },
                { name: 'Albania', code: 'AL' },
                { name: 'Algeria', code: 'DZ' },
                { name: 'Andorra', code: 'AD' },
                { name: 'Angola', code: 'AO' },
                { name: 'Antigua and Barbuda', code: 'AG' },
                { name: 'Argentina', code: 'AR' },
                { name: 'Armenia', code: 'AM' },
                { name: 'Australia', code: 'AU' },
                { name: 'Austria', code: 'AT' },
                { name: 'Azerbaijan', code: 'AZ' },
                { name: 'Bahamas', code: 'BS' },
                { name: 'Bahrain', code: 'BH' },
                { name: 'Bangladesh', code: 'BD' },
                { name: 'Barbados', code: 'BB' },
                { name: 'Belarus', code: 'BY' },
                { name: 'Belgium', code: 'BE' },
                { name: 'Belize', code: 'BZ' },
                { name: 'Benin', code: 'BJ' },
                { name: 'Bhutan', code: 'BT' },
                { name: 'Bolivia', code: 'BO' },
                { name: 'Bosnia and Herzegovina', code: 'BA' },
                { name: 'Botswana', code: 'BW' },
                { name: 'Brazil', code: 'BR' },
                { name: 'Brunei', code: 'BN' },
                { name: 'Bulgaria', code: 'BG' },
                { name: 'Burkina Faso', code: 'BF' },
                { name: 'Burundi', code: 'BI' },
                { name: 'Cambodia', code: 'KH' },
                { name: 'Cameroon', code: 'CM' },
                { name: 'Canada', code: 'CA' },
                { name: 'Cape Verde', code: 'CV' },
                { name: 'Central African Republic', code: 'CF' },
                { name: 'Chad', code: 'TD' },
                { name: 'Chile', code: 'CL' },
                { name: 'China', code: 'CN' },
                { name: 'Colombia', code: 'CO' },
                { name: 'Comoros', code: 'KM' },
                { name: 'Iraq', code: 'IQ' },
                { name: 'Ireland', code: 'IE' },
                { name: 'Israel', code: 'IL' },
                { name: 'Italy', code: 'IT' },
                { name: 'Jamaica', code: 'JM' },
                { name: 'Japan', code: 'JP' },
                { name: 'Jordan', code: 'JO' },
                { name: 'Kazakhstan', code: 'KZ' },
                { name: 'Kenya', code: 'KE' },
                { name: 'Kiribati', code: 'KI' },
                { name: 'North Korea', code: 'KP' },
                { name: 'South Korea', code: 'KR' },
                { name: 'Kuwait', code: 'KW' },
                { name: 'Kyrgyzstan', code: 'KG' },
                { name: 'Laos', code: 'LA' },
                { name: 'Latvia', code: 'LV' },
                { name: 'Lebanon', code: 'LB' },
                { name: 'Lesotho', code: 'LS' },
                { name: 'Liberia', code: 'LR' },
                { name: 'Libya', code: 'LY' },
                { name: 'Liechtenstein', code: 'LI' },
                { name: 'Lithuania', code: 'LT' },
                { name: 'Luxembourg', code: 'LU' },
                { name: 'Madagascar', code: 'MG' },
                { name: 'Malawi', code: 'MW' },
                { name: 'Malaysia', code: 'MY' },
                { name: 'Maldives', code: 'MV' },
                { name: 'Mali', code: 'ML' },
                { name: 'Malta', code: 'MT' },
                { name: 'Marshall Islands', code: 'MH' },
                { name: 'Mauritania', code: 'MR' },
                { name: 'Mauritius', code: 'MU' },
                { name: 'Mexico', code: 'MX' },
                { name: 'Micronesia', code: 'FM' },
                { name: 'Moldova', code: 'MD' },
                { name: 'Monaco', code: 'MC' },
                { name: 'Mongolia', code: 'MN' },
                { name: 'Montenegro', code: 'ME' },
                { name: 'Morocco', code: 'MA' },
                { name: 'Mozambique', code: 'MZ' },
                { name: 'Myanmar', code: 'MM' },
                { name: 'Namibia', code: 'NA' },
                { name: 'Nauru', code: 'NR' },
                { name: 'Nepal', code: 'NP' },
                { name: 'Netherlands', code: 'NL' },
                { name: 'New Zealand', code: 'NZ' },
                { name: 'Nicaragua', code: 'NI' },
                { name: 'Niger', code: 'NE' },
                { name: 'Nigeria', code: 'NG' },
                { name: 'Norway', code: 'NO' },
                { name: 'Oman', code: 'OM' },
                { name: 'Pakistan', code: 'PK' },
                { name: 'Palau', code: 'PW' },
                { name: 'Palestine', code: 'PS' },
                { name: 'Panama', code: 'PA' },
                { name: 'Papua New Guinea', code: 'PG' },
                { name: 'Paraguay', code: 'PY' },
                { name: 'Peru', code: 'PE' },
                { name: 'Philippines', code: 'PH' },
                { name: 'Senegal', code: 'SN' },
                { name: 'Serbia', code: 'RS' },
                { name: 'Seychelles', code: 'SC' },
                { name: 'Sierra Leone', code: 'SL' },
                { name: 'Singapore', code: 'SG' },
                { name: 'Slovakia', code: 'SK' },
                { name: 'Slovenia', code: 'SI' },
                { name: 'Solomon Islands', code: 'SB' },
                { name: 'Somalia', code: 'SO' },
                { name: 'South Africa', code: 'ZA' },
                { name: 'Tanzania', code: 'TZ' },
                { name: 'Thailand', code: 'TH' },
                { name: 'Timor-Leste', code: 'TL' },
                { name: 'Togo', code: 'TG' },
                { name: 'Tonga', code: 'TO' },
                { name: 'Trinidad and Tobago', code: 'TT' },
                { name: 'Tunisia', code: 'TN' },
                { name: 'Turkey', code: 'TR' },
            ],
            form: {
                accountid:'',
                firstname: '',
                lastname: '',
                region: '',
                bod: '',
                email: '',
            },            
            rules:{
                email: [
                { required: true, message: "Please input email", trigger: "blur" },
                { type: "email", message: "Please input correct email format", trigger: "blur" }
                ],
                firstname: [
                { required: true, message: "Please input first name", trigger: "blur" },
                { validator: this.firstnameLengthValidation, trigger: "blur" }
                ],
                lastname: [
                { required: true, message: "Please input last name", trigger: "blur" },
                { validator: this.lastnameLengthValidation, trigger: "blur" }
                ],

            }
        };
    },
    methods: {  
        firstnameLengthValidation(rule, value, callback) {
            if (value.length > 10) {
                callback(new Error("Firstname length should be less than 10"));
            } else {
                callback();
                }
        },
        lastnameLengthValidation(rule, value, callback) {
            if (value.length > 10) {
                callback(new Error("Lastname length should be less than 10"));
            } else {
                callback();
                }
        },
        submitForm() {
            this.$refs.form.validate(valid => {
            if (valid) {
            this.EditUser();
            this.$router.replace('/userhome'); 
            } else {
            this.$message({
                showClose: true,
                message: 'Form is invalid',
                type: 'warning'
            });
            }
            });
            console.log(this.form.accountid),
            console.log(this.form.firstname),
            console.log(this.form.lastname),
            console.log(this.form.region),
            console.log(this.form.bod),
            console.log(this.form.email)
        },
        EditUser(){
            axios.post('http://127.0.0.1:8088/editprofile', this.form).then(res => {
            console.log(res.data)
            if (res.data.state == 1) {
                this.$message({
                showClose: true,
                message: 'Successfully modified information',
                type: 'success'
                });
                          
                } else {
                alert('Incorrect information');
                return false;
                }
            });
        }
    },
    computed: {
        accountid() {
            this.form.accountid = this.$store.state.accountid
            
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
#regist-input {
    background: #1f3d70;
    border-color: #1f3d70;
    border-radius: 100px;
    color: #f5efe0;

}

</style>
