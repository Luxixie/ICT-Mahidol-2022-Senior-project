@@ -1,291 +1,300 @@
<template>
  <div style="margin-top: 5%">
    <el-row>
      <el-col :span="12" :offset="9">
        <h1 style="color: #f5efe0">Register Your Account</h1>
      </el-col>
    </el-row>
    <el-form id="regist-form" ref="form" :model="form" :rules="rules">
      <el-form-item
        label="First Name"
        style="font-weight: bold; color: aliceblue"
        prop="firstname"
        :rules="[
          { required: true, message: 'Please enter your first name' },
          { min: 4, message: 'First name should be at least 4 characters' },
        ]"
      >
        <el-input
          id="regist-input"
          placeholder="First Name"
          v-model="form.firstname"
          style="width: 100%"
        ></el-input>
      </el-form-item>

      <el-form-item
        label="Last Name"
        style="font-weight: bold; color: aliceblue"
        prop="lastname"
        :rules="[
          { required: true, message: 'Please enter your last name' },
          { min: 4, message: 'Last name should be at least 4 characters' },
        ]"
      >
        <el-input
          id="regist-input"
          placeholder="Last Name"
          v-model="form.lastname"
          prop="lastname"
          style="width: 100%"
        ></el-input>
      </el-form-item>

      <el-form-item label="Country" style="font-weight: bold; color: aliceblue">
        <el-select
          id="regist-input"
          v-model="form.region"
          placeholder="Please select a country"
          style="width: 35%"
        >
          <el-option
            v-for="country in countries"
            :key="country.code"
            :label="country.name"
            :value="country.code"
          />
        </el-select>
        <!-- <el-input id="regist-input" placeholder="Birth Date" v-model="form.name" ></el-input> -->
        <span style="color: gray"> Birth Date</span>
        <el-date-picker
          id="regist-input"
          style="width: 40%; float: right"
          v-model="form.bod"
          format="yyyy-MM-dd"
          value-format="yyyy-MM-dd"
          type="date"
          placeholder="Birth Date"
        >
        </el-date-picker>
      </el-form-item>
      <el-form-item
        prop="email"
        label="Email"
        style="font-weight: bold; color: aliceblue"
      >
        <el-input
          id="regist-input"
          placeholder="Email"
          v-model="form.email"
          type="email"
        ></el-input>
      </el-form-item>
      <el-form-item
        label="Password"
        style="font-weight: bold; color: aliceblue"
      >
        <el-input
          id="regist-input"
          placeholder="Password"
          show-password
          v-model="form.password"
        ></el-input>
      </el-form-item>
      <el-form-item
        label="Confirm Password"
        style="font-weight: bold; color: aliceblue"
      >
        <el-input
          id="regist-input"
          placeholder="Confirm Password"
          show-password
          v-model="form.confirmPassword"
        />
      </el-form-item>
      <el-form-item>
        <el-button
          round
          type="warning"
          @click="submitForm"
          style="width: 45%; margin-left: 25%"
          >Create User</el-button
        >
      </el-form-item>
    </el-form>
  </div>
