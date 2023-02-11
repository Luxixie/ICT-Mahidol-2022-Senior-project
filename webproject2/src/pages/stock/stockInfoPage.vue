<template>
    <div>
      <div ref="chartMin" style="width:540px;height:300px"></div>
    </div>
  </template>
  
<script>
  export default {
    data() {
      return{
        a: 'sh600000',
        data1: [],
        data2: [],
        data3: [],
      }
    },
    methods: {
      getChart() {
        this.code = (this.a).slice(2);
        if (this.code[0] == 6) {
          this.type = 'sse';
        } else {
          this.type = 'szse';
        }
    
        jsonp('http://webstock.quote.hermes.hexun.com/a/minute?code='
        + this.type + this.code + '&start=20181026000000&number=500&callback=chart2', {fn: 'chart2'}).then((res) => {
          const total = res.Data[0];
          for (const j of Object.keys(total)) {
            const time = total[j][0] + '';
            const year = time.slice(0, 4);
            const month = time.slice(4, 6);
            const day = time.slice(6, 8);
            const hour = time.slice(8, 10);
            const minute = time.slice(10, 12);
            const second = time.slice(12, 14);
            const yeartwo = year + '-' + month + '-' + day;
            const timetwo = hour + ':' + minute + ':' + second;
            this.data1.push(timetwo);
            const chartprice = total[j][1] / 100;
            this.data2.push(chartprice);

            const chg = parseFloat(Number((chartprice - this.yes) / this.yes * 100)).toFixed(2);
            this.data3.push(chg);
          }

          this.chart.setOption({
    
            grid: {
              left: '10%',
              right: '10%',
              bottom: '10%',
            },
            tooltip : {
              trigger: 'axis',
              axisPointer: {
                type: 'cross',
                animation: false,
                label: {
                  backgroundColor: '#505765',
                },
              },
            },
            // 下方滑块
            // dataZoom: [
            //     {
            //         show: true,
            //         realtime: true,
            //     },
            //     {
            //         type: 'inside',
            //         realtime: true,
            //     },
            // ],
            xAxis: [
              {
                type : 'category',
                boundaryGap : false,
                axisLine: {onZero: false},
                data : this.data1
                .map((str) => {
                    return str.replace(' ', '\n');
                }),
              },
            ],
            yAxis: [
              {
                name: 'Price',
                type: 'value',
                scale: true,
                splitNumber: 4,
              },
              {
                name: 'Rise and fall(%)',
                type: 'value',
                scale: true,
                splitNumber: 4,
                splitLine: false,
              },
            ],
            series: [
              {
                name: 'Price',
                type: 'line',
                animation: false,
                symbol: 'none',
                lineStyle: {
                    width: 1,
                },
                data: this.data2,
              },
              {
                name: 'Rise and fall',
                type: 'line',
                yAxisIndex: 1,
                animation: false,
                symbol: 'none',
                lineStyle: {
                  width: 1,
                  color: 'transparent',
                },
                markLine: {
                  silent: true,
                  
                  symbol: 'none',
                  data: [{
                      yAxis: 0,
                  }],
                  lineStyle: {
                      normal: {
                          type: 'dashed',
                          color: 'red',
                      },
                  },
                  label: {
                    formatter: '',
                  },
                },
                data: this.data3,
              },
            ],
          });
        });
        // },3000);
      },
    },
    initchart() {
      this.chart = echarts.init(this.$refs.chartMin);
    },
    mounted () {
      this.initchart();
    },
  }

</script>