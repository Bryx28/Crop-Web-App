window.onload = function() {

  var chart = new CanvasJS.Chart("cropChart", {
    animationEnabled: true,
    title: {
      text: "Crop Production Percentage"
    },
    data: [{
      type: "pie",
      startAngle: 240,
      yValueFormatString: "##0.00\"%\"",
      indexLabel: "{label} {y}",
      dataPoints: [
        {y: 18.77, label: "Rice Crop"},
        {y: 16.78, label: "Banana"},
        {y: 12.25, label: "Mango"},
        {y: 12.19, label: "Orange"},
        {y: 10.65, label: "Coconut"},
        {y: 10.41, label: "Durian"},
        {y: 9.92,  label: "Grapes"},
        {y: 9.03,  label: "Others"}
      ]
    }]
  });
  chart.render();
  
  }