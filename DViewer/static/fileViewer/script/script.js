      google.charts.load("current", {packages:["corechart"]});
      google.charts.setOnLoadCallback(drawChart);
      google.charts.setOnLoadCallback(drawBarChart);

      function drawChart() {
        var data = google.visualization.arrayToDataTable([
          ['language', 'documents'],
          ['nl', {{ query_nl_documents.count }}],
          ['fr', {{ query_fr_documents.count }}],
        ]);

        var options = {
          title: 'Documents per language',
          width: 450,
          height: 250,
          pieHole: 0.4,
        };

        var chart = new google.visualization.PieChart(document.getElementById('donutchart'));
        chart.draw(data, options);
      }

      function drawBarChart() {
         var data = google.visualization.arrayToDataTable([
         ['Language', 'Documents', { role: 'style' }],
         ['Dutch', {{ query_nl_documents.count }}, '#ADD8E6'],
         ['French', {{ query_fr_documents.count }}, '#FFB6C1'],
      ]);

        var options = {
            title: "Documents per language - BarChart ",
            width: 400,
            height: 250,
            bar: {groupWidth: "75%"},
            legend: { position: "none" },
          };
        var chart = new google.visualization.BarChart(document.getElementById('barchartdoc'));
        chart.draw(data, options);
      }
