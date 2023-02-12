<template>
  <el-row class="para1" style="background: #d9d9d9;">
    <el-col :span="4">
      <img src="./imges/logo.png" height="100" width="200">
    </el-col>
    <el-col :span="13">
      <div class="SearchPart">
        <el-input id="searchBar" placeholder="Search" prefix-icon="el-icon-search" />
      </div>
    </el-col>
    <el-col :span="5">
      <div class="userInfo" style="margin-top: 8%;" v-if="username">
        <el-button size="medium" type="info" round @click="GoHome">Home</el-button>
        <el-button style="margin-left: 5%;" size="medium" type="info" circle @click="Gouser">{{ username.charAt(0) }}</el-button>
        <span style="margin-left: 5%;">{{ username }}</span>
      </div>
      <div class="LoginPart" v-if="!username" style="margin-top: 8%;">
        <el-button size="medium" type="info" round @click="GoLoginPage">Log In</el-button>
        <el-button id="signupbt" size="medium" type="info" @click="GoSignUpPage" round>Sign Up</el-button>
      </div>
    </el-col>
  </el-row>
</template>
<script>
import { Spinner } from 'element-ui';
import { computed } from 'vue';
import { mapGetters } from 'vuex'

export default {
  name: "Header",
  data() {
    return {

    }
  }
  ,
  methods: {
    GoLoginPage() {
      this.$router.push("/login");
    },
    GoSignUpPage() {
      this.$router.push("/signup");
    },
    GoHome() {
      this.$router.push("/home");
    },
    Gouser(){
      this.$router.push("/userhome")
    }

  },
  created() {
    console.log();
  },
  updated() {
    console.log(this.$store.state.username);
  },
  computed: {
   
    username() {
      return this.$store.state.username
    }
  },
  watch: {
    '$store.state.username'(newVal,oldVal){

		}
  },
  components: { Spinner }
}
</script>

<style>
#signupbt {
  margin-left: 30px;
}


.SearchPart {

  padding: 30px;
  margin-right: 30px;
}

#searchBar {
  background: #f5efe1;
}

.LoginPart {}
</style>