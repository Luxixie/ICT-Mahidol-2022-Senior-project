<template>
    <el-row class="para1" style="background: #d9d9d9;" >
      <el-col :span="4" >
        <img src="./imges/logo.png" height="100" width="200">
      </el-col>
      <el-col :span="13" >
        <div class="SearchPart">
          <el-input  id="searchBar"  placeholder="Search" prefix-icon="el-icon-search" />
        </div>
      </el-col>
      <el-col :span="5">
        <div class="LoginPart">
          <el-button size="medium"  type="info"  round @click="GoLoginPage">Log In</el-button>
          <el-button id="signupbt" size="medium" type="info" @click="GoSignUpPage" round>Sign Up</el-button>
        </div>
      </el-col>
    </el-row>
  </template>
  <script>
  export default {
    name: "Header",
    methods:{
        GoLoginPage(){
            this.$router.push('/login')
        },
        GoSignUpPage(){
            this.$router.push('/signup')
        }
    }
  }
  </script>
  
  <style>
  #signupbt{
    margin-left: 30px;
  }
  
  
  .SearchPart{
    
    padding: 30px;
    margin-right: 30px;  
  }
  
  #searchBar{
    background: #f5efe1;
  }
  
  .LoginPart{
    
    padding: 30px;
  }
  </style>