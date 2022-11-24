let plots = [];

Highcharts.getJSON(
  "https://api.binance.com/api/v3/klines?symbol=BTCBUSD&interval=4h",
  function (data) {
    Highcharts.stockChart("chart1", {
      chart: {
        backgroundColor: "transparent",
        color: "#f1f1f1",
        polar: true,
      },
      rangeSelector: {
        selected: 1,
      },
      navigator: {
        series: {
          color: Highcharts.getOptions().colors[0],
        },
      },
      xAxis: {
        //#2dff2d
        plotLines: plots,
      },
      series: [
        {
          type: "hollowcandlestick",
          name: "Hollow Candlestick",
          data: data.map((candle) => {
            return candle.map((item) => {
              return parseFloat(item);
            });
          }),
        },
      ],
      credits: false,
    });
  }
);

Highcharts.getJSON(
  "https://api.binance.com/api/v3/klines?symbol=BTCBUSD&interval=4h",
  function (data) {
    Highcharts.stockChart("chart2", {
      chart: {
        backgroundColor: "transparent",
        color: "#f1f1f1",
        polar: true,
      },
      rangeSelector: {
        selected: 1,
      },
      navigator: {
        series: {
          color: Highcharts.getOptions().colors[0],
        },
      },
      xAxis: {
        //#2dff2d
        plotLines: plots,
      },
      series: [
        {
          type: "hollowcandlestick",
          name: "Hollow Candlestick",
          data: data.map((candle) => {
            return candle.map((item) => {
              return parseFloat(item);
            });
          }),
        },
      ],
      credits: false,
    });
  }
);

Highcharts.getJSON(
  "https://api.binance.com/api/v3/klines?symbol=BTCBUSD&interval=8h",
  function (data) {
    Highcharts.stockChart("chart3", {
      chart: {
        backgroundColor: "transparent",
        color: "#f1f1f1",
        polar: true,
      },
      rangeSelector: {
        selected: 1,
      },
      navigator: {
        series: {
          color: Highcharts.getOptions().colors[0],
        },
      },
      xAxis: {
        //#2dff2d
        plotLines: plots,
      },
      series: [
        {
          type: "hollowcandlestick",
          name: "Hollow Candlestick",
          data: data.map((candle) => {
            return candle.map((item) => {
              return parseFloat(item);
            });
          }),
        },
      ],
      credits: false,
    });
  }
);

Highcharts.getJSON(
  "https://api.binance.com/api/v3/klines?symbol=BTCBUSD&interval=1h",
  function (data) {
    Highcharts.stockChart("chart4", {
      chart: {
        backgroundColor: "transparent",
        color: "#f1f1f1",
        polar: true,
      },
      rangeSelector: {
        selected: 1,
      },
      navigator: {
        series: {
          color: Highcharts.getOptions().colors[0],
        },
      },
      xAxis: {
        //#2dff2d
        plotLines: plots,
      },
      series: [
        {
          type: "hollowcandlestick",
          name: "Hollow Candlestick",
          data: data.map((candle) => {
            return candle.map((item) => {
              return parseFloat(item);
            });
          }),
        },
      ],
      credits: false,
    });
  }
);

Highcharts.getJSON(
  "https://api.binance.com/api/v3/klines?symbol=BTCBUSD&interval=2h",
  function (data) {
    Highcharts.stockChart("chart5", {
      chart: {
        backgroundColor: "transparent",
        color: "#f1f1f1",
        polar: true,
      },
      rangeSelector: {
        selected: 1,
      },
      navigator: {
        series: {
          color: Highcharts.getOptions().colors[0],
        },
      },
      xAxis: {
        //#2dff2d
        plotLines: plots,
      },
      series: [
        {
          type: "hollowcandlestick",
          name: "Hollow Candlestick",
          data: data.map((candle) => {
            return candle.map((item) => {
              return parseFloat(item);
            });
          }),
        },
      ],
      credits: false,
    });
  }
);

Highcharts.getJSON(
  "https://api.binance.com/api/v3/klines?symbol=BTCBUSD&interval=6h",
  function (data) {
    Highcharts.stockChart("chart6", {
      chart: {
        backgroundColor: "transparent",
        color: "#f1f1f1",
        polar: true,
      },
      rangeSelector: {
        selected: 1,
      },
      navigator: {
        series: {
          color: Highcharts.getOptions().colors[0],
        },
      },
      xAxis: {
        //#2dff2d
        plotLines: plots,
      },
      series: [
        {
          type: "hollowcandlestick",
          name: "Hollow Candlestick",
          data: data.map((candle) => {
            return candle.map((item) => {
              return parseFloat(item);
            });
          }),
        },
      ],
      credits: false,
    });
  }
);