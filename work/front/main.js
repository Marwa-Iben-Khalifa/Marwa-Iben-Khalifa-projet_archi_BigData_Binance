const crypto_list = [
  'BNBBUSD',
  'ETHBUSD',
  'BTCBUSD',
  'AVAXBUSD',
  'MATICBUSD',
  'SOLBUSD'
]

const idlist = [
  'chart1',
  'chart2',
  'chart3',
  'chart4',
  'chart5',
  'chart6',

]

// Function to create charts
async function create_chart(coin, containerId) {
  const res = await fetch(`http://127.0.0.1:5000/api/stock?coin=${coin}`);
  const result = await res.json();

  let candles = [];

  const indicators = [];
  // result.columns.map((elem, index) => {
  //   if (index > 5) {

  //     indicators.push({
  //         type: "line",
  //         linkedTo: "crypto",
  //         name: elem.split("_")[0],
  //         zIndex: 1,
  //         data: result.data.map((e) => {
  //             return [e[1], e[index]];
  //         }),
  //     });
      
  //   }
  // });

  result.data.map((elem) => {
    candles.push([elem[0], elem[1], elem[2], elem[3], elem[4]]);
    console.log(elem[0])
  });

  // create the chart
  Highcharts.stockChart(containerId, {
    chart: {
      backgroundColor: "#1e1e1d",
    },
    rangeSelector: {
      buttons: [
        {
          type: "hour",
          count: 1,
          text: "1h",
        },
        {
          type: "day",
          count: 1,
          text: "1d",
        },
        {
          type: "month",
          count: 1,
          text: "1m",
        },
        {
          type: "year",
          count: 1,
          text: "1y",
        },
        {
          type: "all",
          text: "All",
        },
      ],
      inputEnabled: false, // it supports only days
      selected: 1, // all
    },
    credits: { enabled: false },
    exporting: { enabled: false },

    yAxis: [
      {
        gridLineColor: "transparent",
        gridTextColor: "#ffffff",
        lineColor: "transparent",
        tickColor: "transparent",
        startOnTick: false,
        endOnTick: false,
        labels: {
          align: "right",
          x: -3,
        },
        title: {
          text: "OHLC",
        },
        height: "70%",
        lineWidth: 1,
        resize: {
          enabled: false,
        },
      },

      {
        gridLineColor: "transparent",
        gridTextColor: "#ffffff",
        lineColor: "transparent",
        tickColor: "transparent",
        height: "10%",
        top: "90%",
        lineWidth: 1,
        resize: {
          enabled: true,
        },
      },
      {
        gridLineColor: "transparent",
        gridTextColor: "#ffffff",
        lineColor: "transparent",
        tickColor: "transparent",
        height: "20%",
        top: "70%",
        lineWidth: 1,
        resize: {
          enabled: true,
        },
      },
      {
        gridLineColor: "transparent",
        gridTextColor: "#ffffff",
        lineColor: "transparent",
        tickColor: "transparent",
        height: "10%",
        top: "80%",
        lineWidth: 1,
        resize: {
          enabled: true,
        },
      },
    ],

    tooltip: {
      split: true,
    },

    plotOptions: {
      hollowcandlestick: {
        color: "#ff6d29",
        upColor: "#29b1ff",
      },
      series: {},
    },

    series: [
      {
        name: "Coin",
        id: "crypto",
        type: "hollowcandlestick",
        zIndex: 2,
        data: candles,
      },
      ...indicators.map((e) => {
        return e;
      }),
    ],
  });
}


for (let i = 0; i < crypto_list.length; i++) {
  const crypt = crypto_list[i]
  const id_chart = idlist[i]

  create_chart(crypt, id_chart)
}