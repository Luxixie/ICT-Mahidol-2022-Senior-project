<template>
  <div>
    <h1>Multiple Choice Questions</h1>
    <div v-for="question in questions" :key="question.id">
      <h2>{{ question.text }}</h2>
      <form>
        <input type="radio" :name="question.id" value="1">{{ question.answer_1 }}<br>
        <input type="radio" :name="question.id" value="2">{{ question.answer_2 }}<br>
        <input type="radio" :name="question.id" value="3">{{ question.answer_3 }}<br>
        <input type="radio" :name="question.id" value="4">{{ question.answer_4 }}<br>
      </form>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
    data() {
        return {
        questions: []
        }
    },

}
</script>
    mounted() {
        this.$refs.questions.validate(
        axios.post('http://127.0.0.1:8088/login', this.questions).then(res => {
            console.log(res.data)
        .then(response => response.json())
        .then(data => this.questions = data)
        }
    }