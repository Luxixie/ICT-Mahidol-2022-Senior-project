<template>
  <el-row class="para1" style="background: #d9d9d9">
    <el-col :span="3">
      <img src="./imges/logo.png" height="110" width="200" />
    </el-col>
    <el-col :span="10" :offset="2">
      <div class="SearchPart">
        <el-autocomplete
          style="width:100%;margin-top: 2%"
          class="inline-input"
          v-model="searchTerm"
          :fetch-suggestions="querySearch"
          placeholder="Search"
          :trigger-on-focus="false"
          @select="handleSelect"
          prefix-icon="el-icon-search"
          @keydown.enter="handleSelect(searchTerm)"
        ></el-autocomplete>
      </div>
    </el-col>
    <el-col :span="8" :offset="1">

      <div class="userInfo" style="margin-top: 8%" v-if="username">
        <el-button size="medium" type="info" round @click="GoHome"
          >Home</el-button
        >
        <el-button style="margin-left: 3%" size="medium" type="info" circle>{{
          username.charAt(0).toUpperCase()
        }}</el-button>
        <el-dropdown @command="handleCommand">
          <span class="el-dropdown-link">
            {{ username }}<i class="el-icon-arrow-down el-icon--right"></i>
          </span>
          <el-dropdown-menu slot="dropdown">
            <el-dropdown-item icon="el-icon-user" command="userhome"
              >User profile</el-dropdown-item
            >
            <el-dropdown-item icon="el-icon-shopping-cart-2" command="watchlist"
              >Watch list</el-dropdown-item
            >
            <el-dropdown-item icon="el-icon-s-finance" command="portfolio"
              >Portfolio</el-dropdown-item
            >
            <el-dropdown-item icon="el-icon-tickets" command="quiz"
              >Quiz review</el-dropdown-item
            >
            <el-dropdown-item icon="el-icon-s-management" command="Lprogress"
              >Learning progress</el-dropdown-item
            >
            <el-dropdown-item icon="el-icon-refresh-left" command="logout"
              >Log out</el-dropdown-item
            >
          </el-dropdown-menu>
        </el-dropdown>
        <el-badge :value="100" :max="1">
          <el-link icon="el-icon-message-solid" style="width: 5%"></el-link>
        </el-badge>
      </div>

      <div class="LoginPart" v-if="!username" style="margin-top: 8%">
        <el-button size="medium" type="info" round @click="GoHome"
          >Home</el-button
        >
        <el-button size="medium" type="info" round @click="GoLoginPage"
          >Log In</el-button
        >
        <el-button
          id="signupbt"
          size="medium"
          type="info"
          @click="GoSignUpPage"
          round
          >Sign Up</el-button
        >
      </div>
    </el-col>
  </el-row>
</template>
<script>
import axios from "axios";
import { Spinner } from "element-ui";
import { computed } from "vue";
import { mapGetters } from "vuex";

export default {
  name: "Header",
  data() {
    return {
      searchTerm: "",
      stocks: [],
    };
  },
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
    loadAll() {
      axios.post("http://127.0.0.1:8088/GetStockInfo").then((res) => {
        //console.log(res.data)
        this.stocks = res.data;
      });
    },
    querySearch(queryString, cb) {
      var stocks = this.stocks;
      console.log(stocks)
      var results = queryString
        ? stocks.filter(this.createFilter(queryString))
        : stocks;
      

      //console.log(results)
      cb(results);
      //console.log(results)
    },
    createFilter(queryString) {
      return (stocks) => {
        return (
          stocks.value.toLowerCase().indexOf(queryString.toLowerCase()) === 0
        );
      };
    },
    handleCommand(command) {
      switch (command) {
        case "userhome":
          this.$router.push("/userhome");
          break;
        case "watchlist":
          this.$router.push("/watchlist");
          break;
        case "portfolio":
          this.$router.push("/portfolio");
          break;
        case "quiz":
          this.$router.push("/quizreview");
          break;
        case "Lprogress":
          this.$router.push("/Learningprogress");
          break;
        case "logout":
          window.location.href = "/home";
      }
    },

    handleSelect(item) {
      console.log(item);
      this.Goinfor(item.value)
    },
    Goinfor(value) {
      console.log(value);
      //this.$router.push('/buyandsell')
      this.$router.push({
        path: "/buyandsell/" + value,
        params: { tickerName: value },
      });
     
    },

  },
  mounted() {
    this.stocks = this.loadAll();
  },
  created() {
    console.log();
  },
  updated() {
    console.log(this.$store.state.username);
  },

  computed: {
    username() {
      return this.$store.state.username;
    },
    accountid() {
      return this.$store.state.accountid;
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
  watch: {
    "$store.state.username"(newVal, oldVal) {},
  },
  components: { Spinner },
};
</script>

<style>
#signupbt {
  margin-left: 2%;
}

.SearchPart {
  padding: 30px;
  margin-right: 30px;
}

#searchBar {
  background: #f5efe1;
}

.LoginPart {
}

.item {
  margin-top: 10px;
  margin-right: 40px;
}
</style>