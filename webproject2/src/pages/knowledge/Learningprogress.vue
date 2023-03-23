<template>
  <div>
    <el-row style="margin-top: 2%">
      <span
        style="margin-left: 5%; margin-top: 2%; color: #f5efe1; font-size: 30px"
        >Learning progress</span
      >
    </el-row>
    <el-row
      :span="8"
      :offfset="5"
      style="margin-left: 5%; margin-right: 5%; margin-top: 2%"
    >
      <el-table :data="tableData" border style="width: 100%">
        <el-table-column
          prop="Time"
          label="Time"
          align="center"
          :v-model="tableData.Time"
        >
        </el-table-column>
        <el-table-column prop="chapter_id" label="Chapter" align="center">
        </el-table-column>
        <el-table-column
          prop="subchapters_id"
          label="Subchapter"
          align="center"
        >
        </el-table-column>
        <el-table-column prop="isLearned" label="State" align="center">
        </el-table-column>
      </el-table>
    </el-row>
  </div>
</template>



<script>
import axios from "axios";
export default {
  data() {
    return {
      tableData: [],
    };
  },
  created() {
    var id = this.$store.state.accountid;
    console.log(id)
    axios.post("http://127.0.0.1:8088/learningprocess/" + id).then((res) => {
      this.tableData = [];
      res.data.forEach((res) => {
        if (res.isLearned == 1) {
          res.isLearned = "Done";
          
        }
        this.tableData.push(res);

        console.log(this.tableData);
      });
    });
  },
};
</script>

<style>
#title {
  color: #ffffff;
  font-size: 30px;
}
</style>
          this.tableData = response.data
          console.log(this.tableData)