</template>
<script>
import axios from "axios";
export default {
  data() {
    return {
      selectedCountry: "",
      countries: [
        { name: "Afghanistan", code: "AF" },
        { name: "Albania", code: "AL" },
        { name: "Algeria", code: "DZ" },
        { name: "Andorra", code: "AD" },
        { name: "Angola", code: "AO" },
        { name: "Antigua and Barbuda", code: "AG" },
        { name: "Argentina", code: "AR" },
        { name: "Armenia", code: "AM" },
        { name: "Australia", code: "AU" },
        { name: "Austria", code: "AT" },
        { name: "Azerbaijan", code: "AZ" },
        { name: "Bahamas", code: "BS" },
        { name: "Bahrain", code: "BH" },
        { name: "Bangladesh", code: "BD" },
        { name: "Barbados", code: "BB" },
        { name: "Belarus", code: "BY" },
        { name: "Belgium", code: "BE" },
        { name: "Belize", code: "BZ" },
        { name: "Benin", code: "BJ" },
        { name: "Bhutan", code: "BT" },
        { name: "Bolivia", code: "BO" },
        { name: "Bosnia and Herzegovina", code: "BA" },
        { name: "Botswana", code: "BW" },
        { name: "Brazil", code: "BR" },
        { name: "Brunei", code: "BN" },
        { name: "Bulgaria", code: "BG" },
        { name: "Burkina Faso", code: "BF" },
        { name: "Burundi", code: "BI" },
        { name: "Cambodia", code: "KH" },
        { name: "Cameroon", code: "CM" },
        { name: "Canada", code: "CA" },
        { name: "Cape Verde", code: "CV" },
        { name: "Central African Republic", code: "CF" },
        { name: "Chad", code: "TD" },
        { name: "Chile", code: "CL" },
        { name: "China", code: "CN" },
        { name: "Colombia", code: "CO" },
        { name: "Comoros", code: "KM" },
        { name: "Iraq", code: "IQ" },
        { name: "Ireland", code: "IE" },
        { name: "Israel", code: "IL" },
        { name: "Italy", code: "IT" },
        { name: "Jamaica", code: "JM" },
        { name: "Japan", code: "JP" },
        { name: "Jordan", code: "JO" },
        { name: "Kazakhstan", code: "KZ" },
        { name: "Kenya", code: "KE" },
        { name: "Kiribati", code: "KI" },
        { name: "North Korea", code: "KP" },
        { name: "South Korea", code: "KR" },
        { name: "Kuwait", code: "KW" },
        { name: "Kyrgyzstan", code: "KG" },
        { name: "Laos", code: "LA" },
        { name: "Latvia", code: "LV" },
        { name: "Lebanon", code: "LB" },
        { name: "Lesotho", code: "LS" },
        { name: "Liberia", code: "LR" },
        { name: "Libya", code: "LY" },
        { name: "Liechtenstein", code: "LI" },
        { name: "Lithuania", code: "LT" },
        { name: "Luxembourg", code: "LU" },
        { name: "Madagascar", code: "MG" },
        { name: "Malawi", code: "MW" },
        { name: "Malaysia", code: "MY" },
        { name: "Maldives", code: "MV" },
        { name: "Mali", code: "ML" },
        { name: "Malta", code: "MT" },
        { name: "Marshall Islands", code: "MH" },
        { name: "Mauritania", code: "MR" },
        { name: "Mauritius", code: "MU" },
        { name: "Mexico", code: "MX" },
        { name: "Micronesia", code: "FM" },
        { name: "Moldova", code: "MD" },
        { name: "Monaco", code: "MC" },
        { name: "Mongolia", code: "MN" },
        { name: "Montenegro", code: "ME" },
        { name: "Morocco", code: "MA" },
        { name: "Mozambique", code: "MZ" },
        { name: "Myanmar", code: "MM" },
        { name: "Namibia", code: "NA" },
        { name: "Nauru", code: "NR" },
        { name: "Nepal", code: "NP" },
        { name: "Netherlands", code: "NL" },
        { name: "New Zealand", code: "NZ" },
        { name: "Nicaragua", code: "NI" },
        { name: "Niger", code: "NE" },
        { name: "Nigeria", code: "NG" },
        { name: "Norway", code: "NO" },
        { name: "Oman", code: "OM" },
        { name: "Pakistan", code: "PK" },
        { name: "Palau", code: "PW" },
        { name: "Palestine", code: "PS" },
        { name: "Panama", code: "PA" },
        { name: "Papua New Guinea", code: "PG" },
        { name: "Paraguay", code: "PY" },
        { name: "Peru", code: "PE" },
        { name: "Philippines", code: "PH" },
        { name: "Senegal", code: "SN" },
        { name: "Serbia", code: "RS" },
        { name: "Seychelles", code: "SC" },
        { name: "Sierra Leone", code: "SL" },
        { name: "Singapore", code: "SG" },
        { name: "Slovakia", code: "SK" },
        { name: "Slovenia", code: "SI" },
        { name: "Solomon Islands", code: "SB" },
        { name: "Somalia", code: "SO" },
        { name: "South Africa", code: "ZA" },
        { name: "Tanzania", code: "TZ" },
        { name: "Thailand", code: "TH" },
        { name: "Timor-Leste", code: "TL" },
        { name: "Togo", code: "TG" },
        { name: "Tonga", code: "TO" },
        { name: "Trinidad and Tobago", code: "TT" },
        { name: "Tunisia", code: "TN" },
        { name: "Turkey", code: "TR" },
      ],
      form: {
        firstname: "",
        lastname: "",
        region: "",
        bod: "",
        email: "",
        password: "",
        confirmpassword: "",
      },
      rules: {
        email: [
          { required: true, message: "Please input email", trigger: "blur" },
          {
            type: "email",
            message: "Please input correct email format",
            trigger: "blur",
          },
        ],
      },
    };
  },
  methods: {
    /*disabledDate(date) {
            const today = new Date();
            console.log("error");
            return date > today;
        },*/
    validatePassword() {
      if (this.form.password === this.form.confirmPassword) {
        console.log(this.form.password);
        console.log(this.form.confirmPassword);
        if (this.form.password.length < 8) {
          //console.log("Passwords do not longer than 8");
          this.$alert("Passwords do not longer than 8", "Password error", {
            confirmButtonText: "Next",
          });
          return false;
        }
        // check the number
        if (!/\d/.test(this.form.password)) {
          //console.log("Passwords do not include number");
          this.$alert("Passwords do not include number", "Password error", {
            confirmButtonText: "Next",
          });
          return false;
        }
        // check the symbol
        if (!/[!@#$%^&*(),.?":{}|<>]/g.test(this.form.password)) {
          //console.log("Passwords do not include symbol");
          this.$alert("Passwords do not include symbol", "Password error", {
            confirmButtonText: "Next",
          });
          return false;
        }
        // Check whether it contains at least one uppercase letter and one lowercase letter
        if (
          !/[a-z]/g.test(this.password) ||
          !/[A-Z]/g.test(this.form.password)
        ) {
          this.$alert(
            "Passwords do not include at least one uppercase letter and one lowercase letter",
            "Password error",
            {
              confirmButtonText: "Next",
            }
          );
          return false;
        }
        // If all conditions are met, the password meets the requirements
        return true;
      } else {
        //console.log("Passwords do not match");
        this.$alert("Passwords do not match", "Password error", {
          confirmButtonText: "Next",
        });
      }
    },
    submitForm() {
      this.$refs.form.validate((valid) => {
        var checkResult = this.validatePassword();
        if (checkResult) {
          var result = this.CreateUser();
          console.log(result);
        } else {
          this.$message({
            showClose: true,
            message: "Form is invalid",
            type: "warning",
          });
        }
      });
    },
    CreateUser() {
      axios.post("http://127.0.0.1:8088/signup", this.form).then((res) => {
        console.log(res.data);
        if (res.data.state == 1) {
          this.$message({
            showClose: true,
            message:
              "Congratulations on your registration and thank you for choosing to belong to Stock Plenty",
            type: "success",
          });

          this.$confirm(
            "Do you want to learn some stock knowledge first?",
            "Open Test",
            {
              confirmButtonText: "Yes",
              cancelButtonText: "No",
              type: "info",
            }
          )
            .then(() => {
              this.$router.replace("/opentest");
            })
            .catch(() => {
              this.$router.replace("/login");
            });
        }
        else if (res.data.state == 2) {
          alert("Account alreay exists");
          return false;
        } else {
          alert("Incorrect user name or password!");
          return false;
        }
      });
    },
  },
};
</script>

<style>
#regist-input {
  background: #1f3d70;
  border-color: #1f3d70;
  border-radius: 100px;
  color: #f5efe0;
}

#regist-form {
  margin-left: 30%;
  margin-right: 30%;
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
