<template>
<div>
    <el-row style="margin-top:2%">
        <div>
            <span style="margin-left: 5%; margin-top: 2%; color: #f5efe1; font-size: 30px">Quiz review</span>
        </div>
    </el-row>
    <el-row :span = "8" :offfset= "5" style="margin-left: 5%;margin-right: 5%;margin-top:2%">
        <el-table :data="tableData" border style="width: 100%">
        <el-table-column
            prop="Time"
            label="Time"
            align="center"
            :v-model="tableData.Time">
        </el-table-column>
        <el-table-column
            prop="chapter_id"
            label="Chapter"
            align="center">
        </el-table-column>

        <el-table-column
            prop="Score"
            label="Score"
            align="center">
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
    axios.post("http://127.0.0.1:8088/quizreview/" + id).then((res) => {
      this.tableData = [];
      //console.log(res.data)
      res.data.forEach(result  => {
        this.tableData.push(result);
      });
      console.log(this.tableData);
    });
  },
};
</script>

<style>


</style>