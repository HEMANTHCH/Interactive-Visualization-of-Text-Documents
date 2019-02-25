/*
	@params:
		element: DOM node inside which graph will be created,
		data: scatter plot data in format [[point1, point2, DOC ID], ...]
		xlab: X Axis label,
		ylab: Y Axis label,
*/

function createScatterPlot(element, data, xlab = '', ylab = '') {
	google.charts.load('current', {packages: ['corechart']});
	google.charts.setOnLoadCallback(drawChart);
	function drawChart() {
		let dataTable = new google.visualization.DataTable();
    
		dataTable.addColumn('number', xlab);
		dataTable.addColumn('number', ylab);
    
		dataTable.addColumn({type: 'string', role: 'tooltip'});
		
		dataTable.addRows(data);
    
		let gridlineOpts = {
							gridlines: {
								color: 'transparent',
							},
							minorGridlines: {
								color: 'transparent',
							},
								baselineColor: 'transparent',
							};
		var options = {
                    legend: 'none', 
					vAxis: gridlineOpts,
					hAxis: gridlineOpts,
					'top': '10%',
					'left': '20%',
					'chartArea': {
                            'width': '80%', 'height': '60%',
                            backgroundColor: { stroke: '#000' },
                    },
					'pointSize': 16,
					'colors': ['turquoise'],
                 };
    
    var chart = new google.visualization.ScatterChart(element);
    
    google.visualization.events.addListener(chart, 'select', function() {
        let selection = chart.getSelection();
	   if(selection[0]) {
          let doc_id = dataTable.getValue(selection[0].row, 2);
          document.querySelector(`[value="${doc_id}"]`).click();
       }
	});
    
    google.visualization.events.addListener(chart, 'onmouseout', function (pos) {
        let doc_id = dataTable.getValue(pos.row, 2);
        
        document.querySelectorAll(`[value="${doc_id}"]`).forEach(e => e.parentNode.classList.remove('active'));
    });
    
    google.visualization.events.addListener(chart, 'onmouseover', function (pos) {
        
      let doc_id = dataTable.getValue(pos.row, 2);
        document.querySelectorAll(`[value="${doc_id}"]`).forEach(e => e.parentNode.classList.add('active'));
    });
    
    
    chart.draw(dataTable, options)
  }
}
