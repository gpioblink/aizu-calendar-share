<template>
  <div class="hello" id="helloid">
    <h1>{{ msg }}</h1>
    <p>
      みんなの学籍をいれてね
    </p>
    <textarea v-model="studentIds" placeholder="学籍番号を改行区切で入力(5人まで)\n例)s1260250"></textarea>
    <br>
    <input type="radio" id="one" value="6" v-model="semester4q">
    <label for="one">一学期</label>
    <br>
    <input type="radio" id="two" value="7" v-model="semester4q">
    <label for="two">二学期</label>
    <br>
    <button type="button" @click="createAvailableTable(studentIds)">確定</button>
    <br>
    <br>
    <table id="calendar" class="table table-bordered">
      <thead>
      <tr>
        <th>時限</th>
        <td v-for="(value, index) in schedule">{{index}}</td>
      </tr>
      </thead>
      <tbody>
      <tr v-for="n in 11">
        <th>{{n}}限</th>
        <td v-for="(value, index) in schedule">{{value[n-1]}}</td>
      </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
  import Vue from 'vue'
  import classWeekInfo from '../mixins/classWeekInfo'
  export default {
    name: 'HelloWorld',
    mixins: [classWeekInfo],
    data: function () {
      return {
        studentIds: 's1260250',
        result: [],
        semester2q: '1',
        semester4q: '6',
        schedule: {
          '月': [0,0,0,0,0,0,0,0,0,0,0],
          '火': [0,0,0,0,0,0,0,0,0,0,0],
          '水': [0,0,0,0,0,0,0,0,0,0,0],
          '木': [0,0,0,0,0,0,0,0,0,0,0],
          '金': [0,0,0,0,0,0,0,0,0,0,0],
        }
      }
    },
    props: {
      msg: String
    },
    methods: {
      createAvailableTable: function(studentIds){
        for(let key in this.schedule){this.schedule[key] = this.schedule[key].map(e => e = 0)}
        //console.log(this.semester)
        studentIds.split('\n').forEach(studentId => {
          this.fetchPerson(studentId);
        });
      },
      fetchPerson: function (studentId) {
        const axios = require('axios');
        this.length = 5;
        axios.get('https://' + window.location.host + '/people/'+ studentId +'.txt')
        .then((res) => {
          const rawlist = res.data.split('\n');
          const output = rawlist.map((e) => {
            const classId = e.substring(12).slice(0,-4);
            this.fillTimeCellByClassId(classId);
            return classId;
          });
          Vue.set(this, 'result', output);
          //console.log(this.result);
        });
      },
      fillTimeCellByClassId: function(classId) {
        //console.log(classId,classId.slice(1,2))

        if(this.classWeekInfo[classId] && (classId.slice(1,2) == this.semester2q || classId.slice(1,2) == this.semester4q)) {
          const oneClassInfo = this.classWeekInfo[classId]['weektime']
          const weeks = oneClassInfo.match(/([月,火,水,木,金]+)[^月,火,水,木,金]*$/)[1].split(',')
          const times = oneClassInfo.split('-').map(e => e.replace(/[^0-9]/g, ''))
          const startTime = times[0]
          const endTime = times[1] || startTime
          weeks.forEach(week => {
            //console.log('処理中:',week,startTime,endTime,oneClassInfo)
            for (let i = Number(startTime); i <= Number(endTime); i++){
              this.schedule[week][i - 1]+=1
            }
            this.$forceUpdate();
          })
        }
      }
    },
    mounted: function () {
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
/* カレンダーのスタイル */
.table {
  margin: auto;
}

.table th, td{
  text-align: center;
}

#calendar th:first-child {
  background-color: #FEEEFF;
}
#calendar td:first-child {
  background-color: #FEEEFF;
}


#calendar td:hover {
  opacity: 0.6;
}
</style>
